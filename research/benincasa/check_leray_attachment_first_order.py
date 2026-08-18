"""Compute first-order motion of the weighted Leray attachment sections."""
from __future__ import annotations

import json

import sympy as sp

import check_physical_residue_at_weighted_tangencies as source

tau, r, n, x, y = sp.symbols("tau r n x y")
alpha, beta = sp.symbols("alpha beta")
energy = tau**2


def main() -> None:
    weighted = sp.expand(source.K.subs({
        source.x: x,
        source.y: y,
        source.z: energy - x - y,
        source.a: y + tau**2 * r,
        source.b: x - tau**2 * r + tau**3 * n,
    }))
    normalized = sp.expand(weighted / tau**6)
    leading = sp.factor(normalized.coeff(tau, 0))
    assert sp.factor(
        leading - (4 * x**2 * y**2 * n**2 + 8 * x * y * (x + y) * (r**2 - 1))
    ) == 0

    sections = {}
    for sign, label in ((-1, "minus"), (1, "plus")):
        trial = sp.expand(normalized.subs({n: 0, r: sign + alpha * tau + beta * tau**2}))
        alpha_value = sp.solve(sp.factor(trial.coeff(tau, 1)), alpha)[0]
        beta_value = sp.factor(
            sp.solve(sp.factor(trial.coeff(tau, 2).subs(alpha, alpha_value)), beta)[0]
        )
        assert alpha_value == 0
        expected_beta = -sign * (x + y) / (4 * x * y)
        assert sp.factor(beta_value - expected_beta) == 0
        sections[label] = {
            "special_point": sign,
            "tau_coefficient": str(alpha_value),
            "E_coefficient": str(beta_value),
        }

    print(json.dumps({
        "schema": "marici.leray-attachment-first-order.v1",
        "weighted_surface_lead": str(leading),
        "sections": sections,
        "boundary_vector": [-1, 1],
        "boundary_gauss_manin_first_order": [0, 0],
        "new_poles": [],
        "quartic_support": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
