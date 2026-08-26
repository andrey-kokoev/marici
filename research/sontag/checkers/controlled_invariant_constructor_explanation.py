"""Exact finite test of the controlled-invariant constructor explanation."""

import itertools
import json
from pathlib import Path


SOURCES = (0, 1)
PLANT = (0, 1)
STATES = tuple(itertools.product(SOURCES, PLANT))
ACTIONS = ("noop", "set0", "set1")
DISTURBANCES = ("noop", "flip")


def disturb(x, disturbance):
    return x if disturbance == "noop" else 1 - x


def actuate(x, action):
    if action == "noop":
        return x
    return int(action[-1])


def cost(action):
    return int(action != "noop")


def goal(source, x):
    return source == x


def policies(actions=ACTIONS):
    for choices in itertools.product(actions, repeat=len(STATES)):
        yield dict(zip(STATES, choices))


def source_blind_policies(actions=ACTIONS):
    for choices in itertools.product(actions, repeat=len(PLANT)):
        yield dict(zip(PLANT, choices))


def robust(policy, actions=ACTIONS, budget=1):
    for source in SOURCES:
        for disturbance in DISTURBANCES:
            damaged = disturb(source, disturbance)
            action = policy[(source, damaged)]
            if action not in actions or cost(action) > budget:
                return False
            if not goal(source, actuate(damaged, action)):
                return False
    return True


def robust_source_blind(policy):
    for source in SOURCES:
        for disturbance in DISTURBANCES:
            damaged = disturb(source, disturbance)
            action = policy[damaged]
            if not goal(source, actuate(damaged, action)):
                return False
    return True


def intervention_score(policy):
    return sum(cost(policy[state]) for state in STATES)


def terminal_readout(_source, _x):
    return 0


def main():
    robust_policies = tuple(p for p in policies() if robust(p))
    minimum_score = min(intervention_score(p) for p in robust_policies)
    minimal = tuple(p for p in robust_policies if intervention_score(p) == minimum_score)
    relational = {
        (0, 0): "noop",
        (0, 1): "set0",
        (1, 0): "set1",
        (1, 1): "noop",
    }
    lookup_one = {state: "set1" for state in STATES}
    reset_zero = {state: "set0" for state in STATES}
    observer_actions = ("noop",)

    checks = {
        "a_robust_constructor_policy_exists": len(robust_policies) > 0,
        "source_blind_control_cannot_repair_both_tasks": not any(
            robust_source_blind(p) for p in source_blind_policies()
        ),
        "lookup_one_fails_source_zero": not robust(lookup_one),
        "reset_zero_fails_source_one": not robust(reset_zero),
        "observer_without_set_actions_has_no_robust_policy": not any(
            robust(p, actions=observer_actions) for p in policies(observer_actions)
        ),
        "zero_repair_budget_has_no_robust_policy": not any(
            robust(p, budget=0) for p in policies()
        ),
        "relational_policy_is_robust": robust(relational),
        "minimal_intervention_selects_relational_policy": minimal == (relational,),
        "constant_terminal_readout_hides_goal_failure": terminal_readout(0, 0) == terminal_readout(0, 1),
        "source_relative_goal_separates_hidden_failure": goal(0, 0) and not goal(0, 1),
        "disturbance_suite_exposes_need_for_repair": disturb(0, "flip") == 1,
        "resource_trace_distinguishes_noop_from_redundant_reset": cost("noop") != cost("set0"),
    }
    payload = {
        "schema": "marici.sontag.controlled_invariant_constructor_explanation.v1",
        "passed": sum(checks.values()),
        "total": len(checks),
        "all_passed": all(checks.values()),
        "checks": checks,
        "robust_policy_count": len(robust_policies),
        "minimum_intervention_score": minimum_score,
        "minimal_policy_count": len(minimal),
        "minimal_policy": {f"s{source}_x{x}": action for (source, x), action in relational.items()},
        "verdict": (
            "The finite reusable object is explained by a source-relative robust controlled "
            "invariant, not by its terminal value. Source relation, disturbance family, "
            "authorized controls, resource bound, transition law, and evidence readout perform "
            "independent causal jobs. Minimal future-capability realization removes redundant "
            "policy presentation while retaining resource-distinct behavior."
        ),
    }
    output = Path(__file__).parents[1] / "results" / "controlled_invariant_constructor_explanation.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if payload["all_passed"] else 1)


if __name__ == "__main__":
    main()
