#!/usr/bin/env python3
"""Audit whether current packets can instantiate the differentiated cone square."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BEN = ROOT / "research" / "benincasa" / "results"
OUT = ROOT / "research" / "aspect" / "results" / "differentiated_cone_export_contract.json"

cone = json.loads((BEN / "rank26-conductor-specialization-cone-homology.json").read_text(encoding="utf-8"))
wall = json.loads((BEN / "rank26-bidual-quotient-horizontality-x-at-3-4-5.json").read_text(encoding="utf-8"))

required_exports = {
    "wall_chain_blocks": ["d_C_at_wall", "F_at_wall", "d_D_at_wall"],
    "gram_normal_jets": ["d_C_normal_jet", "F_normal_jet", "d_D_normal_jet"],
    "gram_tangent_jets": ["d_C_tangent_jet", "F_tangent_jet", "d_D_tangent_jet"],
    "frame_transport": ["retained_pivot_transport", "denominator_occurrence_permutation", "residue_jacobian_unit", "inversion_transition"],
}
available_evidence = {
    "generic_assembled_cone_d_minus_two": "d_minus_two_columns" in cone.get("mapping_cone", {}),
    "generic_assembled_cone_d_minus_one": "d_minus_one_columns" in cone.get("mapping_cone", {}),
    "generic_explicit_B_primitive": cone.get("defect_primitive", {}).get("middle_degree_vector") == {"B": 1, "N": {}},
    "wall_base_relation_vectors": "base_relation_vectors" in wall,
    "wall_obstructed_relation_vectors": "obstructed_base_relation_vectors" in wall,
    "wall_obstruction_classes": "obstruction_classes" in wall,
    "wall_mixed_vectors": "mixed_vectors" in wall,
}
all_packets = {**cone, **wall}
missing = {group: [field for field in fields if field not in all_packets] for group, fields in required_exports.items()}
missing = {group: fields for group, fields in missing.items() if fields}

checks = {
    "all_current_partial_evidence_is_present": all(available_evidence.values()),
    "separated_wall_blocks_are_not_exported": set(missing.get("wall_chain_blocks", [])) == set(required_exports["wall_chain_blocks"]),
    "normal_jets_are_not_exported": set(missing.get("gram_normal_jets", [])) == set(required_exports["gram_normal_jets"]),
    "tangent_zero_cannot_be_checked_at_block_level": set(missing.get("gram_tangent_jets", [])) == set(required_exports["gram_tangent_jets"]),
    "full_frame_transport_is_not_exported": set(missing.get("frame_transport", [])) == set(required_exports["frame_transport"]),
}
passed = all(checks.values())
payload = {
    "schema": "marici.aspect.differentiated-cone-export-contract.v1",
    "available_evidence": available_evidence,
    "required_exports": required_exports,
    "missing_exports": missing,
    "checks": checks,
    "passed": passed,
    "classification": "differentiated_cone_not_instantiable_from_current_exports" if passed else "export_audit_inconclusive",
    "consequence": "The assembled generic cone and wall relation summaries do not determine the separated differentiated square. Reconstructing it would require unexported gauge and frame choices.",
    "next_falsifier": "export the thirteen named block, jet, and frame-transport fields from one source-normalized reducer and evaluate the differentiated chain equation without post-hoc basis alignment",
}
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if passed else 1)
