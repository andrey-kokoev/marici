#!/usr/bin/env python3
"""Count labelled strata at the deeper soft-triangle degeneration."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
critical = json.loads((ROOT / "research/nima/finite-sextic-higher-critical-locus.json").read_text(encoding="utf-8"))
orbits = json.loads((ROOT / "research/nima/generic-finite-collision-cyclic-orbits.json").read_text(encoding="utf-8"))

movable = []
forced_e_zero = []
for row in critical["representatives"]:
    coords = tuple(row["marked_point"][axis].replace(" ", "") for axis in ("a", "b"))
    (forced_e_zero if "-E" in coords else movable).append(row["labels"])

assert len(orbits["orbits"]) == 8
assert len(movable) == 3
assert len(forced_e_zero) == 5

occurrences = 3
movable_reduced_branches = 4  # P2=+-P1 and E=+-P1; choice of P1/P2 no longer doubles them.
forced_reduced_branches = 1   # E=0 plus E^2=P_i^2 and P1^2=P2^2 forces P1=P2=0.
movable_strata = len(movable) * occurrences * movable_reduced_branches
all_soft_strata = len(forced_e_zero) * occurrences * forced_reduced_branches
total = movable_strata + all_soft_strata
assert (movable_strata, all_soft_strata, total) == (36, 15, 51)

print(json.dumps({
    "movable_one_scale_strata": movable_strata,
    "forced_all_soft_strata": all_soft_strata,
    "total_labelled_strata": total,
    "regular_C3_families": total // occurrences,
    "support_character": [total, 0, 0],
}, indent=2))
