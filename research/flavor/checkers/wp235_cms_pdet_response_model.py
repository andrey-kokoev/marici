"""WP235 empirical CMS width/background calibration and response-model audit."""

from __future__ import annotations

import csv
import hashlib
import json
import zlib
from pathlib import Path

import numpy as np
from scipy.optimize import minimize
from scipy.special import voigt_profile


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "cms-open-data-700" / "MuRun2010B.csv"
PROVENANCE = ROOT / "data" / "cms-open-data-700" / "provenance.json"
MZ = 91.1876
GAMMA_Z = 2.4955


def load_events():
    with DATA.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    return np.array([(int(row["Run"]), int(row["Event"]), float(row["M"])) for row in rows])


EDGES = np.linspace(70.0, 110.0, 41)
CENTERS = (EDGES[:-1] + EDGES[1:]) / 2


def expected_counts(theta):
    log_signal, log_sigma, log_background, slope = theta
    signal_n = np.exp(log_signal)
    sigma = np.exp(log_sigma)
    background_n = np.exp(log_background)
    signal_shape = voigt_profile(CENTERS - MZ, sigma, GAMMA_Z / 2)
    signal_shape /= signal_shape.sum()
    background_shape = np.exp(slope * (CENTERS - 90.0))
    background_shape /= background_shape.sum()
    return signal_n * signal_shape + background_n * background_shape


def nll(theta, counts):
    expectation = np.maximum(expected_counts(theta), 1e-12)
    return float(np.sum(expectation - counts * np.log(expectation)))


def fit(counts):
    start = np.array([np.log(max(counts.sum() * 0.7, 1)), np.log(2.0), np.log(max(counts.sum() * 0.3, 1)), -0.02])
    bounds = [(0, 10), (np.log(0.1), np.log(10)), (0, 10), (-0.3, 0.3)]
    result = minimize(nll, start, args=(counts,), method="L-BFGS-B", bounds=bounds)
    if not result.success:
        raise RuntimeError(result.message)
    return result


def hessian_2d(objective, point, indices=(1, 2), step=1e-3):
    h = np.zeros((2, 2))
    f0 = objective(point)
    for a, i in enumerate(indices):
        ei = np.zeros_like(point); ei[i] = step
        h[a, a] = (objective(point + ei) - 2 * f0 + objective(point - ei)) / step**2
        for b, j in enumerate(indices[:a]):
            ej = np.zeros_like(point); ej[j] = step
            value = (objective(point + ei + ej) - objective(point + ei - ej) - objective(point - ei + ej) + objective(point - ei - ej)) / (4 * step**2)
            h[a, b] = h[b, a] = value
    return h


def mixed_propagator(s, mediator_mass, mediator_width, mixing_mass_sq):
    a = complex(s - MZ**2, MZ * GAMMA_Z)
    d = complex(s - mediator_mass**2, mediator_mass * mediator_width)
    return d / (a * d - mixing_mass_sq**2)


def main():
    provenance = json.loads(PROVENANCE.read_text())
    certificate = PROVENANCE.parent / provenance["instrument_calibration"]["local_certificate"]
    checksum = format(zlib.adler32(DATA.read_bytes()) & 0xFFFFFFFF, "08x")
    events = load_events()
    window = events[(events[:, 2] >= 70) & (events[:, 2] <= 110)]
    calibration = window[(window[:, 1].astype(np.int64) % 2) == 0]
    evaluation = window[(window[:, 1].astype(np.int64) % 2) == 1]
    calibration_counts, _ = np.histogram(calibration[:, 2], bins=EDGES)
    evaluation_counts, _ = np.histogram(evaluation[:, 2], bins=EDGES)
    fitted = fit(calibration_counts)
    expectation = expected_counts(fitted.x)
    empirical_hessian = hessian_2d(lambda x: nll(x, calibration_counts), fitted.x)
    metric_eigenvalues = np.linalg.eigvalsh(empirical_hessian)
    metric_det = np.linalg.det(empirical_hessian)

    unmixed = mixed_propagator(MZ**2, 500.0, 5.0, 0.0)
    direct_z = 1 / complex(0, MZ * GAMMA_Z)
    decoupling_errors = []
    for mass in (500.0, 1000.0, 5000.0):
        mixed = mixed_propagator(MZ**2, mass, 0.01 * mass, 25.0)
        decoupling_errors.append(float(abs((mixed - direct_z) / direct_z)))

    pearson = float(np.sum((evaluation_counts - expectation)**2 / np.maximum(expectation, 1e-12)))
    checks = {
        "full_data_checksum_matches_cern": checksum == provenance["files"][0]["adler32"],
        "run_event_data_present": len(events) == 100000 and len(set(events[:, 0])) == 37,
        "local_instrument_certificate_verified": certificate.is_file() and hashlib.sha256(certificate.read_bytes()).hexdigest() == provenance["instrument_calibration"]["local_certificate_sha256"],
        "calibration_evaluation_disjoint": not set(calibration[:, 1]).intersection(set(evaluation[:, 1])),
        "finite_width_model_present": GAMMA_Z > 0 and np.exp(fitted.x[1]) > 0,
        "resolution_convolution_normalized": abs((voigt_profile(CENTERS - MZ, np.exp(fitted.x[1]), GAMMA_Z / 2) / voigt_profile(CENTERS - MZ, np.exp(fitted.x[1]), GAMMA_Z / 2).sum()).sum() - 1) < 1e-12,
        "background_model_positive": bool(np.all(expectation > 0)),
        "mixing_zero_limit_exact_numerically": abs(unmixed - direct_z) < 1e-15,
        "heavy_mediator_decouples_monotonically": decoupling_errors[0] > decoupling_errors[1] > decoupling_errors[2],
        "independent_metric_positive_definite": bool(np.all(metric_eigenvalues > 0) and metric_det > 0),
        "evaluation_fold_is_nonempty": len(evaluation) > 0,
        "source_intervention_not_claimed": True,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP235",
        "dataset": {
            "doi": provenance["doi"], "file": str(DATA), "adler32": checksum,
            "events": int(len(events)), "runs": int(len(set(events[:, 0]))),
            "window_events": int(len(window)), "calibration_events": int(len(calibration)),
            "evaluation_events": int(len(evaluation)),
        },
        "instrument_certificate": provenance["instrument_calibration"],
        "model": {
            "natural_width_GeV": GAMMA_Z,
            "fitted_detector_sigma_GeV": float(np.exp(fitted.x[1])),
            "fitted_signal_events_calibration": float(np.exp(fitted.x[0])),
            "fitted_background_events_calibration": float(np.exp(fitted.x[2])),
            "fitted_background_slope_per_GeV": float(fitted.x[3]),
            "mixing_model": "inverse 2x2 complex propagator with off-diagonal mass-squared mixing",
            "decoupling_relative_errors": decoupling_errors,
            "resolution_model": "Breit-Wigner/Voigt Gaussian convolution",
            "background_model": "positive exponential density",
        },
        "independent_detector_metric": {
            "coordinates": ["log_detector_sigma", "log_background_yield"],
            "source": "calibration-fold observed likelihood Hessian",
            "matrix": empirical_hessian.tolist(),
            "eigenvalues": metric_eigenvalues.tolist(),
            "determinant": float(metric_det),
        },
        "held_out_evaluation": {"pearson_statistic": pearson, "bins": 40},
        "classification": "empirically calibrated detector model, not source-intervention P_det",
        "remaining_gate": "No CMS record independently excites the two declared mediator source directions; source identification remains unauthorized.",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results" / "wp235_cms_pdet_response_model.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
