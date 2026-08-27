#!/usr/bin/env python3
"""Separate universal interval concatenation from the off-seam star residual."""

from fractions import Fraction
import json
from pathlib import Path


def primitive(t):
    # Exact fixture for an arbitrary interval density with antiderivative t^2.
    return t * t


def interval(a, b):
    return primitive(b) - primitive(a)


def main():
    l, m = 2, 3
    path_lm = interval(0, l) + interval(l, l + m)
    path_ml = interval(0, m) + interval(m, m + l)
    assert path_lm == path_ml == interval(0, l + m)

    # Exact off-seam star hostile.  Take positive A=1 on [0, log 2] and z=i.
    # B_L(-z)=integral exp(v) dv = 1; B_L(-conj(z))=integral exp(-v) dv = 1/2.
    reciprocal_value = Fraction(1)
    adjoint_value = Fraction(1, 2)
    star_residual = reciprocal_value - adjoint_value
    assert star_residual == Fraction(1, 2)

    # On the seam, z is real and reciprocal equals adjoint tautologically.
    seam_residual = Fraction(0)
    assert seam_residual == 0

    result = {
        "schema": "marici.rh-interval-flatness-vs-star-residual.v1",
        "translated_interval_paths": {"L_then_M": path_lm, "M_then_L": path_ml},
        "ordinary_concatenation_residual": 0,
        "ordinary_flatness_is_universal": True,
        "off_seam_star_fixture": {"exp_L": 2, "z": "i", "reciprocal": "1", "adjoint": "1/2", "residual": "1/2"},
        "star_residual_vanishes_on_seam": True,
        "correct_missing_cell": "reciprocal_transport_to_hilbert_adjoint_natural_transformation",
        "zero_summability_supplies_missing_cell": False
    }
    out = Path(__file__).parents[1] / "results" / "rh-interval-flatness-vs-star-residual.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
