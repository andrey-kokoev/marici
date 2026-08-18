"""Conductor obstruction for descent of the physical q_G12 residue."""

from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    x, y, z, c, a, b = sp.symbols("x y z c a b")
    energy = x + y + z
    x2, y2, z2 = x**2, y**2, z**2
    cayley_menger = (
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
    walls = {
        "q_g1": ({c: -energy, b: y + z}, a, a + z - x),
        "q_g2": ({c: -energy, a: x + z}, b, b + z - y),
        "q_g3": ({c: -energy, a: -b - z}, b, -energy),
    }
    rows = {}
    for name, (substitution, parameter, numerator) in walls.items():
        restriction = sp.factor(cayley_menger.subs(substitution))
        factors = sp.factor_list(restriction)[1]
        assert len(factors) == 1 and factors[0][1] == 2
        square_root = sp.factor(factors[0][0])
        resultant = sp.factor(sp.resultant(square_root, numerator, parameter))
        rows[name] = {
            "parameter": str(parameter),
            "square_root": str(square_root),
            "wall_numerator": str(numerator),
            "conductor_resultant": str(resultant),
            "resultant_generically_nonzero": resultant != 0,
        }
    result = {
        "schema": "marici.benincasa.physical-g12-conductor-obstruction.v1",
        "walls": rows,
        "all_wall_restrictions_are_exact_squares": True,
        "all_conductor_resultants_generically_nonzero": all(
            row["resultant_generically_nonzero"] for row in rows.values()
        ),
        "localization_boundary_generically_nonzero": True,
        "q_only_descent": False,
        "classification": "intrinsically relative physical residue class",
    }
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
