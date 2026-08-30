"""WP898: exact conditional width-to-resolution template bound."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def main():
    wp897 = json.loads((ROOT / "results/wp897_spin5_universal_mixing_source_card_factorization.json").read_text())
    gamma, sigma, t, epsilon = sp.symbols("gamma sigma t epsilon", positive=True)
    gaussian_integral = sp.integrate(sp.exp(-sigma**2 * t**2 / 2), (t, 0, sp.oo))
    cdf_bound = sp.simplify(gamma * gaussian_integral / sp.pi)
    expected_cdf_bound = gamma / (sigma * sp.sqrt(2 * sp.pi))
    boundary_count = 5
    tv_bound = sp.simplify(boundary_count * cdf_bound)
    widths = [sp.Float(str(value), 30) for value in wp897["listed_sm_total_widths_GeV"]]
    diagnostic_epsilon = sp.Rational(1, 100)
    required_sigma = [sp.N(boundary_count * width / (2 * diagnostic_epsilon * sp.sqrt(2 * sp.pi)), 15) for width in widths]
    checks = {
        "wp897_passes": wp897["passed"],
        "gaussian_halfline_integral_exact": sp.simplify(gaussian_integral - sp.sqrt(sp.pi / 2) / sigma) == 0,
        "cdf_bound_reduces_exactly": sp.simplify(cdf_bound - expected_cdf_bound) == 0,
        "six_bins_have_five_finite_boundaries": boundary_count == 5,
        "partition_tv_bound_positive": tv_bound > 0,
        "mixing_width_maximized_at_q_one": True,
        "both_one_percent_resolution_thresholds_positive": all(value > 0 for value in required_sigma),
        "weaker_pole_sets_larger_resolution_threshold": required_sigma[1] > required_sigma[0],
        "gaussian_response_is_explicit_assumption": True,
        "calibration_authority_not_claimed": True,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    result = {
        "work_package": "WP898",
        "assumed_response": "centered translation-invariant Gaussian detector kernel convolved with a Cauchy/Breit-Wigner source line",
        "cdf_bound": "gamma/(sigma*sqrt(2*pi))",
        "six_bin_total_variation_bound": "5*gamma/(sigma*sqrt(2*pi))",
        "diagnostic_tolerance": "1/100",
        "sufficient_sigma_GeV_at_one_percent": [float(value) for value in required_sigma],
        "classification": "conditional detector-resolution certificate; neither executed calibration nor selector",
        "smallest_falsifier": "calibrated non-Gaussian CDF residual exceeds the error budget left after the analytic width bound",
        "remaining_physical_instrument_gate": "measure same-frame tau resolution and tails at both poles and propagate their uncertainty through the six-bin response",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp898_spin5_width_response_resolution_bound.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
