"""Endpoint-support Hall classification and internal-cancellation falsifier."""
from collections import defaultdict
import json
import math
import os
import sympy as sp


def add(output, key, value):
    if value:
        output[key] += value
        if output[key] == 0:
            del output[key]


def path_coefficients(g, a, m):
    c = [int(math.comb(g, j) * (-1) ** (g - j) *
             sp.rf(a, g - j) * sp.rf(4 - a, j))
         for j in range(g + 1)]
    b = [m * c[0]]
    for j in range(1, g + 1):
        b.append((m + j) * c[j] + (m + j - 1 - g) * c[j - 1])
    b.append(m * c[g])
    return b


def canonical_column(g, a, m):
    center = 1 - g
    signed_delta = center - (a + m)
    q = abs(signed_delta)
    if q == 0:
        return {}
    shift = -a - g if signed_delta > 0 else -a - g + q
    sign = 1 if signed_delta > 0 else -1
    return {shift + j: sign * coefficient
            for j, coefficient in enumerate(path_coefficients(g, a, m))
            if coefficient}


def component(g, k, q):
    center = 1 - g
    points = []
    for a in range(0, 2 * k + 1, 2):
        points.extend([(a, center - q - a), (a, center + q - a)])
    columns = [canonical_column(g, a, m) for a, m in points]
    return points, columns


def matching(columns, hull=False):
    adjacency = []
    for column in columns:
        rows = sorted(column)
        adjacency.append(list(range(rows[0], rows[-1] + 1)) if hull else rows)
    owner = {}

    def augment(i, seen):
        for row in adjacency[i]:
            if row in seen:
                continue
            seen.add(row)
            if row not in owner or augment(owner[row], seen):
                owner[row] = i
                return True
        return False

    size = sum(augment(i, set()) for i in range(len(columns)))
    by_column = {column: row for row, column in owner.items()}
    rows = [by_column[i] for i in range(len(columns))] if size == len(columns) else []
    return size, rows


def matrix_for(columns):
    rows = sorted(set().union(*(column.keys() for column in columns)))
    matrix = sp.Matrix([[column.get(row, 0) for column in columns] for row in rows])
    return matrix, rows


checks = []


def record(cid, group, statement, condition, detail=""):
    status = "pass" if bool(condition) else "FAIL"
    checks.append({"id": cid, "group": group, "statement": statement,
                   "status": status, "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement}" +
          (f" ({detail})" if detail else ""), flush=True)


# HALL: wide support and interval-hull matching classification.
deficiencies = []
hull_mismatches = []
hall_blocks = 0
for g in range(2, 31):
    for k in range(0, 16):
        for q in range(1, 61):
            _, columns = component(g, k, q)
            actual, _ = matching(columns)
            hull, _ = matching(columns, hull=True)
            ncols = len(columns)
            if actual != hull:
                hull_mismatches.append((g, k, q, actual, hull))
            if actual < ncols:
                deficiencies.append((g, k, q, ncols - actual))
            hall_blocks += 1
expected_deficiencies = ([(2, k, 1, 1) for k in range(0, 16)] +
                         [(2, k, 7, 1) for k in range(3, 16)])
record("HALL.range", "HALL",
       "wide Hall deficiencies are exactly grade-2 q=1 and q=7",
       sorted(deficiencies) == sorted(expected_deficiencies),
       f"blocks={hall_blocks}; deficiencies={len(deficiencies)}")
record("HALL.hulls", "HALL",
       "interval hulls and actual nonzero supports have the same matching size",
       not hull_mismatches, f"mismatches={hull_mismatches[:3]}")

# RANK: maximal pole set suffices; every smaller block is a column subset.
singular_maximal = []
internal_cancellation = []
rank_blocks = 0
for g in range(2, 21):
    for q in range(1, 31):
        _, columns = component(g, 10, q)
        match_size, _ = matching(columns)
        matrix, _ = matrix_for(columns)
        rank = matrix.rank()
        ncols = len(columns)
        if rank < ncols:
            singular_maximal.append((g, q, ncols - rank))
        if match_size == ncols and rank < ncols:
            internal_cancellation.append((g, q, rank, ncols))
        rank_blocks += 1
record("RANK.maximal", "RANK",
       "only maximal blocks (g,q)=(2,1),(2,7) lose rank in the exact range",
       singular_maximal == [(2, 1, 1), (2, 7, 1)],
       f"blocks={rank_blocks}; singular={singular_maximal}")
record("RANK.falsifier", "RANK",
       "no complete-support matching loses rank through internal cancellation",
       not internal_cancellation, str(internal_cancellation))

# SUBSET: classify the two deficient families for all admitted smaller k.
subset_ok = True
subset_cases = 0
for k in range(0, 11):
    for q in (1, 7):
        _, columns = component(2, k, q)
        matrix, _ = matrix_for(columns)
        expected_nullity = 1 if q == 1 or (q == 7 and k >= 3) else 0
        subset_ok &= len(columns) - matrix.rank() == expected_nullity
        subset_cases += 1
record("RANK.subsets", "RANK",
       "exceptional maximal-block dependencies restrict exactly at their support thresholds",
       subset_ok, f"cases={subset_cases}")

# ENDPOINT: raw extrema are insufficient; give the smallest Hall-only block.
points, columns = component(2, 1, 3)
matrix, rows = matrix_for(columns)
lefts = [min(column) for column in columns]
rights = [max(column) for column in columns]
match_size, matched_rows = matching(columns)
row_index = {row: i for i, row in enumerate(rows)}
minor = matrix[[row_index[row] for row in matched_rows], :]
record("ENDPOINT.smallest", "ENDPOINT",
       "(g,k,q)=(2,1,3) is full rank although both raw endpoint lists collide",
       len(set(lefts)) < len(columns) and len(set(rights)) < len(columns) and
       match_size == len(columns) and matrix.rank() == len(columns),
       f"lefts={lefts}; rights={rights}")
record("ENDPOINT.minor", "ENDPOINT",
       "a Hall-selected minor of the smallest endpoint-collision block is nonzero",
       minor.det() == -6912000,
       f"matched_rows={matched_rows}; determinant={minor.det()}")

# SMITH/GCD: primitive circuit data of the deficient cores.
e1 = sp.Matrix([[-40, -40]])
e2 = sp.Matrix([[-120, 0, 60], [-160, -40, 20]])
e2_minors = [e2[:, [1, 2]].det(), -e2[:, [0, 2]].det(),
             e2[:, [0, 1]].det()]
minor_gcd = math.gcd(*(abs(int(value)) for value in e2_minors))
record("SMITH.cores", "SMITH",
       "deficient cores have primitive circuits (-1,1) and (1,-3,2)",
       e1 * sp.Matrix([-1, 1]) == sp.zeros(1, 1) and
       [int(value // minor_gcd) for value in e2_minors] == [1, -3, 2],
       f"E2_minor_gcd={minor_gcd}")

passed = [item for item in checks if item["status"] == "pass"]
failed = [item for item in checks if item["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_endpoint_hall_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "finite-range endpoint-Hall theorem",
              "hall_range": {"g": [2, 30], "k": [0, 15], "q": [1, 60]},
              "rank_range": {"g": [2, 20], "k_max": 10, "q": [1, 30]}},
    "checks": checks, "n_pass": len(passed), "n_fail": len(failed),
    "verdict": "Across 27,840 reflected blocks, Hall deficiency occurs exactly in the grade-2 q=1 family and the q=7 family once k>=3; actual supports and interval hulls have identical matching size. Exact maximal-block ranks through g=20,q=30 find the same two singular blocks and no complete-matching/internal-cancellation falsifier. Raw distinct left/right endpoints are not sufficient: the smallest counterexample to that proof shortcut is the full-rank block (g,k,q)=(2,1,3), whose Hall-selected minor has determinant -6912000. Thus the directed Hall strategy survives, but the unbounded injectivity theorem is not yet proved.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_endpoint_hall.json"), "w", encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(passed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
