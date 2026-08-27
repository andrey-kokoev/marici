import json
from fractions import Fraction
from pathlib import Path


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)]
            for i in range(2)]


def flatten(a):
    return [a[0][0], a[0][1], a[1][0], a[1][1]]


def rank(vectors):
    a = [[Fraction(x) for x in vector] for vector in vectors]
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
XZ = matmul(X, Z)

generated_basis = [flatten(I), flatten(X), flatten(Z), flatten(XZ)]
generated_rank = rank(generated_basis)
union_rank = rank([flatten(I), flatten(X), flatten(Z)])
intersection_dimension = 2 + 2 - union_rank

assert generated_rank == 4
assert union_rank == 3
assert intersection_dimension == 1

result = {
    "status": "pass",
    "claim": "joining incompatible record frames generates full records and leaves scalar control",
    "record_X_dimension": 2,
    "record_Z_dimension": 2,
    "generated_record_dimension": generated_rank,
    "surviving_control_dimension": intersection_dimension,
    "generated_basis": ["I", "X", "Z", "XZ"],
    "record_join_dual_to_control_meet": True,
    "compatibility_confers_authority": False,
}

out = Path(__file__).parents[1] / "results" / "incompatible-record-join.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

