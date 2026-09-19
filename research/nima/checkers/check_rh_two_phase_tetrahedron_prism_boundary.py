#!/usr/bin/env python3
"""Exact oriented boundary of the staircase triangulation of Δ¹ × Δ³."""

from collections import defaultdict
import hashlib
import json
from pathlib import Path

labels = ("S", "A", "C", "G")

# Staircase triangulation.  Simplex r switches from phase 0 to phase 1 at r.
simplices = []
for r in range(4):
    simplex = tuple((labels[i], 0) for i in range(r + 1)) + tuple(
        (labels[i], 1) for i in range(r, 4)
    )
    simplices.append(simplex)


def canonical(face):
    ordered = tuple(sorted(face, key=lambda v: (labels.index(v[0]), v[1])))
    positions = {v: i for i, v in enumerate(ordered)}
    perm = [positions[v] for v in face]
    inversions = sum(perm[i] > perm[j] for i in range(len(perm)) for j in range(i + 1, len(perm)))
    return ordered, -1 if inversions % 2 else 1


boundary = defaultdict(int)
# Alternating simplex orientations realize the product orientation.
for r, simplex in enumerate(simplices):
    simplex_orientation = (-1) ** r
    for i in range(5):
        face = simplex[:i] + simplex[i + 1 :]
        key, orient = canonical(face)
        boundary[key] += simplex_orientation * ((-1) ** i) * orient
boundary = {face: coefficient for face, coefficient in boundary.items() if coefficient}

# Internal tetrahedra cancel. The remaining tetrahedra triangulate two ends and
# four side prisms, one for each omitted presentation label.
classes = {"phase_0_end": [], "phase_1_end": []}
for omitted in labels:
    classes[f"side_omit_{omitted}"] = []

unclassified = []
for face, coefficient in boundary.items():
    phases = {v[1] for v in face}
    present = {v[0] for v in face}
    row = {
        "vertices": [f"{name}{phase}" for name, phase in face],
        "coefficient": coefficient,
    }
    if phases == {0}:
        classes["phase_0_end"].append(row)
    elif phases == {1}:
        classes["phase_1_end"].append(row)
    elif len(present) == 3:
        omitted = next(name for name in labels if name not in present)
        classes[f"side_omit_{omitted}"].append(row)
    else:
        unclassified.append(row)

checks = {
    "four_top_simplices": len(simplices) == 4,
    "eight_vertices": len({v for simplex in simplices for v in simplex}) == 8,
    "one_tetrahedron_each_end": len(classes["phase_0_end"]) == 1 and len(classes["phase_1_end"]) == 1,
    "four_side_prisms_present": all(classes[f"side_omit_{x}"] for x in labels),
    "side_prism_tetrahedra_count": sum(len(classes[f"side_omit_{x}"]) for x in labels) == 12,
    "no_unclassified_boundary_faces": not unclassified,
    "total_boundary_tetrahedra": len(boundary) == 14,
}
assert all(checks.values())

payload = {
    "schema": "marici.nima.rh-two-phase-tetrahedron-prism-boundary.v1",
    "polytope": "Delta^1 x Delta^3",
    "cellular_boundary": "T_plus - T_minus - H_ACG + H_SCG - H_SAG + H_SAC",
    "staircase_four_simplices": [
        [f"{name}{phase}" for name, phase in simplex] for simplex in simplices
    ],
    "boundary_classes": classes,
    "checks": checks,
    "passed": True,
    "interpretation": "The eight-node packet is a four-dimensional homotopy prism. Its boundary has two tetrahedral end systems and four triangular side homotopies.",
}
canonical_payload = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical_payload).hexdigest()

out = Path(__file__).parents[1] / "results" / "rh-two-phase-tetrahedron-prism-boundary.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
