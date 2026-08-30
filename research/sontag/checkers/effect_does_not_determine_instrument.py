import json
from pathlib import Path


initial = "x"


def instrument_i(state):
    assert state == "x"
    return 0, "a"


def instrument_j(state):
    assert state == "x"
    return 0, "b"


def later_probe(state):
    return {"a": 0, "b": 1}[state]


record_i, post_i = instrument_i(initial)
record_j, post_j = instrument_j(initial)
joint_i = (record_i, later_probe(post_i))
joint_j = (record_j, later_probe(post_j))

effect_i = {initial: record_i}
effect_j = {initial: record_j}

checks = {
    "present_records_are_equal": record_i == record_j == 0,
    "induced_effects_are_equal": effect_i == effect_j,
    "post_record_states_are_distinct": post_i != post_j,
    "later_probe_separates_post_record_states": later_probe(post_i)
    != later_probe(post_j),
    "joint_record_words_are_distinct": joint_i != joint_j,
    "first_distinguishing_continuation_depth_is_one": joint_i[0] == joint_j[0]
    and joint_i[1] != joint_j[1],
}

result = {
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "instrument_i": {"first_record": record_i, "post_state": post_i},
    "instrument_j": {"first_record": record_j, "post_state": post_j},
    "joint_record_i": list(joint_i),
    "joint_record_j": list(joint_j),
    "classification": "effect equivalence without instrument or predictive equivalence",
}

output = Path(__file__).parents[1] / "results" / "effect_does_not_determine_instrument.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

