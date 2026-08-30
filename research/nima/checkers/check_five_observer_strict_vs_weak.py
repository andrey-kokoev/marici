import itertools
import json
from pathlib import Path


def compose(left, right):
    return tuple(left[right[index]] for index in range(len(left)))


def inverse(permutation):
    result = [0] * len(permutation)
    for index, value in enumerate(permutation):
        result[value] = index
    return tuple(result)


def transition(left_frame, right_frame):
    return compose(left_frame, inverse(right_frame))


identity = (0, 1, 2)
group = list(itertools.permutations(range(3)))
frame_system_count = 0

for frames in itertools.product(group, repeat=5):
    a = transition(frames[0], frames[1])
    b = transition(frames[1], frames[2])
    c = transition(frames[2], frames[3])
    d = transition(frames[3], frames[4])

    p1 = compose(compose(compose(a, b), c), d)
    p2 = compose(compose(a, b), compose(c, d))
    p3 = compose(a, compose(b, compose(c, d)))
    p4 = compose(a, compose(compose(b, c), d))
    p5 = compose(compose(a, compose(b, c)), d)
    endpoint = transition(frames[0], frames[4])

    assert {p1, p2, p3, p4, p5} == {endpoint}
    frame_system_count += 1

# Five individually invertible scalar comparison cells need not satisfy the
# weak pentagon. Absolute-value projection hides this sign defect.
weak_cells = [1, 1, 1, 1, -1]
weak_loop_product = 1
for cell in weak_cells:
    assert cell in (-1, 1)
    weak_loop_product *= cell
assert weak_loop_product == -1
assert abs(weak_loop_product) == 1

result = {
    "schema": "marici.five-observer-strict-vs-weak.v1",
    "group": "S3",
    "five_frame_systems_checked": frame_system_count,
    "strict_parenthesizations_equal": True,
    "strict_endpoint_telescoping": True,
    "weak_associator_cells": weak_cells,
    "weak_pentagon_product": weak_loop_product,
    "absolute_value_projection_false_pass": True,
    "verdict": "strict transport closes while weak transport requires a pentagon gate",
}

output = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "five-observer-strict-vs-weak.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
