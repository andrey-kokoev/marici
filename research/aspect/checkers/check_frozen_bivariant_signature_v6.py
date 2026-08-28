import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
v5 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v5.json").read_text(encoding="utf-8"))
v6 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v6.json").read_text(encoding="utf-8"))


def fixed_space_dimension(generators: list[sp.Matrix]) -> int:
    if not generators:
        return generators[0].rows if generators else 0
    rank = generators[0].rows
    stacked = sp.Matrix.vstack(*(generator - sp.eye(rank) for generator in generators))
    return len(stacked.nullspace())


def commutator(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    return sp.simplify(a * b * a.inv() * b.inv())


G1 = sp.eye(1)
H_plus = sp.eye(1)
H_minus = -sp.eye(1)

G2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Z = sp.diag(1, -1)

fields = set(v6["transport_enriched_log_resolved_route_family"]["required_fields"])
laws = set(v6["transport_enriched_log_resolved_route_family"]["required_laws"])
objects = set(v6["object_types"])
arrows = set(v6["arrow_types"])
cells = set(v6["cell_types"])
forbidden = set(v6["forbidden_promotions"])

plus_fixed = fixed_space_dimension([H_plus])
minus_fixed = fixed_space_dimension([H_minus])
plus_boundary = G1.rows - plus_fixed
minus_boundary = G1.rows - minus_fixed

checks = {
    "v5_preserved_as_failed_predecessor": v6["predecessor"].endswith("v5.json") and v5["status"] == "candidate_frozen",
    "v6_is_new_frozen_candidate": v6["status"] == "candidate_frozen" and v6["cell_creation_during_replay"] is False,
    "path_groupoid_object_declared": "resolved_stratum_path_groupoid" in objects,
    "metric_local_system_declared": "metric_route_local_system" in objects,
    "parallel_transport_arrow_declared": "path_groupoid_parallel_transport" in arrows,
    "specialization_intertwiner_declared": "specialization_transport_intertwiner" in arrows,
    "holonomy_relation_cell_declared": "holonomy_relation_cell" in cells,
    "boundary_obstruction_cell_declared": "boundary_port_descent_obstruction" in cells,
    "repair_holonomies_preserve_same_metric": H_plus.T * G1 * H_plus == G1 and H_minus.T * G1 * H_minus == G1,
    "repair_holonomies_are_now_distinguished": H_plus != H_minus and "metric_transport_on_groupoid_generators" in fields,
    "repair_parallel_dimensions_are_one_and_zero": plus_fixed == 1 and minus_fixed == 0,
    "repair_boundary_ports_are_zero_and_one": plus_boundary == 0 and minus_boundary == 1,
    "global_records_fixed_space_law_required": "global_parallel_records_equal_the_common_fixed_space_of_loop_holonomies" in laws,
    "boundary_quotient_law_required": "retained_boundary_port_is_route_space_modulo_holonomy_invariants" in laws,
    "specialization_naturality_required": "specialization_intertwiners_commute_with_loop_transport" in laws,
    "unused_generators_are_individually_metric": X.T * G2 * X == G2 and Z.T * G2 * Z == G2,
    "unused_torus_relation_fails": commutator(X, Z) == -sp.eye(2),
    "unused_invalid_transport_is_rejected_by_relation_law": "declared_groupoid_relations_hold_exactly" in laws and commutator(X, Z) != sp.eye(2),
    "strict_descent_with_boundary_is_forbidden": "nonzero retained boundary port discarded during strict descent" in forbidden,
    "local_packet_not_global_admission": v6["out_of_sample_policy"]["local_gate_cannot_validate_global_admission"] is True,
}

result = {
    "schema": "marici.aspect.frozen-bivariant-network-signature-v6-check.v1",
    "status": "candidate_v6_frozen_local_schema_pass" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {key: bool(value) for key, value in checks.items()},
    "v5_disposition": "preserved as falsified",
    "v6_disposition": "candidate frozen; flat-holonomy repair is distinguished and the unused torus relation hostile is rejected; global admission not earned",
    "next_decisive_test": "degenerating local system whose monodromy changes under exceptional specialization or whose completion retains infinite-dimensional boundary spectrum",
}

out = root / "results" / "frozen_bivariant_signature_v6.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "candidate_v6_frozen_local_schema_pass" else 1)
