"""Resolve physical tangency residues over the generic conductor sheets."""
from __future__ import annotations

import json

import sympy as sp

import check_physical_residue_at_weighted_tangencies as source

t, x, y, z = source.t, source.x, source.y, source.z


def reduced_tangent(substitution: dict[sp.Symbol, sp.Expr]) -> sp.Expr:
    restriction = sp.Poly(
        sp.expand(source.K.subs(substitution)),
        t,
        domain=sp.QQ.frac_field(x, y, z),
    )
    tangent = sp.gcd(restriction, restriction.diff()).monic().as_expr()
    return sp.Poly(
        sp.fraction(sp.together(tangent))[0], t, x, y, z
    ).as_expr()


def sheet_row(name: str, vanishing_root: sp.Expr) -> dict[str, object]:
    substitution, numerator, denominator = source.walls[name]
    tangent = reduced_tangent(substitution)
    conductor = sp.factor(tangent.subs(t, vanishing_root))
    unit_root = sp.factor(-vanishing_root)

    rows = []
    for label, root in (("vanishing", vanishing_root), ("deck_conjugate", unit_root)):
        values = {
            "sheet": label,
            "root_on_conductor": str(root),
            "numerator": str(sp.factor(numerator.subs(t, root))),
            "tangent_equation": str(sp.factor(tangent.subs(t, root))),
            "tangent_derivative": str(sp.factor(sp.diff(tangent, t).subs(t, root))),
            "remaining_denominator": str(sp.factor(denominator.subs(t, root))),
        }
        rows.append(values)

    assert sp.expand(numerator.subs(t, vanishing_root)) == 0
    assert sp.factor(tangent.subs(t, unit_root) - conductor) == 0
    assert sp.expand(numerator.subs(t, unit_root)) != 0
    assert sp.expand(sp.diff(tangent, t).subs(t, vanishing_root)) != 0
    assert sp.expand(sp.diff(tangent, t).subs(t, unit_root)) != 0
    assert sp.expand(denominator.subs(t, vanishing_root)) != 0
    assert sp.expand(denominator.subs(t, unit_root)) != 0

    return {
        "conductor": str(conductor),
        "generic_sheet_valuations": [1, 0],
        "deck_action": "exchanges the vanishing and unit sheets",
        "sheets": rows,
    }


def main() -> None:
    result = {
        "schema": "marici.physical-tangency-individual-sheets.v1",
        "walls": {
            "g1": sheet_row("g1", x - z),
            "g2": sheet_row("g2", y - z),
        },
        "generic_conductor_lattice": "saturated",
        "hidden_opposite_sheet_pole": False,
        "quartic_support": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
