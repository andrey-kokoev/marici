"""WP334: exact local finite-sample information for CP-bias detection."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    beta, c0, epsilon = sp.symbols("beta c0 epsilon", real=True, positive=True)
    alpha, delta = sp.symbols("alpha delta", real=True, nonnegative=True)
    samples = sp.symbols("N", integer=True, positive=True)
    contrast = 1 - alpha - delta
    true_probability = 1 / (1 + sp.exp(-2 * beta * epsilon * c0))
    observed_probability = sp.simplify(alpha + contrast * true_probability)
    derivative = sp.simplify(sp.diff(observed_probability, epsilon))
    fisher_per_sample = sp.simplify(derivative**2 / (observed_probability * (1 - observed_probability)))
    boundary_probability = sp.simplify(observed_probability.subs(epsilon, 0))
    boundary_fisher = sp.factor(fisher_per_sample.subs(epsilon, 0))
    expected_boundary_fisher = sp.factor(
        beta**2 * c0**2 * contrast**2 / (1 - (alpha - delta) ** 2)
    )
    symmetric_error = sp.symbols("r", real=True, nonnegative=True)
    symmetric_boundary_fisher = sp.factor(boundary_fisher.subs({alpha: symmetric_error, delta: symmetric_error}))
    perfect_boundary_fisher = sp.simplify(boundary_fisher.subs({alpha: 0, delta: 0}))
    checks = {
        "zero_bias_true_probability_is_half": true_probability.subs(epsilon, 0) == sp.Rational(1, 2),
        "boundary_observed_probability_is_exact": boundary_probability == (1 + alpha - delta) / 2,
        "perfect_detector_boundary_information_is_beta2c02": perfect_boundary_fisher == beta**2 * c0**2,
        "boundary_information_has_exact_contrast_form": sp.simplify(boundary_fisher - expected_boundary_fisher) == 0,
        "symmetric_confusion_penalty_is_contrast_squared": sp.simplify(symmetric_boundary_fisher - beta**2 * c0**2 * (1 - 2 * symmetric_error) ** 2) == 0,
        "independent_samples_add_information": sp.simplify(samples * boundary_fisher / boundary_fisher) == samples,
        "zero_contrast_kills_boundary_information": sp.simplify(boundary_fisher.subs(delta, 1 - alpha)) == 0,
        "probability_denominator_has_difference_of_squares_form": sp.simplify(1 - (alpha - delta) ** 2 + (alpha - delta - 1) * (alpha - delta + 1)) == 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP334",
        "admitted_state_domain": "independent CP-domain Bernoulli trials near epsilon=0 with known positive beta,c0 and calibrated rates alpha,delta satisfying 0<=alpha,delta and alpha+delta<1",
        "faithful_quotient_coordinate": "the local signed bias epsilon inferred from detector-level branch frequencies",
        "candidate_physical_instrument": "N repeated domain preparations passed through the calibrated WP329 binary detector",
        "true_positive_probability": str(true_probability),
        "observed_positive_probability": str(observed_probability),
        "zero_bias_observed_probability": str(boundary_probability),
        "fisher_information_per_sample": str(fisher_per_sample),
        "zero_bias_fisher_per_sample": str(boundary_fisher),
        "symmetric_error_zero_bias_fisher": str(symmetric_boundary_fisher),
        "cramer_rao_rule": "for N independent trials, Var(epsilon_hat) is at least 1/(N*I_epsilon); detector confusion reduces I_epsilon and cannot be repaired by algebraic inversion alone",
        "contextual_partition": "nonzero calibrated contrast makes nearby biases statistically distinguishable only asymptotically; finite N leaves overlapping outcome distributions",
        "classification": "a finite-sample resolution contract for an identifying instrument, not a selector or a proof of independent domain preparation",
        "smallest_exact_falsifier": "alpha+delta=1 sets the Fisher information to zero for every sample count, so repetitions cannot repair a blind detector",
        "remaining_physical_instrument_gate": "establish independent or correctly correlated domain trials, freeze beta and c0 uncertainties, propagate calibration uncertainty, choose a declared confidence and power criterion, and demonstrate sufficient N",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp334_cp_bias_finite_sample_resolution.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
