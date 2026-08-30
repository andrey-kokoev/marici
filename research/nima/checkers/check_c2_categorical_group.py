import itertools
import json
from pathlib import Path


GROUP = (0, 1)
AUTOMORPHISMS = (-1, 1)


def add(left, right):
    return left ^ right


def omega(a, b, c):
    return -1 if a * b * c else 1


def trivial_omega(a, b, c):
    return 1


normalization_checks = 0
for a, b in itertools.product(GROUP, repeat=2):
    assert omega(0, a, b) == 1
    assert omega(a, 0, b) == 1
    assert omega(a, b, 0) == 1
    normalization_checks += 3

pentagon_checks = 0
for a, b, c, d in itertools.product(GROUP, repeat=4):
    left = omega(b, c, d) * omega(a, add(b, c), d) * omega(a, b, c)
    right = omega(add(a, b), c, d) * omega(a, b, add(c, d))
    assert left == right
    pentagon_checks += 1

assert all(omega(a, b, c) in AUTOMORPHISMS for a, b, c in itertools.product(GROUP, repeat=3))


def normalized_beta(value_at_11):
    return {(0, 0): 1, (0, 1): 1, (1, 0): 1, (1, 1): value_at_11}


def coboundary(beta, a, b, c):
    return (
        beta[(b, c)]
        * beta[(a, add(b, c))]
        // beta[(add(a, b), c)]
        // beta[(a, b)]
    )


trivializations = []
for value_at_11 in AUTOMORPHISMS:
    beta = normalized_beta(value_at_11)
    if all(
        coboundary(beta, a, b, c) == omega(a, b, c)
        for a, b, c in itertools.product(GROUP, repeat=3)
    ):
        trivializations.append(value_at_11)
assert trivializations == []

# Both categorical groups have the same object-level multiplication table.
object_table_nontrivial = [[add(a, b) for b in GROUP] for a in GROUP]
object_table_trivial = [[add(a, b) for b in GROUP] for a in GROUP]
assert object_table_nontrivial == object_table_trivial
assert omega(1, 1, 1) != trivial_omega(1, 1, 1)

result = {
    "schema": "marici.c2-categorical-group.v1",
    "object_group": "C2",
    "automorphism_group": "mu_2",
    "normalization_checks": normalization_checks,
    "pentagon_checks": pentagon_checks,
    "all_associators_invertible": True,
    "source_local_trivializations": trivializations,
    "object_shadow_equal_to_trivial_model": True,
    "higher_models_distinct": True,
    "verdict": "a coherent nontrivial associator can be constitutive categorical-group data",
}

output = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "c2-categorical-group.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
