#!/usr/bin/env python3
"""Exact coefficient algebra for delta/principal-value chart sewing."""

import json
from fractions import Fraction
from pathlib import Path


def mat_vec(matrix, vector):
    return tuple(sum(a * b for a, b in zip(row, vector)) for row in matrix)


def determinant_2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def main():
    sewing = (
        (Fraction(-1, 2), Fraction(-1, 2)),
        (Fraction(1, 2), Fraction(-1, 2)),
    )
    det = determinant_2(sewing)
    assert det == Fraction(1, 2)

    inner = (Fraction(1), Fraction(0))
    outer = (Fraction(0), Fraction(1))
    assert mat_vec(sewing, inner) == (Fraction(-1, 2), Fraction(1, 2))
    assert mat_vec(sewing, outer) == (Fraction(-1, 2), Fraction(-1, 2))

    chart_reflection = ((0, 1), (1, 0))
    boundary_reflection = ((1, 0), (0, -1))
    for vector in (inner, outer, (Fraction(2), Fraction(-3))):
        left = mat_vec(sewing, mat_vec(chart_reflection, vector))
        right = mat_vec(boundary_reflection, mat_vec(sewing, vector))
        assert left == right

    orientation = (Fraction(1), Fraction(-1))
    sewn_orientation = mat_vec(sewing, orientation)
    assert sewn_orientation == (Fraction(0), Fraction(1))
    delta_only = sewn_orientation[0]
    assert delta_only == 0

    # Two arithmetic grades give two identical blocks.
    four_lane_determinant = det * det
    assert four_lane_determinant == Fraction(1, 4)

    result = {
        "schema": "marici.rh-delta-principal-value-sewing.v1",
        "status": "pass",
        "chart_sewing_determinant": [det.numerator, det.denominator],
        "reflection_intertwining": True,
        "orientation_maps_to_principal_value_only": True,
        "delta_only_kills_orientation": delta_only == 0,
        "four_lane_block_determinant": [four_lane_determinant.numerator, four_lane_determinant.denominator],
        "universal_chart_sewing_closed": True,
        "arithmetic_continuity_closed": False,
        "disposition": "universal sewing is faithful; remaining obstruction is arithmetic boundary continuity",
    }
    out = Path(__file__).parents[1] / "results" / "rh-delta-principal-value-sewing.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

