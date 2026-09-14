#!/usr/bin/env python3
"""Exact 3-horn filling in the additive shadow of one coherence pyramid."""
import json
from fractions import Fraction
from pathlib import Path

# Oriented tetrahedral boundary: h234 - h134 + h124 - h123 = 0.
SIGNS = {"123": -1, "124": 1, "134": -1, "234": 1}


def strict_filler(known, missing):
    total = sum(Fraction(SIGNS[k]) * v for k, v in known.items())
    return -total / SIGNS[missing]


def boundary(faces):
    return sum(Fraction(SIGNS[k]) * faces[k] for k in SIGNS)


def main():
    base = {"123": Fraction(2), "124": Fraction(-3), "134": Fraction(5), "234": Fraction(10)}
    assert boundary(base) == 0

    recovered = {}
    for missing in SIGNS:
        known = {k: v for k, v in base.items() if k != missing}
        recovered[missing] = strict_filler(known, missing)
        assert recovered[missing] == base[missing]

    # Deliberate nonexistence: the strict filler is 10, outside the admitted alphabet.
    admitted = {Fraction(-1), Fraction(0), Fraction(1)}
    hostile_known = {"123": Fraction(2), "124": Fraction(-3), "134": Fraction(5)}
    required = strict_filler(hostile_known, "234")
    assert required == 10 and required not in admitted

    # Deliberate ambiguity after a parity-only readout of the missing integral face.
    bounded_candidates = list(range(-4, 5))
    parity_candidates = [x for x in bounded_candidates if x % 2 == int(required) % 2]
    assert len(parity_candidates) == 5

    result = {
        "schema": "marici.voevodsky.coherence-pyramid-3-horns.v1",
        "coefficient_object": "Q",
        "boundary_equation": "h234-h134+h124-h123=0",
        "strict_recovery": {k: str(v) for k, v in recovered.items()},
        "strict_horns_checked": 4,
        "strict_fillers_unique": True,
        "admissibility_hostile": {
            "required_filler": str(required),
            "admitted_values": [str(x) for x in sorted(admitted)],
            "filler_exists": False,
        },
        "compressed_readout_hostile": {
            "readout": "parity",
            "bounded_integral_candidates": bounded_candidates,
            "compatible_candidates": parity_candidates,
            "filler_unique": False,
        },
        "claim_boundary": "Exact theorem for an additive 3-truncated shadow; not a horn theorem for the full coherence-pyramid computad.",
    }
    out = Path(__file__).parents[1] / "results" / "coherence_pyramid_3_horns.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
