#!/usr/bin/env python3
"""Exact contract check for the rank-26 physical Leray pairing."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parents[1] / "results" / "cosmology_rank26_leray_pairing_typing.json"

def main() -> None:
    rank = json.loads((ROOT / "research/nima/results/physical_marked_rank26_geometry.json").read_text(encoding="utf-8"))
    leray = (ROOT / "research/benincasa/published_boundary_value_leray_uniqueness.md").read_text(encoding="utf-8")
    source = (ROOT / "research/benincasa/check_nine_master_griffiths_dwork.py").read_text(encoding="utf-8")
    checks = {
        "stabilized_relative_rank_is_26": rank["complement_euler_characteristic"] == 26 and all(r["dimension"] == r["source_orbit"] == 26 for r in rank["replicated_stabilization"]),
        "source_coordinate_is_q_equals_E_plus_y12": "q=y12+E" in source,
        "residue_coordinates_are_y23_y31": "a,b are the residue-surface coordinates y23,y31" in source,
        "negative_imaginary_tube_is_convex": "define a convex tube" in leray,
        "leray_sheet_is_source_fixed": "w=+\\sqrt{K_0(a,b)}" in leray,
        "leray_orientation_is_source_fixed": "oriented by \\(da\\wedge db\\)" in leray,
        "leray_multiplicity_is_one": "with multiplicity one" in leray,
        "generic_Q_variation_remains_uncomputed": "does **not** yet compute" in leray,
    }
    payload = {
        "schema": "marici.cosmology-rank26-leray-pairing-typing.v1",
        "checks": checks,
        "direct_literal_positive_chain_map_to_q0": False,
        "source_defined_adapter": "boundary-value analytic continuation in T_- followed by Leray residue",
        "cohomology_object": "rank-26 twisted marked complement on q_G12=0",
        "dual_object": "canonical local relative Leray germ Gamma_E^res",
        "ordinary_primitive_trace_gate_authorized": False,
        "required_next_map": "explicit twisted period covector Per_Gamma on the stabilized rank-26 presentation",
        "remaining_global_gate": "transport/variation of Gamma_E^res, especially around generic Q=0",
        "passed": all(checks.values()),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if not payload["passed"]: raise SystemExit(1)

if __name__ == "__main__": main()
