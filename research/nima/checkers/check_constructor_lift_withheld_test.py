import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PREDICTION = ROOT / "research/nima/results/constructor_lift_withheld_prediction.json"
TEST = ROOT / "research/nima/results/constructor_lift_withheld_test.json"


def main() -> None:
    prediction = json.loads(PREDICTION.read_text(encoding="utf-8"))
    test = json.loads(TEST.read_text(encoding="utf-8"))
    observed = test["observed"]
    expected = prediction["prediction"]
    gates = {
        "prediction_was_frozen": prediction["inspection_state"] == "prediction_frozen_before_withheld_evidence",
        "withheld_sector_matches": prediction["withheld_sector"] == test["withheld_sector"],
        "prediction_not_changed": test["prediction_changed_after_inspection"] is False,
        "normalized_readout_exists": observed["source_normalized_score"] and observed["fixed_state_mixed_readout"],
        "observer_family_is_faithful": observed["contextually_faithful_observer_family"],
        "no_successor_leg": not observed["outcome_bearing_interaction"] and not observed["conditional_successor_states"],
        "no_resource_cycle": not observed["pointer_preparation_and_reset"] and not observed["repeatability_or_stabilization"],
        "first_failure_predicted": observed["first_failed_arrow"] == expected["first_failed_arrow"],
        "constructor_verdict_predicted": observed["constructor_exists"] == expected["constructor_exists"],
        "criterion_survives": test["prediction_verdict"] == "confirmed" and test["criterion_status"] == "survives_one_withheld_sector",
        "three_hashed_sources": len(test["evidence"]) == 3 and all(len(item["sha256"]) == 64 for item in test["evidence"]),
    }
    failed = [name for name, passed in gates.items() if not passed]
    print(json.dumps({"gates": gates, "passed": len(gates) - len(failed), "total": len(gates), "failed": failed}, indent=2))
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
