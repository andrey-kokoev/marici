"""Eliminate shared-wall tangent roots against the wall-normal K derivative."""
from __future__ import annotations

import json
import sympy as sp

a, b, t, x, y, z = sp.symbols("a b t x y z")
E = x + y + z
x2, y2, z2, E2 = x**2, y**2, z**2, E**2
K = (
    x2 * a**4
    - (x2 + y2 - z2) * a**2 * b**2
    + y2 * b**4
    + (x2 * (x2 - y2 - z2) + E2 * (y2 - x2 - z2)) * a**2
    + (y2 * (y2 - x2 - z2) + E2 * (x2 - y2 - z2)) * b**2
    + z2 * E2**2
    + E2 * z2 * (z2 - x2 - y2)
    + z2 * x2 * y2
)
Q = sp.expand(
    -16 * (x * y) ** 2
    - 8 * x * y * E**2
    + 8 * (x + y) * E**3
    - 5 * E**4
)

walls = {
    "g1": ({a: t, b: y + z}, sp.diff(K, b)),
    "g2": ({a: x + z, b: t}, sp.diff(K, a)),
    "g3": ({a: t, b: -z - t}, sp.diff(K, a)),
}


def normalized_factor_list(poly: sp.Expr) -> list[dict[str, object]]:
    coefficient, factors = sp.factor_list(sp.Poly(poly, x, y, z))
    return [
        {"factor": str(sp.factor(factor.as_expr())), "multiplicity": multiplicity}
        for factor, multiplicity in factors
    ]


def main() -> None:
    rows = {}
    product = sp.Integer(1)
    for name, (substitution, normal_derivative) in walls.items():
        restriction = sp.Poly(sp.expand(K.subs(substitution)), t, domain=sp.QQ.frac_field(x, y, z))
        tangent_factor = sp.gcd(restriction, restriction.diff())
        tangent_expr = sp.together(tangent_factor.monic().as_expr())
        tangent_num = sp.Poly(sp.fraction(tangent_expr)[0], t, x, y, z).as_expr()
        normal = sp.Poly(sp.expand(normal_derivative.subs(substitution)), t)
        resultant = sp.factor(sp.resultant(tangent_num, normal.as_expr(), t))
        product = sp.expand(product * resultant)
        rows[name] = {
            "restriction_factorization": str(sp.factor(restriction.as_expr())),
            "repeated_tangent_factor": str(sp.factor(tangent_num)),
            "normal_resultant": str(resultant),
            "normal_resultant_factors": normalized_factor_list(resultant),
            "gcd_with_Q": str(sp.factor(sp.gcd(sp.Poly(resultant, x, y, z), sp.Poly(Q, x, y, z)).as_expr())),
        }

    product_gcd = sp.factor(sp.gcd(sp.Poly(product, x, y, z), sp.Poly(Q, x, y, z)).as_expr())
    result = {
        "schema": "marici.shared-wall-higher-tangency-support.v1",
        "quartic_Q": str(sp.factor(Q)),
        "walls": rows,
        "product_gcd_with_Q": str(product_gcd),
        "Q_is_higher_tangency_support": product_gcd != 1,
        "classification": "shared-wall weighted-corner coefficient support",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
