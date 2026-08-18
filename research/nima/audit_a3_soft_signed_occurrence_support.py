#!/usr/bin/env python3
"""Count the generic labelled occurrence support of the soft-signed A3 corners."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
critical = json.loads((ROOT / "research/nima/finite-sextic-higher-critical-locus.json").read_text(encoding="utf-8"))
orbits = json.loads((ROOT / "research/nima/generic-finite-collision-cyclic-orbits.json").read_text(encoding="utf-8"))
local = json.loads((ROOT / "research/benincasa/finite-sextic-coordinate-boundary-vanishing.json").read_text(encoding="utf-8"))

movable = []
coalesced = []
for row in critical["representatives"]:
    coordinates = tuple(row["marked_point"][axis].replace(" ", "") for axis in ("a", "b"))
    target = coalesced if "-E" in coordinates else movable
    target.append({"labels": row["labels"], "marked_coordinates": list(coordinates)})

assert len(orbits["orbits"]) == 8
assert len(movable) == 3
assert len(coalesced) == 5
a3 = local["double_coordinate_boundary"]["soft_signed_corners"]
assert a3["milnor_rank"] == 3
assert a3["generic_kato_specialization_rank"] == 1
assert a3["unaccounted_rank"] == 2

occurrences_per_orbit = 3
movable_branches_per_occurrence = 4
coalesced_branches_per_occurrence = 2
movable_germs = len(movable) * occurrences_per_orbit * movable_branches_per_occurrence
coalesced_germs = len(coalesced) * occurrences_per_orbit * coalesced_branches_per_occurrence
germs = movable_germs + coalesced_germs
assert movable_germs == 36
assert coalesced_germs == 30
assert germs == 66

print(json.dumps({
    "movable_signed_collision_orbits": len(movable),
    "coalesced_signed_collision_orbits": len(coalesced),
    "movable_A3_germs": movable_germs,
    "coalesced_A3_germs": coalesced_germs,
    "labelled_A3_germs": germs,
    "A3_total_rank": 3 * germs,
    "generic_kato_rank": germs,
    "excess_rank": 2 * germs,
    "total_C3_character": [3 * germs, 0, 0],
    "excess_C3_character": [2 * germs, 0, 0],
}, indent=2))
