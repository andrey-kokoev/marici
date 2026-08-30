import itertools
import json
from pathlib import Path


# Exact arithmetic in Q[x]/(x^2-x+1), where x is a primitive sixth root.
def add(left, right):
    return (left[0] + right[0], left[1] + right[1])


def mul(left, right):
    a, b = left
    c, d = right
    # x^2 = x - 1
    return (a * c - b * d, a * d + b * c + b * d)


def power(exponent):
    value = (1, 0)
    x = (0, 1)
    for _ in range(exponent % 6):
        value = mul(value, x)
    return value


zero = (0, 0)
six = (6, 0)
gram = []
for left_row in range(6):
    row = []
    for right_row in range(6):
        value = zero
        for column in range(6):
            exponent = ((right_row - left_row) * column) % 6
            value = add(value, power(exponent))
        row.append(value)
    gram.append(row)

for i in range(6):
    for j in range(6):
        assert gram[i][j] == (six if i == j else zero)

types = (
    "primitive",
    "prime_square",
    "seam",
    "endpoint",
    "connected_tail",
    "archimedean",
)
assignments = list(itertools.permutations(types))
assert len(assignments) == 720
assert len(set(assignments)) == 720

# Every row permutation preserves the exact Gram matrix because it permutes
# both row indices of 6I.
preserved_gram_count = 0
for permutation in itertools.permutations(range(6)):
    permuted = [
        [gram[permutation[i]][permutation[j]] for j in range(6)]
        for i in range(6)
    ]
    assert permuted == gram
    preserved_gram_count += 1

result = {
    "schema": "marici.z6-typed-incidence-ambiguity.v1",
    "cyclic_dimension": 6,
    "exact_unnormalized_gram_diagonal": 6,
    "exact_fourier_orthogonality": True,
    "typed_assignments": len(assignments),
    "assignments_preserving_gram": preserved_gram_count,
    "unitarity_selects_typed_assignment": False,
    "first_assignment": list(assignments[0]),
    "last_assignment": list(assignments[-1]),
    "verdict": "finite cyclic Fourier control leaves a 720-fold source-typing ambiguity",
}

output = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "z6-typed-incidence-ambiguity.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
