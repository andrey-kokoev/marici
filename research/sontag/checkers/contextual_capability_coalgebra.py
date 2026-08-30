"""Exact finite reconstruction of latent packet axes from future context behavior."""

import itertools
import json
from pathlib import Path


CONTEXTS = (("observer", 0), ("observer", 1), ("controller", 0), ("controller", 1))
CONTEXT_COMMANDS = ("grant", "replenish")


def enabled_actions(context):
    actor, budget = context
    if actor == "controller" and budget == 1:
        return ("noop", "set0", "set1")
    return ("noop",)


def advance(context, command):
    actor, budget = context
    if command == "grant":
        actor = "controller"
    elif command == "replenish":
        budget = 1
    return actor, budget


def words(depth):
    result = [()]
    frontier = [()]
    for _ in range(depth):
        frontier = [word + (command,) for word in frontier for command in CONTEXT_COMMANDS]
        result.extend(frontier)
    return tuple(result)


def context_trace(context, word):
    trace = [enabled_actions(context)]
    for command in word:
        context = advance(context, command)
        trace.append(enabled_actions(context))
    return tuple(trace)


def signature(context, depth):
    return tuple((word, context_trace(context, word)) for word in words(depth))


def partition(depth):
    fibers = {}
    for context in CONTEXTS:
        fibers.setdefault(signature(context, depth), []).append(context)
    return tuple(sorted(tuple(group) for group in fibers.values()))


def index(groups):
    return {context: i for i, group in enumerate(groups) for context in group}


def transition_well_defined(source_depth, target_depth):
    source_groups = partition(source_depth)
    target_index = index(partition(target_depth))
    for group in source_groups:
        for command in CONTEXT_COMMANDS:
            images = {target_index[advance(context, command)] for context in group}
            if len(images) != 1:
                return False
    return True


def main():
    p0 = partition(0)
    p1 = partition(1)
    poor = (("observer", 0), ("observer", 1), ("controller", 0))
    checks = {
        "three_contexts_have_same_immediate_capability": all(
            enabled_actions(context) == ("noop",) for context in poor
        ),
        "rich_context_has_set_actions": enabled_actions(("controller", 1)) == ("noop", "set0", "set1"),
        "immediate_partition_collapses_three_latent_causes": any(set(group) == set(poor) for group in p0),
        "grant_alone_does_not_create_capability_without_budget": enabled_actions(advance(("observer", 0), "grant")) == ("noop",),
        "replenish_alone_does_not_create_capability_without_authority": enabled_actions(advance(("observer", 0), "replenish")) == ("noop",),
        "grant_after_replenish_creates_capability": enabled_actions(advance(("observer", 1), "grant")) == ("noop", "set0", "set1"),
        "replenish_after_grant_creates_capability": enabled_actions(advance(("controller", 0), "replenish")) == ("noop", "set0", "set1"),
        "one_step_future_behavior_separates_all_contexts": len(p1) == len(CONTEXTS),
        "immediate_quotient_has_no_same_level_context_dynamics": not transition_well_defined(0, 0),
        "graded_context_transition_is_well_defined": transition_well_defined(1, 0),
        "grant_and_replenish_commute_on_context": all(
            advance(advance(c, "grant"), "replenish") == advance(advance(c, "replenish"), "grant")
            for c in CONTEXTS
        ),
    }
    payload = {
        "schema": "marici.sontag.contextual_capability_coalgebra.v1",
        "passed": sum(checks.values()),
        "total": len(checks),
        "all_passed": all(checks.values()),
        "checks": checks,
        "partitions": {"immediate": p0, "one_step_contextual": p1},
        "verdict": (
            "Authority and resource are not reconstructible from one immediate capability "
            "fiber, but are reconstructed as distinct latent axes by lawful grant and "
            "replenish continuations. Packet fields are therefore presentation coordinates "
            "of a context-indexed capability coalgebra exactly when context changes address "
            "them independently; otherwise future-capability minimization must quotient them."
        ),
    }
    output = Path(__file__).parents[1] / "results" / "contextual_capability_coalgebra.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if payload["all_passed"] else 1)


if __name__ == "__main__":
    main()
