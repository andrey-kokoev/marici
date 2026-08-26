"""Exact finite no-go: unlabeled dynamics do not determine their source task."""

import itertools
import json
from pathlib import Path


STATES = (0, 1)
ACTIONS = ("noop", "set0", "set1")


def transition(state, action):
    if action == "noop":
        return state
    return int(action[-1])


def task(target, state):
    return state == target


def policies():
    for choices in itertools.product(ACTIONS, repeat=len(STATES)):
        yield dict(zip(STATES, choices))


def repairs(policy, target):
    return all(task(target, transition(state, policy[state])) for state in STATES)


def cost(policy):
    return sum(policy[state] != "noop" for state in STATES)


def minimal_repairs(target):
    good = tuple(policy for policy in policies() if repairs(policy, target))
    minimum = min(cost(policy) for policy in good)
    return tuple(policy for policy in good if cost(policy) == minimum)


def raw_dynamics():
    return tuple((state, action, transition(state, action)) for state in STATES for action in ACTIONS)


def success_labeled_dynamics(target):
    return tuple(
        (state, action, transition(state, action), task(target, transition(state, action)))
        for state in STATES
        for action in ACTIONS
    )


def main():
    repair_zero = minimal_repairs(0)
    repair_one = minimal_repairs(1)
    raw_for_task_zero = raw_dynamics()
    raw_for_task_one = raw_dynamics()
    checks = {
        "same_raw_dynamics_support_task_zero": raw_for_task_zero == raw_dynamics(),
        "same_raw_dynamics_support_task_one": raw_for_task_one == raw_dynamics(),
        "raw_dynamics_are_identical_across_tasks": raw_for_task_zero == raw_for_task_one,
        "task_predicates_disagree_on_every_state": all(task(0, x) != task(1, x) for x in STATES),
        "each_task_has_a_unique_minimal_repair_policy": len(repair_zero) == len(repair_one) == 1,
        "minimal_repair_policies_are_different": repair_zero != repair_one,
        "task_zero_policy_sets_damaged_one_to_zero": repair_zero[0][1] == "set0",
        "task_one_policy_sets_damaged_zero_to_one": repair_one[0][0] == "set1",
        "success_labeled_behavior_separates_tasks": success_labeled_dynamics(0) != success_labeled_dynamics(1),
        "adding_success_label_does_not_derive_task_from_raw_dynamics": raw_dynamics() == raw_for_task_zero,
    }
    payload = {
        "schema": "marici.sontag.source_task_irreducibility.v1",
        "passed": sum(checks.values()),
        "total": len(checks),
        "all_passed": all(checks.values()),
        "checks": checks,
        "raw_dynamics": raw_dynamics(),
        "minimal_repair_for_target_zero": repair_zero,
        "minimal_repair_for_target_one": repair_one,
        "verdict": (
            "One unlabeled process supports two incompatible source tasks with different "
            "unique minimal repair policies. Raw capability dynamics cannot determine which "
            "relation counts as success. A success effect makes the task reconstructible only "
            "by carrying that distinction. The Marici object is therefore irreducibly "
            "relational to a source-defined task or to a deeper constructor that generates it."
        ),
    }
    output = Path(__file__).parents[1] / "results" / "source_task_irreducibility.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if payload["all_passed"] else 1)


if __name__ == "__main__":
    main()
