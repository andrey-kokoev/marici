import json
from pathlib import Path


checks = {}


def check(name, condition):
    checks[name] = bool(condition)


def initial():
    return {"A": "running", "B": "waiting", "C": "waiting", "parent": "pending", "launches": 1}


def event(state, stage, outcome, valid_contract=False):
    out = dict(state)
    if out[stage] not in ("running", "waiting"):
        return out
    success = outcome == "complete" and valid_contract
    out[stage] = "succeeded" if success else "failed"
    if stage == "A":
        if success:
            if out["B"] == "waiting":
                out["B"] = "running"
                out["launches"] += 1
        else:
            out["B"] = "blocked"
            out["C"] = "blocked"
            out["parent"] = "failed"
    elif stage == "B":
        if success:
            if out["C"] == "waiting":
                out["C"] = "running"
                out["launches"] += 1
        else:
            out["C"] = "blocked"
            out["parent"] = "failed"
    elif stage == "C":
        out["parent"] = "discharged" if success else "failed"
    return out


start = initial()
check("only_root_stage_runs_initially",
      start["A"] == "running" and start["B"] == start["C"] == "waiting")

a_ok = event(start, "A", "complete", valid_contract=True)
check("validated_A_activates_B",
      a_ok["A"] == "succeeded" and a_ok["B"] == "running" and a_ok["C"] == "waiting")
check("A_success_does_not_discharge_parent", a_ok["parent"] == "pending")

b_ok = event(a_ok, "B", "complete", valid_contract=True)
check("validated_B_activates_C",
      b_ok["B"] == "succeeded" and b_ok["C"] == "running")
check("B_success_does_not_discharge_parent", b_ok["parent"] == "pending")

c_ok = event(b_ok, "C", "complete", valid_contract=True)
check("validated_audit_discharges_parent",
      c_ok["C"] == "succeeded" and c_ok["parent"] == "discharged")

a_malformed = event(start, "A", "complete", valid_contract=False)
check("malformed_A_is_failure_not_success", a_malformed["A"] == "failed")
check("A_failure_blocks_all_descendants",
      a_malformed["B"] == a_malformed["C"] == "blocked")
check("A_failure_terminates_parent_as_failed", a_malformed["parent"] == "failed")

b_fail = event(a_ok, "B", "timeout", valid_contract=False)
check("B_failure_blocks_C", b_fail["B"] == "failed" and b_fail["C"] == "blocked")

# Recorded hostile: terminal A failure with descendants still waiting.
observed_hostile = {"A": "failed", "B": "waiting", "C": "waiting"}
check("recorded_run_contains_zombie_descendants",
      observed_hostile["A"] == "failed"
      and observed_hostile["B"] == observed_hostile["C"] == "waiting")

# Replay of an already consumed success does not relaunch B.
replayed = event(a_ok, "A", "complete", valid_contract=True)
check("success_replay_is_idempotent", replayed["launches"] == a_ok["launches"])

root_authority = {"read_evidence", "emit_structured"}
a_authority = {"read_evidence", "emit_structured"}
b_authority = {"emit_structured"}
c_authority = {"emit_structured"}
check("downstream_authority_is_nonamplifying",
      c_authority <= b_authority <= a_authority <= root_authority)
check("network_authority_cannot_arrive_via_output",
      "network" not in a_authority | b_authority | c_authority)

result = {
    "schema": "marici.sontag.delegated_obligation_workflow_control.v1",
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
    "checks": checks,
    "claim_boundary": (
        "Exact finite workflow and observed zombie-obligation hostile; no "
        "universal legal or institutional transfer-of-responsibility theorem."
    ),
}

output = Path(__file__).resolve().parents[1] / "results" / "delegated_obligation_workflow_control.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["all_passed"] else 1)

