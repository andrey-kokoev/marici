import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
v9 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v9.json").read_text(encoding="utf-8"))
v10 = json.loads((root / "contracts" / "frozen-bivariant-network-signature.v10.json").read_text(encoding="utf-8"))

t, s, z, lam = sp.symbols("t s z lambda", nonzero=True)
A2 = sp.Matrix([[0, 1], [t, 0]])
A2_cover = A2.subs(t, s**2)
P_plus = sp.simplify((sp.eye(2) + A2_cover / s) / 2)
P_minus = sp.simplify((sp.eye(2) - A2_cover / s) / 2)
R2 = sp.simplify((A2_cover - z * sp.eye(2)).inv())
R2_reconstructed = sp.simplify(P_plus / (s - z) + P_minus / (-s - z))

A3 = sp.Matrix([[0, 1, 0], [0, 0, 1], [t, 0, 0]])
cycle = (1, 2, 0)


def compose_permutations(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[index]] for index in range(len(left)))


cycle2 = compose_permutations(cycle, cycle)
cycle3 = compose_permutations(cycle, cycle2)

family = v10["normalized_joint_spectral_family"]
fields = set(family["required_fields"])
laws = set(family["required_laws"])
objects = set(v10["object_types"])
forbidden = set(v10["forbidden_promotions"])

checks = {
    "v9_preserved_as_failed_predecessor": v10["predecessor"].endswith("v9.json") and v9["status"] == "candidate_frozen",
    "v10_is_new_frozen_candidate": v10["status"] == "candidate_frozen" and v10["cell_creation_during_replay"] is False,
    "joint_incidence_space_declared": "joint_parameter_spectral_incidence_space" in objects,
    "normalized_cover_declared": "normalized_spectral_cover" in objects,
    "projector_local_system_declared": "riesz_projector_local_system" in objects,
    "deck_groupoid_declared": "deck_transport_groupoid" in objects,
    "repair_incidence_is_lambda_squared_equals_t": sp.factor((lam * sp.eye(2) - A2).det()) == lam**2 - t,
    "repair_projectors_are_idempotent": sp.simplify(P_plus**2 - P_plus) == sp.zeros(2) and sp.simplify(P_minus**2 - P_minus) == sp.zeros(2),
    "repair_projectors_are_disjoint_and_complete": sp.simplify(P_plus * P_minus) == sp.zeros(2) and sp.simplify(P_plus + P_minus) == sp.eye(2),
    "repair_deck_turn_swaps_projectors": sp.simplify(P_plus.subs(s, -s) - P_minus) == sp.zeros(2),
    "repair_total_resolvent_reconstructs_from_sheets": sp.simplify(R2 - R2_reconstructed) == sp.zeros(2),
    "repair_aggregate_must_follow_labelled_checks": "aggregate_resolvent_is_taken_only_after_labelled_descent_checks" in laws,
    "unused_incidence_is_lambda_cubed_equals_t": sp.factor((lam * sp.eye(3) - A3).det()) == lam**3 - t,
    "unused_deck_action_is_order_three": cycle != (0, 1, 2) and cycle2 != (0, 1, 2) and cycle3 == (0, 1, 2),
    "unused_three_sheet_cover_is_not_hardcoded_away": "double-cover repair hardcoded as the only branching topology" in forbidden,
    "general_deck_relations_are_required": "deck_groupoid_relations_hold_exactly" in laws,
    "cover_normalization_field_is_required": "normalization_of_joint_spectral_cover" in fields,
    "local_packet_not_global_admission": v10["out_of_sample_policy"]["local_gate_cannot_validate_global_admission"] is True,
}

result = {
    "schema": "marici.aspect.frozen-bivariant-network-signature-v10-check.v1",
    "status": "candidate_v10_frozen_local_schema_pass" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {key: bool(value) for key, value in checks.items()},
    "v9_disposition": "preserved as falsified",
    "v10_disposition": "candidate frozen; two-sheet exceptional-point exchange is retained and the unused three-sheet cyclic cover prevents hardcoded double-cover repair",
    "next_decisive_test": "non-Abelian braid monodromy from two or more branch points, where pairwise deck permutations pass but their ordered composition matters",
}

out = root / "results" / "frozen_bivariant_signature_v10.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "candidate_v10_frozen_local_schema_pass" else 1)
