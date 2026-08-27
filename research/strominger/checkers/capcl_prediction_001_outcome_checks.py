import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTCOME_PATH = ROOT / "research/strominger/results/capcl_sclp_prediction_001_outcome.json"
BASE_RESULT_PATH = ROOT / "research/strominger/results/dependency_aware_partial_repairs.json"


outcome = json.loads(OUTCOME_PATH.read_text(encoding="utf-8"))
base = json.loads(BASE_RESULT_PATH.read_text(encoding="utf-8"))["theta_repair_triangle"]
errors = []
admissible = sum(path.get("dynamically_admissible") is True for path in base.get("paths", []))
codes = sorted({path.get("first_rejection", {}).get("code") for path in base.get("paths", [])})
actual_digest = hashlib.sha256(BASE_RESULT_PATH.read_bytes()).hexdigest()

if outcome.get("outcome") != "ill_typed_target":
    errors.append("unreachable_target_not_classified_ill_typed")
if outcome.get("prediction_confirmed") or outcome.get("prediction_falsified"):
    errors.append("unreached_prediction_scored")
if outcome.get("target_reached") is not False:
    errors.append("target_reachability_overclaimed")
if len(base.get("paths", [])) != 6 or admissible != 0:
    errors.append("base_subdiagram_reachability_changed")
if codes != ["distinction_erased_before_required_repair", "theta_pro_gram_instantiation_blocked_missing_incidence", "valuation_completion_not_source_authorized"]:
    errors.append("base_failure_packet_mismatch")
if actual_digest != outcome.get("evidence", {}).get("sha256"):
    errors.append("adjudication_evidence_drift")
if outcome.get("calculus_modified_before_adjudication") is not False:
    errors.append("calculus_retrofitted_before_adjudication")

print(json.dumps({
    "prediction_id": outcome.get("prediction_id"),
    "passed": not errors,
    "outcome": outcome.get("outcome"),
    "target_reached": outcome.get("target_reached"),
    "base_admissible_path_count": admissible,
    "errors": errors,
}, indent=2))
raise SystemExit(0 if not errors else 1)
