"""Generated algebra of the typed rank-26 source-cyclic connection."""

import contextlib
import hashlib
import importlib
import io
import json
import os

with contextlib.redirect_stdout(io.StringIO()):
    cyclic = importlib.import_module("check_rank26_unsplit_source_cyclicity")

base = cyclic.base
if os.environ.get("MARICI_RANK26_POINT"):
    cyclic.charts.SOURCE_POINT = tuple(
        int(value) for value in os.environ["MARICI_RANK26_POINT"].split(",")
    )
pres, span, _, record = cyclic.source_closure(14)
assert len(span) == 26
basis_pivots = sorted(span, reverse=True)
basis = [span[pivot] for pivot in basis_pivots]
pivot_position = {pivot: index for index, pivot in enumerate(basis_pivots)}


def coordinates(vector):
    row = dict(vector)
    out = [0] * len(basis)
    while row:
        active = [column for column in row if column in span]
        if not active:
            raise AssertionError(f"connection escaped cyclic span: {sorted(row)[:8]}")
        pivot = max(active)
        coefficient = row[pivot]
        out[pivot_position[pivot]] = coefficient
        for column, value in span[pivot].items():
            base.add_value(row, column, -coefficient * value)
    return out


matrices = []
for axis in range(3):
    matrix = [[0] * 26 for _ in range(26)]
    for source_index, vector in enumerate(basis):
        image = cyclic.connection_image(pres, vector, axis)
        for target_index, value in enumerate(coordinates(image)):
            matrix[target_index][source_index] = value
    matrices.append(matrix)


def multiply(left, right):
    size = len(left)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for k, value in enumerate(left[i]):
            if value:
                for j, other in enumerate(right[k]):
                    if other:
                        result[i][j] = (result[i][j] + value * other) % base.PRIME
    return result


def flatten(matrix):
    return [value for row in matrix for value in row]


identity = [[int(i == j) for j in range(26)] for i in range(26)]
algebra_pivots = {}
algebra_basis = []
frontier = [identity]
while frontier and len(algebra_basis) < 26 * 26:
    candidate = frontier.pop()
    row = {i: value for i, value in enumerate(flatten(candidate)) if value}
    before = len(algebra_pivots)
    base.add_pivot(row, algebra_pivots)
    if len(algebra_pivots) == before:
        continue
    algebra_basis.append(candidate)
    frontier.extend(multiply(candidate, generator) for generator in matrices)

digest = hashlib.sha256(json.dumps(matrices, separators=(",", ":")).encode()).hexdigest()
result = {
    "schema": "marici.benincasa.rank26_connection_algebra.v1",
    "field": base.PRIME,
    "kinematics": list(cyclic.charts.SOURCE_POINT),
    "basis_dimension": 26,
    "connection_axes": ["X1", "X2", "X3"],
    "generated_associative_algebra_dimension": len(algebra_basis),
    "full_matrix_algebra_dimension": 676,
    "absolutely_irreducible_at_tested_fiber": len(algebra_basis) == 676,
    "connection_matrices_sha256": digest,
    "source_cyclicity_record": record,
}
print(json.dumps(result, sort_keys=True))
