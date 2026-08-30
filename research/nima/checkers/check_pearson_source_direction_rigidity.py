from fractions import Fraction
from itertools import permutations
import json
from pathlib import Path


ZERO = (Fraction(0), Fraction(0))
ONE = (Fraction(1), Fraction(0))
C = (Fraction(0), Fraction(1))


def transfer(j):
    a = Fraction(j, 1) + Fraction(19, 4)
    b = Fraction(3, 2) * (Fraction(j, 1) + Fraction(5, 4))
    return (
        ((a, Fraction(0)), (-b, Fraction(0)), ONE),
        (ONE, ZERO, ZERO),
        (ZERO, ZERO, C),
    )


def commutes(perm, matrix):
    inverse = tuple(perm.index(j) for j in range(3))
    left = tuple(tuple(matrix[perm[i]][j] for j in range(3)) for i in range(3))
    right = tuple(tuple(matrix[i][inverse[j]] for j in range(3)) for i in range(3))
    return left == right


perms = list(permutations(range(3)))
m0 = transfer(0)
m1 = transfer(1)
commutes_m0 = []
commutes_m1 = []
commutes_both = []

for perm in perms:
    c0 = commutes(perm, m0)
    c1 = commutes(perm, m1)
    if c0:
        commutes_m0.append(perm)
    if c1:
        commutes_m1.append(perm)
    if c0 and c1:
        commutes_both.append(perm)

assert commutes_both == [(0, 1, 2)]

result = {
    "schema": "marici.nima.pearson-source-direction-rigidity.v1",
    "permutations_tested": len(perms),
    "wall_parameter": "indeterminate c",
    "commuting_with_degree_0": [list(p) for p in commutes_m0],
    "commuting_with_degree_1": [list(p) for p in commutes_m1],
    "simultaneous_centralizer": [list(p) for p in commutes_both],
    "verdict": "finite Pearson transfer rigidifies the three coordinate roles",
}

out = Path(__file__).parents[1] / "results" / "pearson-source-direction-rigidity.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
