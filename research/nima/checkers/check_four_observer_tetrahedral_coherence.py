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


def conjugate(frame, value):
    return compose(compose(frame, value), inverse(frame))


def parity(permutation):
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


identity = (0, 1, 2)
group = list(itertools.permutations(range(3)))
edge_names = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def edge(edges, i, j):
    if i < j:
        return edges[(i, j)]
    return inverse(edges[(j, i)])


def face(edges, i, j, k):
    return compose(compose(edge(edges, i, j), edge(edges, j, k)), inverse(edge(edges, i, k)))


assignment_count = 0
for values in itertools.product(group, repeat=len(edge_names)):
    edges = dict(zip(edge_names, values))
    c012 = face(edges, 0, 1, 2)
    c023 = face(edges, 0, 2, 3)
    c123 = face(edges, 1, 2, 3)
    c013 = face(edges, 0, 1, 3)
    left = compose(c012, c023)
    right = compose(conjugate(edge(edges, 0, 1), c123), c013)
    assert left == right
    assignment_count += 1

cycle = (1, 2, 0)
hostile_faces = {
    "c012": identity,
    "c023": identity,
    "c123": cycle,
    "c013": identity,
}
hostile_left = compose(hostile_faces["c012"], hostile_faces["c023"])
hostile_right = compose(hostile_faces["c123"], hostile_faces["c013"])
assert hostile_left != hostile_right
assert parity(hostile_left) == parity(hostile_right) == 1

result = {
    "schema": "marici.four-observer-tetrahedral-coherence.v1",
    "group": "S3",
    "edge_assignments_checked": assignment_count,
    "tetrahedral_identity_holds_for_all_edge_assignments": True,
    "hostile_left": list(hostile_left),
    "hostile_right": list(hostile_right),
    "hostile_full_identity_fails": True,
    "hostile_scalar_sign_test_passes": True,
    "verdict": "four observers generate a coherence law among face holonomies",
}

output = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "four-observer-tetrahedral-coherence.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
