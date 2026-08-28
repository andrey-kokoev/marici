import json
from pathlib import Path


root = Path(__file__).parents[1]
marici = root.parents[1]
contract = json.loads((root / "contracts" / "dual-gamma-cyclic-closure-admission.v1.json").read_text(encoding="utf-8"))
candidates = [
    json.loads((marici / "research" / "benincasa" / "results" / name).read_text(encoding="utf-8"))
    for name in (
        "rank26-dual-gamma-cyclic-atlas-closure.json",
        "rank26-dual-gamma-cyclic-atlas-closure-p32003.json",
    )
]

required = contract["required_values"]
def observe(candidate):
    return {
        "quotient_transport_matrix_count": len(candidate.get("quotient_transport_matrices", [])),
        "epsilon_edge_unit_count": len(candidate.get("epsilon_edge_units", [])),
        "bockstein_line_edge_unit_count": len(candidate.get("bockstein_line_edge_units", [])),
        "quotient_identity_residual_rank": candidate.get("quotient_identity_residual_rank"),
        "epsilon_edge_product": candidate.get("epsilon_edge_product"),
        "bockstein_line_edge_product": candidate.get("bockstein_line_edge_product"),
    }


observations = {str(candidate["prime"]): observe(candidate) for candidate in candidates}

missing_or_wrong = {
    prime: {
        key: {"required": value, "observed": observed.get(key)}
        for key, value in required.items()
        if observed.get(key) != value
    }
    for prime, observed in observations.items()
}
missing_or_wrong = {prime: failures for prime, failures in missing_or_wrong.items() if failures}

accepted = not missing_or_wrong

checks = {
    "contract_was_frozen_before_repaired_replay": contract["status"] == "frozen_before_repaired_replay",
    "both_primes_are_present": set(observations) == {"32009", "32003"},
    "both_packets_pass_their_source_checks": all(candidate.get("passed") is True for candidate in candidates),
    "both_packets_satisfy_every_frozen_value": accepted,
    "both_packets_export_chart_provenance": all(len(candidate.get("chart_construction_provenance", [])) == 3 for candidate in candidates),
    "both_packets_export_ordered_matrix_product": all("ordered_quotient_matrix_product" in candidate for candidate in candidates),
}

result = {
    "schema": "marici.aspect.dual-gamma-cyclic-closure-admission-check.v1",
    "status": "repaired_candidate_admitted" if all(checks.values()) else "current_candidate_rejected_or_audit_failure",
    "checks": checks,
    "observations": observations,
    "missing_or_wrong": missing_or_wrong,
    "admitted_scope": "strict cyclic descent on the rank-26 quotient, literal epsilon coordinate, and common gamma-Bockstein line at the two checked primes",
    "next_gate": "actual specialization-cone cohomology rather than another chart-descent refinement",
}

out = root / "results" / "dual_gamma_cyclic_closure_admission.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "repaired_candidate_admitted" else 1)
