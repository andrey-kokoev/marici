"""Derive the norm divisor of the physical residue on each tangency double cover."""
from __future__ import annotations

import json
import sympy as sp

import check_physical_residue_at_weighted_tangencies as source

t, x, y, z = source.t, source.x, source.y, source.z
Q = sp.expand(
    -16 * (x * y) ** 2
    - 8 * x * y * source.E**2
    + 8 * (x + y) * source.E**3
    - 5 * source.E**4
)


def factors(expr: sp.Expr) -> list[dict[str, object]]:
    coefficient, rows = sp.factor_list(sp.Poly(expr, x, y, z))
    return [
        {"factor": str(sp.factor(factor.as_expr())), "multiplicity": multiplicity}
        for factor, multiplicity in rows
    ]


def main() -> None:
    rows = {}
    total_numerator = sp.Integer(1)
    total_denominator = sp.Integer(1)
    for name, (substitution, numerator, denominator) in source.walls.items():
        restriction = sp.Poly(
            sp.expand(source.K.subs(substitution)),
            t,
            domain=sp.QQ.frac_field(x, y, z),
        )
        tangent = sp.gcd(restriction, restriction.diff()).monic().as_expr()
        tangent = sp.Poly(
            sp.fraction(sp.together(tangent))[0], t, x, y, z
        ).as_expr()
        h = sp.Poly(tangent, t)
        lc = h.LC()
        degree_n = sp.degree(numerator, t)
        degree_d = sp.degree(denominator, t)
        res_n = sp.resultant(tangent, numerator, t)
        res_hprime = sp.resultant(tangent, sp.diff(tangent, t), t)
        res_d = sp.resultant(tangent, denominator, t)

        # Product over the two roots r of N(r)/(h'(r)D(r)).
        norm = sp.cancel(
            res_n * lc ** (1 + degree_d - degree_n) / (res_hprime * res_d)
        )
        norm_n, norm_d = map(sp.factor, sp.fraction(norm))
        total_numerator *= norm_n
        total_denominator *= norm_d
        rows[name] = {
            "norm": str(sp.factor(norm)),
            "zero_divisor": factors(norm_n),
            "pole_divisor": factors(norm_d),
            "gcd_zero_divisor_with_Q": str(
                sp.factor(sp.gcd(sp.Poly(norm_n, x, y, z), sp.Poly(Q, x, y, z)).as_expr())
            ),
            "gcd_pole_divisor_with_Q": str(
                sp.factor(sp.gcd(sp.Poly(norm_d, x, y, z), sp.Poly(Q, x, y, z)).as_expr())
            ),
        }

    total_numerator = sp.factor(total_numerator)
    total_denominator = sp.factor(total_denominator)
    result = {
        "schema": "marici.physical-tangency-residue-norm.v1",
        "walls": rows,
        "total_zero_divisor": factors(total_numerator),
        "total_pole_divisor": factors(total_denominator),
        "total_zero_gcd_with_Q": str(
            sp.factor(sp.gcd(sp.Poly(total_numerator, x, y, z), sp.Poly(Q, x, y, z)).as_expr())
        ),
        "total_pole_gcd_with_Q": str(
            sp.factor(sp.gcd(sp.Poly(total_denominator, x, y, z), sp.Poly(Q, x, y, z)).as_expr())
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
