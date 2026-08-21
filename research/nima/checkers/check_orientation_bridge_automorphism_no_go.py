#!/usr/bin/env python3
"""No canonical bridge from two disconnected character-line diagrams."""

import json
from pathlib import Path


# A bridge between rank-one integral lines is multiplication by an integer a.
# The independent target sign gauge s=-1 preserves the target's internal
# character action, but sends a -> s*a. Naturality under all automorphisms of
# the disconnected input diagram forces a=-a, hence a=0 over Z/Q.
candidate_range = range(-8, 9)
invariant = [a for a in candidate_range if a == -a]
isomorphisms = [-1, 1]

assert invariant == [0]
assert all(a not in invariant for a in isomorphisms)

result = {
    "status": "PASS",
    "coefficient_ring": "Z (and hence characteristic-zero fields)",
    "independent_target_sign_automorphism": -1,
    "bridge_transformation": "a -> -a",
    "automorphism_invariant_bridges": invariant,
    "integral_equivariant_isomorphisms_before_canonicity": isomorphisms,
    "conclusion": "no canonical nonzero bridge from disconnected internal diagrams",
    "required_new_datum": "a cross-sector source map or pairing that couples the two sign gauges",
}

out = Path(__file__).resolve().parents[1] / "results" / "orientation_bridge_automorphism_no_go.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
