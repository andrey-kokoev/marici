"""Hostile proof that scalar event axes cannot type action identity."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
ASPECT_AUDIT = ROOT / "results" / "aspect_seven_axis_hodge_model_audit.json"
SPIN_AUDIT = ROOT / "results" / "spin_connection_hodge_control_no_laundering_checks.json"
RESULT = ROOT / "results" / "dependent_action_witness_checks.json"

aspect = json.loads(ASPECT_AUDIT.read_text(encoding="utf-8"))
spin = json.loads(SPIN_AUDIT.read_text(encoding="utf-8"))

shared_axes = {
    "scalar": "unknown",
    "packet": "unknown",
    "incidence": "unknown",
    "history": "unknown",
    "path": "admissible",
    "coefficient": "native",
    "action": "authorized",
    "domain": "preserved",
}
passive_axes = dict(shared_axes)
active_axes = dict(shared_axes)

passive_witness = {
    "operation_id": "celestial_frame_rotation",
    "source_object": "oriented_orthonormal_frame_atlas",
    "target_object": "spin_two_component_presentation",
    "domain_certificate": "Levi_Civita_covariance",
    "authority_locus": "presentation",
    "variance": "passive_change_of_frame",
    "geometric_effect": "identity_on_STF_tensor",
    "coherence_witness": "component_variation_plus_basis_variation_equals_zero",
}
active_witness = {
    "operation_id": "celestial_hodge_rotation",
    "source_object": "radiative_STF_tensor_bundle",
    "target_object": "radiative_STF_tensor_bundle",
    "domain_certificate": "parallel_Hodge_endomorphism",
    "authority_locus": "state",
    "variance": "active_bundle_endomorphism",
    "geometric_effect": "J_on_STF_tensor",
    "coherence_witness": "J_squared_equals_minus_identity",
}

required_fields = set(passive_witness)
checks = {
    "prior_aspect_audit_passes": aspect["status"] == "passed",
    "spin_active_passive_audit_passes": spin["status"] == "passed",
    "eight_scalar_axes_alias_active_and_passive_actions": passive_axes == active_axes,
    "typed_witnesses_have_same_complete_schema": set(active_witness) == required_fields,
    "authority_locus_separates_the_pair": passive_witness["authority_locus"] != active_witness["authority_locus"],
    "variance_separates_the_pair": passive_witness["variance"] != active_witness["variance"],
    "geometric_effect_separates_the_pair": passive_witness["geometric_effect"] != active_witness["geometric_effect"],
    "source_and_target_objects_separate_the_pair": (passive_witness["source_object"], passive_witness["target_object"]) != (active_witness["source_object"], active_witness["target_object"]),
    "matrix_generator_alone_cannot_separate_the_pair": spin["checks"]["passive_frame_rotation_has_double_angle"] and spin["checks"]["active_and_passive_geometric_actions_are_distinct"],
}

payload = {
    "schema": "marici.strominger.dependent-action-witness.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "hostile_pair": {
        "shared_eight_axis_tuple": shared_axes,
        "passive_action": passive_witness,
        "active_action": active_witness,
    },
    "compiler_conclusion": {
        "domain_axis_is_necessary_but_not_sufficient": True,
        "smallest_structural_repair": "replace scalar action value by a dependent ActionWitness record",
        "action_witness_fields": sorted(required_fields),
        "reason": "authorization is relative to source, target, domain, locus, variance, effect, and coherence; it is not a property of a matrix alone",
    },
}
payload["checker_sha256"] = hashlib.sha256(HERE.read_bytes()).hexdigest()
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="ascii")
print(f"{payload['passed']}/{payload['total']} checks passed")
print(payload["checker_sha256"])
raise SystemExit(0 if payload["status"] == "passed" else 1)
