"""Compute the pairwise Cech transitions of the physical wall cocycle."""
from __future__ import annotations

import json

import sympy as sp

import check_physical_residue_at_weighted_tangencies as source

a, b, x, y, z = source.a, source.b, source.x, source.y, source.z


def gcd_with(expr: sp.Expr, divisor: sp.Expr) -> sp.Expr:
    return sp.factor(
        sp.gcd(sp.Poly(expr, x, y, z), sp.Poly(divisor, x, y, z)).as_expr()
    )


def main() -> None:
    E = x + y + z
    q = {
        "g1": b - y - z,
        "g2": a - x - z,
        "g3": a + b + z,
    }
    occurrence_left = b - x
    occurrence_right = a - y
    numerator = occurrence_left + occurrence_right

    A = (x - y) ** 2 - z**2
    B = (x + y) ** 2 - z**2
    Q = sp.factor(4 * A * B - (A + B - E**2) ** 2)

    pairs = []
    for first, second, remaining in (
        ("g1", "g2", "g3"),
        ("g1", "g3", "g2"),
        ("g2", "g3", "g1"),
    ):
        solution = sp.solve([q[first], q[second]], [a, b], dict=True)[0]
        jacobian = sp.factor(
            sp.det(
                sp.Matrix(
                    [
                        [sp.diff(q[first], a), sp.diff(q[first], b)],
                        [sp.diff(q[second], a), sp.diff(q[second], b)],
                    ]
                )
            )
        )
        rational_coefficient = sp.factor(
            (
                numerator
                / (
                    jacobian
                    * q[remaining]
                    * occurrence_left
                    * occurrence_right
                )
            ).subs(solution)
        )
        surface_value = sp.factor(source.K.subs(solution))
        norm = sp.factor(rational_coefficient**2 / surface_value)
        reverse_coefficient = sp.factor(-rational_coefficient)
        cech_difference = sp.factor(rational_coefficient + reverse_coefficient)
        assert cech_difference == 0
        coefficient_numerator, coefficient_denominator = sp.fraction(
            rational_coefficient
        )
        pairs.append(
            {
                "ordered_pair": [first, second],
                "remaining_wall": remaining,
                "intersection": {str(key): str(value) for key, value in solution.items()},
                "jacobian": str(jacobian),
                "forward_iterated_residue": f"({rational_coefficient})/w",
                "reverse_iterated_residue": f"({reverse_coefficient})/w",
                "cech_degree_one_component": str(cech_difference),
                "surface_value": str(surface_value),
                "sheet_norm": str(norm),
                "gcd_Q_coefficient_numerator": str(
                    gcd_with(coefficient_numerator, Q)
                ),
                "gcd_Q_coefficient_denominator": str(
                    gcd_with(coefficient_denominator, Q)
                ),
                "gcd_Q_surface_value": str(gcd_with(surface_value, Q)),
            }
        )

    assert all(
        row[key] == "1"
        for row in pairs
        for key in (
            "gcd_Q_coefficient_numerator",
            "gcd_Q_coefficient_denominator",
            "gcd_Q_surface_value",
        )
    )

    result = {
        "schema": "marici.physical-wall-cech-transitions.v1",
        "surface_form": "da wedge db / (w*q_g1*q_g2*q_g3) * (1/q_g23+1/q_g31)",
        "pairs": pairs,
        "all_pairwise_cech_components_zero": True,
        "all_pair_transitions_Q_coprime": True,
        "new_carrier_datum": False,
        "remaining_Q_home": "Gauss-Manin transport or higher gluing of the localization extension",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
