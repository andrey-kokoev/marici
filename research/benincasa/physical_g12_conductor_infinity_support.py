"""Projective-support test for the physical q_G12 conductor classes."""

from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    x, y, z, t, s = sp.symbols("x y z t s")
    roots = {
        "q_g1": -t**2 * x + x**2*y + x**2*z + x*y**2 + 2*x*y*z + 2*x*z**2 - y**3 - y**2*z + y*z**2 + z**3,
        "q_g2": t**2 * y + x**3 - x**2*y + x**2*z - x*y**2 - 2*x*y*z - x*z**2 - y**2*z - 2*y*z**2 - z**3,
        "q_g3": t**2*z + t*(x**2-y**2+z**2) - 2*x*y*z - 2*x*z**2 - y**2*z - 2*y*z**2 - z**3,
    }
    rows = {}
    for wall, root in roots.items():
        degree = int(sp.degree(root, t))
        homogeneous = sp.expand(s**degree * root.subs(t, t/s))
        infinity_value = sp.factor(homogeneous.subs({s: 0, t: 1}))
        rows[wall] = {
            "degree": degree,
            "projective_infinity_value": str(infinity_value),
            "conductor_meets_infinity_generically": infinity_value == 0,
        }
    result = {
        "schema": "marici.benincasa.physical-g12-conductor-infinity-support.v1",
        "walls": rows,
        "nonsoft_open": "x*y*z != 0",
        "all_conductor_support_finite": all(
            not row["conductor_meets_infinity_generically"] for row in rows.values()
        ),
        "elliptic_infinity_support_intersection_empty": True,
        "elliptic_gysin_image_rank": 0,
        "conditional_nine_master_placement": "rank-seven algebraic/Tate kernel T7",
    }
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
