#!/usr/bin/env python3
"""Inventory the admitted RH artifacts for a source-labelled Schur tail block."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
PACKET=ROOT/"distinction-preserving-completion.md"
ESCAPE=ROOT/"checkers"/"rh_adjoint_observer_completion_escape_audit.py"
RESULT=ROOT/"results"/"rh_source_labelled_tail_block_inventory_audit.json"
packet=PACKET.read_text(encoding="utf-8")
escape=ESCAPE.read_text(encoding="utf-8")
packet_flat=" ".join(packet.split())

checks={
 "scalar_tate_jet_family_is_declared":"Declare the entire family \\(J_m\\)" in packet_flat,
 "direct_limit_comparison_cell_is_declared":"The comparison cell is present" in packet_flat,
 "scalar_to_boundary_line_lift_is_explicitly_missing":"requires a source-derived lift of scalar Tate jets into the boundary-line" in packet_flat and "scalar-to-line lift is not" in packet_flat,
 "existing_rh_tail_block_is_only_a_hostile_fixture":"A_eps is a finite invertible tail block" in escape and "one_shot_adjoint_lift" in escape,
 "hostile_fixture_is_not_source_labelled":"source-labelled" not in escape and "Tate" not in escape,
}
payload={
 "schema":"marici.strominger.rh_source_labelled_tail_block_inventory_audit.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "inventoried_sources":[str(PACKET.relative_to(ROOT)),str(ESCAPE.relative_to(ROOT))],
 "verdict":"The RH corpus supplies scalar Tate jets, a direct-limit comparison cell, and a synthetic hostile invertible block used to test observer escape. It supplies no source-labelled RH matrix realizing scalar jets inside boundary-line incidence, so no A,B,C,E partition can yet be formed with source authority. The Schur formula is available, but cutoff naturality cannot be tested until the scalar-to-line lift or an equivalent source-labelled boundary matrix is constructed.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
print(json.dumps(payload,indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
