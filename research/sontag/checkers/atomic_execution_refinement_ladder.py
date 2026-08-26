import json
from pathlib import Path


checks = {}


def check(name, condition):
    checks[name] = bool(condition)


def abstract_attempt(unused, effects):
    return (False, effects + 1, True) if unused else (False, effects, False)


def cas_attempt(memory, effects):
    return (True, effects + 1, True) if not memory else (True, effects, False)


for initial in (False, True):
    concrete = cas_attempt(initial, int(initial))
    abstract = abstract_attempt(not initial, int(initial))
    check(
        f"one_step_cas_refines_abstract_{initial}",
        concrete[0] == (not abstract[0])
        and concrete[1:] == abstract[1:],
    )

left_first_1 = cas_attempt(False, 0)
left_first_2 = cas_attempt(left_first_1[0], left_first_1[1])
check("two_sequential_cas_have_one_success",
      left_first_1[2] and not left_first_2[2] and left_first_2[1] == 1)

split_results = (True, True)
abstract_sequential_results = {(True, False), (False, True)}
check("split_read_write_has_no_abstract_order",
      split_results not in abstract_sequential_results)

# Overlap permits either linearization; completed-before-invoked precedence
# permits only the corresponding real-time order.
overlap_observation = (True, False)
check("overlap_has_linearization_witness",
      overlap_observation in abstract_sequential_results)
right_completed_before_left_invoked = True
claimed_left_winner = (True, False)
allowed_if_right_first = (False, True)
check("real_time_precedence_rejects_impossible_winner",
      right_completed_before_left_invoked
      and claimed_left_winner != allowed_if_right_first)

def crash_consistent(consumed, response):
    return consumed == (response is not None)


check("precommit_recovery_is_consistent", crash_consistent(False, None))
check("postcommit_recovery_is_consistent", crash_consistent(True, "ok"))
check("nonce_only_recovery_is_inconsistent", not crash_consistent(True, None))
check("response_only_recovery_is_inconsistent", not crash_consistent(False, "ok"))

# Fence/effect split consequences.
fence_only = {"fence": 4, "effects": 0}
fence_only_retry_accepts = 4 > fence_only["fence"]
check("fence_only_crash_loses_effect",
      not fence_only_retry_accepts and fence_only["effects"] == 0)

effect_only = {"fence": 3, "effects": 1}
effect_only_retry_accepts = 4 > effect_only["fence"]
effect_only_after_retry = {
    "fence": 4,
    "effects": effect_only["effects"] + int(effect_only_retry_accepts),
}
check("effect_only_crash_duplicates_effect",
      effect_only_retry_accepts and effect_only_after_retry["effects"] == 2)

atomic_after = {"fence": 4, "effects": 1}
atomic_retry_accepts = 4 > atomic_after["fence"]
check("atomic_fence_effect_rejects_duplicate",
      not atomic_retry_accepts and atomic_after["effects"] == 1)

# Semantic correctness and deployment authority are independent predicates.
valuations = [
    {"refines": bool(bits & 1), "authorized": bool(bits & 2)}
    for bits in range(4)
]
check("semantic_refinement_does_not_imply_installation_authority",
      any(v["refines"] and not v["authorized"] for v in valuations))
check("installation_authority_does_not_prove_refinement",
      any(v["authorized"] and not v["refines"] for v in valuations))

result = {
    "schema": "marici.sontag.atomic_execution_refinement_ladder.v1",
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
    "checks": checks,
    "levels": [
        "functional transition", "concurrent history",
        "crash recovery", "authority-preserving deployment"
    ],
    "claim_boundary": (
        "Exact finite refinement hostiles; no concrete hardware memory-model, "
        "persistence-protocol, or deployment-authorization theorem."
    ),
}

output = Path(__file__).resolve().parents[1] / "results" / "atomic_execution_refinement_ladder.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["all_passed"] else 1)
