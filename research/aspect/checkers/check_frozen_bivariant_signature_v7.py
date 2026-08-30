import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
v6 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v6.json").read_text(encoding="utf-8"))
v7 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v7.json").read_text(encoding="utf-8"))

H_near = sp.diag(1, -1)
H_exceptional = sp.eye(1)
J = sp.Matrix([[1, 0]])
kernel_basis = J.nullspace()

# First unused packet: 0 -> A -> B -> C -> 0 as Z-representations.
# B is unipotent; A and C are trivial one-dimensional representations.
T_A = sp.eye(1)
T_B = sp.Matrix([[1, 1], [0, 1]])
T_C = sp.eye(1)
i = sp.Matrix([[1], [0]])
p = sp.Matrix([[0, 1]])


def fixed_basis(T: sp.Matrix) -> list[sp.Matrix]:
    return (T - sp.eye(T.rows)).nullspace()


fields = set(v7["derived_transport_enriched_resolved_route_family"]["required_fields"])
laws = set(v7["derived_transport_enriched_resolved_route_family"]["required_laws"])
objects = set(v7["object_types"])
cells = set(v7["cell_types"])
forbidden = set(v7["forbidden_promotions"])

checks = {
    "v6_preserved_as_failed_predecessor": v7["predecessor"].endswith("v6.json") and v6["status"] == "candidate_frozen",
    "v7_is_new_frozen_candidate": v7["status"] == "candidate_frozen" and v7["cell_creation_during_replay"] is False,
    "specialization_complex_declared": "equivariant_specialization_complex" in objects,
    "vanishing_cycle_transport_declared": "vanishing_cycle_transport_object" in objects,
    "derived_fixed_object_declared": "derived_holonomy_fixed_object" in objects,
    "boundary_cofiber_declared": "homotopy_fixed_point_boundary_cofiber" in objects,
    "distinguished_triangle_declared": "distinguished_specialization_triangle" in cells,
    "repair_specialization_is_equivariant": J * H_near == H_exceptional * J,
    "repair_kernel_retains_half_turn_transport": len(kernel_basis) == 1 and H_near * kernel_basis[0] == -kernel_basis[0],
    "repair_kernel_and_cokernel_retention_required": "specialization_cone_retains_kernel_and_cokernel_transport" in laws,
    "repair_boundary_triangle_required": "boundary_cofiber_preserves_the_specialization_triangle" in laws,
    "unused_sequence_is_exact_underlying": i.rank() == 1 and p.rank() == 1 and p * i == sp.zeros(1, 1) and i.columnspace() == p.nullspace(),
    "unused_maps_are_equivariant": T_B * i == i * T_A and p * T_B == T_C * p,
    "unused_A_and_C_invariants_are_one_dimensional": len(fixed_basis(T_A)) == 1 and len(fixed_basis(T_C)) == 1,
    "unused_B_invariants_are_only_the_subobject": fixed_basis(T_B) == [sp.Matrix([1, 0])],
    "ordinary_invariant_map_B_to_C_is_zero": p * fixed_basis(T_B)[0] == sp.zeros(1, 1),
    "ordinary_invariants_are_not_right_exact": len(fixed_basis(T_C)) == 1 and (p * fixed_basis(T_B)[0]).rank() == 0,
    "v7_forbids_ordinary_invariants_as_exact": "ordinary invariant spaces treated as an exact functor" in forbidden,
    "v7_requires_derived_fixed_triangle": "derived_holonomy_fixed_points_are_applied_to_the_full_triangle" in laws,
    "strict_descent_has_two_zero_gates": "strict_descent_requires_zero_derived_boundary_and_zero_vanishing_cycle_defect" in laws,
    "local_packet_not_global_admission": v7["out_of_sample_policy"]["local_gate_cannot_validate_global_admission"] is True,
}

result = {
    "schema": "marici.aspect.frozen-bivariant-network-signature-v7-check.v1",
    "status": "candidate_v7_frozen_local_schema_pass" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {key: bool(value) for key, value in checks.items()},
    "v6_disposition": "preserved as falsified",
    "v7_disposition": "candidate frozen; the specialization kernel survives as a transport defect and the unused nonexact-invariants packet forces derived fixed points",
    "next_decisive_test": "an infinite-dimensional completed transport complex where homotopy fixed points fail to commute with the chosen completion or inverse limit",
}

out = root / "results" / "frozen_bivariant_signature_v7.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "candidate_v7_frozen_local_schema_pass" else 1)
