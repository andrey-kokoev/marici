import json
from pathlib import Path


def matmul(left, right):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0])))
        for i in range(len(left))
    )


def determinant_2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


A = ((-1, -1), (1, 1))
zero = ((0, 0), (0, 0))
assert matmul(A, A) == zero


def U(z):
    return ((1 - z, -z), (z, 1 + z))


samples = (-3, -1, 0, 1, 2, 7)
assert all(determinant_2(U(z)) == 1 for z in samples)

# U' is A and A U(z)=A because A^2=0.
assert all(matmul(A, U(z)) == A for z in samples)

fixed_overlap_samples = {str(z): U(z)[0][0] for z in samples}
assert fixed_overlap_samples["1"] == 0
assert U(1)[0][0] == 0
assert (U(1)[0][0], U(1)[1][0]) == (0, 1)

result = {
    "connection_matrix": A,
    "connection_square_zero": True,
    "transport_formula": "I+zA",
    "horizontal_equation_verified": True,
    "determinant_samples": {str(z): determinant_2(U(z)) for z in samples},
    "fixed_overlap_samples": fixed_overlap_samples,
    "zero_parameter": 1,
    "transported_state_at_zero_parameter": [0, 1],
    "transport_invertible_at_overlap_zero": True,
    "verdict": "horizontal invertible transport does not protect a fixed reference overlap",
}

output = Path(__file__).parents[1] / "results" / "rh-horizontal-transport-overlap.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))

