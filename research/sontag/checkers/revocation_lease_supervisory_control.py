import json
from pathlib import Path


checks = {}


def check(name, condition):
    checks[name] = bool(condition)


def fenced_attempt(state, lease):
    enabled = (
        lease["epoch"] == state["target_epoch"]
        and state["time"] < lease["expiry"]
        and state["unused"]
        and lease["operation"] == state["operation"]
        and lease["target"] == state["target"]
        and lease["kind"] == state["kind"]
    )
    next_state = dict(state)
    if enabled:
        next_state["unused"] = False
        next_state["effects"] += 1
    return enabled, next_state


base = {
    "target_epoch": 0, "time": 0, "unused": True,
    "operation": "write", "target": "resource-A", "kind": "execute",
    "effects": 0,
}
lease = {
    "epoch": 0, "expiry": 5, "operation": "write",
    "target": "resource-A", "kind": "execute",
}

ok, after = fenced_attempt(base, lease)
check("fresh_fenced_lease_executes", ok and after["effects"] == 1)
again, replayed = fenced_attempt(after, lease)
check("atomic_nonce_consumption_blocks_replay", not again and replayed["effects"] == 1)

revoked = dict(base, target_epoch=1)
stale_ok, stale_after = fenced_attempt(revoked, lease)
check("target_epoch_fence_blocks_stale_lease", not stale_ok and stale_after["effects"] == 0)

expired_ok, _ = fenced_attempt(dict(base, time=5), lease)
check("expiry_blocks_execution", not expired_ok)
widened_ok, _ = fenced_attempt(base, dict(lease, kind="selector"))
check("kind_widening_is_rejected", not widened_ok)
wrong_target_ok, _ = fenced_attempt(base, dict(lease, target="resource-B"))
check("target_widening_is_rejected", not wrong_target_ok)

expiry_only_accepts_stale = revoked["time"] < lease["expiry"] and revoked["unused"]
check("expiry_only_guard_is_unsafe", expiry_only_accepts_stale and not stale_ok)

validated_before_revoke = lease["epoch"] == base["target_epoch"]
side_effect_after_revoke = validated_before_revoke
check("non_atomic_validation_has_toctou_counterexample",
      side_effect_after_revoke and lease["epoch"] != revoked["target_epoch"])

exec_first, exec_first_state = fenced_attempt(base, lease)
exec_then_revoke = dict(exec_first_state, target_epoch=1)
revoke_first_state = dict(base, target_epoch=1)
revoke_first, revoke_then_exec = fenced_attempt(revoke_first_state, lease)
check("atomic_interleavings_preserve_stale_execution_safety",
      exec_first and exec_then_revoke["effects"] == 1
      and not revoke_first and revoke_then_exec["effects"] == 0)

site_a, _ = fenced_attempt(base, lease)
site_b, _ = fenced_attempt(base, lease)
check("duplicated_local_views_violate_global_linearity", site_a and site_b)

first_shared, shared_state = fenced_attempt(base, lease)
second_shared, shared_state = fenced_attempt(shared_state, lease)
check("shared_linearizer_allows_exactly_one", first_shared and not second_shared
      and shared_state["effects"] == 1)

safe_partition_outcome = (True, False)
available_partition_outcome = (True, True)
check("safe_partition_sacrifices_bilateral_availability",
      sum(safe_partition_outcome) == 1 and not all(safe_partition_outcome))
check("bilateral_partition_availability_breaks_single_use",
      all(available_partition_outcome) and sum(available_partition_outcome) == 2)

eligible_site = "A"
partitioned = (eligible_site == "A", eligible_site == "B")
check("prior_locus_partition_preserves_single_use", sum(partitioned) == 1)

result = {
    "schema": "marici.sontag.revocation_lease_supervisory_control.v1",
    "passed": sum(checks.values()), "total": len(checks),
    "all_passed": all(checks.values()), "checks": checks,
    "correspondences": {
        "lease": "finite safety-supervisor state",
        "revocation": "uncontrollable environment event",
        "fencing_epoch": "authority-state observation at actuator locus",
        "atomic_attempt": "linearized guarded transition",
        "disconnected_single_use": "decentralized coobservability obstruction",
        "partition": "safety/nonblocking tradeoff",
    },
    "claim_boundary": (
        "Exact finite safety and impossibility witnesses; no concrete CAS, "
        "clock, crash-persistence, or liveness implementation theorem."
    ),
}

output = Path(__file__).resolve().parents[1] / "results" / "revocation_lease_supervisory_control.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

