#!/usr/bin/env python3
"""Oriented staircase boundary of Δ¹ × Δ⁴ for two complete rung laws."""

from collections import defaultdict
import hashlib
import json
from pathlib import Path

labels = ("B", "S", "A", "C", "G")

simplices = []
for r in range(5):
    simplices.append(
        tuple((labels[i], 0) for i in range(r + 1))
        + tuple((labels[i], 1) for i in range(r, 5))
    )


def canonical(face):
    ordered = tuple(sorted(face, key=lambda v: (labels.index(v[0]), v[1])))
    positions = {v: i for i, v in enumerate(ordered)}
    perm = [positions[v] for v in face]
    inversions = sum(perm[i] > perm[j] for i in range(len(perm)) for j in range(i + 1, len(perm)))
    return ordered, -1 if inversions % 2 else 1


boundary = defaultdict(int)
for r, simplex in enumerate(simplices):
    for i in range(6):
        face = simplex[:i] + simplex[i + 1 :]
        key, orient = canonical(face)
        boundary[key] += (-1) ** r * (-1) ** i * orient
boundary = {face: coefficient for face, coefficient in boundary.items() if coefficient}

classes = {"phase_0_end": [], "phase_1_end": []}
for omitted in labels:
    classes[f"side_omit_{omitted}"] = []
unclassified = []
for face, coefficient in boundary.items():
    phases = {v[1] for v in face}
    present = {v[0] for v in face}
    row = {"vertices": [f"{name}{phase}" for name, phase in face], "coefficient": coefficient}
    if phases == {0}:
        classes["phase_0_end"].append(row)
    elif phases == {1}:
        classes["phase_1_end"].append(row)
    elif len(present) == 4:
        omitted = next(name for name in labels if name not in present)
        classes[f"side_omit_{omitted}"].append(row)
    else:
        unclassified.append(row)

checks = {
    "five_top_simplices": len(simplices) == 5,
    "ten_labelled_vertices": len({v for simplex in simplices for v in simplex}) == 10,
    "one_four_simplex_each_end": len(classes["phase_0_end"]) == 1 and len(classes["phase_1_end"]) == 1,
    "five_side_prisms_present": all(classes[f"side_omit_{x}"] for x in labels),
    "four_simplices_per_side_prism": all(len(classes[f"side_omit_{x}"]) == 4 for x in labels),
    "no_unclassified_boundary_faces": not unclassified,
    "total_boundary_four_simplices": len(boundary) == 22,
}
assert all(checks.values())

payload = {
    "schema": "marici.nima.rh-two-phase-rung-law-prism-boundary.v1",
    "polytope": "Delta^1 x Delta^4",
    "vertex_roles": list(labels),
    "cellular_boundary": "K_plus - K_minus - H_SACG + H_BACG - H_BSCG + H_BSAG - H_BSAC",
    "staircase_five_simplices": [[f"{n}{p}" for n, p in simplex] for simplex in simplices],
    "boundary_classes": classes,
    "checks": checks,
    "passed": True,
    "interpretation": "The next-level comparison has two complete four-simplex laws and five tetrahedron-prism side homotopies; omitting B recovers the prior S,A,C,G prism.",
}
canonical_payload = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical_payload).hexdigest()
out = Path(__file__).parents[1] / "results" / "rh-two-phase-rung-law-prism-boundary.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
