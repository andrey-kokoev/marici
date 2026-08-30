#!/usr/bin/env python3
"""Exact projection of the one-mode Gaussian CP cone to late-time readouts."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "results" / "de-sitter-complete-positive-readout.json"


def pure_lift(P: Fraction, S: Fraction) -> tuple[Fraction, Fraction]:
    """Return nu and |kappa|^2 for a pure lift when S>-1/2."""
    denominator = 2 * S + 1
    assert denominator > 0
    nu = (P * P + S * S) / denominator
    kappa_squared = P * P + (S - nu) * (S - nu)
    assert kappa_squared == nu * (nu + 1)
    return nu, kappa_squared


def main() -> None:
    tests = 0
    # Exact constructive verification over a rational grid in the predicted
    # image. The algebraic identity in pure_lift is the proof.
    for p_num in range(-12, 13):
        for s_num in range(-4, 13):
            P = Fraction(p_num, 3)
            S = Fraction(s_num, 7)
            if S > Fraction(-1, 2):
                nu, k2 = pure_lift(P, S)
                assert nu >= 0 and k2 >= 0
                tests += 1

    # Below or on the boundary, positivity would imply
    # P^2+S^2 <= (2S+1)nu, whose RHS is nonpositive while the LHS is
    # strictly positive at S<=-1/2.
    for S in [Fraction(-1, 2), Fraction(-3, 4), Fraction(-2)]:
        assert 2 * S + 1 <= 0
        assert S * S > 0

    packet = {
        "schema": "marici.de_sitter_complete_positive_readout.v1",
        "intrinsic_gaussian_condition": "nu>=0 and abs(kappa)^2<=nu(nu+1)",
        "readout_typing": (
            "After the source mode-phase rotation, P is one anomalous quadrature and "
            "S=nu plus the orthogonal anomalous quadrature."
        ),
        "elimination_identity": (
            "P^2+(S-nu)^2<=nu(nu+1) iff P^2+S^2<=(2S+1)nu"
        ),
        "image": {
            "condition": "S>-1/2",
            "type": "open half-plane",
            "dimension": 2,
            "boundary": "S=-1/2 is approached only as nu tends to infinity",
            "rank_collapse": False,
        },
        "constructive_pure_lift": {
            "nu": "(P^2+S^2)/(2S+1)",
            "orthogonal_kappa_quadrature": "S-nu",
            "identity": "P^2+(S-nu)^2=nu(nu+1)",
        },
        "exact_constructive_tests": tests,
        "conclusion": (
            "Complete one-mode Gaussian positivity preserves a two-dimensional late-time "
            "readout. It supplies the universal lower bound S>-1/2 rather than a projective ray."
        ),
        "classification": "physical covariance cone over unchanged carrier",
    }
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"exact_pure_lifts": tests, "image": "S>-1/2", "dimension": 2}))


if __name__ == "__main__":
    main()
