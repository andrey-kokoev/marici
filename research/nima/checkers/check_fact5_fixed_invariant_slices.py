#!/usr/bin/env python3
"""Exact classification of five-point slices fixing three nonadjacent invariants."""
import itertools
import json
from pathlib import Path
from sympy import Matrix, Rational

# b=C*a from five-point massless momentum conservation.
C = Matrix([
    [-1, -1, 0, 1, 0],
    [0, -1, -1, 0, 1],
    [1, 0, -1, -1, 0],
    [0, 1, 0, -1, -1],
    [-1, 0, 1, 0, -1],
])
assert C.det() != 0
ones = Matrix([1] * 5)
compatible = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]


def det(u, v):
    return Matrix.hstack(u, v).det()


def solve_facets(constants, gradients, i, j):
    matrix = Matrix([[gradients[i][0], gradients[i][1]], [gradients[j][0], gradients[j][1]]])
    if matrix.det() == 0:
        return None
    return matrix.inv() * Matrix([-constants[i], -constants[j]])


records = []
for fixed in itertools.combinations(range(5), 3):
    constraint = C[list(fixed), :]
    if constraint.rank() != 3:
        continue
    null_basis = constraint.nullspace()
    assert len(null_basis) == 2
    gradients = [Matrix([null_basis[0][i], null_basis[1][i]]) for i in range(5)]
    jacobians = [det(gradients[i], gradients[j]) for i, j in compatible]
    common_nonzero = jacobians[0] != 0 and all(value == jacobians[0] for value in jacobians)

    # Fix the selected b-values to those of a=(1,1,1,1,1). This gives an exact
    # interior point and tests whether all five adjacent facet intersections
    # are vertices with the remaining inequalities strict.
    constants = list(ones)
    vertices = []
    bounded_pentagon = common_nonzero
    for i, j in compatible:
        point = solve_facets(constants, gradients, i, j)
        if point is None:
            bounded_pentagon = False
            break
        values = [constants[k] + gradients[k].dot(point) for k in range(5)]
        if values[i] != 0 or values[j] != 0 or any(values[k] <= 0 for k in range(5) if k not in (i, j)):
            bounded_pentagon = False
        vertices.append([str(point[0]), str(point[1])])
    records.append({
        "fixed_b_indices": list(fixed),
        "gradient_basis": [[str(x) for x in vector] for vector in gradients],
        "cyclic_jacobians": list(map(str, jacobians)),
        "common_nonzero_jacobian": common_nonzero,
        "unit_interior_support_gives_pentagon": bounded_pentagon,
        "vertices": vertices if bounded_pentagon else None,
    })

assert len(records) == 10
common = [record for record in records if record["common_nonzero_jacobian"]]
pentagons = [record for record in records if record["unit_interior_support_gives_pentagon"]]

result = {
    "schema": "marici.fact5-fixed-invariant-slices.v1",
    "status": "passed",
    "strength": "exhaustive rank-three choices among five conservation-derived nonadjacent invariants at five points; source selection and general n remain open",
    "choices_checked": len(records),
    "common_jacobian_choices": len(common),
    "bounded_pentagon_choices_for_declared_support": len(pentagons),
    "records": records,
    "boundary": "fixing three b_i is source-typed by the universal linear relations; the choice of indices and constants is not selected by those relations",
}
out = Path("research/nima/results/fact5_fixed_invariant_slices.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
