"""Forced-pivot core growth checker for the magnetic Hall minors."""
from collections import deque
import json
import math
import os
import sympy as sp


def path_data(g, a, m):
    c = [int(math.comb(g, j) * (-1) ** (g - j) *
             sp.rf(a, g - j) * sp.rf(4 - a, j)) for j in range(g + 1)]
    parts = [(m * c[0], 0)]
    parts += [((m + j) * c[j], (m + j - 1 - g) * c[j - 1])
              for j in range(1, g + 1)]
    parts.append((0, m * c[g]))
    return [left + right for left, right in parts]


def canonical_column(g, a, m):
    delta = 1 - g - (a + m)
    q = abs(delta)
    shift = -a - g if delta > 0 else -a - g + q
    sign = 1 if delta > 0 else -1
    return {shift + j: sign * value for j, value in enumerate(path_data(g, a, m))
            if value}


def component(g, k, q):
    center = 1 - g
    points = [(a, m) for a in range(0, 2 * k + 1, 2)
              for m in (center - q - a, center + q - a)]
    return [canonical_column(g, a, m) for a, m in points]


def hall_rows(columns):
    owner = {}
    def augment(column, seen):
        for row in sorted(columns[column]):
            if row in seen:
                continue
            seen.add(row)
            if row not in owner or augment(owner[row], seen):
                owner[row] = column
                return True
        return False
    size = sum(augment(column, set()) for column in range(len(columns)))
    by_column = {column: row for row, column in owner.items()}
    return size, [by_column[column] for column in range(len(columns))]


def hall_minor(g, k, q):
    columns = component(g, k, q)
    size, rows = hall_rows(columns)
    assert size == len(columns)
    return sp.Matrix([[column.get(row, 0) for column in columns] for row in rows])


def forced_core(matrix):
    active_rows = set(range(matrix.rows))
    active_columns = set(range(matrix.cols))
    pivots = []
    while True:
        forced = None
        for row in sorted(active_rows):
            neighbors = [column for column in active_columns if matrix[row, column]]
            if len(neighbors) == 1:
                forced = (row, neighbors[0])
                break
        if forced is None:
            for column in sorted(active_columns):
                neighbors = [row for row in active_rows if matrix[row, column]]
                if len(neighbors) == 1:
                    forced = (neighbors[0], column)
                    break
        if forced is None:
            break
        row, column = forced
        pivots.append((row, column, int(matrix[row, column])))
        active_rows.remove(row)
        active_columns.remove(column)
    rows, columns = sorted(active_rows), sorted(active_columns)
    return pivots, matrix[rows, columns]


def support_connected(matrix):
    start = ("r", 0)
    seen, queue = {start}, deque([start])
    while queue:
        side, index = queue.popleft()
        neighbors = (("c", j) for j in range(matrix.cols) if matrix[index, j]) if side == "r" else \
                    (("r", i) for i in range(matrix.rows) if matrix[i, index])
        for node in neighbors:
            if node not in seen:
                seen.add(node)
                queue.append(node)
    return len(seen) == matrix.rows + matrix.cols


def rank_mod(matrix, prime=1_000_000_007):
    rows = [[int(matrix[i, j]) % prime for j in range(matrix.cols)]
            for i in range(matrix.rows)]
    rank = 0
    for column in range(matrix.cols):
        pivot = next((i for i in range(rank, matrix.rows) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], prime - 2, prime)
        rows[rank] = [value * inverse % prime for value in rows[rank]]
        for i in range(matrix.rows):
            if i != rank and rows[i][column]:
                factor = rows[i][column]
                rows[i] = [(x - factor * y) % prime for x, y in zip(rows[i], rows[rank])]
        rank += 1
    return rank


checks = []
def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


data = []
for k in range(2, 31):
    minor = hall_minor(2, k, 2)
    pivots, core = forced_core(minor)
    nonzeros = sum(bool(core[i, j]) for i in range(core.rows) for j in range(core.cols))
    max_degree = max(sum(bool(core[i, j]) for j in range(core.cols))
                     for i in range(core.rows))
    data.append((k, minor, pivots, core, nonzeros, max_degree))

record("CORE.first", "the first member has a 2 by 2 residual core",
       data[0][3].shape == (2, 2), data[0][3].tolist())
record("CORE.growth", "the residual core order is 2k-2 for every tested k",
       all(core.rows == core.cols == 2 * k - 2 for k, _, _, core, _, _ in data),
       "2<=k<=30")
record("CORE.pivots", "forced degree-one stripping removes exactly four pivots",
       all(len(pivots) == 4 for _, _, pivots, _, _, _ in data), "2<=k<=30")
record("CORE.connected", "every residual support graph is connected",
       all(support_connected(core) for _, _, _, core, _, _ in data), "2<=k<=30")
record("CORE.band", "the growing core has maximum row degree at most four",
       all(degree <= 4 for _, _, _, _, _, degree in data),
       f"degrees={[item[5] for item in data[:6]]}")
record("CORE.nnz", "for k>=3 the residual support has exactly 8k-14 edges",
       all(nonzeros == 8 * k - 14 for k, _, _, _, nonzeros, _ in data[1:]),
       f"k30={data[-1][4]}")
record("CORE.rank", "every growing residual core is nonsingular modulo 1000000007",
       all(rank_mod(core) == core.rows for _, _, _, core, _, _ in data), "2<=k<=30")
record("CORE.falsifier", "bounded forced-pivot cores are falsified by linear growth",
       data[-1][3].rows > data[0][3].rows and data[-1][3].rows == 58,
       "core orders 2 through 58")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_forced_core_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "finite-range structural falsifier", "g": 2,
              "q": 2, "k": [2, 30], "prime": 1000000007},
    "checks": checks, "n_pass": len(checks) - len(failed), "n_fail": len(failed),
    "verdict": "Forced degree-one pivot stripping does not reduce Hall minors to bounded exceptional graphs. For (g,q)=(2,2), the connected residual core has order 2k-2 after exactly four pivots; its row degree is at most four and it remains full rank modulo 1000000007 through k=30. The proof target is therefore an unbounded banded determinant or transfer recurrence."
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_forced_core.json"), "w", encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
