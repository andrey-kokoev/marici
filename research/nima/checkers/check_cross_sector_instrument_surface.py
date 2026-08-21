#!/usr/bin/env python3
"""Exact formal instrument-completion and diagnostic-refinement audit."""

import json
from pathlib import Path

import sympy as sp


def projectors(frame):
    return [frame[:, i] * frame[:, i].T for i in range(frame.cols)]


def instrument(effect, state):
    return sp.simplify(effect * state * effect)


def trace(m):
    return sp.simplify(sp.trace(m))


def main():
    # Scattering analyzer context.
    rot2 = sp.Matrix([
        [sp.Rational(3, 5), sp.Rational(4, 5)],
        [-sp.Rational(4, 5), sp.Rational(3, 5)],
    ])
    scatter_effects = projectors(rot2)
    scatter_state = sp.diag(sp.Rational(9, 25), sp.Rational(16, 25))
    scatter_branches = [instrument(e, scatter_state) for e in scatter_effects]
    scatter_probs = [trace(x) for x in scatter_branches]
    scatter_post = [sp.simplify(x / trace(x)) for x in scatter_branches]

    # Flavor down-mass context acting on a selected up-mass state.
    rot3 = sp.Matrix([
        [sp.Rational(3, 5), sp.Rational(4, 5), 0],
        [-sp.Rational(4, 5), sp.Rational(3, 5), 0],
        [0, 0, 1],
    ]) * sp.Matrix([
        [1, 0, 0],
        [0, sp.Rational(5, 13), sp.Rational(12, 13)],
        [0, -sp.Rational(12, 13), sp.Rational(5, 13)],
    ])
    flavor_effects = projectors(rot3)
    flavor_state = sp.diag(1, 0, 0)
    flavor_branches = [instrument(e, flavor_state) for e in flavor_effects]
    flavor_probs = [trace(x) for x in flavor_branches]
    flavor_post = [
        sp.simplify(x / trace(x)) if trace(x) != 0 else None
        for x in flavor_branches
    ]

    # Same public coarse effect, different hidden backaction.
    e0, e1, e2 = projectors(sp.eye(3))
    coherent = sp.Matrix([
        [sp.Rational(1, 2), sp.Rational(1, 4), 0],
        [sp.Rational(1, 4), sp.Rational(1, 2), 0],
        [0, 0, 0],
    ])
    coarse_effect = e0 + e1
    direct_coarse = instrument(coarse_effect, coherent)
    fine_then_forget = instrument(e0, coherent) + instrument(e1, coherent)

    checks = {
        "scattering_outcomes_normalize": sp.simplify(sum(scatter_probs) - 1) == 0,
        "scattering_poststates_normalize": all(trace(x) == 1 for x in scatter_post),
        "scattering_instrument_repeatable": all(
            instrument(scatter_effects[i], scatter_post[i]) == scatter_post[i]
            for i in range(2)
        ),
        "flavor_outcomes_normalize": sp.simplify(sum(flavor_probs) - 1) == 0,
        "flavor_nonzero_poststates_normalize": all(
            x is None or trace(x) == 1 for x in flavor_post
        ),
        "flavor_instrument_repeatable": all(
            flavor_post[i] is None
            or instrument(flavor_effects[i], flavor_post[i]) == flavor_post[i]
            for i in range(3)
        ),
        "public_coarse_probability_agrees": trace(direct_coarse) == trace(fine_then_forget),
        "diagnostic_refinement_changes_backaction": direct_coarse != fine_then_forget,
        "direct_coarse_preserves_hidden_coherence": direct_coarse[0, 1] != 0,
        "fine_then_forget_erases_hidden_coherence": fine_then_forget[0, 1] == 0,
    }

    payload = {
        "schema": "marici.formal-instrument-completion.v2",
        "scattering_probabilities": [str(x) for x in scatter_probs],
        "flavor_probabilities": [str(x) for x in flavor_probs],
        "coarse_probability": str(trace(direct_coarse)),
        "direct_coarse_state": [[str(x) for x in direct_coarse.row(i)] for i in range(3)],
        "fine_then_forget_state": [[str(x) for x in fine_then_forget.row(i)] for i in range(3)],
        "checks": checks,
        "all_passed": all(checks.values()),
        "verdict": (
            "The scattering and flavor effect algebras admit repeatable formal "
            "Luders instrument completions. A fine diagnostic completion and a "
            "direct coarse completion can return the same probability while "
            "inducing different backaction. The checker does not establish that "
            "either physical source selects these state-update maps."
        ),
        "scope": (
            "Formal Hilbert-space completion only; source-derived scattering "
            "detector dynamics and flavor transition instruments remain absent."
        ),
    }
    out = Path(__file__).parents[1] / "results" / "cross-sector-instrument-surface.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if not payload["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
