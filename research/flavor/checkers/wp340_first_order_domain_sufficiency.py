"""WP340: exact first-order sufficiency on the independent Bernoulli domain family."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    probability, alpha, gamma = sp.symbols("p alpha gamma", real=True)
    source_tower = sp.Matrix([probability**order for order in range(7)])
    observed_first = alpha + gamma * probability
    recovered_probability = sp.simplify((observed_first - alpha) / gamma)
    iid_two_count_law = sp.Matrix([sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(1, 4)])
    correlated_two_count_law = sp.Matrix([sp.Rational(1, 2), 0, sp.Rational(1, 2)])
    weights = sp.Matrix([0, 1, 2])
    pair_counts = sp.Matrix([0, 0, 1])
    iid_u1 = sp.simplify((weights.dot(iid_two_count_law)) / 2)
    correlated_u1 = sp.simplify((weights.dot(correlated_two_count_law)) / 2)
    iid_u2 = sp.simplify(pair_counts.dot(iid_two_count_law))
    correlated_u2 = sp.simplify(pair_counts.dot(correlated_two_count_law))
    checks = {
        "iid_tower_is_power_sequence": source_tower == sp.Matrix([1, probability, probability**2, probability**3, probability**4, probability**5, probability**6]),
        "first_source_moment_equals_probability": source_tower[1] == probability,
        "calibrated_first_observed_moment_recovers_probability": recovered_probability == probability,
        "all_higher_iid_moments_are_determined_by_first": all(source_tower[j] == source_tower[1] ** j for j in range(2, 7)),
        "hostile_laws_are_distinct": iid_two_count_law != correlated_two_count_law,
        "hostile_laws_share_first_moment": iid_u1 == correlated_u1 == sp.Rational(1, 2),
        "hostile_laws_differ_at_second_order": iid_u2 == sp.Rational(1, 4) and correlated_u2 == sp.Rational(1, 2),
        "first_order_detector_gain_is_gamma_not_gamma_power_six": sp.diff(observed_first, probability) == gamma,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP340",
        "admitted_state_domain": "the frozen independent identically distributed Bernoulli CP-domain family with one source parameter p",
        "faithful_quotient_coordinate": "the Bernoulli probability p",
        "candidate_probe_family": "first normalized domain moment observed through independently calibrated alpha and nonzero gamma",
        "source_authorization": "conditional on an independently derived or validated iid preparation grammar",
        "source_moment_tower": [str(value) for value in source_tower],
        "first_order_inverse": "p=(r1-alpha)/gamma",
        "hostile_out_of_family_pair": {
            "iid_two_domain_count_law": [str(value) for value in iid_two_count_law],
            "perfectly_correlated_count_law": [str(value) for value in correlated_two_count_law],
            "common_first_moment": str(iid_u1),
            "second_moments": [str(iid_u2), str(correlated_u2)],
        },
        "contextual_partition": "first order has singleton fibers on the one-parameter iid family but merges correlated laws outside that family",
        "classification": "first order is sufficient and maximally economical for the frozen iid source grammar; the complete tower is needed only to test or reconstruct broader correlation structure",
        "smallest_exact_falsifier": "the iid and perfectly correlated two-domain laws both have first moment 1/2 but second moments 1/4 and 1/2",
        "remaining_physical_instrument_gate": "derive or experimentally validate independence and identical preparation before discarding higher coincidences; retain calibrated first-order background and contrast controls",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp340_first_order_domain_sufficiency.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
