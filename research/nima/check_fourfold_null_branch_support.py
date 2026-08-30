"""Exact circumcenter support for fourfold five-site Kummer branching."""

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


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def det3(a):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def adj3(a):
    return [
        [
            a[1][1] * a[2][2] - a[1][2] * a[2][1],
            a[0][2] * a[2][1] - a[0][1] * a[2][2],
            a[0][1] * a[1][2] - a[0][2] * a[1][1],
        ],
        [
            a[1][2] * a[2][0] - a[1][0] * a[2][2],
            a[0][0] * a[2][2] - a[0][2] * a[2][0],
            a[0][2] * a[1][0] - a[0][0] * a[1][2],
        ],
        [
            a[1][0] * a[2][1] - a[1][1] * a[2][0],
            a[0][1] * a[2][0] - a[0][0] * a[2][1],
            a[0][0] * a[1][1] - a[0][1] * a[1][0],
        ],
    ]


def mv(a, v):
    return tuple(dot(row, v) for row in a)


rows = []
for subset in combinations(range(5), 4):
    r0 = points[subset[0]]
    vecs = [sub(points[i], r0) for i in subset[1:]]
    gram = [[dot(v, w) for w in vecs] for v in vecs]
    d = tuple(dot(v, v) for v in vecs)
    detg = det3(gram)
    adj = adj3(gram)
    numerator = dot(d, mv(adj, d))
    radius2 = numerator / (4 * detg)
    # Coordinates in the vec basis: alpha = (1/2) G^-1 d.
    alpha_num = mv(adj, d)
    center_rel = tuple(
        sum(alpha_num[i] * vecs[i][j] for i in range(3)) / (2 * detg)
        for j in range(3)
    )
    center = tuple(r0[j] + center_rel[j] for j in range(3))
    direct = dot(sub(center, r0), sub(center, r0))
    assert direct == radius2
    rows.append({
        "subset": [i + 1 for i in subset],
        "gram_determinant": str(detg),
        "cayley_gram_numerator": str(numerator),
        "radius_squared": str(radius2),
        "fourfold_null_branch_realized": radius2 == 0,
    })

result = {
    "schema": "marici.cosmology.fourfold_null_branch_support.v1",
    "quadruples": len(rows),
    "rows": rows,
    "realized_quadruples": sum(r["fourfold_null_branch_realized"] for r in rows),
    "passed": True,
    "theorem": "away from detG=0, four null quadrics meet iff d^T adj(G) d=0",
}
out = Path(__file__).with_name("results") / "fourfold-null-branch-support.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
