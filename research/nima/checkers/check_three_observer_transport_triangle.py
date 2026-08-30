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


def parity(permutation):
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


identity = (0, 1, 2)
group = list(itertools.permutations(range(3)))


def transition(left_frame, right_frame):
    return compose(left_frame, inverse(right_frame))


triple_count = 0
for g0 in group:
    for g1 in group:
        for g2 in group:
            t01 = transition(g0, g1)
            t12 = transition(g1, g2)
            t02 = transition(g0, g2)
            t20 = transition(g2, g0)
            assert compose(t01, t12) == t02
            assert compose(compose(t01, t12), t20) == identity
            triple_count += 1

cycle = (1, 2, 0)
assert cycle != identity
assert parity(cycle) == 1

g0, g1, g2 = identity, (1, 0, 2), (0, 2, 1)
t01 = transition(g0, g1)
t12 = transition(g1, g2)
t20 = transition(g2, g0)
hostile_t12 = compose(inverse(t01), compose(cycle, inverse(t20)))
hostile_holonomy = compose(compose(t01, hostile_t12), t20)
assert hostile_holonomy == cycle
assert parity(t01) * parity(hostile_t12) * parity(t20) == 1

result = {
    "schema": "marici.three-observer-transport-triangle.v1",
    "group": "S3",
    "frame_triples_checked": triple_count,
    "exact_triangles_have_identity_holonomy": True,
    "hostile_holonomy": list(hostile_holonomy),
    "hostile_holonomy_nonidentity": True,
    "sign_character_of_hostile_holonomy": parity(hostile_holonomy),
    "scalar_sign_test_false_pass": True,
    "verdict": "three observers generate a holonomy gate that must be tested before projection",
}

output = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "three-observer-transport-triangle.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
