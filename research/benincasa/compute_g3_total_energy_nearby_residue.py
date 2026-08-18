"""Compute the ramified g3 physical residue at the total-energy boundary."""
from __future__ import annotations

import json

import sympy as sp

import check_physical_residue_at_weighted_tangencies as source

t, x, y, z = source.t, source.x, source.y, source.z
epsilon = sp.symbols("epsilon")
E = epsilon**2


def main() -> None:
    substitution, numerator, denominator = source.walls["g3"]
    restriction = sp.Poly(
        sp.expand(source.K.subs(substitution)),
        t,
        domain=sp.QQ.frac_field(x, y, z),
    )
    tangent = sp.gcd(restriction, restriction.diff()).monic().as_expr()
    tangent = sp.Poly(
        sp.fraction(sp.together(tangent))[0], t, x, y, z
    ).as_expr()

    transverse = {z: E - x - y}
    h = sp.expand(tangent.subs(transverse))
    n = sp.expand(numerator.subs(transverse))
    d = sp.expand(denominator.subs(transverse))

    c = sp.sqrt(-2 * x * y / (x + y))
    quadratic_term = -x / (x + y)
    residue = sp.factor(n / (sp.diff(h, t) * d))

    branches = []
    leading_coefficients = []
    for sign in (-1, 1):
        root = y + sign * c * epsilon + quadratic_term * epsilon**2
        coefficient = sp.factor(
            sp.limit(epsilon * residue.subs(t, root), epsilon, 0)
        )
        leading_coefficients.append(coefficient)
        branches.append(
            {
                "sign": sign,
                "root_through_order_epsilon_squared": str(root),
                "residue_epsilon_order": -1,
                "leading_coefficient": str(coefficient),
            }
        )

    assert sp.factor(leading_coefficients[0] + leading_coefficients[1]) == 0
    assert sp.factor(sp.discriminant(h, t)).subs(epsilon, 0) == 0

    result = {
        "schema": "marici.g3-total-energy-nearby-residue.v1",
        "transverse_coordinate": "E=epsilon^2",
        "special_fiber": str(sp.factor(h.subs(epsilon, 0))),
        "branches": branches,
        "deck_action": "epsilon -> -epsilon exchanges the two roots",
        "residue_character": "anti-invariant before Kummer normalization",
        "normalized_line": "epsilon times residue is invariant and regular",
        "kummer_exponent_in_E": "-1/2",
        "nilpotent_monodromy_on_rank_one_residue_line": "N=0",
        "new_carrier_datum": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
