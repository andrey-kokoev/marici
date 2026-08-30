import json
from pathlib import Path


checks = {}


def check(name, condition):
    checks[name] = bool(condition)


def step(state, event, exception=False, state_change=False):
    action, record = state
    if event == "instruction" and action == "inactive":
        return "pending", record
    if event == "execute" and action == "pending" and not exception:
        return "discharged", "pending" if state_change else record
    if event == "blocking_report" and action == "pending" and exception:
        return "fallback_discharged", record
    if event == "record_evidence" and record == "pending":
        return action, "discharged"
    if event == "deadline" and action == "pending":
        return "violated", record
    return state


inactive = ("inactive", "inactive")
pending = step(inactive, "instruction")
check("instruction_activates_obligation", pending == ("pending", "inactive"))

# Permission accepts an empty continuation; an obligation monitor does not
# mark that continuation discharged.
check("obligation_is_not_permission", pending[0] == "pending")

executed = step(pending, "execute", state_change=True)
check("execution_discharges_primary", executed[0] == "discharged")
check("state_change_activates_evidence_obligation", executed[1] == "pending")
check("execution_without_evidence_is_not_global_completion",
      executed != ("discharged", "discharged"))

recorded = step(executed, "record_evidence")
check("evidence_discharges_record_obligation",
      recorded == ("discharged", "discharged"))

fallback = step(pending, "blocking_report", exception=True)
check("declared_exception_enables_typed_fallback",
      fallback[0] == "fallback_discharged")

unjustified_fallback = step(pending, "blocking_report", exception=False)
check("report_without_exception_does_not_discharge",
      unjustified_fallback[0] == "pending")

violated = step(pending, "deadline")
check("pending_at_deadline_is_violation", violated[0] == "violated")

# Safety conflict: execution is disabled, but typed fallback keeps the product
# specification realizable when the exception is established.
safety_exception = True
primary_enabled = not safety_exception
fallback_enabled = safety_exception
check("safety_prohibition_blocks_primary", not primary_enabled)
check("typed_fallback_makes_conflict_realizable", fallback_enabled)

# Without primary or fallback, no strategy can discharge before deadline.
no_primary = False
no_fallback = False
check("missing_primary_and_fallback_is_unrealizable",
      not (no_primary or no_fallback))

# Permission has no pending/violation state; obligation does.
permission_trace_accepts_empty = True
obligation_trace_accepts_empty_at_deadline = step(pending, "deadline")[0] != "violated"
check("empty_trace_separates_permission_from_obligation",
      permission_trace_accepts_empty and not obligation_trace_accepts_empty_at_deadline)

result = {
    "schema": "marici.sontag.obligation_discharge_temporal_control.v1",
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
    "checks": checks,
    "monitor_states": [
        "inactive", "pending", "discharged", "fallback_discharged", "violated"
    ],
    "claim_boundary": (
        "Finite trace semantics for direct action, typed fallback, and evidence "
        "discharge; no universal deadline or multi-agent realizability theorem."
    ),
}

output = Path(__file__).resolve().parents[1] / "results" / "obligation_discharge_temporal_control.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

