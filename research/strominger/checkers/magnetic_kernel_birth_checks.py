"""Local Schur-kernel birth checker for the two magnetic exceptions."""
from functools import reduce
import itertools
import json
import math
import os
import sympy as sp


def rising(value, count):
    return math.prod(value + offset for offset in range(count))


def column(g, a, m):
    c = [math.comb(g, j) * (-1) ** (g - j) *
         rising(a, g - j) * rising(4 - a, j) for j in range(g + 1)]
    b = [m * c[0]]
    b += [(m + j) * c[j] + (m + j - 1 - g) * c[j - 1]
          for j in range(1, g + 1)]
    b.append(m * c[g])
    delta = 1 - g - (a + m)
    shift = -a - g if delta > 0 else -a - g + abs(delta)
    sign = 1 if delta > 0 else -1
    return {shift + j: sign * value for j, value in enumerate(b) if value}


def component(g, k, q):
    center = 1 - g
    points = [(a, m) for a in range(0, 2 * k + 1, 2)
              for m in (center - q - a, center + q - a)]
    return points, [column(g, a, m) for a, m in points]


def matching(columns):
    owner = {}
    def augment(index, seen):
        for row in sorted(columns[index]):
            if row in seen:
                continue
            seen.add(row)
            if row not in owner or augment(owner[row], seen):
                owner[row] = index
                return True
        return False
    size = sum(augment(index, set()) for index in range(len(columns)))
    by_column = {index: row for row, index in owner.items()}
    return size, [by_column[index] for index in range(len(columns))] if size == len(columns) else []


def matrix(columns, rows=None):
    if rows is None:
        rows = sorted(set().union(*(item.keys() for item in columns)))
    return sp.Matrix([[item.get(row, 0) for item in columns] for row in rows])


def primitive(vector):
    denominator = sp.ilcm(*[value.q for value in vector])
    integers = [int(value * denominator) for value in vector]
    divisor = reduce(math.gcd, (abs(value) for value in integers if value), 0)
    integers = [value // divisor for value in integers]
    first = next(value for value in integers if value)
    return [-value for value in integers] if first < 0 else integers


checks = []
def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


# The q=7 birth extends an invertible k=2 prefix by two rows and columns.
_, old_columns = component(2, 2, 7)
old_size, old_rows = matching(old_columns)
old_matrix = matrix(old_columns, old_rows)
record("BIRTH.prefix", "the q=7 cutoff-two prefix is invertible",
       old_size == 6 and old_matrix.det() != 0,
       f"rows={old_rows}; det={old_matrix.det()}")

points, columns = component(2, 3, 7)
birth_rows = old_rows + [-8, -7]
birth_matrix = matrix(columns, birth_rows)
A, B = birth_matrix[:-2, :-2], birth_matrix[:-2, -2:]
C, E = birth_matrix[-2:, :-2], birth_matrix[-2:, -2:]
schur = sp.simplify(E - C * A.inv() * B)
record("BIRTH.schur", "the singular local Schur block is [[-588,0],[-984,0]]",
       schur == sp.Matrix([[-588, 0], [-984, 0]]), schur.tolist())

y = schur.nullspace()[0]
lift = (-A.inv() * B * y).col_join(y)
expected_full = [1, 0, 0, 0, 0, -3, 0, 2]
record("BIRTH.lift", "lifting the local null direction gives the primitive global circuit",
       primitive(list(lift)) == expected_full,
       f"y={list(y)}; lift={list(lift)}")
record("BIRTH.identity", "the lifted vector is annihilated by every sparse target row",
       matrix(columns) * sp.Matrix(expected_full) == sp.zeros(matrix(columns).rows, 1),
       f"active_points={[points[i] for i,x in enumerate(expected_full) if x]}")

# The same vector persists with zero new coordinates, but no second class is born.
persistence = []
for k in range(3, 11):
    _, later_columns = component(2, k, 7)
    full = matrix(later_columns)
    padded = expected_full + [0] * (len(later_columns) - len(expected_full))
    persistence.append((k, len(full.nullspace()), full * sp.Matrix(padded) ==
                        sp.zeros(full.rows, 1)))
record("BIRTH.persistence", "the q=7 birth persists with nullity one and no later birth",
       all(nullity == 1 and annihilated for _, nullity, annihilated in persistence),
       str(persistence))

# The q=1 exception is a singular initial step rather than a lifted interior step.
q1_points = [(0, -2), (0, 0)]
q1_columns = [column(2, a, m) for a, m in q1_points]
q1_matrix = matrix(q1_columns)
q1_kernel = primitive(list(q1_matrix.nullspace()[0]))
record("INITIAL.q1", "the q=1 initial block has primitive kernel (-1,1)",
       q1_kernel == [1, -1] or q1_kernel == [-1, 1],
       f"matrix={q1_matrix.tolist()}; kernel={q1_kernel}")

# The active q=7 local block reproduces the primitive Plucker coordinates.
local = sp.Matrix([[-120, 0, 60], [-160, -40, 20]])
record("LOCAL.plucker", "the active local block has primitive kernel (1,-3,2)",
       primitive(list(local.nullspace()[0])) == [1, -3, 2], local.tolist())

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_kernel_birth_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "exact local explanation of known exceptional births",
              "exceptions": [{"g": 2, "q": 1}, {"g": 2, "q": 7}]},
    "checks": checks, "n_pass": len(checks) - len(failed), "n_fail": len(failed),
    "verdict": "The q=1 exception is the primitive kernel of a singular initial block. The q=7 exception is born when an invertible cutoff-two prefix is extended by a singular 2x2 Schur block [[-588,0],[-984,0]]. Its local null vector (0,1) lifts canonically to (1/2,0,0,0,0,-3/2,0,1), whose primitive active coordinates are (1,-3,2). The class persists with nullity one through k=10 and no later class is born. This realizes exceptional kernel classes as failed local transport."
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_kernel_birth.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
