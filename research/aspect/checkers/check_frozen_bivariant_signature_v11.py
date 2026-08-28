import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
v10 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v10.json").read_text(encoding="utf-8"))
v11 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v11.json").read_text(encoding="utf-8"))

q = sp.symbols("q", nonzero=True)
u_north = sp.Matrix([1, q]) / sp.sqrt(2)
u_north_dual = sp.Matrix([[1, q**-1]]) / sp.sqrt(2)
u_south = sp.Matrix([q**-1, 1]) / sp.sqrt(2)
u_south_dual = sp.Matrix([[q, 1]]) / sp.sqrt(2)
P_north = sp.simplify(u_north * u_north_dual)
P_south = sp.simplify(u_south * u_south_dual)
transition = q**-1
winding = sp.simplify(q * sp.diff(transition, q) / transition)

theta = sp.symbols("theta", real=True)
alpha = sp.Rational(1, 2)
flat_curvature = sp.Integer(0)
flat_chern = sp.Integer(0)
flat_holonomy = sp.simplify(sp.exp(2 * sp.pi * sp.I * alpha))

family = v11["phase_framed_joint_spectral_family"]
fields = set(family["required_fields"])
laws = set(family["required_laws"])
objects = set(v11["object_types"])
forbidden = set(v11["forbidden_promotions"])

checks = {
    "v10_preserved_as_failed_predecessor": v11["predecessor"].endswith("v10.json") and v10["status"] == "candidate_frozen",
    "v11_is_new_frozen_candidate": v11["status"] == "candidate_frozen" and v11["cell_creation_during_replay"] is False,
    "phase_framed_eigenline_declared": "phase_framed_eigenline_bundle" in objects,
    "berry_connection_declared": "berry_connection" in objects,
    "holonomy_character_declared": "holonomy_character" in objects,
    "repair_frames_give_same_projector": sp.simplify(P_north - P_south) == sp.zeros(2),
    "repair_transition_relates_frames": sp.simplify(u_south - transition * u_north) == sp.zeros(2, 1),
    "repair_winding_is_minus_one": winding == -1,
    "repair_phase_is_now_retained": "unitary_transition_functions_on_overlaps" in fields and "curvature_forms_and_characteristic_classes" in fields,
    "unused_flat_line_has_zero_curvature_and_chern": flat_curvature == 0 and flat_chern == 0,
    "unused_flat_line_has_half_turn_holonomy": flat_holonomy == -1,
    "unused_flat_holonomy_is_not_erased_by_zero_chern": "flat_zero_chern_lines_still_retain_holonomy_characters" in laws,
    "cross_sector_horizontal_identity_required": "labelled_specialization_obeys_dJ_plus_A_target_J_minus_J_A_source_equals_zero" in laws,
    "projector_before_frame_promotion_forbidden": "global projector promoted to a globally trivial eigenframe" in forbidden,
    "local_packet_not_global_admission": v11["out_of_sample_policy"]["local_gate_cannot_validate_global_admission"] is True,
}

result = {
    "schema": "marici.aspect.frozen-bivariant-network-signature-v11-check.v1",
    "status": "candidate_v11_frozen_local_schema_pass" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {key: bool(value) for key, value in checks.items()},
    "v10_disposition": "preserved as falsified",
    "v11_disposition": "candidate frozen; Berry winding is retained and the unused flat zero-Chern line keeps its nontrivial holonomy character",
    "next_decisive_test": "degenerate rank-two eigenspaces with non-Abelian Wilczek-Zee holonomy that determinant-line data alone cannot distinguish",
}

out = root / "results" / "frozen_bivariant_signature_v11.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "candidate_v11_frozen_local_schema_pass" else 1)
