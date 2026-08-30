#!/usr/bin/env python3
"""Exact elimination of the Gaussian convergence cone onto late-time readouts."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "results" / "de-sitter-gaussian-readout-cone.json"


def feasible(P: Fraction, S: Fraction, c: Fraction, s: Fraction) -> bool:
    """Eliminate Q from cQ-sP >= |S-Q| for -1<c<1."""
    lower = (S + s * P) / (1 + c)
    upper = (S - s * P) / (1 - c)
    return lower <= upper


def main() -> None:
    # Hostile exact rational points on the unit circle and a bounded lattice
    # verify the elimination identity without floating arithmetic.
    phases = [
        (Fraction(3, 5), Fraction(4, 5)),
        (Fraction(5, 13), Fraction(12, 13)),
        (Fraction(-3, 5), Fraction(4, 5)),
    ]
    tests = 0
    for c, s in phases:
        assert c * c + s * s == 1
        for p_int in range(-9, 10):
            for s_int in range(-9, 10):
                P, S = Fraction(p_int), Fraction(s_int)
                projected_half_plane = c * S - s * P >= 0
                assert feasible(P, S, c, s) == projected_half_plane
                tests += 1

    packet = {
        "schema": "marici.de_sitter_gaussian_readout_cone.v1",
        "source_convergence_cone": "beta+B>=0 and beta-B>=0, equivalently beta>=abs(B)",
        "horizontal_coordinates": {
            "C": "P+iQ=A r(x)^2",
            "N": "B(1+x^2)",
            "readout": "(P,S) with S=Q+N",
            "phase": "r(x)^2/(1+x^2)=c+i s",
        },
        "pre_elimination_inequality": "c Q-s P>=abs(N), N=S-Q",
        "elimination": {
            "Q_lower": "(S+sP)/(1+c)",
            "Q_upper": "(S-sP)/(1-c)",
            "projected_condition": "c S-s P>=0",
        },
        "projected_geometry": {
            "type": "closed half-plane through the origin",
            "dimension": 2,
            "interior": "c S-s P>0",
            "rank_collapse": False,
        },
        "stronger_B_nonpositive_check": (
            "Adding B<=0, equivalently N<=0, imposes Q>=S; for -1<c<1 "
            "the same projected condition cS-sP>=0 remains necessary and sufficient."
        ),
        "exact_grid_tests": tests,
        "qualification": (
            "This proves the projection of the ordinary convergent Gaussian quadratic-form cone. "
            "Complete positive-operator and uncertainty inequalities for the renormalized density "
            "matrix remain a stronger separate test."
        ),
        "classification": "physical coefficient cone over unchanged carrier",
    }
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"exact_tests": tests, "projected_dimension": 2, "rank_collapse": False}))


if __name__ == "__main__":
    main()
