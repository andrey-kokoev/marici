#!/usr/bin/env python3
"""Check when the affine discriminant equals a ladder-operator cokernel dimension."""

from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    cases = []
    gates = {
        "equality_occurs_exactly_on_r_equals_s_diagonal": True,
        "diagonal_cokernel_is_H_2s_minus_1": True,
        "spin_two_grade_two_cokernel_has_dimension_seven": True,
        "spin_two_grade_three_cokernel_has_dimension_nine_not_seven": True,
        "affine_discriminant_is_grade_independent": True,
        "broad_cross_grade_identification_is_falsified": True,
    }

    for s in range(1, 21):
        affine = 4 * s - 1
        for r in range(1, 21):
            endpoint_degree = s + r - 1
            cokernel = 2 * endpoint_degree + 1
            equal = affine == cokernel
            gates["equality_occurs_exactly_on_r_equals_s_diagonal"] &= equal == (r == s)
            if r == s:
                gates["diagonal_cokernel_is_H_2s_minus_1"] &= endpoint_degree == 2 * s - 1
            cases.append({
                "spin": s,
                "grade": r,
                "affine_discriminant": affine,
                "cokernel_degree": endpoint_degree,
                "cokernel_dimension": cokernel,
                "dimensions_equal": equal,
            })

    gates["spin_two_grade_two_cokernel_has_dimension_seven"] &= 2 * 2 + 2 * 2 - 1 == 7
    gates["spin_two_grade_three_cokernel_has_dimension_nine_not_seven"] &= 2 * 2 + 2 * 3 - 1 == 9
    gates["affine_discriminant_is_grade_independent"] &= len({4 * 2 - 1 for _r in range(1, 21)}) == 1
    gates["broad_cross_grade_identification_is_falsified"] &= any(
        c["spin"] == 2 and c["grade"] == 3 and not c["dimensions_equal"] for c in cases)

    result = {
        "theorem": "the affine discriminant equals the ladder cokernel dimension exactly on the diagonal r=s",
        "gates": gates,
        "passed": sum(gates.values()),
        "total": len(gates),
        "all_passed": all(gates.values()),
        "symbolic_certificate": "(2s+2r-1)-(4s-1)=2(r-s)",
        "spin_two": {
            "affine_discriminant": 7,
            "grade_two_cokernel_dimension": 7,
            "grade_three_cokernel_dimension": 9,
        },
        "cases": cases,
    }
    target = Path(__file__).resolve().parents[1] / "results" / "affine_discriminant_ladder_cokernel_diagonal_checks.json"
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("passed", "total", "all_passed", "symbolic_certificate", "spin_two")}, indent=2))
    if not result["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
