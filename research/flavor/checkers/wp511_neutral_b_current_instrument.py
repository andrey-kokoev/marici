"""Executable neutral-B instrument for two real flavor-current coordinates."""

import json
import multiprocessing as mp
from pathlib import Path


_original_get_context = mp.get_context
mp.get_context = lambda method=None: _original_get_context(
    "spawn" if method == "fork" else method
)

import flavio
import numpy as np
from wilson import Wilson


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp455 = load("wp455_correlated_kaon_response_constructor.json")
wp459 = load("wp459_executable_kaon_likelihood_kernel.json")
wp510 = load("wp510_common_source_total_width_closure.json")

observables = ["DeltaM_d", "DeltaM_s"]
ratio_observable = "DeltaM_d/DeltaM_s"
sectors = ["bdbd", "bsbs"]
probe = 1e-15
scale_gev = 160.0

measurements = {}
for observable in observables + [ratio_observable]:
    distribution = flavio.combine_measurements(observable)
    matching = sorted(
        name
        for name, measurement in flavio.Measurement.instances.items()
        if observable in measurement.all_parameters
    )
    measurements[observable] = {
        "matching_measurements": matching,
        "central_value": distribution.central_value,
        "standard_deviation": distribution.standard_deviation,
    }


def prediction_vector(sector, coefficient):
    wilson = Wilson(
        {
            f"CVLL_{sector}": coefficient,
            f"CVRR_{sector}": coefficient,
            f"CVLR_{sector}": 2 * coefficient,
        },
        scale=scale_gev,
        eft="WET",
        basis="flavio",
    )
    return np.array(
        [flavio.np_prediction(observable, wilson) for observable in observables],
        dtype=float,
    )


def ratio_prediction(sector, coefficient):
    wilson = Wilson(
        {
            f"CVLL_{sector}": coefficient,
            f"CVRR_{sector}": coefficient,
            f"CVLR_{sector}": 2 * coefficient,
        },
        scale=scale_gev,
        eft="WET",
        basis="flavio",
    )
    return float(flavio.np_prediction(ratio_observable, wilson))


sm = np.array([flavio.sm_prediction(observable) for observable in observables])
experiment = np.array(
    [measurements[observable]["central_value"] for observable in observables]
)
experimental_covariance = np.diag(
    [
        measurements[observable]["standard_deviation"] ** 2
        for observable in observables
    ]
)

jacobian = np.zeros((2, 2))
ratio_jacobian = np.zeros((1, 2))
for column, sector in enumerate(sectors):
    jacobian[:, column] = (
        prediction_vector(sector, probe) - prediction_vector(sector, -probe)
    ) / (2 * probe)
    ratio_jacobian[0, column] = (
        ratio_prediction(sector, probe) - ratio_prediction(sector, -probe)
    ) / (2 * probe)

# Freeze the theory-nuisance transport rather than silently using only the much
# narrower experimental errors.  The seed and draw count are part of the
# executable instrument contract.
np.random.seed(511)
theory_covariance = np.asarray(
    flavio.sm_covariance(observables, N=200, threads=1), dtype=float
)
total_covariance = experimental_covariance + theory_covariance
weight = np.linalg.inv(total_covariance)
gram = jacobian.T @ weight @ jacobian
coefficient_covariance = np.linalg.inv(gram)
coefficient_hat = (
    coefficient_covariance @ jacobian.T @ weight @ (experiment - sm)
)
coefficient_sigma = np.sqrt(np.diag(coefficient_covariance))

ratio_chain_rule = np.array(
    [
        [
            jacobian[0, 0] / sm[1],
            -sm[0] * jacobian[1, 1] / sm[1] ** 2,
        ]
    ]
)
augmented_jacobian = np.vstack([jacobian, ratio_jacobian])

checks = {
    "wp455_dependency_passed": bool(wp455["passed"]),
    "wp459_dependency_passed": bool(wp459["passed"]),
    "wp510_dependency_passed": bool(wp510["passed"]),
    "flavio_version_is_pinned": flavio.__version__ == "2.7.0",
    "two_cp_even_oscillation_observables_are_registered": all(
        observable in flavio.Observable.instances for observable in observables
    ),
    "delta_md_has_bundled_measurement": measurements["DeltaM_d"][
        "matching_measurements"
    ]
    == ["HFAG osc summer 2015"],
    "delta_ms_has_bundled_measurement": measurements["DeltaM_s"][
        "matching_measurements"
    ]
    == ["HFAG osc summer 2015"],
    "real_two_coordinate_response_has_rank_two": np.linalg.matrix_rank(
        jacobian
    )
    == 2,
    "cross_sector_responses_vanish": bool(
        jacobian[0, 1] == 0 and jacobian[1, 0] == 0
    ),
    "theory_covariance_is_positive_definite": bool(
        np.all(np.linalg.eigvalsh(theory_covariance) > 0)
    ),
    "detector_weighted_gram_is_positive_definite": bool(
        np.all(np.linalg.eigvalsh(gram) > 0) and np.linalg.det(gram) > 0
    ),
    "ratio_response_obeys_chain_rule": bool(
        np.allclose(ratio_jacobian, ratio_chain_rule, rtol=2e-5, atol=0)
    ),
    "ratio_adds_no_third_local_direction": np.linalg.matrix_rank(
        augmented_jacobian
    )
    == 2,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP511",
    "runtime": {
        "python": "3.12",
        "flavio": flavio.__version__,
        "particle": "0.25.4",
        "theory_covariance_seed": 511,
        "theory_covariance_draws": 200,
    },
    "admitted_state_domain": "Two real correlated WET rays (CVLL,CVRR,CVLR)=x_q(1,1,2) for q=d,s at 160 GeV",
    "source_authorized_probe_family": [
        "real bdbd correlated vector-current ray",
        "real bsbs correlated vector-current ray",
    ],
    "physical_instrument": {
        "observables": observables,
        "measurements": measurements,
        "sm_predictions": sm.tolist(),
        "experimental_covariance": experimental_covariance.tolist(),
        "frozen_theory_covariance": theory_covariance.tolist(),
    },
    "response": {
        "jacobian": jacobian.tolist(),
        "rank": int(np.linalg.matrix_rank(jacobian)),
        "detector_gram": gram.tolist(),
        "detector_gram_determinant": float(np.linalg.det(gram)),
        "local_gaussian_coefficient_hat_GeV^-2": coefficient_hat.tolist(),
        "local_gaussian_coefficient_sigma_GeV^-2": coefficient_sigma.tolist(),
        "coefficient_correlation": float(
            coefficient_covariance[0, 1]
            / np.sqrt(
                coefficient_covariance[0, 0] * coefficient_covariance[1, 1]
            )
        ),
    },
    "ratio_observable": {
        "name": ratio_observable,
        "jacobian": ratio_jacobian.tolist(),
        "augmented_rank": int(np.linalg.matrix_rank(augmented_jacobian)),
        "classification": "derived correlated readout; it does not add a third local source direction",
    },
    "contextual_partition": "The executable DeltaM_d and DeltaM_s family is locally faithful on the admitted two-real-coordinate WET packet; each coordinate has a distinct calibrated oscillation port.",
    "classification": "Actual calibrated CP-even flavor-current instrument with local rank two on the declared WET packet. It constrains realized current coefficients but is neither a source selector nor a pole-residue instrument.",
    "selector": False,
    "rigidifier": False,
    "reference_port_required": False,
    "instrument_realized": bool(np.linalg.det(gram) > 0),
    "smallest_exact_falsifier": "Either diagonal response derivative vanishes, the calibrated covariance loses positive rank, or the two source coordinates are mapped to one WET coefficient before the detector interface.",
    "remaining_gate": "Derive the WP510 mass-basis orientation map into bdbd and bsbs coefficients from the same messenger vacuum. The contact experiment collapses the pole decomposition, so a separate on-shell instrument is still required to read individual WP509 residues and widths.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp511_neutral_b_current_instrument.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
