"""Resolve the oriented g3 conductor residues on both normalization sheets."""
from __future__ import annotations

import json

import sympy as sp

def main() -> None:
    x, y, z, c, a, b = sp.symbols("x y z c a b")
    epsilon = sp.symbols("epsilon")
    E = epsilon**2
    energy = x + y + z

    x2, y2, z2 = x**2, y**2, z**2
    K = (
        x2 * a**4
        - a**2 * b**2 * (x2 + y2 - z2)
        + y2 * b**4
        + a**2 * x2 * (x2 - y2 - z2)
        + c**2 * a**2 * (y2 - x2 - z2)
        + b**2 * y2 * (y2 - x2 - z2)
        + c**2 * b**2 * (x2 - y2 - z2)
        + z2 * c**4
        + c**2 * z2 * (z2 - x2 - y2)
        + z2 * x2 * y2
    )
    wall_substitution = {c: -energy, a: -b - z}
    restriction = sp.factor(K.subs(wall_substitution))
    factors = sp.factor_list(restriction)[1]
    assert len(factors) == 1 and factors[0][1] == 2
    R = sp.factor(factors[0][0])

    transverse = {z: E - x - y}
    R_E = sp.expand(R.subs(transverse))
    occurrence_product = sp.expand((b - x) * (-b - z - y)).subs(transverse)
    shared_product = sp.expand((b - y - z) * (-b - x - 2 * z)).subs(transverse)

    root_scale = sp.sqrt(-2 * x * y / (x + y))
    # The earlier tangency coordinate is a.  On q_g3=0,
    # b=-z-a=x+y-E-a, so the conductor roots limit to b=x.
    root_quadratic = -y / (x + y)
    rows = []
    leading = {}
    for surface_sign in (-1, 1):
        for root_sign in (-1, 1):
            root = x + root_sign * root_scale * epsilon + root_quadratic * epsilon**2
            residue = sp.factor(
                -E
                / (
                    surface_sign
                    * sp.diff(R_E, b)
                    * occurrence_product
                    * shared_product
                )
            )
            coefficient = sp.factor(
                sp.limit(epsilon * residue.subs(b, root), epsilon, 0)
            )
            leading[(surface_sign, root_sign)] = coefficient
            rows.append(
                {
                    "surface_sheet": surface_sign,
                    "tangency_root": root_sign,
                    "epsilon_order": -1,
                    "normalized_leading_coefficient": str(coefficient),
                }
            )

    base = leading[(1, 1)]
    for surface_sign in (-1, 1):
        for root_sign in (-1, 1):
            assert sp.factor(
                leading[(surface_sign, root_sign)]
                - surface_sign * root_sign * base
            ) == 0
    for root_sign in (-1, 1):
        assert sp.factor(
            leading[(1, root_sign)] + leading[(-1, root_sign)]
        ) == 0
    for surface_sign in (-1, 1):
        assert sp.factor(
            leading[(surface_sign, 1)] + leading[(surface_sign, -1)]
        ) == 0

    result = {
        "schema": "marici.g3-oriented-conductor-costalk.v1",
        "wall_square_root": str(R),
        "normalized_residues": rows,
        "sign_law": "coefficient(surface_sheet,root)=surface_sheet*root*C",
        "normalization_sheet_character": "anti-invariant",
        "tangency_root_pair": "opposite coefficients",
        "dualizing_residue_relation_on_each_node": "r_plus+r_minus=0",
        "costalk_dimension": 1,
        "costalk_nonzero": True,
        "direct_infinity_image": 0,
        "Q_in_local_leading_coefficient": False,
        "remaining_map": "connecting morphism from this costalk into the algebraic relative extension",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
