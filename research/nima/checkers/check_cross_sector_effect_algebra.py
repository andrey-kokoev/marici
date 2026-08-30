#!/usr/bin/env python3
"""Exact scattering/flavor comparison through finite commutative effect algebras."""

import json
from pathlib import Path

import sympy as sp


def born(state, effect):
    return sp.simplify(sp.trace(state * effect))


def rank_one_projectors(frame):
    return [frame[:, i] * frame[:, i].T for i in range(frame.cols)]


def main():
    # Flavor: a fixed up-type mass eigenstate interrogated by the three
    # down-type spectral effects.
    v12 = sp.Matrix([[sp.Rational(3, 5), sp.Rational(4, 5), 0],
                     [-sp.Rational(4, 5), sp.Rational(3, 5), 0],
                     [0, 0, 1]])
    v23 = sp.Matrix([[1, 0, 0],
                     [0, sp.Rational(5, 13), sp.Rational(12, 13)],
                     [0, -sp.Rational(12, 13), sp.Rational(5, 13)]])
    v = v12 * v23
    flavor_state = sp.diag(1, 0, 0)
    flavor_effects = rank_one_projectors(v)
    flavor_p = [born(flavor_state, e) for e in flavor_effects]
    flavor_coarse = flavor_effects[0] + flavor_effects[1]

    # Scattering: a reduced helicity density state interrogated by the two
    # helicity effects. This is the exact Schmidt example (3,4).
    scatter_state = sp.diag(sp.Rational(9, 25), sp.Rational(16, 25))
    scatter_effects = [sp.diag(1, 0), sp.diag(0, 1)]
    scatter_p = [born(scatter_state, e) for e in scatter_effects]
    scatter_coarse = scatter_effects[0] + scatter_effects[1]

    checks = {
        "flavor_effects_complete": sum(flavor_effects, sp.zeros(3)) == sp.eye(3),
        "flavor_effects_orthogonal": all(
            flavor_effects[i] * flavor_effects[j] == sp.zeros(3)
            for i in range(3) for j in range(3) if i != j
        ),
        "flavor_effects_idempotent": all(e * e == e for e in flavor_effects),
        "flavor_state_trace_one": sp.trace(flavor_state) == 1,
        "flavor_probabilities_positive": all(x >= 0 for x in flavor_p),
        "flavor_probabilities_normalized": sp.simplify(sum(flavor_p) - 1) == 0,
        "flavor_coarse_probability_is_sum": (
            born(flavor_state, flavor_coarse) == flavor_p[0] + flavor_p[1]
        ),
        "scattering_effects_complete": sum(scatter_effects, sp.zeros(2)) == sp.eye(2),
        "scattering_effects_idempotent": all(e * e == e for e in scatter_effects),
        "scattering_state_trace_one": sp.trace(scatter_state) == 1,
        "scattering_probabilities_positive": all(x >= 0 for x in scatter_p),
        "scattering_probabilities_normalized": sp.simplify(sum(scatter_p) - 1) == 0,
        "scattering_coarse_probability_is_sum": (
            born(scatter_state, scatter_coarse) == sum(scatter_p)
        ),
    }

    payload = {
        "schema": "marici.cross-sector-effect-algebra.v1",
        "flavor_probabilities": [str(x) for x in flavor_p],
        "scattering_probabilities": [str(x) for x in scatter_p],
        "checks": checks,
        "all_passed": all(checks.values()),
        "verdict": (
            "Flavor spectral transitions and scattering helicity reduction "
            "instantiate the same finite commutative effect-algebra interface: "
            "a positive normalized state paired with orthogonal exhaustive "
            "effects, with coarse-graining implemented by effect addition."
        ),
    }
    out = Path(__file__).parents[1] / "results" / "cross-sector-effect-algebra.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if not payload["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
