"""Canonical path-polynomial and primitive-minor checker."""
from collections import defaultdict
from functools import reduce
import json
import math
import os
import sympy as sp

checks = []


def add(output, key, value):
    if value:
        output[key] += value
        if output[key] == 0:
            del output[key]


def fold_coefficients(g, a):
    return [int(math.comb(g, j) * (-1) ** (g - j) *
                sp.rf(a, g - j) * sp.rf(4 - a, j))
            for j in range(g + 1)]


def path_coefficients(g, a, m):
    c = fold_coefficients(g, a)
    b = [m * c[0]]
    for j in range(1, g + 1):
        b.append((m + j) * c[j] + (m + j - 1 - g) * c[j - 1])
    b.append(m * c[g])
    return b


def direct_column(g, a, m):
    terms = {(-a, m): 1}
    for weight in range(2, g + 2):
        nxt = defaultdict(int)
        for (r, t), coefficient in terms.items():
            add(nxt, (r - 1, t), coefficient * r)
            add(nxt, (r, t + 1), coefficient * (r + weight + 2))
        terms = dict(nxt)
    output = defaultdict(int)
    for (r, t), coefficient in terms.items():
        add(output, (r, t - 1), coefficient * t)
        add(output, (r + 1, t), coefficient * (t - g))
        add(output, (t - 1, r), -coefficient * t)
        add(output, (t, r + 1), -coefficient * (t - g))
    return dict(output)


def canonical_direct_column(g, a, m):
    center = 1 - g
    q = abs(a + m - center)
    if q == 0:
        return {}
    output = {}
    for (r, t), coefficient in direct_column(g, a, m).items():
        if r - t == q:
            output[r] = coefficient
    return output


def canonical_path_column(g, a, m):
    center = 1 - g
    signed_delta = center - (a + m)
    q = abs(signed_delta)
    if q == 0:
        return {}
    shift = -a - g if signed_delta > 0 else -a - g + q
    sign = 1 if signed_delta > 0 else -1
    output = {}
    for j, coefficient in enumerate(path_coefficients(g, a, m)):
        if coefficient:
            output[shift + j] = sign * coefficient
    return output


def block_matrix(g, points):
    columns = [canonical_path_column(g, a, m) for a, m in points]
    rows = sorted(set().union(*(column.keys() for column in columns)))
    if not rows:
        return sp.zeros(0, len(columns)), rows
    return (sp.Matrix([[column.get(row, 0) for column in columns]
                       for row in rows]), rows)


def primitive(values):
    integers = [int(value) for value in values]
    divisor = reduce(math.gcd, (abs(value) for value in integers if value), 0)
    reduced = [value // divisor for value in integers]
    first = next(value for value in reduced if value)
    return [-value for value in reduced] if first < 0 else reduced


def record(cid, group, statement, condition, detail=""):
    status = "pass" if bool(condition) else "FAIL"
    checks.append({"id": cid, "group": group, "statement": statement,
                   "status": status, "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement}" +
          (f" ({detail})" if detail else ""), flush=True)


# PATH: the one-dimensional polynomial exactly represents the sparse column.
path_cases = 0
path_ok = True
for g in range(2, 11):
    for a in range(0, 13, 2):
        for m in (-12, -5, 0, 3, 9):
            path_ok &= canonical_path_column(g, a, m) == canonical_direct_column(g, a, m)
            path_cases += 1
record("PATH.identity", "PATH",
       "canonical path polynomial equals the direct sparse magnetic column",
       path_ok, f"columns={path_cases}")

# CUBIC: at grade 2 the general path coefficients have a closed cubic form.
cubic_cases = 0
cubic_ok = True
for a in range(0, 21, 2):
    for m in range(-10, 11):
        expected = [
            m * a * (a + 1),
            a * ((3 * a - 7) * m - 10),
            (a - 4) * ((3 * a - 5) * m - 10),
            m * (a - 4) * (a - 5),
        ]
        cubic_ok &= path_coefficients(2, a, m) == expected
        cubic_cases += 1
record("CUBIC.g2", "CUBIC",
       "grade-2 component columns obey the explicit cubic coefficient law",
       cubic_ok, f"cases={cubic_cases}")

# E1: equal one-row columns give the primitive incidence flow (-1,1).
e1_points = [(0, -2), (0, 0)]
e1_matrix, e1_rows = block_matrix(2, e1_points)
record("MINOR.E1.block", "MINOR", "E1 canonical block is one row with equal weights",
       e1_matrix == sp.Matrix([[-40, -40]]), f"rows={e1_rows}; matrix={e1_matrix.tolist()}")
record("MINOR.E1.flow", "MINOR", "E1 primitive null flow is (-1,1)",
       primitive([-e1_matrix[0, 1], e1_matrix[0, 0]]) == [1, -1] and
       e1_matrix * sp.Matrix([-1, 1]) == sp.zeros(1, 1))

# E2: signed maximal minors produce the coefficients (1,-3,2).
e2_points = [(0, -8), (4, 2), (6, 0)]
e2_matrix, e2_rows = block_matrix(2, e2_points)
expected_e2_matrix = sp.Matrix([[-120, 0, 60], [-160, -40, 20]])
record("MINOR.E2.block", "MINOR", "E2 reduces to the exact two-row integer block",
       e2_matrix == expected_e2_matrix,
       f"rows={e2_rows}; matrix={e2_matrix.tolist()}")
signed_minors = [
    e2_matrix[:, [1, 2]].det(),
    -e2_matrix[:, [0, 2]].det(),
    e2_matrix[:, [0, 1]].det(),
]
record("MINOR.E2.raw", "MINOR", "E2 signed maximal minors are (2400,-7200,4800)",
       signed_minors == [2400, -7200, 4800], str(signed_minors))
record("MINOR.E2.primitive", "MINOR", "gcd normalization gives primitive flow (1,-3,2)",
       primitive(signed_minors) == [1, -3, 2] and
       e2_matrix * sp.Matrix([1, -3, 2]) == sp.zeros(2, 1))

# SING: classify full reflected blocks in a widened bounded range.
singular = []
block_cases = 0
for g in range(2, 21):
    center = 1 - g
    for q in range(1, 31):
        points = []
        for a in range(0, 21, 2):
            points.append((a, center - q - a))
            points.append((a, center + q - a))
        matrix, _ = block_matrix(g, points)
        nullity = len(points) - matrix.rank()
        if nullity:
            singular.append((g, q, nullity))
        block_cases += 1
record("SING.range", "SING",
       "only the grade-2 q=1 and q=7 reflected blocks are singular in range",
       singular == [(2, 1, 1), (2, 7, 1)],
       f"blocks={block_cases}; singular={singular}")

passed = [item for item in checks if item["status"] == "pass"]
failed = [item for item in checks if item["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_path_block_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "source-typed local block theorem plus finite-range singular-block classification",
              "grades": [2, 20], "pole_depth_max": 20,
              "component_distance": [1, 30]},
    "checks": checks, "n_pass": len(passed), "n_fail": len(failed),
    "verdict": "Each reflected magnetic component is represented by a canonical Laurent path polynomial whose coefficients are binomial/rising-factorial path counts followed by derivative weights. The exceptional integer coefficients are primitive signed maximal minors of the local component block. E1 comes from two equal one-row columns. E2 has block [[-120,0,60],[-160,-40,20]], signed minors (2400,-7200,4800), and primitive flow (1,-3,2). Across g=2..20, a<=20, q=1..30, only (g,q)=(2,1),(2,7) are singular. Unbounded injectivity outside this range remains open.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_path_blocks.json"), "w", encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(passed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
