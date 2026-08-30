#!/usr/bin/env python3
"""Exact third-grade separation of the Gaussian initial-state pair at freeze-out."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "results" / "de-sitter-initial-state-freezeout-grade.json"


ComplexQ = tuple[Fraction, Fraction]


def cmul(a: ComplexQ, b: ComplexQ) -> ComplexQ:
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cadd(a: ComplexQ, b: ComplexQ) -> ComplexQ:
    return (a[0] + b[0], a[1] + b[1])


def convolve(a: list[ComplexQ], b: list[ComplexQ], degree: int) -> list[ComplexQ]:
    out = [(Fraction(0), Fraction(0))] * (degree + 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if i + j <= degree:
                out[i + j] = cadd(out[i + j], cmul(ai, bj))
    return out


def main() -> None:
    # q(y)=(1+i y)e^{-i y}, through y^3, in exact rational arithmetic.
    exp_minus_iy = [
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(-1)),
        (Fraction(-1, 2), Fraction(0)),
        (Fraction(0), Fraction(1, 6)),
    ]
    q = convolve([(Fraction(1), Fraction(0)), (Fraction(0), Fraction(1))], exp_minus_iy, 3)
    q2 = convolve(q, q, 3)

    assert q == [
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0)),
        (Fraction(1, 2), Fraction(0)),
        (Fraction(0), Fraction(-1, 3)),
    ]
    assert q2 == [
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(-2, 3)),
    ]

    # If r(x)^2=U+iV and R=|r(x)|^2=1+x^2, then the equal-time
    # linearized correction has coefficient rows below after taking actual
    # y-derivatives at y=0 (rather than Taylor coefficients).
    rows = {
        "grade_0": ["2 U", "2 R"],
        "grade_1": ["0", "0"],
        "grade_2": ["4 U", "4 R"],
        "grade_3": ["8 V", "0"],
    }
    determinant_03 = "-16 R V"

    packet = {
        "schema": "marici.de_sitter_initial_state_freezeout_grade.v1",
        "source_mode_factors": {
            "late_time": "q(y)=(1+i y) exp(-i y), y=k eta",
            "initial": "r(x)=(1-i x) exp(i x), x=k eta0",
            "definitions": {
                "U": "Re(r(x)^2)=(1-x^2) cos(2x)+2x sin(2x)",
                "V": "Im(r(x)^2)=(1-x^2) sin(2x)-2x cos(2x)",
                "R": "abs(r(x))^2=1+x^2",
            },
        },
        "q_taylor_through_degree_3": ["1", "0", "1/2", "-i/3"],
        "q_squared_taylor_through_degree_3": ["1", "0", "1", "-2i/3"],
        "derivative_rows_beta_B": rows,
        "rank_audit": {
            "grades_0_only": 1,
            "grades_0_to_1": 1,
            "grades_0_to_2": 1,
            "grades_0_to_3_generic": 2,
            "determinant_grades_0_and_3": determinant_03,
            "exceptional_locus": "V(x)=0 (R=1+x^2 is positive on real x)",
        },
        "conclusion": (
            "de Sitter freeze-out collapses the ordinary, first, and second normal readouts "
            "to one coefficient combination; the third conformal-time normal grade generically "
            "restores the beta direction and yields rank two."
        ),
        "classification": "higher readout filtration; no new carrier incidence",
    }
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ranks": [1, 1, 1, 2], "determinant_03": determinant_03}))


if __name__ == "__main__":
    main()
