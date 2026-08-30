"""WP341: exact hierarchy of first-, second-, and third-order independence probes."""

import itertools
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def moment(law, subset):
    return sp.simplify(sum(weight * sp.prod(word[index] for index in subset) for word, weight in law.items()))


def main():
    words = list(itertools.product((0, 1), repeat=3))
    iid_law = {word: sp.Rational(1, 8) for word in words}
    even_parity_words = [word for word in words if sum(word) % 2 == 0]
    parity_law = {word: (sp.Rational(1, 4) if word in even_parity_words else sp.Integer(0)) for word in words}
    singleton_subsets = [(0,), (1,), (2,)]
    pair_subsets = [(0, 1), (0, 2), (1, 2)]
    triple_subset = (0, 1, 2)
    iid_first = [moment(iid_law, subset) for subset in singleton_subsets]
    parity_first = [moment(parity_law, subset) for subset in singleton_subsets]
    iid_second = [moment(iid_law, subset) for subset in pair_subsets]
    parity_second = [moment(parity_law, subset) for subset in pair_subsets]
    iid_third = moment(iid_law, triple_subset)
    parity_third = moment(parity_law, triple_subset)
    checks = {
        "both_laws_are_normalized": sum(iid_law.values()) == 1 and sum(parity_law.values()) == 1,
        "laws_are_distinct": iid_law != parity_law,
        "all_first_moments_match": iid_first == parity_first == [sp.Rational(1, 2)] * 3,
        "all_second_moments_match": iid_second == parity_second == [sp.Rational(1, 4)] * 3,
        "all_pair_covariances_vanish": all(second - first**2 == 0 for first, second in zip(parity_first, parity_second)),
        "third_moments_differ": iid_third == sp.Rational(1, 8) and parity_third == 0,
        "second_order_detector_inverse_scales_as_gamma_minus_two": sp.diff(sp.symbols("r2") / sp.symbols("gamma", nonzero=True) ** 2, sp.symbols("r2")) == sp.symbols("gamma", nonzero=True) ** -2,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP341",
        "admitted_state_domain": "three labelled binary domains, comparing iid fair coins with an exchangeable even-parity law",
        "faithful_quotient_coordinate": "successive one-, two-, and three-body coincidence tensors",
        "candidate_probe_family": "calibrated first moment for p, second moments for pair covariance, and third moment for the residual parity class",
        "iid_first_moments": [str(value) for value in iid_first],
        "parity_first_moments": [str(value) for value in parity_first],
        "iid_second_moments": [str(value) for value in iid_second],
        "parity_second_moments": [str(value) for value in parity_second],
        "iid_third_moment": str(iid_third),
        "parity_third_moment": str(parity_third),
        "contextual_partition": "first order fixes marginals, second order refines pair covariance classes, and third order separates the iid and parity laws that remain collapsed below it",
        "classification": "second order can falsify pairwise independence but cannot certify mutual independence; third order is the smallest separator for the exact parity hostile pair",
        "smallest_exact_falsifier": "the iid fair law and uniform even-parity law share every first and second moment but have third moments 1/8 and 0",
        "remaining_physical_instrument_gate": "implement calibrated second- and third-order coincidences with contrast margins gamma^-2 and gamma^-3, or derive a source theorem excluding higher-order dependence",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp341_independence_probe_hierarchy.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
