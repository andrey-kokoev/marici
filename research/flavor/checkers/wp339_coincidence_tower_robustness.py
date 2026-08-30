"""WP339: exact contrast-conditioning audit for the order-six coincidence tower."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    gamma = sp.symbols("gamma", real=True, positive=True)
    r6 = sp.symbols("r6", real=True)
    diagonal_response = sp.diag(*[gamma**order for order in range(7)])
    gram = diagonal_response.T * diagonal_response
    recovered_sixth = r6 / gamma**6
    contrast_derivative = sp.factor(sp.diff(recovered_sixth, gamma))
    logarithmic_sensitivity = sp.simplify(gamma * contrast_derivative / recovered_sixth)
    benchmark_half = sp.Rational(1, 2)
    benchmark_tenth = sp.Rational(1, 10)
    checks = {
        "background_free_response_is_diagonal": diagonal_response.is_diagonal(),
        "order_six_singular_value_is_gamma_power_six": diagonal_response[6, 6] == gamma**6,
        "order_six_gram_eigenvalue_is_gamma_power_twelve": gram[6, 6] == gamma**12,
        "inverse_order_six_gain_is_gamma_power_minus_six": sp.diff(recovered_sixth, r6) == gamma**-6,
        "relative_contrast_sensitivity_is_minus_six": logarithmic_sensitivity == -6,
        "half_contrast_amplifies_by_64": benchmark_half**-6 == 64,
        "tenth_contrast_amplifies_by_one_million": benchmark_tenth**-6 == 1_000_000,
        "zero_contrast_limit_diverges": sp.limit(gamma**-6, gamma, 0, dir="+") == sp.oo,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP339",
        "admitted_state_domain": "the background-free alpha=0 specialization of the calibrated order-six coincidence response with contrast 0<gamma<=1",
        "faithful_quotient_coordinate": "source coincidence moments u_0 through u_6, with focus on worst-order noise amplification",
        "response_diagonal": [str(gamma**order) for order in range(7)],
        "order_six_forward_gain": "gamma^6",
        "order_six_inverse_gain": "gamma^(-6)",
        "order_six_gram_eigenvalue": "gamma^12",
        "relative_contrast_sensitivity": str(logarithmic_sensitivity),
        "benchmark_amplification": {"gamma=1/2": 64, "gamma=1/10": 1_000_000},
        "robustness_rule": "a sixth-order detected-moment error delta is amplified to delta/gamma^6 before background-subtraction errors are included",
        "contextual_partition": "every nonzero contrast is algebraically faithful, but finite error budgets resolve only contrasts bounded away from zero by an independently certified margin",
        "classification": "an exact conditioning obstruction for the complete calibrated tower; formal invertibility does not imply experimentally useful faithfulness",
        "smallest_exact_falsifier": "at gamma=1/2 the sixth-order inverse already multiplies error by 64, while at gamma=1/10 it multiplies error by one million",
        "remaining_physical_instrument_gate": "establish a contrast lower bound, per-order noise and calibration covariance, background-subtraction stability, and a source-law separation margin larger than the propagated inverse error",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp339_coincidence_tower_robustness.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
