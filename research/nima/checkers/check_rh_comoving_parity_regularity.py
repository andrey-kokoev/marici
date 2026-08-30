#!/usr/bin/env python3
"""Exact finite two-chart parity and regularity typing checks."""

import json
from pathlib import Path


def main():
    # Grid u=-2,-1,1,2, avoiding the Heaviside convention at zero.
    inner = (-1, -1, 0, 0)
    outer = (0, 0, -1, -1)
    reflection = lambda vector: tuple(reversed(vector))

    assert reflection(inner) == outer
    assert reflection(outer) == inner

    overlap = tuple(a + b for a, b in zip(inner, outer))
    oriented = tuple(a - b for a, b in zip(inner, outer))
    assert overlap == (-1, -1, -1, -1)
    assert reflection(overlap) == overlap
    assert reflection(oriented) == tuple(-value for value in oriented)

    # Coefficient-level overlap projection (a,b) -> a+b has anti-diagonal kernel.
    chart_pairs = ((1, 0), (0, 1), (1, -1))
    overlap_readouts = tuple(a + b for a, b in chart_pairs)
    assert overlap_readouts == (1, 1, 0)
    assert chart_pairs[2] != (0, 0) and overlap_readouts[2] == 0

    regularities = ("primitive_exponential", "square_tempered")
    parities = ("overlap_even", "front_odd")
    typed_lanes = tuple((regularity, parity) for regularity in regularities for parity in parities)
    assert len(typed_lanes) == 4

    result = {
        "schema": "marici.rh-comoving-parity-regularity.v1",
        "status": "pass",
        "inner_outer_reflection_exchange": True,
        "overlap_constant": list(overlap),
        "overlap_reflection_character": "even",
        "oriented_front_reflection_character": "odd",
        "overlap_projection_has_antidiagonal_kernel": True,
        "regularity_grades": list(regularities),
        "parity_characters": list(parities),
        "minimum_typed_lanes": len(typed_lanes),
        "disposition": "relative sewing must preserve two charts, two parities, and two regularity grades",
    }
    out = Path(__file__).parents[1] / "results" / "rh-comoving-parity-regularity.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

