import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FINITE = ROOT / "research/nima/results/evans-joint-response-finite-source-map.json"
PRIOR = ROOT / "research/nima/results/evans-euler-comparison-structure-audit.json"
OUT = ROOT / "research/nima/results/evans-joint-response-forward-realization-status.json"

finite = json.loads(FINITE.read_text(encoding="utf-8"))
prior = json.loads(PRIOR.read_text(encoding="utf-8"))
checks = {
    "finite_source_operation_passed": finite.get("passed") is True,
    "both_response_coordinates_retained": finite["checks"]["both_response_coordinates_retained"],
    "source_state_nollapse": finite["checks"]["joint_source_map_is_injective"],
    "transport_intertwines": finite["checks"]["translation_transport_intertwines"],
    "fixed_marginal_hostile_rejected": finite["checks"]["fixed_marginal_hostile_has_nonzero_joint_residual"],
    "prior_common_operator_promotion_remains_refused": prior["checks"]["common_operator_promotion_refused"],
}
assert all(checks.values()), checks
result = {
    "schema": "marici.nima.evans-joint-response-forward-realization-status.v1",
    "classification": "finite_forward_realization_constructed_attachment_transport_blocked",
    "stratum": "finite based Evans history to density-Haar joint graph before determinant attachment",
    "checks": checks,
    "first_missing_typed_object": "source-derived boundary differential or polarization pairing the seam correspondence into the endpoint-Euler-archimedean determinant packet",
    "failed_consequence": "no packet clutching, determinant monodromy, completion, or Haar energy-cycle readout follows from the forward map",
    "acceptance_test": "derive the attachment before determinant formation and prove exact moving-window recovery, Fourier-Tate transport, order-three anomaly compatibility, and cutoff-uniform Douglas domination on the arithmetic source module",
    "known_hostile": "the universal truncated-Fourier bulk has Gaussian packets with vanishing bulk energy and nonvanishing moving-window row, so it fails cutoff-uniform Douglas domination",
    "passed": True,
}
OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
