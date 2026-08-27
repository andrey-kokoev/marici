import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CONTRACT_PATH = ROOT / "research/strominger/contracts/capcl-sclp-preregistration.v1.json"
RESULT_PATH = ROOT / "research/strominger/results/capcl_sclp_preregistration.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
errors = []

if contract.get("status") != "preregistered_unverified":
    errors.append("prediction_status_not_unverified")
if contract.get("target", {}).get("future_outcome_artifact") is not None:
    errors.append("future_outcome_inspected_or_fitted")
if contract.get("prediction", {}).get("first_obstruction_coordinate") != "descent":
    errors.append("first_obstruction_not_preregistered_as_descent")
if contract.get("prediction", {}).get("downstream_coordinates_not_yet_reached") != ["higher_coherence", "selector", "observation", "execution"]:
    errors.append("downstream_obstructions_overclaimed")
if len(contract.get("prediction", {}).get("required_witnesses", [])) != 4:
    errors.append("primitive_completion_witness_packet_incomplete")
if len(contract.get("falsifiers", [])) != 3:
    errors.append("prediction_not_sharply_falsifiable")

source_checks = []
for item in contract.get("source_snapshots", []):
    path = ROOT / item["path"]
    actual = digest(path)
    matches = actual == item["sha256"]
    if not matches:
        errors.append("source_snapshot_drift:" + item["path"])
    source_checks.append({"path": item["path"], "sha256": actual, "matches": matches})

protocol = contract.get("resolution_protocol", {})
if not (
    protocol.get("freeze_calculus_during_test") is True
    and protocol.get("compare_before_schema_revision") is True
    and protocol.get("allowed_outcomes") == ["confirmed", "falsified", "ill_typed_target"]
    and protocol.get("schema_change_before_outcome_invalidates_prediction_test") is True
):
    errors.append("resolution_protocol_not_frozen")

result = {
    "schema": "marici.strominger.capcl-preregistration-result.v1",
    "prediction_id": contract.get("prediction_id"),
    "passed": not errors,
    "status": "preregistration_valid" if not errors else "invalid",
    "prediction_outcome": "not_yet_tested",
    "first_obstruction_coordinate": contract.get("prediction", {}).get("first_obstruction_coordinate"),
    "source_checks": source_checks,
    "errors": errors,
}
RESULT_PATH.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
