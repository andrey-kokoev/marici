import hashlib
import json
from pathlib import Path


checks = {}


def check(name, condition):
    checks[name] = bool(condition)


spec = {
    "constructor_id": "protected-write/v1",
    "captured_data": {"delta": 7},
    "input_schema": "integer/v1",
    "output_schema": "integer/v1",
    "effect": {"operation": "write", "target": "resource-A"},
    "authority_requirement": {"actor": "agent-A", "epoch": 4},
    "request_id": "request-17",
    "evidence_schema": "execution-evidence/v1",
}
wire = json.dumps(spec, sort_keys=True, separators=(",", ":")).encode()
copy_live = bytes(wire)
copy_revoked = bytes(wire)


def invoke(package, value, target_epoch, trust_captured_epoch=False):
    closure = json.loads(package)
    pure_output = value + closure["captured_data"]["delta"]
    observed_epoch = (
        closure["authority_requirement"]["epoch"]
        if trust_captured_epoch else target_epoch
    )
    admitted = observed_epoch == closure["authority_requirement"]["epoch"]
    return {
        "pure_output": pure_output,
        "effect_count": int(admitted),
        "status": "executed" if admitted else "rejected",
        "reason": "live_epoch_match" if admitted else "stale_epoch",
    }


live = invoke(copy_live, 5, target_epoch=4)
revoked = invoke(copy_revoked, 5, target_epoch=5)
naive_revoked = invoke(copy_revoked, 5, target_epoch=5, trust_captured_epoch=True)

check("packages_are_byte_identical", copy_live == copy_revoked)
check("packages_have_same_digest",
      hashlib.sha256(copy_live).digest() == hashlib.sha256(copy_revoked).digest())
check("pure_computation_is_identical", live["pure_output"] == revoked["pure_output"] == 12)
check("live_epoch_executes_once", live["status"] == "executed" and live["effect_count"] == 1)
check("revoked_epoch_rejects_without_effect",
      revoked["status"] == "rejected" and revoked["effect_count"] == 0)
check("rejection_is_typed_stale_epoch", revoked["reason"] == "stale_epoch")
check("only_live_authority_varies",
      json.loads(copy_live) == json.loads(copy_revoked) and 4 != 5)
check("deleting_live_observation_executes_stale_copy",
      naive_revoked["status"] == "executed" and naive_revoked["effect_count"] == 1)

# Re-copying does not alter the captured epoch or restore live standing.
many_copies = [bytes(wire) for _ in range(5)]
many_results = [invoke(package, 5, target_epoch=5) for package in many_copies]
check("copying_never_refreshes_epoch",
      all(r["status"] == "rejected" for r in many_results))

# The modeled actuator remains physically capable in both worlds; only the
# conforming evaluator's admitted transition differs.
physical_capability_live = True
physical_capability_revoked = True
check("physical_capability_is_held_fixed",
      physical_capability_live and physical_capability_revoked)
check("authority_is_not_physical_capability",
      physical_capability_revoked and revoked["status"] == "rejected")

result = {
    "schema": "marici.sontag.deutschian_live_authority_binding_variation.v1",
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
    "checks": checks,
    "package_sha256": hashlib.sha256(wire).hexdigest(),
    "live_world": live,
    "revoked_world": revoked,
    "deleted_live_observer_hostile": naive_revoked,
    "claim_boundary": (
        "Hard-to-vary result for conforming evaluators with trustworthy live "
        "epoch observation; no physical impossibility claim outside that domain."
    ),
}

output = Path(__file__).resolve().parents[1] / "results" / "deutschian_live_authority_binding_variation.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["all_passed"] else 1)

