#!/usr/bin/env python3
"""Exact checks for the two-extremal-per-grade endpoint filtration."""

from __future__ import annotations

import json
from pathlib import Path


def raise_squared(degree: int, source_spin: int, target_spin: int) -> int:
    value = 1
    for spin in range(source_spin, target_spin):
        value *= (degree - spin) * (degree + spin + 1)
    return value


def j_squared(l: int, m: int):
    return 2 * ((l + 1) ** 2 - m * m), (l + 1) * (2 * l + 3)


def main() -> None:
    gates = {
        "base_plus_two_per_grade_covers_every_target_weight": True,
        "filtered_port_count_equals_endpoint_dimension": True,
        "successive_quotient_dimension_is_two": True,
        "all_source_raise_coefficients_are_nonzero": True,
        "all_transport_coefficients_are_nonzero": True,
        "full_kernel_and_final_endpoint_counts_remain_distinct": True,
        "spin_two_grade_three_is_five_plus_two_plus_two": True,
        "spin_two_grade_three_unused_kernel_ports_equal_twelve": True,
    }
    cases = []
    for s in range(1, 11):
        for r in range(1, 11):
            top = s + r - 1
            labelled_weights = {m: s for m in range(-s, s + 1)}
            for degree in range(s + 1, top + 1):
                labelled_weights[-degree] = degree
                labelled_weights[degree] = degree

            target_weights = set(range(-top, top + 1))
            gates["base_plus_two_per_grade_covers_every_target_weight"] &= set(labelled_weights) == target_weights
            filtered_count = len(labelled_weights)
            endpoint_dimension = 2 * s + 2 * r - 1
            gates["filtered_port_count_equals_endpoint_dimension"] &= filtered_count == endpoint_dimension
            gates["successive_quotient_dimension_is_two"] &= endpoint_dimension - (2 * s + 2 * (r - 1) - 1) == 2 if r > 1 else True

            for weight, source_degree in labelled_weights.items():
                gates["all_source_raise_coefficients_are_nonzero"] &= raise_squared(source_degree, s, source_degree) > 0
                for l in range(source_degree, top):
                    numerator, denominator = j_squared(l, weight)
                    gates["all_transport_coefficients_are_nonzero"] &= numerator > 0 and denominator > 0

            full_kernel_ports = r * (2 * s + r)
            gates["full_kernel_and_final_endpoint_counts_remain_distinct"] &= full_kernel_ports >= filtered_count and (full_kernel_ports == filtered_count) == (r == 1)
            cases.append({
                "spin": s,
                "grade": r,
                "top_degree": top,
                "base_port_count": 2 * s + 1,
                "extremal_pairs_added": r - 1,
                "filtered_endpoint_port_count": filtered_count,
                "endpoint_dimension": endpoint_dimension,
                "full_kernel_port_count": full_kernel_ports,
                "unused_for_final_endpoint": full_kernel_ports - filtered_count,
            })

    spin_two_grade_three = next(c for c in cases if c["spin"] == 2 and c["grade"] == 3)
    gates["spin_two_grade_three_is_five_plus_two_plus_two"] &= spin_two_grade_three["base_port_count"] == 5 and spin_two_grade_three["extremal_pairs_added"] == 2 and spin_two_grade_three["filtered_endpoint_port_count"] == 9
    gates["spin_two_grade_three_unused_kernel_ports_equal_twelve"] &= spin_two_grade_three["full_kernel_port_count"] == 21 and spin_two_grade_three["unused_for_final_endpoint"] == 12

    result = {
        "schema": "marici.strominger.general-two-extremal-per-grade-filtration-result.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "gates": gates,
        "passed": sum(gates.values()),
        "total": len(gates),
        "theorem": "the grade-r endpoint is observed by 2s+1 base ports plus r-1 extremal pairs",
        "filtered_count": "2s+1+2(r-1)=2s+2r-1",
        "full_kernel_count": "r(2s+r)",
        "spin_two_grade_three": spin_two_grade_three,
        "cases": cases,
    }
    target = Path(__file__).resolve().parents[1] / "results" / "general_two_extremal_per_grade_filtration_checks.json"
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("status", "passed", "total", "theorem", "filtered_count", "full_kernel_count", "spin_two_grade_three")}, indent=2))
    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
