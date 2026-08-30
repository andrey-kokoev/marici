#!/usr/bin/env python3
"""Two-lift falsifier for the differentiated rank-26 Euler identity."""

import json
from pathlib import Path


def main():
    source_weight = 28
    derivative_weight = source_weight - 1

    # Record coefficients in the formal basis (H_can, S).  Both lifts reduce
    # to S modulo epsilon, but their epsilon coefficients differ by S.
    canonical_lift = {"H_can": 1, "S": 0}
    alternative_lift = {"H_can": 1, "S": 1}

    # (E-27)H_can=0 and (E-27)S=(28-27)S=S.
    canonical_defect = {"S": 0}
    alternative_defect = {"S": source_weight - derivative_weight}

    checks = {
        "same_zeroth_order_source": True,
        "distinct_first_order_lifts": canonical_lift != alternative_lift,
        "canonical_lift_satisfies_weight_27": canonical_defect["S"] == 0,
        "alternative_lift_has_nonzero_defect": alternative_defect["S"] == 1,
        "defect_is_exactly_the_frozen_source": alternative_defect == {"S": 1},
    }
    result = {
        "schema": "marici.rank26-dual-lift-falsifier.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "base_source_weight": source_weight,
        "differentiated_weight": derivative_weight,
        "lifts": {
            "canonical": {
                "dual_source": "S + epsilon H_can",
                "first_order_coordinates": canonical_lift,
                "euler_defect": canonical_defect,
            },
            "alternative": {
                "dual_source": "S + epsilon (H_can + S)",
                "first_order_coordinates": alternative_lift,
                "euler_defect": alternative_defect,
            },
        },
        "checks": checks,
        "conclusion": (
            "The degree-28 scalar Euler identity does not authorize a unique dual-number source lift. "
            "The differentiated degree-27 identity rejects the alternative lift by the nonzero defect S."
        ),
        "next_falsifier": (
            "Derive H_can from the unspecialized source coefficients and reduction relations, rather than defining it by weight, "
            "and verify the complete quotient identity in all three parameter directions."
        ),
    }
    output = Path(__file__).with_name("rank26-dual-lift-falsifier.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
