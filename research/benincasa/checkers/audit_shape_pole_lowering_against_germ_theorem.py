#!/usr/bin/env python3
"""Audit the shape-pole lowering construct against Aspect's revised germ gates."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
six = json.loads((ROOT / "research/benincasa/results/relative-shape-six-term-jet.json").read_text())
pole = json.loads((ROOT / "research/benincasa/results/relative-shape-pole-depth.json").read_text())

checks = {
    "native_arity_is_retained": six["native_arity"] == 6 and len(six["terms"]) == 6,
    "linear_associated_grade_is_exactly_typed": all(
        row["leading_symbol_is_invertible"] for row in pole["proper_face_lowering"].values()
    ),
    "full_filtered_fiber_gate_remains_open": not pole["filtered_lowering_homotopy_constructed"],
    "intersection_arity_gate_remains_open": not pole["pairwise_coherence_constructed"],
    "authority_gate_remains_open": not pole["physical_cycle_authority_established"],
}
assert all(checks.values()), checks

result = {
    "schema": "marici.shape-pole-germ-theorem-audit.v1",
    "checks": checks,
    "verdict": "associated-grade theorem only",
    "permitted_claim": "no independent generator on a higher proper-face pole grade",
    "prohibited_claim": "the complete filtered relative pole complex is contractible",
    "next_required_objects": [
        "finite triangular lowering homotopy",
        "full linear-fiber constancy check",
        "pairwise wall associator/coherence",
        "source-authorized physical cycle pairing",
    ],
}
out = ROOT / "research/benincasa/results/shape-pole-germ-theorem-audit.json"
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print(out)
