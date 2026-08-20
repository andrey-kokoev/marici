"""Typed composition of sheet parity and occurrence forgetting."""
import json
import itertools
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/rank12-e6-parity-occurrence-composition.json"

# Source occurrence order:
# (12|23),(12|31),(23|31),(23|12),(31|12),(31|23).
F = [
    [1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1],
]

# The oriented physical boundary is e_- - e_+.  Under the canonical
# sheet-difference to primitive odd-coinvariant map it becomes -2c.
S = [[-2 if i == j else 0 for j in range(6)] for i in range(6)]

def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

def matvec(a, x):
    return [sum(row[j] * x[j] for j in range(len(x))) for row in a]

def det(m):
    if len(m) == 1:
        return m[0][0]
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    return sum((-1) ** j * m[0][j] * det([row[:j] + row[j + 1:] for row in m[1:]])
               for j in range(len(m)))

def determinantal_divisor(a, k):
    values = []
    for rows in itertools.combinations(range(len(a)), k):
        for cols in itertools.combinations(range(len(a[0])), k):
            values.append(abs(det([[a[i][j] for j in cols] for i in rows])))
    return math.gcd(*values)

C = matmul(F, S)
x = [1] * 6
y = [1] * 3

assert matvec(S, x) == [-2 * z for z in x]
assert matvec(F, x) == [2 * z for z in y]
assert matvec(C, x) == [-4 * z for z in y]
d1, d2, d3 = (determinantal_divisor(C, k) for k in (1, 2, 3))
smith_nonzero = [d1, d2 // d1, d3 // d2]
assert smith_nonzero == [2, 2, 2]

packet = {
    "schema": "marici.benincasa.rank12_e6_parity_occurrence_composition.v1",
    "occurrence_order": ["12|23", "12|31", "23|31", "23|12", "31|12", "31|23"],
    "sheet_parity_matrix": S,
    "occurrence_forgetting_matrix": F,
    "composite_matrix": C,
    "determinantal_divisors": [d1, d2, d3],
    "full_composite_smith_nonzero": smith_nonzero,
    "invariant_source_generator": [1] * 6,
    "invariant_target_generator": [1] * 3,
    "invariant_line_map": -4,
    "invariant_line_cokernel": "Z/4",
    "physical_e6_betti_torsion_proved": False,
    "qualification": "The typed source-side composition explains the factor four. It does not identify the rational e6 vector as primitive in a physical integral Betti lattice.",
    "new_carrier_datum": False,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps(packet))
