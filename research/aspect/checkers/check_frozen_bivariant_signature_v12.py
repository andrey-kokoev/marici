import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
v11 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v11.json").read_text(encoding="utf-8"))
v12 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v12.json").read_text(encoding="utf-8"))

I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Z = sp.diag(1, -1)
U = sp.I * X
V_noncommuting = sp.I * Z
V_commuting = sp.I * X


def commutator(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    return sp.simplify(a * b * a.inv() * b.inv())


def spectral_summary(a: sp.Matrix) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    return (sp.trace(a), sp.det(a), sp.factor(a.charpoly().as_expr()))


family = v12["nonabelian_framed_spectral_family"]
fields = set(family["required_fields"])
laws = set(family["required_laws"])
objects = set(v12["object_types"])
forbidden = set(v12["forbidden_promotions"])

checks = {
    "v11_preserved_as_failed_predecessor": v12["predecessor"].endswith("v11.json") and v11["status"] == "candidate_frozen",
    "v12_is_new_frozen_candidate": v12["status"] == "candidate_frozen" and v12["cell_creation_during_replay"] is False,
    "full_rank_r_bundle_declared": "rank_r_degenerate_eigenvector_bundle" in objects,
    "u_r_connection_declared": "u_r_connection" in objects,
    "matrix_holonomy_representation_declared": "matrix_holonomy_path_groupoid_representation" in objects,
    "repair_holonomies_are_unitary": U.conjugate().T * U == I2 and V_noncommuting.conjugate().T * V_noncommuting == I2,
    "repair_commutator_is_retained": commutator(U, V_noncommuting) == -I2,
    "repair_determinant_shadow_is_trivial": sp.det(U) == sp.det(V_noncommuting) == sp.det(commutator(U, V_noncommuting)) == 1,
    "unused_pairs_have_matching_individual_spectral_summaries": spectral_summary(U) == spectral_summary(V_noncommuting) == spectral_summary(V_commuting),
    "unused_pairs_have_different_joint_commutators": commutator(U, V_noncommuting) == -I2 and commutator(U, V_commuting) == I2,
    "unused_joint_transport_not_replaced_by_loop_summaries": "individual_loop_spectra_traces_and_determinants_do_not_replace_joint_matrix_transport" in laws,
    "path_order_and_relations_required": "all_path_groupoid_and_braid_relations_hold_as_matrix_equalities" in laws,
    "matrix_horizontal_specialization_required": "horizontal_matrix_specialization_maps" in fields,
    "determinant_promotion_forbidden": "determinant holonomy promoted to full degenerate-mode transport" in forbidden,
    "local_packet_not_global_admission": v12["out_of_sample_policy"]["local_gate_cannot_validate_global_admission"] is True,
}

result = {
    "schema": "marici.aspect.frozen-bivariant-network-signature-v12-check.v1",
    "status": "candidate_v12_frozen_local_schema_pass" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {key: bool(value) for key, value in checks.items()},
    "v11_disposition": "preserved as falsified",
    "v12_disposition": "candidate frozen; the SU(2) commutator is retained and matching individual loop spectra do not collapse distinct joint representations",
    "next_decisive_test": "projectively identical matrix transports that differ by a higher central cocycle or gerbe class over triple loop composition",
}

out = root / "results" / "frozen_bivariant_signature_v12.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "candidate_v12_frozen_local_schema_pass" else 1)
