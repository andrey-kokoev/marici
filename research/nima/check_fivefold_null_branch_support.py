"""Exact cleared support equations for fivefold null-branch intersection."""

from fractions import Fraction as F
import json
from pathlib import Path


pts = [
    (F(0), F(0), F(0)),
    (F(1), F(0), F(0)),
    (F(0), F(2), F(0)),
    (F(0), F(0), F(3)),
    (F(1), F(2), F(4)),
]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def det3(a):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def adj3(a):
    return [
        [a[1][1]*a[2][2]-a[1][2]*a[2][1], a[0][2]*a[2][1]-a[0][1]*a[2][2], a[0][1]*a[1][2]-a[0][2]*a[1][1]],
        [a[1][2]*a[2][0]-a[1][0]*a[2][2], a[0][0]*a[2][2]-a[0][2]*a[2][0], a[0][2]*a[1][0]-a[0][0]*a[1][2]],
        [a[1][0]*a[2][1]-a[1][1]*a[2][0], a[0][1]*a[2][0]-a[0][0]*a[2][1], a[0][0]*a[1][1]-a[0][1]*a[1][0]],
    ]


def mv(a, v):
    return tuple(dot(r, v) for r in a)


a, b, c, p = pts[1], pts[2], pts[3], pts[4]
vecs = [a, b, c]
gram = [[dot(v, w) for w in vecs] for v in vecs]
d = tuple(dot(v, v) for v in vecs)
detg = det3(gram)
adj_d = mv(adj3(gram), d)
radius_numerator = dot(d, adj_d)
center_numerator = tuple(sum(adj_d[i] * vecs[i][j] for i in range(3)) for j in range(3))
fifth_numerator = detg * dot(p, p) - dot(p, center_numerator)

center = tuple(x / (2 * detg) for x in center_numerator)
radius2 = dot(center, center)
fifth_value = dot(tuple(center[j] - p[j] for j in range(3)), tuple(center[j] - p[j] for j in range(3)))
assert radius2 == radius_numerator / (4 * detg)
assert fifth_value - radius2 == fifth_numerator / detg

result = {
    "schema": "marici.cosmology.fivefold_null_branch_support.v1",
    "gram_determinant": str(detg),
    "zero_radius_numerator": str(radius_numerator),
    "fifth_cosphericity_numerator": str(fifth_numerator),
    "radius_squared": str(radius2),
    "fifth_minus_radius_squared": str(fifth_value - radius2),
    "fivefold_realized": radius_numerator == 0 and fifth_numerator == 0,
    "passed": True,
    "theorem": "away from detG=0, five null quadrics meet iff zero-radius and fifth-cosphericity numerators both vanish",
}
out = Path(__file__).with_name("results") / "fivefold-null-branch-support.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
