#!/usr/bin/env python3
"""Exact obstruction/refinement test for a common probability-readout interface."""

import json
from pathlib import Path

import sympy as sp


def normalize(v):
    total = sum(v)
    return sp.simplify(v / total)


def projective_action(k, v):
    return normalize(k * v)


def main():
    p = sp.Matrix([1, 0])
    q = sp.Matrix([0, 1])
    midpoint = (p + q) / 2

    biased = sp.diag(1, 2)
    scalar = 2 * sp.eye(2)
    stochastic = sp.Matrix([[sp.Rational(2, 3), sp.Rational(1, 4)],
                            [sp.Rational(1, 3), sp.Rational(3, 4)]])
    second_filter = sp.Matrix([[2, 1], [1, 3]])

    biased_midpoint = projective_action(biased, midpoint)
    midpoint_of_biased_endpoints = (
        projective_action(biased, p) + projective_action(biased, q)
    ) / 2

    generic = sp.Matrix([sp.Rational(2, 5), sp.Rational(3, 5)])
    composed = projective_action(second_filter, biased * generic)
    sequential = projective_action(second_filter, projective_action(biased, generic))

    checks = {
        "biased_postselection_is_not_affine": biased_midpoint != midpoint_of_biased_endpoints,
        "scalar_acceptance_is_identity_after_normalization": projective_action(scalar, generic) == generic,
        "stochastic_map_preserves_normalization_linearly": sum(stochastic * generic) == 1,
        "projective_positive_composition_is_strict": sp.simplify(composed - sequential) == sp.zeros(2, 1),
        "positive_filter_preserves_positive_cone": all(x >= 0 for x in biased * generic),
    }

    payload = {
        "schema": "marici.projective-positive-readout-interface.v1",
        "biased_midpoint": [str(x) for x in biased_midpoint],
        "midpoint_of_biased_endpoints": [str(x) for x in midpoint_of_biased_endpoints],
        "checks": checks,
        "all_passed": all(checks.values()),
        "verdict": (
            "FinStoch is too narrow for the common readout calculus. "
            "Sector maps live naturally as positive linear maps on unnormalized "
            "cones; normalization projectivizes them. These projective actions "
            "compose strictly but are generally non-affine on normalized states."
        ),
    }

    out = Path(__file__).parents[1] / "results" / "projective-positive-readout-interface.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if not payload["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
