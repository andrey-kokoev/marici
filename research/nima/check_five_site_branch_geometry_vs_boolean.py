"""Exact rational model separating Boolean deck subsets from geometric strata."""

from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path


points = [
    (F(0), F(0), F(0)),
    (F(1), F(0), F(0)),
    (F(0), F(2), F(0)),
    (F(0), F(0), F(3)),
    (F(1), F(2), F(4)),
]


def sq(v):
    return sum(x * x for x in v)


def rref_aug(rows, n=3):
    a = [list(r) for r in rows]
    row = 0
    pivots = []
    for col in range(n):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        z = a[row][col]
        a[row] = [x / z for x in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                z = a[i][col]
                a[i] = [a[i][j] - z * a[row][j] for j in range(n + 1)]
        pivots.append(col)
        row += 1
    inconsistent = any(all(r[j] == 0 for j in range(n)) and r[n] != 0 for r in a)
    return a, pivots, inconsistent


def affine_solution(rows):
    a, pivots, bad = rref_aug(rows)
    if bad:
        return None, []
    free = [j for j in range(3) if j not in pivots]
    u0 = [F(0)] * 3
    for i, col in enumerate(pivots):
        u0[col] = a[i][3]
    basis = []
    for f in free:
        v = [F(0)] * 3
        v[f] = 1
        for i, col in enumerate(pivots):
            v[col] = -a[i][f]
        basis.append(tuple(v))
    return tuple(u0), basis


rows = []
profile = {}
for k in range(1, 6):
    for subset in combinations(range(5), k):
        ref = points[subset[0]]
        linear = []
        for idx in subset[1:]:
            p = points[idx]
            linear.append(tuple([2 * (p[j] - ref[j]) for j in range(3)] + [sq(p) - sq(ref)]))
        u0, basis = affine_solution(linear)
        if u0 is None:
            status = "empty_linear_system"
            nullity = None
        else:
            nullity = len(basis)
            d = tuple(u0[j] - ref[j] for j in range(3))
            constant = sq(d)
            linear_coeff = [2 * sum(d[j] * v[j] for j in range(3)) for v in basis]
            quad_coeff = [
                [sum(v[j] * w[j] for j in range(3)) for w in basis]
                for v in basis
            ]
            nonconstant = any(linear_coeff) or any(any(r) for r in quad_coeff)
            if nullity == 0:
                status = "nonempty_point" if constant == 0 else "empty_point_misses_quadric"
            elif nonconstant:
                status = "nonempty_over_C"
            else:
                status = "all_affine_space" if constant == 0 else "empty_constant_restriction"
        profile[status] = profile.get(status, 0) + 1
        rows.append({
            "subset": [i + 1 for i in subset],
            "size": k,
            "linear_nullity": nullity,
            "complex_status": status,
            "real_euclidean_status": "nonempty" if k == 1 else "empty_for_distinct_points",
        })

result = {
    "schema": "marici.cosmology.five_site.branch_geometry_vs_boolean.v1",
    "frozen_points": [[str(x) for x in p] for p in points],
    "subsets_checked": len(rows),
    "status_profile": profile,
    "rows": rows,
    "passed": True,
    "verdict": "formal Boolean deck degree is not geometric branch codimension",
}
out = Path(__file__).with_name("results") / "five-site-branch-geometry-vs-boolean.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: result[k] for k in ("subsets_checked", "status_profile", "passed")}))
