#!/usr/bin/env python3
"""Prove the rank-one D3 no-go and construct the minimal rank-two escape."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "d3-mu3-activation-no-go.json"


def main() -> None:
    # Scalar roots satisfying both lambda^3=1 and lambda=lambda^-1.
    x = sp.symbols("x")
    common = sp.gcd(sp.Poly(x**3 - 1, x), sp.Poly(x**2 - 1, x))
    assert common.as_expr() == x - 1

    R = sp.Matrix([[0, -1], [1, -1]])
    K = sp.Matrix([[1, -1], [0, -1]])
    identity = sp.eye(2)
    assert R**3 == identity
    assert K**2 == identity
    assert K * R * K == R.inv()
    assert R.trace() == -1
    assert R.det() == 1
    assert R.charpoly(x).as_expr() == x**2 + x + 1

    result = {
        "status": "PASS",
        "rank_one_constraints": ["lambda^3=1", "lambda=lambda^-1"],
        "rank_one_common_polynomial": str(common.as_expr()),
        "rank_one_allowed_holonomy": [1],
        "mu2_intersection_mu3": [1],
        "primitive_rank_one_activation_possible": False,
        "minimal_linear_D3_rank": 2,
        "rank_two_rotation": [[int(v) for v in row] for row in R.tolist()],
        "rank_two_reflection": [[int(v) for v in row] for row in K.tolist()],
        "rank_two_rotation_characteristic_polynomial": "x^2+x+1",
        "rank_two_rotation_trace": int(R.trace()),
        "rank_two_D3_relations_pass": True,
        "progressive_reopening_target": "source-derived conjugate rank-two coefficient transport",
        "other_typed_escapes": ["reflection breaking", "anti-linear reflection"],
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
