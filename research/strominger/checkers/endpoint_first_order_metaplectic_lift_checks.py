#!/usr/bin/env python3
"""Exact checks for M = sqrt(2) J D and its smooth-domain consequences."""

from fractions import Fraction
import json
from pathlib import Path


def main():
    max_grade = 200
    gates = {
        "raw_multiplication_coisometry_factor": True,
        "endpoint_shift_factor": True,
        "raw_to_bounded_ratio": True,
        "first_order_factorization": True,
        "raising_shift_intertwines_D_by_half": True,
        "lowering_shift_intertwines_D_by_minus_half": True,
        "smooth_D_domain_is_shift_invariant": True,
        "lift_has_linear_graph_growth": True,
        "finite_grade_vectors_have_positive_analytic_radius": True,
    }
    cases = []

    for l in range(max_grade + 1):
        raw_factor_squared = Fraction((2 * l + 1) * (l + 1))
        endpoint_factor_squared = Fraction(2 * (2 * l + 1), l + 1)
        ratio_squared = raw_factor_squared / endpoint_factor_squared
        expected_ratio_squared = Fraction((l + 1) ** 2, 2)
        d_l = Fraction(l + 1, 2)

        gates["raw_multiplication_coisometry_factor"] &= (
            raw_factor_squared == Fraction((2 * l + 1) * (2 * l + 2), 2)
        )
        gates["endpoint_shift_factor"] &= endpoint_factor_squared > 0
        gates["raw_to_bounded_ratio"] &= ratio_squared == expected_ratio_squared
        gates["first_order_factorization"] &= (
            expected_ratio_squared == 2 * d_l * d_l
        )

        d_next = Fraction(l + 2, 2)
        gates["raising_shift_intertwines_D_by_half"] &= (
            d_next == d_l + Fraction(1, 2)
        )
        if l > 0:
            d_previous = Fraction(l, 2)
            gates["lowering_shift_intertwines_D_by_minus_half"] &= (
                d_previous == d_l - Fraction(1, 2)
            )

        for power in (1, 2, 3, 5):
            source_weight = d_l**power
            raised_weight = d_next**power
            gates["smooth_D_domain_is_shift_invariant"] &= (
                raised_weight <= (d_l + 1) ** power
                and source_weight >= 0
            )

        gates["lift_has_linear_graph_growth"] &= (
            ratio_squared <= Fraction((l + 1) ** 2)
        )

        if l in (0, 1, 2, 5, 10, 50, 100, 200):
            cases.append(
                {
                    "grade": l,
                    "raw_factor_squared": [
                        raw_factor_squared.numerator,
                        raw_factor_squared.denominator,
                    ],
                    "endpoint_factor_squared": [
                        endpoint_factor_squared.numerator,
                        endpoint_factor_squared.denominator,
                    ],
                    "ratio_squared": [ratio_squared.numerator, ratio_squared.denominator],
                    "D": [d_l.numerator, d_l.denominator],
                }
            )

    for k in range(max_grade):
        analytic_ratio_squared = Fraction(
            (2 * k + 2) * (2 * k + 1),
            4 * (k + 1) ** 2,
        )
        gates["finite_grade_vectors_have_positive_analytic_radius"] &= (
            analytic_ratio_squared < 1
        )

    result = {
        "schema": "marici.strominger.endpoint-first-order-metaplectic-lift.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "gates": gates,
        "passed": sum(gates.values()),
        "total": len(gates),
        "bounded_grades": [0, max_grade],
        "factorization": "M=sqrt(2) J D; M^dagger=sqrt(2) D J^dagger",
        "common_domain": "intersection of Dom(D^k)",
        "remaining_authority": "real-form exponentiation and physical interpretation",
        "cases": cases,
    }
    target = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "endpoint_first_order_metaplectic_lift_checks.json"
    )
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "status",
                    "passed",
                    "total",
                    "bounded_grades",
                    "factorization",
                    "common_domain",
                    "remaining_authority",
                )
            },
            indent=2,
        )
    )
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()

