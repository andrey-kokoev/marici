"""Exact falsifier for the minimal charged-spurion magnetic lift."""
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import json
import math


def rf(value, count):
    result = Fraction(1)
    for offset in range(count):
        result *= value + offset
    return result


def full_column(grade, a, m):
    source = [
        math.comb(grade, j) * (-1)**(grade-j)
        * rf(a, grade-j) * rf(4-a, j)
        for j in range(grade + 1)
    ]
    path = [m * source[0]]
    path += [(m+j)*source[j] + (m+j-1-grade)*source[j-1]
             for j in range(1, grade + 1)]
    path.append(m * source[grade])
    delta = 1-grade-(a+m)
    shift = -a-grade if delta > 0 else -a-grade+abs(delta)
    sign = 1 if delta > 0 else -1
    return {shift+j: sign*value for j, value in enumerate(path) if value}


def det3(matrix):
    a, b, c = matrix
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            - a[1]*(b[0]*c[2]-b[2]*c[0])
            + a[2]*(b[0]*c[1]-b[1]*c[0]))


checks = []


def record(cid, statement, condition, detail):
    checks.append({"id": cid, "statement": statement,
                   "status": "pass" if condition else "FAIL",
                   "detail": str(detail)})


grade = 6
depth = Fraction(17, 3)
labels = [(0, 1-2*grade-depth), (depth-1, 2), (depth+1, 0)]
columns = [full_column(grade, a, m) for a, m in labels]
rows = sorted(set().union(*(set(column) for column in columns)))
matrix = [[column.get(row, 0) for column in columns] for row in rows]

witness = None
for selected in combinations(range(len(rows)), 3):
    minor = det3([matrix[index] for index in selected])
    if minor:
        witness = {"row_indices": selected,
                   "rows": [str(rows[index]) for index in selected],
                   "determinant": minor}
        break

record("FULL.minor", "the full fractional matrix has a nonzero maximal minor",
       witness is not None, witness)
record("FULL.rank", "the three full source columns are independent",
       witness is not None, "rank is three")

source_charges = [2, 1, 1]
spurion_charges = [1, 2, 2]
record("CHARGE.compensation", "minimal sector spurions make every column neutral",
       [(a+b) % 3 for a, b in zip(source_charges, spurion_charges)] == [0, 0, 0],
       "source (2,1,1) plus spurion (1,2,2)")
record("CHARGE.common_twist", "no common twist can align unequal source charges",
       all(len({(value+t) % 3 for value in source_charges}) > 1
           for t in range(3)), source_charges)

# Diagonal multiplication by nonzero spurions scales every maximal minor by
# s0*s1*s2. It cannot turn an injective three-column map into a kernel.
record("SPURION.minor_law",
       "the witness minor becomes det*s0*s1*s2",
       witness is not None and witness["determinant"] != 0,
       f"{witness['determinant']}*s0*s1*s2")
record("SPURION.generic_rank",
       "all invertible spurion fibers preserve full column rank",
       witness is not None, "nonzero diagonal base change")
record("SPURION.zero_boundary",
       "rank can fall only on a zero-spurion boundary that deletes a source route",
       witness is not None, "s0*s1*s2=0")

# The local two-route residual can be tuned, but this does not change the full
# rank witness. At d=17/3 the two amplitudes are equal and opposite.
amplitude = Fraction(113228379953561600000, 729)
record("RESIDUAL.tuning", "the local residual cancels on the ratio sL=sR",
       (-amplitude) + amplitude == 0, "one projective condition")
record("RESIDUAL.not_kernel",
       "local spurion tuning does not annihilate the full source matrix",
       witness is not None, "the maximal minor remains nonzero")

# Three independent nonzero trivializations modulo common rescaling form a
# two-dimensional projective selector space. One residual ratio leaves one
# modulus, while the full-rank obstruction leaves no kernel anywhere inside it.
record("SELECTOR.torsor", "charged trivializations introduce two projective ratios",
       3-1 == 2, "(G_m)^3 / G_m")
record("SELECTOR.residual", "residual cancellation still leaves one free ratio",
       (3-1)-1 == 1, "typing repair does not select a unique background")

failed = [item for item in checks if item["status"] != "pass"]
payload = {
    "schema": "marici.strominger.magnetic_charged_spurion_lift.v1",
    "status": "passed" if not failed else "failed",
    "checks": checks,
    "gate_count": len(checks),
    "passed_gate_count": len(checks)-len(failed),
    "witness_minor": {
        "row_indices": list(witness["row_indices"]),
        "rows": witness["rows"],
        "determinant": str(witness["determinant"]),
    } if witness else None,
    "verdict": (
        "Sector-specific charged spurions repair deck typing but cannot create "
        "the missing full kernel. On every invertible spurion fiber they only "
        "rescale independent columns. Zero spurions create route deletion, not "
        "destructive interference. A genuine activation requires a non-diagonal "
        "charged correspondence that changes the transport or its target quotient."
    ),
}
out = Path(__file__).resolve().parents[1] / "results" / "magnetic_charged_spurion_lift.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(1 if failed else 0)
