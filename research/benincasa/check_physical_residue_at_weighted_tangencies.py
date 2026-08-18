"""Test the physical shared-wall residue on the reduced K-wall tangencies."""
from __future__ import annotations

import json
import sympy as sp

a, b, t, x, y, z = sp.symbols("a b t x y z")
E = x + y + z
K = (
    x**2 * a**4
    - (x**2 + y**2 - z**2) * a**2 * b**2
    + y**2 * b**4
    + (x**2 * (x**2 - y**2 - z**2) + E**2 * (y**2 - x**2 - z**2)) * a**2
    + (y**2 * (y**2 - x**2 - z**2) + E**2 * (x**2 - y**2 - z**2)) * b**2
    + z**2 * E**4 + E**2 * z**2 * (z**2 - x**2 - y**2) + z**2 * x**2 * y**2
)

# (wall substitution, physical residue numerator, remaining denominator product)
walls = {
    "g1": (
        {a: t, b: y + z},
        t + z - x,
        (y + z - x) * (t - y) * (t - x - z) * (t + y + 2*z),
    ),
    "g2": (
        {a: x + z, b: t},
        t + z - y,
        (t - x) * (x + z - y) * (t - y - z) * (x + t + 2*z),
    ),
    "g3": (
        {a: t, b: -z - t},
        -E,
        (-z - t - x) * (t - y) * (-t - y - 2*z) * (t - x - z),
    ),
}


def resultant(f: sp.Expr, g: sp.Expr) -> sp.Expr:
    return sp.factor(sp.resultant(f, g, t))


def main() -> None:
    rows = {}
    for name, (substitution, numerator, denominator) in walls.items():
        restriction = sp.Poly(sp.expand(K.subs(substitution)), t, domain=sp.QQ.frac_field(x, y, z))
        tangent = sp.gcd(restriction, restriction.diff()).monic().as_expr()
        tangent = sp.Poly(sp.fraction(sp.together(tangent))[0], t, x, y, z).as_expr()
        numerator_resultant = resultant(tangent, numerator)
        denominator_resultant = resultant(tangent, denominator)
        rows[name] = {
            "reduced_tangent_factor": str(sp.factor(tangent)),
            "physical_numerator_resultant": str(numerator_resultant),
            "physical_denominator_resultant": str(denominator_resultant),
            "generic_pairing_nonzero": numerator_resultant != 0,
            "generic_pairing_regular": denominator_resultant != 0,
        }
        assert numerator_resultant != 0
        assert denominator_resultant != 0

    print(json.dumps({
        "schema": "marici.physical-residue-weighted-tangency-pairing.v1",
        "walls": rows,
        "all_generic_pairings_regular_and_nonzero": all(
            row["generic_pairing_nonzero"] and row["generic_pairing_regular"]
            for row in rows.values()
        ),
        "pairing_type": "weighted exceptional Stokes functional times physical wall residue",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
