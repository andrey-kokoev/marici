#!/usr/bin/env python3
"""Count the generic labelled occurrence support of the soft-signed A3 corners."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
critical = json.loads((ROOT / "research/nima/finite-sextic-higher-critical-locus.json").read_text(encoding="utf-8"))
orbits = json.loads((ROOT / "research/nima/generic-finite-collision-cyclic-orbits.json").read_text(encoding="utf-8"))
local = json.loads((ROOT / "research/benincasa/finite-sextic-coordinate-boundary-vanishing.json").read_text(encoding="utf-8"))

eligible = []
deeper = []
for row in critical["representatives"]:
    coordinates = tuple(row["marked_point"][axis].replace(" ", "") for axis in ("a", "b"))
    target = deeper if "-E" in coordinates else eligible
    target.append({"labels": row["labels"], "marked_coordinates": list(coordinates)})

assert len(orbits["orbits"]) == 8
assert len(eligible) == 3
assert len(deeper) == 5
a3 = local["double_coordinate_boundary"]["soft_signed_corners"]
assert a3["milnor_rank"] == 3
assert a3["generic_kato_specialization_rank"] == 1
assert a3["unaccounted_rank"] == 2

occurrences_per_orbit = 3
signed_branches_per_occurrence = 4
germs = len(eligible) * occurrences_per_orbit * signed_branches_per_occurrence
assert germs == 36

print(json.dumps({
    "generic_collision_orbits": len(eligible),
    "deeper_collision_orbits": len(deeper),
    "labelled_A3_germs": germs,
    "A3_total_rank": 3 * germs,
    "generic_kato_rank": germs,
    "excess_rank": 2 * germs,
    "total_C3_character": [3 * germs, 0, 0],
    "excess_C3_character": [2 * germs, 0, 0],
}, indent=2))
