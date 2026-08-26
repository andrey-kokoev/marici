"""WP335: exact second-moment audit for correlated CP-domain samples."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    sample_count = sp.symbols("N", integer=True, positive=True)
    probability = sp.symbols("p", real=True, positive=True)
    correlation = sp.symbols("rho", real=True)
    independent_variance = probability * (1 - probability) / sample_count
    correlated_variance = sp.simplify(
        probability * (1 - probability) * (1 + (sample_count - 1) * correlation) / sample_count
    )
    effective_sample_size = sp.simplify(
        independent_variance * sample_count / correlated_variance
    )
    positive_correlation_limit = sp.limit(effective_sample_size, sample_count, sp.oo)
    base = sp.Matrix([sp.Rational(1, 4)] * 4)
    moment_null = sp.Matrix([-1, 3, -3, 1]) / 24
    law_plus = base + moment_null
    law_minus = base - moment_null
    constraints = sp.Matrix([
        [1, 1, 1, 1],
        [0, 1, 2, 3],
        [0, 0, 2, 6],
    ])
    checks = {
        "independence_recovers_binomial_mean_variance": sp.simplify(correlated_variance.subs(correlation, 0) - independent_variance) == 0,
        "effective_sample_size_is_exact": effective_sample_size == sample_count / (1 + (sample_count - 1) * correlation),
        "perfect_correlation_gives_one_effective_sample": sp.simplify(effective_sample_size.subs(correlation, 1)) == 1,
        "positive_correlation_saturates_information_count": positive_correlation_limit == 1 / correlation,
        "psd_lower_boundary_has_zero_mean_variance": sp.simplify(correlated_variance.subs(correlation, -1 / (sample_count - 1))) == 0,
        "variance_inflation_factor_is_exact": sp.simplify(correlated_variance / independent_variance) == 1 + (sample_count - 1) * correlation,
        "counterexample_laws_are_positive_and_normalized": all(value > 0 for value in list(law_plus) + list(law_minus)) and sum(law_plus) == 1 and sum(law_minus) == 1,
        "counterexample_laws_share_first_two_factorial_moments": constraints * law_plus == constraints * law_minus,
        "counterexample_laws_have_different_triple_probability": law_plus[3] != law_minus[3],
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP335",
        "admitted_state_domain": "N exchangeable Bernoulli CP-domain indicators with common probability p and pairwise correlation rho in the positive-semidefinite range",
        "faithful_quotient_coordinate": "the branch probability p as estimated by the sample mean, with only first and second moments admitted",
        "candidate_probe_family": "repeated detector-calibrated domain indicators plus an independently estimated pairwise correlation",
        "sample_mean_variance": str(correlated_variance),
        "variance_inflation_factor": str(sp.simplify(correlated_variance / independent_variance)),
        "effective_sample_size": str(effective_sample_size),
        "positive_correlation_large_N_limit": str(positive_correlation_limit),
        "three_domain_covariance_counterexample": {
            "count_law_plus": [str(value) for value in law_plus],
            "count_law_minus": [str(value) for value in law_minus],
            "shared_normalization_mean_factorial_second": [str(value) for value in constraints * law_plus],
            "all_positive_probabilities": [str(law_plus[3]), str(law_minus[3])],
        },
        "contextual_partition": "the mean and equicorrelation determine sample-mean variance but not the joint outcome law or its full likelihood classes",
        "classification": "an exact second-moment resolution correction, not a Fisher-information theorem and not evidence for repeatable independent domain preparation",
        "smallest_exact_falsifier": "rho=1 makes every nominal repetition one effective sample, so increasing N does not improve sample-mean resolution",
        "remaining_physical_instrument_gate": "measure spatial and temporal domain correlations, specify or bound the joint law beyond covariance, propagate detector correlations, and justify which preparations count as distinct source trials",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp335_correlated_domain_resolution.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
