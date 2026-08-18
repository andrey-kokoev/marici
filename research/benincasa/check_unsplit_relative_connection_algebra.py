"""Extract the rank-21 relative connection and test its generated algebra."""

import hashlib
import json
from pathlib import Path

import physical_four_mark_residue_twisted_derham as model


def add_basis(vector, pivots):
    row = {index: value % model.PRIME for index, value in enumerate(vector) if value % model.PRIME}
    model.add_pivot(row, pivots)


def multiply(left, right):
    size = len(left)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for k, value in enumerate(left[i]):
            if not value:
                continue
            for j, other in enumerate(right[k]):
                if other:
                    result[i][j] = (result[i][j] + value * other) % model.PRIME
    return result


def flatten(matrix):
    return [value for row in matrix for value in row]


names = ("g1", "g2", "g3", "g23", "g31")
low_labels, columns, pivots, free_low = model.presentation(
    names, 5, 10, 5, minimum_q_level=1
)
assert len(free_low) == 21
free_index = {column: index for index, column in enumerate(free_low)}
label_by_column = {columns[label]: label for label in low_labels}

matrices = []
for axis in range(2):
    matrix = [[0] * len(free_low) for _ in free_low]
    for source_index, column in enumerate(free_low):
        image = model.connection_image(label_by_column[column], names, 5, axis, columns)
        reduced = model.reduce_row(image, pivots)
        for target_column, value in reduced.items():
            if target_column in free_index:
                matrix[free_index[target_column]][source_index] = value
    matrices.append(matrix)

identity = [[int(i == j) for j in range(21)] for i in range(21)]
algebra_pivots = {}
algebra_basis = []
frontier = [identity]
while frontier and len(algebra_basis) < 441:
    candidate = frontier.pop()
    before = len(algebra_pivots)
    add_basis(flatten(candidate), algebra_pivots)
    if len(algebra_pivots) == before:
        continue
    algebra_basis.append(candidate)
    frontier.extend(multiply(candidate, generator) for generator in matrices)

matrix_digest = hashlib.sha256(
    json.dumps(matrices, separators=(",", ":")).encode("ascii")
).hexdigest()

result = {
    "schema": "marici.unsplit-relative-connection-algebra.v1",
    "field": model.PRIME,
    "kinematics": [2, 3, 4],
    "basis_dimension": len(free_low),
    "connection_axes": ["X1", "X2"],
    "connection_matrices": matrices,
    "connection_matrices_sha256": matrix_digest,
    "generated_associative_algebra_dimension": len(algebra_basis),
    "full_matrix_algebra_dimension": 441,
    "absolutely_irreducible_at_tested_fiber": len(algebra_basis) == 441,
    "occurrence_reflection_status": "requires transport to the X2/X3-swapped fiber; not an endomorphism at (2,3,4)",
}

out = Path(__file__).with_name("unsplit-relative-connection-algebra.json")
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({key: value for key, value in result.items() if key != "connection_matrices"}, indent=2))
