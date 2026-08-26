from fractions import Fraction
import json
from pathlib import Path


checks = {}


def check(name, condition):
    checks[name] = bool(condition)


# Exact detector decision boundary.
r = Fraction(3, 4)
lam = Fraction(1, 3)
c = Fraction(1, 20)
delta = Fraction(9, 25) * r * (1 - lam) - c
threshold = Fraction(25) * c / (Fraction(9) * (1 - lam))
check("probe_advantage_formula_positive", delta > 0)
check("threshold_rule_matches_advantage", (r >= threshold) == (delta >= 0))

# Changing only the objective changes the recommendation, not the plant.
lam_expensive_readiness = Fraction(9, 10)
delta_expensive_readiness = (
    Fraction(9, 25) * r * (1 - lam_expensive_readiness) - c
)
check("objective_changes_recommendation", delta > 0 and delta_expensive_readiness < 0)

# Enumerate logical valuations to exhibit the non-implications required by
# the claim boundary. These witnesses are deliberately independent of role
# labels: RBAC is not assumed to exhaust authority.
valuations = [
    {
        "capable": bool(bits & 1),
        "recommended": bool(bits & 2),
        "authorized": bool(bits & 4),
        "executed": bool(bits & 8),
        "recorded": bool(bits & 16),
    }
    for bits in range(32)
]


def witness(left, right):
    return any(v[left] and not v[right] for v in valuations)


check("recommendation_does_not_imply_authority", witness("recommended", "authorized"))
check("authority_does_not_imply_capability", witness("authorized", "capable"))
check("capability_does_not_imply_execution", witness("capable", "executed"))
check("execution_does_not_imply_recording", witness("executed", "recorded"))
check("authority_does_not_imply_execution", witness("authorized", "executed"))
check("recording_does_not_imply_authority", witness("recorded", "authorized"))

# A one-shot grant is a minimal endogenous authority transition.
def execute_with_one_shot_grant(capable, recommended, grant_available):
    executed = capable and recommended and grant_available
    next_grant = grant_available and not executed
    evidence = executed
    return executed, next_grant, evidence


first = execute_with_one_shot_grant(True, True, True)
second = execute_with_one_shot_grant(True, True, first[1])
check("authorized_execution_consumes_grant", first == (True, False, True))
check("same_plant_and_policy_blocked_after_consumption", second == (False, False, False))

# Physical and policy state can be identical while authority history changes
# the enabled action set.
check(
    "authority_history_changes_future_actions",
    execute_with_one_shot_grant(True, True, True)[0]
    and not execute_with_one_shot_grant(True, True, False)[0],
)

result = {
    "schema": "marici.sontag.control_authority_plane_conjecture.v1",
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
    "checks": checks,
    "exact_values": {
        "belief": str(r),
        "readiness_shadow_value": str(lam),
        "probe_cost": str(c),
        "probe_advantage": str(delta),
        "threshold": str(threshold),
    },
    "claim_boundary": (
        "Finite witnesses verify predicate independence and one endogenous "
        "authority transition; cross-sector architectural generality remains open."
    ),
}

output = Path(__file__).resolve().parents[1] / "results" / "control_authority_plane_conjecture.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

