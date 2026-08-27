import json
from pathlib import Path


def conjugate_transpose(matrix):
    return tuple(tuple(matrix[j][i].conjugate() for j in range(len(matrix))) for i in range(len(matrix[0])))


def add(left, right):
    return tuple(tuple(left[i][j] + right[i][j] for j in range(len(left[0]))) for i in range(len(left)))


def scalar_multiply(value, matrix):
    return tuple(tuple(value * entry for entry in row) for row in matrix)


A = ((0j, -1 + 0j), (1 + 0j, 0j))
zero = ((0j, 0j), (0j, 0j))

real_direction_residual = add(conjugate_transpose(A), A)
imaginary_generator = scalar_multiply(1j, A)
imaginary_direction_residual = add(conjugate_transpose(imaginary_generator), imaginary_generator)

assert real_direction_residual == zero
assert imaginary_direction_residual != zero
assert imaginary_direction_residual == scalar_multiply(2j, A)

# Solving X+Y=0 and -X+Y=0 gives X=Y=0 exactly; with invertible J,
# Y=JA=0 forces A=0.
equation_solution = {"A_star_J": 0, "J_A": 0, "A": 0}

result = {
    "generator": [[0, -1], [1, 0]],
    "hermitian_form": "identity",
    "real_direction_residual": [[str(v) for v in row] for row in real_direction_residual],
    "imaginary_direction_residual": [[str(v) for v in row] for row in imaginary_direction_residual],
    "real_direction_preserves_form_infinitesimally": True,
    "imaginary_direction_preserves_form_infinitesimally": False,
    "simultaneous_preservation_solution": equation_solution,
    "verdict": "nontrivial holomorphic transport cannot preserve one fixed Hermitian form in both complex directions",
}

output = Path(__file__).parents[1] / "results" / "rh-complex-direction-hermitian-no-go.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))

