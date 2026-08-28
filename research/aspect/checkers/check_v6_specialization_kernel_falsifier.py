import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
v6 = json.loads(
    (root / "contracts" / "frozen-bivariant-network-signature.v6.json").read_text(
        encoding="utf-8"
    )
)

G_near = sp.eye(2)
G_exceptional = sp.eye(1)
H_near = sp.diag(1, -1)
H_exceptional = sp.eye(1)
J = sp.Matrix([[1, 0]])


def fixed_space_dimension(holonomy: sp.Matrix) -> int:
    return len((holonomy - sp.eye(holonomy.rows)).nullspace())


near_fixed = fixed_space_dimension(H_near)
exceptional_fixed = fixed_space_dimension(H_exceptional)
near_boundary = H_near.rows - near_fixed
exceptional_boundary = H_exceptional.rows - exceptional_fixed

family = v6["transport_enriched_log_resolved_route_family"]
associator = v6["transport_enriched_resolved_associator"]
all_terms = (
    set(v6["object_types"])
    | set(v6["arrow_types"])
    | set(v6["cell_types"])
    | set(family["required_fields"])
    | set(family["required_laws"])
    | set(associator["required_laws"])
    | set(v6["forbidden_promotions"])
)

checks = {
    "v6_is_frozen": v6["cell_creation_during_replay"] is False,
    "nearby_holonomy_is_metric": H_near.T * G_near * H_near == G_near,
    "exceptional_holonomy_is_metric": H_exceptional.T * G_exceptional * H_exceptional == G_exceptional,
    "specialization_is_nonzero": J.rank() == 1,
    "specialization_is_not_injective": len(J.nullspace()) == 1,
    "v6_intertwining_square_commutes": J * H_near == H_exceptional * J,
    "kernel_is_exactly_the_half_turn_sector": J.nullspace()[0] == sp.Matrix([0, 1]) and H_near * J.nullspace()[0] == -J.nullspace()[0],
    "nearby_boundary_port_has_dimension_one": near_boundary == 1,
    "exceptional_boundary_port_has_dimension_zero": exceptional_boundary == 0,
    "boundary_port_is_erased_under_admitted_naturality": near_boundary > exceptional_boundary,
    "v6_has_no_specialization_defect_object": not any(
        marker in term
        for term in all_terms
        for marker in ("specialization_kernel", "specialization_cokernel", "vanishing_cycle", "mapping_cone", "defect_complex")
    ),
    "v6_has_no_conservativity_law": not any(
        "faithful" in term or "conservative" in term or "injective_on_boundary" in term
        for term in all_terms
    ),
}

result = {
    "schema": "marici.aspect.v6-specialization-kernel-falsifier.v1",
    "status": "frozen_v6_falsified" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {key: bool(value) for key, value in checks.items()},
    "hostile": "rank-two nearby holonomy diag(1,-1), rank-one exceptional holonomy 1, and specialization J=(1,0)",
    "failure": "the specialization intertwiner law commutes while its kernel deletes the entire nontrivial-holonomy boundary sector",
    "required_future_repair": "retain the specialization kernel, cokernel, or mapping cone as a typed vanishing-cycle defect and require boundary-port transport to be exact through that defect",
}

out = root / "results" / "v6_specialization_kernel_falsifier.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "frozen_v6_falsified" else 1)
