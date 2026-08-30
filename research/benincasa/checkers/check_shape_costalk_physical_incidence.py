#!/usr/bin/env python3
"""Check literal Cayley-Menger contour incidence with the cyclic A1 costalks."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/shape-costalk-physical-incidence.json"

# Source loop variables are edge lengths (y23,y31,y12)=(a,b,c), hence are
# nonnegative on the literal Cayley-Menger chamber.
points = {
    "g1_g2_s12": (-1, -1, 0),
    "g1_g3_s31": (-1, 0, -1),
    "g2_g3_s23": (0, -1, -1),
}

records = {}
checks = {}
for label, point in points.items():
    negative = [name for name, value in zip(("a", "b", "c"), point) if value < 0]
    in_nonnegative_chamber = all(value >= 0 for value in point)
    records[label] = {
        "point": list(point),
        "negative_length_coordinates": negative,
        "in_literal_nonnegative_length_chamber": in_nonnegative_chamber,
        "literal_local_chain_costalk": 0 if not in_nonnegative_chamber else None,
    }
    checks[f"{label}_is_outside_literal_chamber"] = not in_nonnegative_chamber
    checks[f"{label}_has_two_negative_lengths"] = len(negative) == 2

assert all(checks.values()), checks
packet = {
    "schema": "marici.shape-costalk-physical-incidence.v1",
    "source_contour_variables": ["a=y23", "b=y31", "c=y12"],
    "literal_chamber_condition": "a>=0, b>=0, c>=0 plus Cayley-Menger minor inequalities",
    "records": records,
    "all_checks_pass": True,
    "literal_physical_pairing": 0,
    "analytic_continuation_to_costalk_constructed": False,
    "conclusion": "nonzero coefficient costalk is inactive on the literal physical chamber",
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print(OUT)
