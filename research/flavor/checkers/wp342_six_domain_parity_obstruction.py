"""WP342: exact five-wise-independence obstruction on six binary domains."""

import itertools
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def subset_moment(law, subset):
    return sp.simplify(
        sum(weight * sp.prod(word[index] for index in subset) for word, weight in law.items())
    )


def main():
    size = 6
    words = list(itertools.product((0, 1), repeat=size))
    iid_law = {word: sp.Rational(1, 2**size) for word in words}
    odd_words = [word for word in words if sum(word) % 2 == 1]
    parity_law = {
        word: (sp.Rational(1, len(odd_words)) if word in odd_words else sp.Integer(0))
        for word in words
    }
    order_audits = []
    for order in range(size + 1):
        subsets = list(itertools.combinations(range(size), order))
        iid_values = {subset_moment(iid_law, subset) for subset in subsets}
        parity_values = {subset_moment(parity_law, subset) for subset in subsets}
        order_audits.append({
            "order": order,
            "subset_count": len(subsets),
            "iid_values": sorted(str(value) for value in iid_values),
            "parity_values": sorted(str(value) for value in parity_values),
            "all_match": iid_values == parity_values,
        })
    checks = {
        "iid_law_has_64_supported_words": sum(1 for weight in iid_law.values() if bool(weight > 0)) == 64,
        "odd_parity_law_has_32_supported_words": sum(1 for weight in parity_law.values() if bool(weight > 0)) == 32,
        "both_laws_are_normalized": sum(iid_law.values()) == 1 and sum(parity_law.values()) == 1,
        "laws_are_distinct": iid_law != parity_law,
        "all_orders_zero_through_five_match": all(audit["all_match"] for audit in order_audits[:6]),
        "every_order_j_below_six_equals_two_power_minus_j": all(
            audit["iid_values"] == [str(sp.Rational(1, 2**audit["order"]))] and
            audit["parity_values"] == [str(sp.Rational(1, 2**audit["order"]))]
            for audit in order_audits[:6]
        ),
        "sixth_order_separates": order_audits[6]["iid_values"] == ["1/64"] and order_audits[6]["parity_values"] == ["0"] and not order_audits[6]["all_match"],
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP342",
        "admitted_state_domain": "all labelled probability laws on six binary CP-domain indicators",
        "faithful_quotient_coordinate": "the complete labelled six-bit joint law, tested by subset coincidences",
        "candidate_probe_family": "all calibrated labelled subset coincidences through order six",
        "order_audits": order_audits,
        "iid_support_size": 64,
        "odd_parity_support_size": 32,
        "contextual_partition": "every tower truncated below order six merges iid fair domains with the odd-parity law; the sixth-order all-positive coincidence separates them",
        "classification": "no coincidence tower of order at most five certifies six-domain independence on the unrestricted law family; full order six is necessary for this hostile pair",
        "smallest_exact_falsifier": "iid fair and uniform odd-parity laws agree on every one- through five-body marginal but have sixth moments 1/64 and 0",
        "remaining_physical_instrument_gate": "either measure calibrated sixth-order labelled coincidences with the WP339 contrast margin or derive a source theorem excluding global parity constraints before truncating the tower",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp342_six_domain_parity_obstruction.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
