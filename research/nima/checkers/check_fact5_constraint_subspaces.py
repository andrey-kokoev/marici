#!/usr/bin/env python3
"""Exact annihilators of common-Jacobian five-facet gradient families."""
import json
from pathlib import Path
from sympy import Matrix, Rational, simplify, symbols

a, b = symbols("a b")
u = (1 - b) / (a * b - 1)
v = (1 - a) / (a * b - 1)
V = Matrix([[1, 0], [0, 1], [-1, a], [u, v], [b, -1]])
R = Matrix([
    [1, -a, 1, 0, 0],
    [-u, -v, 0, 1, 0],
    [-b, 1, 0, 0, 1],
])
assert R * V == Matrix.zeros(3, 2)
assert simplify(R[:, [0, 1, 2]].det()) != 0

reference = R.subs({a: 0, b: 0})
assert reference == Matrix([[1, 0, 1, 0, 0], [1, 1, 0, 1, 0], [0, 1, 0, 0, 1]])

C = Matrix([
    [-1, -1, 0, 1, 0],
    [0, -1, -1, 0, 1],
    [1, 0, -1, -1, 0],
    [0, 1, 0, -1, -1],
    [-1, 0, 1, 0, -1],
])
reference_in_b = reference * C.inv()
assert reference_in_b * C == reference

# Positivity does not select the reference fan: a nearby rational member with
# all support constants one remains a strict five-facet pentagon.
def pentagon_test(av, bv):
    gradients = V.subs({a: av, b: bv})
    constants = Matrix([1] * 5)
    vertices = []
    for i, j in [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]:
        M = Matrix([[gradients[i, 0], gradients[i, 1]], [gradients[j, 0], gradients[j, 1]]])
        point = M.inv() * Matrix([-1, -1])
        values = constants + gradients * point
        assert values[i] == values[j] == 0
        assert all(values[k] > 0 for k in range(5) if k not in (i, j))
        vertices.append([str(point[0]), str(point[1])])
    return vertices

positive_rivals = []
for av, bv in [(Rational(0), Rational(0)), (Rational(1, 4), Rational(1, 3)), (Rational(-1, 4), Rational(1, 5))]:
    positive_rivals.append({"a": str(av), "b": str(bv), "vertices": pentagon_test(av, bv)})

fmt_matrix = lambda M: [[str(simplify(x)) for x in M.row(i)] for i in range(M.rows)]
result = {
    "schema": "marici.fact5-common-jacobian-constraint-subspaces.v1",
    "status": "passed",
    "strength": "symbolic annihilator for the generic common-Jacobian family and exact five-point comparisons; no source selection",
    "generic_annihilator": fmt_matrix(R),
    "reference_annihilator": fmt_matrix(reference),
    "reference_constraints": ["a0+a2=k2", "a0+a1+a3=k3", "a1+a4=k4"],
    "reference_rows_in_b_coordinates": fmt_matrix(reference_in_b),
    "selection_test": "requiring v2=-v0 and v4=-v1 forces a=b=0, but this parallel-pair condition lacks source authority",
    "positive_rivals": positive_rivals,
    "boundary": "strict pentagon positivity admits non-reference rational members; it does not choose the annihilator or constants",
}
out = Path("research/nima/results/fact5_constraint_subspaces.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
