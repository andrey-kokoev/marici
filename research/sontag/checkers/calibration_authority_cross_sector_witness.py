import json
from pathlib import Path


root = Path(__file__).resolve().parents[2]
source_path = root / "flavor" / "results" / "wp549_temporal_scale_calibration_contract.json"
source = json.loads(source_path.read_text(encoding="utf-8"))

checks = {}


def check(name, condition):
    checks[name] = bool(condition)


table = source["transition_table"]
valid = table["unlinked"]["calibration_success"]
fitted = table["unlinked"]["fitted_row"]
valid_trial = table[valid["next_state"]]["physics_trial"]
fitted_trial = table[fitted["next_state"]]["physics_trial"]

check("source_checker_passed", source["passed"])
check("calibration_is_state_establishing", valid == {
    "next_state": "valid_3", "observation": "reference_readback"
})
check("fitted_row_does_not_establish_state", fitted == {
    "next_state": "unlinked", "observation": "compiler_reject"
})
check("valid_history_enables_trial", valid_trial["observation"] == "accepted_readout")
check("fitted_history_rejects_same_trial", fitted_trial["observation"] == "invalid_readout")
check("accepted_trial_consumes_authority_state", valid_trial["next_state"] == "valid_2")
check("rejected_trial_preserves_unlinked_state", fitted_trial["next_state"] == "unlinked")
check("inactive_rank_is_two", source["rank_by_state"]["unlinked_or_expired"] == 2)
check("valid_rank_is_three", source["rank_by_state"]["valid"] == 3)
check("deletion_restores_scale_kernel", source["rank_by_state"]["deletion_replay_kernel"] == ["1", "1", "0"])
check("deletion_replay_verified", source["checks"]["deletion_replay_invalidates_dependent_readouts"])
check("null_does_not_grant", source["checks"]["null_calibration_does_not_establish_interface"])
check("expiry_revokes_future_readout", source["checks"]["expiry_forbids_late_readout"])

# The numerical row is deliberately represented as one shared immutable value
# referenced by both histories. Only provenance/admission state differs.
presented_row = (0, 1, -1)
history_pair = {
    "calibrated": {"row": presented_row, "state": valid["next_state"]},
    "fitted": {"row": presented_row, "state": fitted["next_state"]},
}
check("same_presented_row_different_authority_state",
      history_pair["calibrated"]["row"] == history_pair["fitted"]["row"]
      and history_pair["calibrated"]["state"] != history_pair["fitted"]["state"])
check("authority_state_changes_enabled_language",
      valid_trial["observation"] != fitted_trial["observation"])

result = {
    "schema": "marici.sontag.calibration_authority_cross_sector_witness.v1",
    "source": str(source_path.relative_to(root.parent)).replace("\\", "/"),
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
    "checks": checks,
    "history_pair": history_pair,
    "claim_boundary": (
        "This is a non-optical endogenous interface-authority witness, not a "
        "universal actor-role-delegation theorem."
    ),
}

output = root / "sontag" / "results" / "calibration_authority_cross_sector_witness.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

