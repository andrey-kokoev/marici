"""Separate etale sheet collisions from ramification in physical tangency residues."""
from __future__ import annotations

import json
import sympy as sp

import check_physical_residue_at_weighted_tangencies as source

t, x, y, z = source.t, source.x, source.y, source.z


def irreducible_factors(expr: sp.Expr) -> list[tuple[sp.Expr, int]]:
    return [
        (sp.factor(poly.as_expr()), multiplicity)
        for poly, multiplicity in sp.factor_list(sp.Poly(expr, x, y, z))[1]
    ]


def main() -> None:
    rows = {}
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
        discriminant = sp.factor(sp.discriminant(tangent, t))
        res_n = sp.factor(sp.resultant(tangent, numerator, t))
        res_d = sp.factor(sp.resultant(tangent, denominator, t))

        boundary_rows = []
        for kind, resultant in (("zero", res_n), ("pole", res_d)):
            for factor, multiplicity in irreducible_factors(resultant):
                ramified = sp.rem(
                    sp.Poly(discriminant, x, y, z),
                    sp.Poly(factor, x, y, z),
                ).is_zero
                boundary_rows.append(
                    {
                        "kind": kind,
                        "factor": str(factor),
                        "resultant_multiplicity": multiplicity,
                        "divides_cover_discriminant": bool(ramified),
                        "generic_local_type": (
                            "ramified collision"
                            if ramified
                            else "etale one-sheet valuation"
                        ),
                    }
                )
        rows[name] = {
            "cover_discriminant": str(discriminant),
            "boundaries": boundary_rows,
            "all_nonramification_resultant_factors_are_etale": all(
                row["generic_local_type"] == "etale one-sheet valuation"
                for row in boundary_rows
                if not row["divides_cover_discriminant"]
            ),
        }

    print(
        json.dumps(
            {
                "schema": "marici.physical-tangency-sheet-boundaries.v1",
                "walls": rows,
                "classification": (
                    "conductor and marked-section collisions are one-sheet "
                    "valuations off the separate tangency-discriminant locus"
                ),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
