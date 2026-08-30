import itertools
import json
from pathlib import Path


GROUP = (0, 1)


def add(left, right):
    return left ^ right


def omega(a, b, c):
    return -1 if a * b * c else 1


quadruples_checked = 0
for a, b, c, d in itertools.product(GROUP, repeat=4):
    left = omega(b, c, d) * omega(a, add(b, c), d) * omega(a, b, c)
    right = omega(add(a, b), c, d) * omega(a, b, add(c, d))
    assert left == right
    quadruples_checked += 1


def normalized_beta(value_at_11):
    return {
        (0, 0): 1,
        (0, 1): 1,
        (1, 0): 1,
        (1, 1): value_at_11,
    }


def coboundary(beta, a, b, c):
    numerator = beta[(b, c)] * beta[(a, add(b, c))]
    denominator = beta[(add(a, b), c)] * beta[(a, b)]
    return numerator // denominator


coboundaries_checked = 0
matching_cochains = []
for value_at_11 in (-1, 1):
    beta = normalized_beta(value_at_11)
    values = {
        (a, b, c): coboundary(beta, a, b, c)
        for a, b, c in itertools.product(GROUP, repeat=3)
    }
    assert values[(1, 1, 1)] == 1
    if all(values[key] == omega(*key) for key in values):
        matching_cochains.append(value_at_11)
    coboundaries_checked += 1

assert matching_cochains == []
assert abs(omega(1, 1, 1)) == 1

result = {
    "schema": "marici.c2-associator-cohomology.v1",
    "group": "C2",
    "pentagon_quadruples_checked": quadruples_checked,
    "normalized_sign_two_cochains_checked": coboundaries_checked,
    "omega_111": omega(1, 1, 1),
    "all_coboundary_111_values": 1,
    "matching_two_cochains": matching_cochains,
    "source_local_strictification_exists": False,
    "absolute_value_projection_erases_obstruction": True,
    "verdict": "pentagon coherence can carry a nontrivial source-preserving strictification obstruction",
}

output = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "c2-associator-cohomology.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
