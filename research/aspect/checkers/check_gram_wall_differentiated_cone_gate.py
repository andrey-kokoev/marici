#!/usr/bin/env python3
"""Identify the normalized candidate for the Gram-wall connecting morphism."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ASPECT = ROOT / "research" / "aspect" / "results"
BEN = ROOT / "research" / "benincasa" / "results"
OUT = ASPECT / "gram_wall_differentiated_cone_gate.json"

cone_packets = [
    json.loads((BEN / "rank26-conductor-specialization-cone-homology.json").read_text(encoding="utf-8")),
    json.loads((BEN / "rank26-conductor-specialization-cone-homology-p31957.json").read_text(encoding="utf-8")),
]
wall = json.loads((ASPECT / "gram_wall_specialization_gate.json").read_text(encoding="utf-8"))
torsor = json.loads((ASPECT / "gram_normal_target_scale_torsor.json").read_text(encoding="utf-8"))
variance = json.loads((ASPECT / "gram_wall_gysin_variance_hostile.json").read_text(encoding="utf-8"))

checks = {
    "generic_cone_packets_pass": all(packet["passed"] for packet in cone_packets),
    "generic_cone_has_explicit_unit_B_primitive": all(packet["defect_primitive"]["middle_degree_vector"] == {"B": 1, "N": {}} for packet in cone_packets),
    "primitive_boundary_is_exact": all(packet["defect_primitive"]["residual"] == {} for packet in cone_packets),
    "primitive_is_cyclically_normalized": all(packet["defect_primitive"]["cyclic_product"] == 1 for packet in cone_packets),
    "chain_identity_survives_relation_basis_change": all(packet["checks"]["relation_basis_change_preserves_chain_identity"] for packet in cone_packets),
    "wall_first_order_defects_factor_through_dh": wall["passed"] and wall["classification"] == "first_order_defect_factors_through_gram_conormal",
    "rank_data_alone_leaves_target_scale_torsor": torsor["passed"] and torsor["classification"] == "conormal_source_fixed_relative_target_scale_unfixed",
    "degree_zero_gysin_shortcut_is_rejected": variance["passed"] and variance["classification"] == "rank_match_without_typed_factorization",
}
passed = all(checks.values())
payload = {
    "schema": "marici.aspect.gram-wall-differentiated-cone-gate.v1",
    "checks": checks,
    "passed": passed,
    "classification": "normalized_candidate_is_gram_normal_derivative_of_mapping_cone" if passed else "normalized_candidate_not_admitted",
    "admitted_scope": "constructor identification from the two-prime generic mapping-cone normalization and the two-prime Gram-wall conormal audit; no wall derivative matrix has yet been computed" if passed else "none",
    "candidate_constructor": "Differentiate the full source chain identity d_D F = F d_C in the Gram-normal direction, retaining the explicit middle primitive B=1. The differentiated square, not a chosen isomorphism of rank-one outputs, must produce the wall obstruction-to-mixed comparison.",
    "why_scale_is_fixed": "The generic cone declares the primitive B=1 and its weighted-sheet boundary before wall specialization; relation-basis and cyclic hostiles preserve it. Its normal derivative therefore transports a source normalization into the wall calculation.",
    "missing_constructors": ["Gram-normal first jet of every block of the normalized specialization-cone differential, including retained-pivot and inversion transport"],
    "next_falsifier": "export the normal jets of d_C, F, and d_D at h=0 and test the differentiated chain equation d_D' F + d_D F' = F' d_C + F d_C'; its residual must equal the coordinate-7 obstruction and common mixed line with zero tangent jet",
}
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if passed else 1)
