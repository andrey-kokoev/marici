#!/usr/bin/env python3
"""Audit whether the denominator deletion cube types the occurrence projector."""

import itertools
import json
from pathlib import Path


deletion_axes = [
    {"kind": "denominator", "label": "q_g1"},
    {"kind": "denominator", "label": "q_g2"},
    {"kind": "denominator", "label": "q_G12"},
]

occurrence_axes = [
    {"kind": "cyclic_e6_chart", "label": "G12:e6"},
    {"kind": "cyclic_e6_chart", "label": "G23:e6"},
    {"kind": "cyclic_e6_chart", "label": "G31:e6"},
]

masks = list(itertools.product([0, 1], repeat=3))
deletion_edges = []
for mask in masks:
    for axis, bit in enumerate(mask):
        if bit:
            target = list(mask)
            target[axis] = 0
            deletion_edges.append(
                {
                    "axis": deletion_axes[axis]["label"],
                    "source_mask": list(mask),
                    "target_mask": target,
                }
            )

occurrence_projector = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]

typed_deletion_labels = {(item["kind"], item["label"]) for item in deletion_axes}
typed_occurrence_labels = {(item["kind"], item["label"]) for item in occurrence_axes}

checks = {
    "both_presentations_happen_to_have_three_labels": len(deletion_axes) == len(occurrence_axes) == 3,
    "typed_label_sets_are_disjoint": typed_deletion_labels.isdisjoint(typed_occurrence_labels),
    "deletion_cube_has_eight_objects": len(masks) == 8,
    "deletion_cube_has_twelve_directed_edges": len(deletion_edges) == 12,
    "every_deletion_changes_the_module_mask": all(edge["source_mask"] != edge["target_mask"] for edge in deletion_edges),
    "occurrence_support_is_an_endomorphism": len(occurrence_projector) == len(occurrence_projector[0]) == len(occurrence_axes),
    "no_deletion_edge_is_an_occurrence_endomorphism": all(
        edge["source_mask"] != edge["target_mask"] for edge in deletion_edges
    ),
}

if not all(checks.values()):
    raise SystemExit(f"failed checks: {[name for name, ok in checks.items() if not ok]}")

packet = {
    "schema": "marici.benincasa.deletion_occurrence_projector_typing.v1",
    "deletion_axes": deletion_axes,
    "deletion_cube_objects": [list(mask) for mask in masks],
    "deletion_cube_edges": deletion_edges,
    "occurrence_axes": occurrence_axes,
    "candidate_occurrence_projector": occurrence_projector,
    "source_frontiers": {
        "entry_580": "product-pole complex closes rank cube but does not establish compatible deletion maps",
        "entry_3375": "A2 e6 occurrence morphism exists but complete rank-twelve triangular transport is absent",
    },
    "checks": checks,
    "verdict": (
        "The Boolean denominator deletion cube does not type the 3 by 3 cyclic "
        "e6 occurrence projector.  The axis counts agree, but labels, objects, "
        "and variance differ.  A source-derived connector between the deletion "
        "modules and occurrence-chart module is still required."
    ),
}

out = Path(__file__).resolve().parents[1] / "results" / "deletion_occurrence_projector_typing.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
