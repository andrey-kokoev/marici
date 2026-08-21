"""Exact invariant audit of the rank-two Kummer cover and fifth selector."""

import json
from fractions import Fraction as F
from pathlib import Path


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(s, a):
    return tuple(s * x for x in a)


a = (F(2), F(0), F(0))
b = (F(0), F(3), F(0))
c = add(a, b)
A, B, C = dot(a, a), dot(b, b), dot(a, b)
det_h = A * B - C * C
adj_d = (B * A - C * B, -C * A + A * B)
radius_numerator = A * adj_d[0] + B * adj_d[1]

h = add(scale(adj_d[0] / (2 * det_h), a), scale(adj_d[1] / (2 * det_h), b))
n = cross(a, b)
assert dot(n, n) == det_h
assert dot(h, h) == radius_numerator / (4 * det_h)
assert 2 * dot(c, h) == dot(c, c)  # cocircular consistency

# With ell=h+tau*n and w=2 det(H) tau, 4 det(H) ell^2=w^2+R.
for tau in (F(-2), F(-1, 3), F(0), F(5, 7)):
    ell = add(h, scale(tau, n))
    w = 2 * det_h * tau
    assert 4 * det_h * dot(ell, ell) == w * w + radius_numerator

# The fifth bisector is N*w=C_p. Eliminating w from w^2+R=0 gives
# C_p^2+N^2 R=0.
fifth_values = []
for p in ((F(1), F(2), F(4)), (F(-1), F(1), F(2)), (F(3), F(5), F(1))):
    gp = (dot(p, a), dot(p, b))
    c_p = det_h * dot(p, p) - (gp[0] * adj_d[0] + gp[1] * adj_d[1])
    normal_pairing = dot(p, n)
    selector = c_p * c_p + normal_pairing * normal_pairing * radius_numerator
    fifth_values.append(selector)
    if normal_pairing:
        tau = c_p / (2 * det_h * normal_pairing)
        ell = add(h, scale(tau, n))
        assert 2 * dot(p, ell) == dot(p, p)
        assert 4 * det_h * dot(ell, ell) == selector / (normal_pairing * normal_pairing)

result = {
    "schema": "marici.cosmology.rank_two_kummer_cover.v1",
    "plane_gram_determinant": str(det_h),
    "planar_zero_radius_numerator": str(radius_numerator),
    "cover_equation": "w^2 + R = 0",
    "fifth_linear_selector": "N*w = C_p",
    "fifth_eliminant": "C_p^2 + N^2*R = 0",
    "generic_fifth_controls": [str(x) for x in fifth_values],
    "passed": True,
}
out = Path(__file__).with_name("results") / "rank-two-kummer-cover.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
