#!/usr/bin/env python3
"""Aggregate the weighted equivariant pullback completion over esd_7(Delta^3)."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).parents[1]/"results"
files={
 "weighted_trace_class":"weighted_global_rotor_trace_class.json",
 "translation_bundle":"translation_covariant_weighted_trace_class.json",
 "port_intertwiner":"moving_port_translation_intertwiner.json",
 "face_equivariance":"three_face_translation_equivariance.json",
 "global_pullback":"global_moving_current_pullback_contract.json",
 "lattice_overlay":"esd7_equivariant_pullback_overlay.json",
}
d={k:json.loads((ROOT/v).read_text(encoding="utf-8")) for k,v in files.items()}
o=d["lattice_overlay"]
checks={
 "all_dependencies_pass":all(x["passed"] for x in d.values()),
 "complete_f_vector_overlay":(len(o["edges"]),len(o["faces"]),len(o["tetrahedra"]))==(560,784,343),
 "finite_divisor_truncations_trace_norm_convergent":d["weighted_trace_class"]["checks"]["weighted_operator_is_positive_trace_class"],
 "translation_action_is_covariant":d["translation_bundle"]["checks"]["centered_weight_family_is_shift_covariant"],
 "moving_port_intertwines":d["port_intertwiner"]["checks"]["centered_port_intertwiner"],
 "three_faces_equivariant":d["face_equivariance"]["checks"]["pullback_witness_preserved"],
 "shared_faces_unique":o["checks"]["shared_face_has_single_overlay_record"],
}
assert all(checks.values())
out={
 "schema":"marici.voevodsky.esd7-equivariant-trace-class-completion.v1",
 "checks":checks,"passed":True,
 "theorem":"Every edge, face, and tetrahedron of esd_7(Delta^3) carries a translation-equivariant weighted trace-class moving-current pullback; finite divisor packets converge in trace norm in every fiber, and all shared-face restrictions agree.",
 "counts":{"edges":560,"faces":784,"tetrahedra":343},
 "bundle":"{P_c^(s)} over c in R with U_a P_c^(s) U_a*=P_(c+a)^(s)",
 "limit":"trace-norm limit of weighted finite divisor truncations, plus strong-Schwartz-dual current limit",
 "scope":"weights chosen beyond divisor-counting and successor-growth exponents",
 "not_claimed":["nonzero strictly translation-invariant trace-class operator","unweighted global trace class","all-path convergence of raw common Hilbert rows"],
 "dependencies":{k:{"path":v,"sha256":hashlib.sha256((ROOT/v).read_bytes()).hexdigest()} for k,v in files.items()}
}
path=ROOT/"esd7_equivariant_trace_class_completion.json"
path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in out.items() if k!="dependencies"},indent=2))
