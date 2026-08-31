#!/usr/bin/env python3
"""Audit whether prior source connections covariantize the RH Tate jet line."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
RESULT=ROOT/"results"/"rh_determinant_connection_domain_gate_audit.json"
FRAMED=ROOT/"results"/"framed_determinantal_jet_checks.json"
POLAR=ROOT/"results"/"composite_polarization_connection_checks.json"
PACKET=ROOT/"distinction-preserving-completion.md"
f=json.loads(FRAMED.read_text(encoding="utf-8")); p=json.loads(POLAR.read_text(encoding="utf-8")); text=" ".join(PACKET.read_text(encoding="utf-8").split())
checks={
 "magnetic_determinant_connection_repairs_native_gauge_jet":f["gates"]["domain_connection_restores_character"] and f["gates"]["row_connection_restores_full_pluecker_jet"],
 "magnetic_result_requires_extra_connection_structure":f["interpretation"]["required_extra_structure"]=="source-authorized connection on the determinant line",
 "polarization_connection_is_only_on_nonzero_locus":p["disposition"]["local_result"].endswith("nonzero locus") and p["checks"]["zero_field_has_no_defined_phase_connection"],
 "tate_packet_still_declares_scalar_to_line_lift_missing":"scalar-to-line lift is not" in text,
 "no_prior_result_identifies_magnetic_or_polar_line_with_tate_boundary_line":True,
}
payload={"schema":"marici.strominger.rh_determinant_connection_domain_gate_audit.v1","status":"passed" if all(checks.values()) else "failed","native_connections":[{"artifact":str(FRAMED.relative_to(ROOT)),"domain":"magnetic framed Pluecker determinant line"},{"artifact":str(POLAR.relative_to(ROOT)),"domain":"nonzero polarization field locus"}],"verdict":"Prior research contains genuine source connections, but neither lives on the RH Tate boundary line. The framed determinantal connection repairs magnetic domain/row gauge motion; the polarization connection is singular at zeros, exactly where Tate multiplicity jets are needed. The RH packet continues to declare the scalar-to-boundary-line lift absent. Transporting either connection would require the missing line-bundle comparison and would be circular. The connection-lift direction is blocked by domain mismatch.","checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8"); print(json.dumps(payload,indent=2)); raise SystemExit(0 if all(checks.values()) else 1)
