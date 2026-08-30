import json
from fractions import Fraction
from pathlib import Path


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)]
            for i in range(2)]


def commutator(a, b):
    ab = matmul(a, b)
    ba = matmul(b, a)
    return [[ab[i][j] - ba[i][j] for j in range(2)] for i in range(2)]


def flatten(a):
    return [a[0][0], a[0][1], a[1][0], a[1][1]]


def rank(matrix):
    if not matrix:
        return 0
    a = [[Fraction(x) for x in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for r in range(rows):
            if r != pivot_row and a[r][col]:
                factor = a[r][col]
                a[r] = [x - factor * y for x, y in zip(a[r], a[pivot_row])]
        pivot_row += 1
    return pivot_row


I = [[1, 0], [0, 1]]
X = [[0, 1], [1, 0]]
Z = [[1, 0], [0, -1]]
J = [[0, -1], [1, 0]]
basis = [I, X, Z, J]


def commutant_dimension(generators):
    constraints = []
    for generator in generators:
        columns = [flatten(commutator(candidate, generator)) for candidate in basis]
        constraints.extend([list(row) for row in zip(*columns)])
    return 4 - rank(constraints)


scalar_dim = commutant_dimension([I])
diagonal_dim = commutant_dimension([I, Z])
full_dim = commutant_dimension([I, X, Z, J])

assert scalar_dim == 4
assert diagonal_dim == 2
assert full_dim == 1
assert commutator(Z, X) != [[0, 0], [0, 0]]

result = {
    "status": "pass",
    "claim": "record and control algebras form an order-reversing commutant Galois connection",
    "commutant_dimensions": {
        "scalar_record_algebra": scalar_dim,
        "diagonal_record_algebra": diagonal_dim,
        "full_control_algebra": full_dim,
    },
    "inclusion_reversal": True,
    "full_control_nondisturbing_record_dimension": full_dim,
    "finite_falsifier": {
        "record": "Z",
        "operation": "X",
        "commutator": commutator(Z, X),
    },
}

out = Path(__file__).parents[1] / "results" / "record-control-commutant-galois.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

