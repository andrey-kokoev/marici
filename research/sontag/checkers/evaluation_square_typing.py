import json
from pathlib import Path


states = ("x", "y", "u", "v")
G = {"x": "u", "y": "v", "u": "u", "v": "v"}
effect = {"x": 0, "y": 0, "u": 0, "v": 1}


def pullback(output, action):
    return {state: output[action[state]] for state in states}


pulled = pullback(effect, G)
present_fiber = {state for state in ("x", "y") if effect[state] == 0}
constraint_domain = present_fiber
observed_domain = set(states)

checks = {
    "present_effect_merges_x_and_y": effect["x"] == effect["y"] == 0,
    "intervention_then_effect_separates_x_and_y": effect[G["x"]]
    != effect[G["y"]],
    "pulled_back_effect_separates_x_and_y": pulled["x"] != pulled["y"],
    "evaluation_square_holds_for_every_state": all(
        effect[G[state]] == pulled[state] for state in states
    ),
    "present_record_fiber_contains_both_states": present_fiber == {"x", "y"},
    "source_constraint_removes_distinguishing_target": G["y"]
    not in constraint_domain,
    "observation_preserves_distinguishing_continuation": G["y"]
    in observed_domain,
}

result = {
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "effect": effect,
    "pulled_back_effect": pulled,
    "classification": {
        "source_constraint": "selects a transition-closed admissible domain",
        "intervention": "acts covariantly on realized states",
        "effect": "pulls back contravariantly against an intervention",
        "record": "is the value of the compatible state-effect evaluation",
    },
}

output = Path(__file__).parents[1] / "results" / "evaluation_square_typing.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

