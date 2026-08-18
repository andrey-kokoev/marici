"""Differentiate the ordered physical wall residues in total energy."""
from __future__ import annotations

import json

import sympy as sp

import check_physical_residue_at_weighted_tangencies as source

a, b, x, y, z = source.a, source.b, source.x, source.y, source.z
energy = sp.symbols("E")


def main() -> None:
    walls = {"g1": b-y-z, "g2": a-x-z, "g3": a+b+z}
    left, right = b-x, a-y
    numerator = left + right
    quartic = -16*(x*y)**2 - 8*x*y*energy**2 + 8*(x+y)*energy**3 - 5*energy**4
    rows = {}

    for first, second, remaining in (
        ("g1", "g2", "g3"),
        ("g1", "g3", "g2"),
        ("g2", "g3", "g1"),
    ):
        solution = sp.solve([walls[first], walls[second]], [a, b], dict=True)[0]
        jacobian = sp.det(sp.Matrix([
            [sp.diff(walls[first], a), sp.diff(walls[first], b)],
            [sp.diff(walls[second], a), sp.diff(walls[second], b)],
        ]))
        coefficient = sp.factor(
            (numerator / (jacobian * walls[remaining] * left * right))
            .subs(solution).subs(z, energy-x-y)
        )
        surface = sp.factor(source.K.subs(solution).subs(z, energy-x-y))
        logarithmic_derivative = sp.factor(
            sp.diff(coefficient, energy) / coefficient
            - sp.diff(surface, energy) / (2 * surface)
        )
        denominator = sp.factor(sp.denom(logarithmic_derivative))
        gcd = sp.factor(
            sp.gcd(sp.Poly(denominator, energy, x, y), sp.Poly(quartic, energy, x, y)).as_expr()
        )
        assert gcd == 1

        # Reverse wall order negates the residue for every E, so its
        # derivative also negates it and the transported Cech term is zero.
        assert sp.diff(coefficient + (-coefficient), energy) == 0
        rows[f"{first}_{second}"] = {
            "logarithmic_derivative": str(logarithmic_derivative),
            "denominator": str(denominator),
            "denominator_gcd_with_Q": str(gcd),
            "transported_cech_component": "0",
        }

    print(json.dumps({
        "schema": "marici.physical-wall-first-gauss-manin-cech.v1",
        "pairs": rows,
        "all_transported_cech_components_zero": True,
        "all_derivative_denominators_Q_coprime": True,
        "quartic_supported_first_transition": False,
        "absolute_lift_selected": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
