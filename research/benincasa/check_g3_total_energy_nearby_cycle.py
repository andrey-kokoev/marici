"""Compute the leading g3 physical residue on the E^(1/2) cover."""
from __future__ import annotations

import json

import sympy as sp

import check_physical_residue_at_weighted_tangencies as source

t, x, y, z = source.t, source.x, source.y, source.z
q, w, lam = sp.symbols("q w lam")
energy = q**2
center = x + z


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

    local = {y: energy - x - z, t: -center + w}
    h_local = sp.expand(tangent.subs(local))
    d_local = sp.factor(denominator.subs(local))
    hp_local = sp.expand(sp.diff(tangent, t).subs(local))

    branch = {w: lam * q}
    h_lead = sp.expand(h_local.subs(branch)).coeff(q, 2)
    hp_lead = sp.expand(hp_local.subs(branch)).coeff(q, 1)
    d_lead = sp.expand(d_local.subs(branch)).coeff(q, 2)
    n_lead = sp.expand(numerator.subs(local).subs(branch)).coeff(q, 2)
    relation = {lam**2: -2 * x * center / z}
    h_lead_reduced = sp.factor(h_lead.xreplace(relation))
    residue_coefficient = sp.factor(n_lead / (hp_lead * d_lead))
    target_coefficient = 1 / (16 * lam * x**2 * center**2)

    assert h_lead_reduced == 0
    assert sp.factor(hp_lead - 2 * z * lam) == 0
    assert sp.factor(d_lead - 4 * x * center * lam**2) == 0
    assert n_lead == -1
    assert sp.factor((residue_coefficient / target_coefficient).subs(relation)) == 1

    result = {
        "schema": "marici.g3-total-energy-nearby-cycle.v1",
        "local_cover": str(sp.factor(h_local)),
        "puiseux_relation": "lambda^2 = -2*x*(x+z)/z",
        "residue_q_order": -1,
        "leading_residue": "1/(16*lambda*x^2*(x+z)^2) * q^-1",
        "deck_character": "odd",
        "regularized_generator": "q*rho",
        "ordinary_logarithmic_extension": False,
        "kummer_nearby_cycle_required": True,
        "quartic_support": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
