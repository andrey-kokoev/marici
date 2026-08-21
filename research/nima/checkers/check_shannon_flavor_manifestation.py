#!/usr/bin/env python3
"""Exact basis-free Shannon manifestation test in the three-flavor sector."""

import json
from pathlib import Path

import sympy as sp


def rational_rotation_12(c, s):
    return sp.Matrix([[c, s, 0], [-s, c, 0], [0, 0, 1]])


def rational_rotation_23(c, s):
    return sp.Matrix([[1, 0, 0], [0, c, s], [0, -s, c]])


def projectors(frame):
    return [frame[:, i] * frame[:, i].T for i in range(3)]


def transition(up_projectors, down_projectors):
    return sp.Matrix(3, 3, lambda i, j: sp.trace(up_projectors[i] * down_projectors[j]))


def main():
    # Two nontrivial rational points on SO(2), composed into a generic SO(3)
    # element. All verification remains over Q.
    v = rational_rotation_12(sp.Rational(3, 5), sp.Rational(4, 5))
    v *= rational_rotation_23(sp.Rational(5, 13), sp.Rational(12, 13))
    u = rational_rotation_23(sp.Rational(7, 25), sp.Rational(24, 25))
    u *= rational_rotation_12(sp.Rational(20, 29), sp.Rational(21, 29))

    identity = sp.eye(3)
    p = transition(projectors(identity), projectors(v))
    p_rotated = transition(projectors(u), projectors(u * v))

    permutation_u = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    permutation_d = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    p_relabelled = transition(
        projectors(identity * permutation_u),
        projectors(v * permutation_d),
    )

    checks = {
        "orthogonal_flavor_frame": sp.simplify(v.T * v - identity) == sp.zeros(3),
        "orthogonal_weak_basis_change": sp.simplify(u.T * u - identity) == sp.zeros(3),
        "positive_weights": all(value >= 0 for value in p),
        "row_normalization": all(sp.simplify(sum(p.row(i)) - 1) == 0 for i in range(3)),
        "column_normalization": all(sp.simplify(sum(p.col(j)) - 1) == 0 for j in range(3)),
        "weak_basis_invariance": sp.simplify(p_rotated - p) == sp.zeros(3),
        "relabeling_covariance": sp.simplify(
            p_relabelled - permutation_u.T * p * permutation_d
        ) == sp.zeros(3),
    }

    # Shannon additivity follows entrywise from log(p_i q_j)=log p_i+log q_j.
    # Record the exact coefficient identity, leaving logarithms formal.
    a, b, c, d = sp.symbols("a b c d", positive=True)
    product_additivity_residual = sp.expand(
        -sum(x * y * (sp.log(x) + sp.log(y)) for x in (a, b) for y in (c, d))
        + sum(x * sp.log(x) for x in (a, b)) * (c + d)
        + sum(y * sp.log(y) for y in (c, d)) * (a + b)
    ).subs({a + b: 1, c + d: 1})
    # SymPy does not rewrite additive assumptions in subs; check coefficients
    # directly under b=1-a,d=1-c.
    checks["product_additivity"] = sp.simplify(
        product_additivity_residual.subs({b: 1 - a, d: 1 - c})
    ) == 0

    payload = {
        "schema": "marici.shannon-flavor-manifestation.v1",
        "transition_matrix": [[str(p[i, j]) for j in range(3)] for i in range(3)],
        "checks": checks,
        "all_passed": all(checks.values()),
        "interpretation": (
            "The spectral-projector overlap matrix is a positive bistochastic "
            "weak-basis invariant. Each physically labelled row is a canonical "
            "conditional probability distribution; Shannon entropy is invariant "
            "under weak-basis changes and covariant under flavor relabeling."
        ),
    }
    out = Path(__file__).parents[1] / "results" / "shannon-flavor-manifestation.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if not payload["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
