import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PATH = ROOT / "research/strominger/contracts/capcl-magnetic-q31-preregistration.v1.json"
contract = json.loads(PATH.read_text(encoding="utf-8"))
errors = []

for item in contract.get("source_snapshots", []):
    actual = hashlib.sha256((ROOT / item["path"]).read_bytes()).hexdigest()
    if actual != item["sha256"]:
        errors.append("source_snapshot_drift:" + item["path"])
eligibility = contract.get("eligibility", {})
target = contract.get("target", {})
prediction = contract.get("prediction", {})
if not (
    contract.get("status") == "preregistered_unverified"
    and eligibility.get("operator_and_component_constructor_defined") is True
    and eligibility.get("target_previously_computed") is False
    and target == {"q": 31, "g_range_inclusive": [2, 20], "k": 10, "column_count": 22, "matrix_kind": "full_reflected_component_matrix_not_preferred_minor"}
):
    errors.append("q31_target_not_frozen_or_eligible")
if not (
    prediction.get("obstruction_coordinate") == "observation"
    and prediction.get("predicted_obstruction") == "none"
    and prediction.get("internal_cancellation_with_complete_Hall_matching") is False
    and prediction.get("chart_minor_zeros_do_not_count_as_falsifiers") is True
    and prediction.get("does_not_claim_unbounded_q_or_g") is True
):
    errors.append("q31_prediction_mistyped")
protocol = contract.get("resolution_protocol", {})
if protocol.get("allowed_outcomes") != ["confirmed_in_declared_range", "falsified", "ill_typed_target"]:
    errors.append("q31_resolution_protocol_mistyped")

print(json.dumps({"prediction_id": contract.get("prediction_id"), "passed": not errors, "status": "preregistration_valid" if not errors else "invalid", "outcome": "not_yet_tested", "errors": errors}, indent=2))
raise SystemExit(0 if not errors else 1)
