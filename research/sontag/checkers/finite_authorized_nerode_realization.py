"""Exact finite hostile test for an authorized, graded Nerode realization."""

import json
from pathlib import Path


STATES = ("p", "q", "u", "v", "z0", "z1")
OUTPUT = {"p": 0, "q": 0, "u": 0, "v": 0, "z0": 0, "z1": 1}
STEP = {
    ("p", "a"): "u",
    ("q", "a"): "v",
    ("u", "a"): "z0",
    ("v", "a"): "z1",
    ("z0", "a"): "z0",
    ("z1", "a"): "z1",
}


def words(alphabet, depth):
    result = [()]
    frontier = [()]
    for _ in range(depth):
        frontier = [word + (action,) for word in frontier for action in alphabet]
        result.extend(frontier)
    return tuple(result)


def trace(state, word):
    values = [OUTPUT[state]]
    for action in word:
        state = STEP[(state, action)]
        values.append(OUTPUT[state])
    return tuple(values)


def signature(state, alphabet, depth):
    return tuple((word, trace(state, word)) for word in words(alphabet, depth))


def partition(alphabet, depth):
    fibers = {}
    for state in STATES:
        fibers.setdefault(signature(state, alphabet, depth), []).append(state)
    return tuple(sorted(tuple(group) for group in fibers.values()))


def class_index(groups):
    return {state: index for index, group in enumerate(groups) for state in group}


def graded_successor_is_well_defined(alphabet, depth):
    if depth == 0:
        return True
    source = partition(alphabet, depth)
    target_index = class_index(partition(alphabet, depth - 1))
    for group in source:
        for action in alphabet:
            images = {target_index[STEP[(state, action)]] for state in group}
            if len(images) != 1:
                return False
    return True


def same_level_successor_is_well_defined(alphabet, depth):
    groups = partition(alphabet, depth)
    index = class_index(groups)
    for group in groups:
        for action in alphabet:
            if len({index[STEP[(state, action)]] for state in group}) != 1:
                return False
    return True


def main():
    observer = ()
    controller = ("a",)
    observer_p0 = partition(observer, 0)
    observer_p2 = partition(observer, 2)
    controlled = {depth: partition(controller, depth) for depth in range(4)}

    checks = {
        "unauthorized_actor_cannot_use_a": words(observer, 3) == ((),),
        "observer_quotient_never_refines": observer_p0 == observer_p2,
        "controller_depth_zero_is_output_partition": controlled[0] == (("p", "q", "u", "v", "z0"), ("z1",)),
        "p_q_equal_at_depth_one": class_index(controlled[1])["p"] == class_index(controlled[1])["q"],
        "p_q_separate_at_depth_two": class_index(controlled[2])["p"] != class_index(controlled[2])["q"],
        "depth_one_same_level_quotient_is_not_congruent": not same_level_successor_is_well_defined(controller, 1),
        "graded_successor_zero_is_well_defined": graded_successor_is_well_defined(controller, 0),
        "graded_successor_one_is_well_defined": graded_successor_is_well_defined(controller, 1),
        "graded_successor_two_is_well_defined": graded_successor_is_well_defined(controller, 2),
        "graded_successor_three_is_well_defined": graded_successor_is_well_defined(controller, 3),
        "unbounded_partition_stabilizes_by_depth_two": controlled[2] == controlled[3],
        "stabilized_quotient_is_a_same_level_congruence": same_level_successor_is_well_defined(controller, 2),
    }
    payload = {
        "schema": "marici.sontag.finite_authorized_nerode_realization.v1",
        "passed": sum(checks.values()),
        "total": len(checks),
        "all_passed": all(checks.values()),
        "checks": checks,
        "partitions": {str(depth): groups for depth, groups in controlled.items()},
        "verdict": (
            "Finite-horizon behavioral state is graded: a control step maps the depth-h "
            "quotient to depth-(h-1), not generally back to the same quotient. A stationary "
            "coalgebra appears only after the authorized Nerode partition stabilizes. The "
            "control alphabet, continuation budget, and source authority are therefore part "
            "of the realization index, not optional metadata."
        ),
    }
    output = Path(__file__).parents[1] / "results" / "finite_authorized_nerode_realization.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if payload["all_passed"] else 1)


if __name__ == "__main__":
    main()
