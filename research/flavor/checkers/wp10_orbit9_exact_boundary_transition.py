"""Exact Gram-preserving boundary transition for the apparent orbit-9 singleton."""
import json
from pathlib import Path

import sympy as sp

a_re, a_im, b, c, d, e, r = sp.symbols(
    "a_re a_im b c d e r", real=True)
a = a_re + sp.I*a_im

# Orbit 9 / member (116,481), with the (d,2,0) normal e.
source = sp.Matrix([
    [a, 0, 0],
    [0, 0, b],
    [e, c, d],
])

# Orbit 16 / member (116,405), with the (d,0,2) normal B.
# The target phase lies on B and is inherited from a.
target = sp.Matrix([
    [a*c/r, 0, a*e/r],
    [0, b, 0],
    [0, d, r],
])

def row_gram(matrix):
    return sp.simplify(matrix * matrix.conjugate().T)

relation = {r**2: c**2 + e**2}
cleared_difference = sp.simplify(
    r**2 * (row_gram(target) - row_gram(source)))
cleared_difference = cleared_difference.applyfunc(
    lambda value: sp.factor(value.xreplace(relation)))
assert cleared_difference == sp.zeros(3)

target_normal_ratio = sp.simplify(target[0, 2] / e)
assert target_normal_ratio == a/r
assert sp.limit(target_normal_ratio, e, 0, dir="+") == a/r

result = {
    "schema": "marici.flavor.orbit9_exact_boundary_transition.v1",
    "source_vertex": {
        "orbit": 9,
        "member": [116, 481],
        "normal": ["d", 2, 0],
        "phase_edge": ["d", 0, 0],
    },
    "target_vertex": {
        "orbit": 16,
        "member": [116, 405],
        "normal": ["d", 0, 2],
        "phase_edge": ["d", 0, 2],
    },
    "transition": {
        "r_squared": "c^2+e^2",
        "A": "a*c/r",
        "B": "a*e/r",
        "C": "b",
        "D": "d",
        "E": "r",
    },
    "exact_row_gram_difference": "zero",
    "target_normal_over_source_normal": "a/r",
    "generic_boundary_valuation": 1,
    "interpretation": (
        "The apparent orbit-9 singleton has an exact Gram-preserving "
        "codimension-one bridge. Its numerical non-unit finite-depth slope "
        "was continuation-path drift, not a carrier obstruction."
    ),
}
output = Path(
    "research/flavor/results/wp10_orbit9_exact_boundary_transition.json")
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
