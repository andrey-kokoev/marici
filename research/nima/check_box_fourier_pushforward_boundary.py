"""Exact endpoint audit for a compactly supported vertex Fourier density."""

from __future__ import annotations

import json
from pathlib import Path

from collections import defaultdict


def main() -> None:
    # Sparse polynomials in Z[q,Lambda], keyed by (deg_q, deg_Lambda).
    q = {(1, 0): 1}
    lam = {(0, 1): 1}

    def add(left, right, scale=1):
        out = defaultdict(int, left)
        for monomial, coefficient in right.items():
            out[monomial] += scale * coefficient
        return {m: c for m, c in out.items() if c}

    def multiply(left, right):
        out = defaultdict(int)
        for (iq, il), a in left.items():
            for (jq, jl), b in right.items():
                out[(iq + jq, il + jl)] += a * b
        return {m: c for m, c in out.items() if c}

    def derivative_q(poly):
        return {(iq - 1, il): iq * c for (iq, il), c in poly.items() if iq}

    def substitute_q_equals_c_lambda(poly, c):
        out = defaultdict(int)
        for (iq, il), coefficient in poly.items():
            out[iq + il] += coefficient * c**iq
        return {degree: coefficient for degree, coefficient in out.items() if coefficient}

    q_plus_lam = add(q, lam)
    numerator = add(q, q_plus_lam, scale=-1)  # q-(q+Lambda)=-Lambda
    denominator = multiply(q, q_plus_lam)
    denominator_prime = derivative_q(denominator)

    assert numerator == {(0, 1): -1}
    assert denominator == {(2, 0): 1, (1, 1): 1}
    assert substitute_q_equals_c_lambda(denominator_prime, 0) == {1: 1}
    assert substitute_q_equals_c_lambda(denominator_prime, -1) == {1: -1}

    # For a simple pole N/D, Res=N(root)/D'(root).
    residue_zero = -1
    residue_left = 1
    residue_infinity = -(residue_zero + residue_left)

    result = {
        "schema": "marici.box-fourier-pushforward-boundary.v1",
        "density_support": "epsilon in [0,Lambda]",
        "translated_wall": "q+epsilon=0",
        "pushforward": "log(q+Lambda)-log(q)",
        "connection": "-Lambda/(q*(q+Lambda)) dq",
        "oriented_endpoint_residues": {"q=0": -1, "q=-Lambda": 1, "q=infinity": 0},
        "residue_sum": 0,
        "conclusion": (
            "The compact support projects the existing translated wall to a "
            "branch interval whose boundary is exactly the two support endpoints; "
            "no additional carrier incidence is required."
        ),
    }
    out = Path(__file__).with_name("results") / "box-fourier-pushforward-boundary.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
