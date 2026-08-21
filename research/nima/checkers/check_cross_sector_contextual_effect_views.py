#!/usr/bin/env python3
"""Exact audit of incompatible commutative effect views in scattering and flavor."""

import json
from pathlib import Path

import sympy as sp


def projectors(frame):
    return [frame[:, i] * frame[:, i].T for i in range(frame.cols)]


def overlap(left, right):
    return sp.Matrix(len(left), len(right), lambda i, j: sp.trace(left[i] * right[j]))


def bistochastic(m):
    return (
        all(sp.simplify(sum(m.row(i)) - 1) == 0 for i in range(m.rows))
        and all(sp.simplify(sum(m.col(j)) - 1) == 0 for j in range(m.cols))
        and all(x >= 0 for x in m)
    )


def some_incompatible(left, right):
    return any(a * b - b * a != sp.zeros(a.rows) for a in left for b in right)


def main():
    flavor_rotation = sp.Matrix([
        [sp.Rational(3, 5), sp.Rational(4, 5), 0],
        [-sp.Rational(4, 5), sp.Rational(3, 5), 0],
        [0, 0, 1],
    ]) * sp.Matrix([
        [1, 0, 0],
        [0, sp.Rational(5, 13), sp.Rational(12, 13)],
        [0, -sp.Rational(12, 13), sp.Rational(5, 13)],
    ])
    flavor_up = projectors(sp.eye(3))
    flavor_down = projectors(flavor_rotation)
    flavor_overlap = overlap(flavor_up, flavor_down)

    scatter_rotation = sp.Matrix([
        [sp.Rational(3, 5), sp.Rational(4, 5)],
        [-sp.Rational(4, 5), sp.Rational(3, 5)],
    ])
    scatter_helicity = projectors(sp.eye(2))
    scatter_analyzer = projectors(scatter_rotation)
    scatter_overlap = overlap(scatter_helicity, scatter_analyzer)

    checks = {
        "flavor_contexts_individually_commutative": all(
            a * b == b * a for context in (flavor_up, flavor_down)
            for a in context for b in context
        ),
        "flavor_contexts_mutually_incompatible": some_incompatible(flavor_up, flavor_down),
        "flavor_overlap_bistochastic": bistochastic(flavor_overlap),
        "scattering_contexts_individually_commutative": all(
            a * b == b * a for context in (scatter_helicity, scatter_analyzer)
            for a in context for b in context
        ),
        "scattering_contexts_mutually_incompatible": some_incompatible(
            scatter_helicity, scatter_analyzer
        ),
        "scattering_overlap_bistochastic": bistochastic(scatter_overlap),
    }

    payload = {
        "schema": "marici.cross-sector-contextual-effect-views.v1",
        "flavor_overlap": [[str(flavor_overlap[i, j]) for j in range(3)] for i in range(3)],
        "scattering_overlap": [[str(scatter_overlap[i, j]) for j in range(2)] for i in range(2)],
        "checks": checks,
        "all_passed": all(checks.values()),
        "verdict": (
            "Both sectors contain incompatible commutative effect views inside "
            "a noncommutative matrix algebra. Their context changes induce "
            "positive bistochastic overlap matrices."
        ),
    }
    out = Path(__file__).parents[1] / "results" / "cross-sector-contextual-effect-views.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if not payload["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
