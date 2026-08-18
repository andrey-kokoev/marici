"""Check whether the ramified g3 conductor support meets fiber infinity."""
from __future__ import annotations

import json

import sympy as sp

import check_physical_residue_at_weighted_tangencies as source

t, x, y, z = source.t, source.x, source.y, source.z
E, T, S = sp.symbols("E T S")


def main() -> None:
    substitution, _, _ = source.walls["g3"]
    restriction = sp.Poly(
        sp.expand(source.K.subs(substitution)),
        t,
        domain=sp.QQ.frac_field(x, y, z),
    )
    tangent = sp.gcd(restriction, restriction.diff()).monic().as_expr()
    tangent = sp.Poly(
        sp.fraction(sp.together(tangent))[0], t, x, y, z
    ).as_expr()
    h = sp.expand(tangent.subs(z, E - x - y))
    degree = sp.degree(h, t)
    homogeneous = sp.expand(S**degree * h.subs(t, T / S))
    infinity_value = sp.factor(homogeneous.subs(S, 0) / T**degree)
    special_fiber = sp.factor(h.subs(E, 0))

    assert degree == 2
    assert sp.factor(infinity_value.subs(E, 0) + x + y) == 0
    assert sp.factor(special_fiber + (x + y) * (t - y) ** 2) == 0

    result = {
        "schema": "marici.g3-nearby-support-at-infinity.v1",
        "homogenized_cover": str(sp.factor(homogeneous)),
        "infinity_coefficient": str(infinity_value),
        "infinity_coefficient_at_E_zero": str(
            sp.factor(infinity_value.subs(E, 0))
        ),
        "special_fiber": str(special_fiber),
        "ramification_point_at_E_zero": "[T:S]=[y:1]",
        "generic_open": "x*y*(x+y) != 0",
        "support_closure_meets_infinity_near_E_zero": False,
        "nearby_support_base_change": "j_infinity^* psi_E i_C! = 0",
        "direct_elliptic_infinity_image_rank": 0,
        "remaining_possible_coupling": "connecting morphism of localization triangles",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
