import json
from pathlib import Path


def matmul(left, right):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0])))
        for i in range(len(left))
    )


def transpose(matrix):
    return tuple(tuple(matrix[j][i] for j in range(len(matrix))) for i in range(len(matrix[0])))


def add(left, right):
    return tuple(tuple(left[i][j] + right[i][j] for j in range(len(left[0]))) for i in range(len(left)))


def scale(value, matrix):
    return tuple(tuple(value * entry for entry in row) for row in matrix)


identity = ((1, 0), (0, 1))
rows = []
for coefficient in (-3, -1, 1, 2, 5):
    differential = ((0, coefficient), (0, 0))
    adjoint = transpose(differential)
    laplacian = add(matmul(differential, adjoint), matmul(adjoint, differential))
    assert laplacian == scale(coefficient * coefficient, identity)
    rows.append({
        "coefficient": coefficient,
        "hilbert_anticommutator_scalar": coefficient * coefficient,
        "sign_retained": False,
    })

assert rows[1]["hilbert_anticommutator_scalar"] == rows[2]["hilbert_anticommutator_scalar"]

# Flipping the adjoint sign flips the entire anticommutator.
d = ((0, 1), (0, 0))
d_star = transpose(d)
positive = add(matmul(d, d_star), matmul(d_star, d))
negative_adjoint = scale(-1, d_star)
negative = add(matmul(d, negative_adjoint), matmul(negative_adjoint, d))
assert positive == identity
assert negative == scale(-1, identity)

result = {
    "hilbert_adjoint_samples": rows,
    "positive_sector_anticommutator": positive,
    "opposite_adjoint_sector_anticommutator": negative,
    "one_positive_adjoint_realizes_signed_normal_coordinate": False,
    "opposite_sector_adjoint_sign_repairs_algebra": True,
    "verdict": "signed Cartan contraction requires opposite sector adjoints or an independently derived indefinite structure",
}

output = Path(__file__).parents[1] / "results" / "rh-signed-cartan-adjoint-obstruction.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))

