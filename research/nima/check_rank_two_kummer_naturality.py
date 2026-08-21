"""Exact naturality checks for the rank-two Kummer line and selector."""

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


def scale(s, a):
    return tuple(s * x for x in a)


def invariants(a, b, p, tau):
    aa, bb, ab = dot(a, a), dot(b, b), dot(a, b)
    delta = aa * bb - ab * ab
    d = (aa, bb)
    adj_d = (bb * d[0] - ab * d[1], -ab * d[0] + aa * d[1])
    radius = d[0] * adj_d[0] + d[1] * adj_d[1]
    n = cross(a, b)
    w = 2 * delta * tau
    gp = (dot(p, a), dot(p, b))
    cp = delta * dot(p, p) - gp[0] * adj_d[0] - gp[1] * adj_d[1]
    normal = dot(p, n)
    return delta, radius, w, normal, cp


a = (F(2), F(1), F(0))
b = (F(-1), F(2), F(0))
p = (F(3), F(-2), F(5))
tau = F(7, 11)
base = invariants(a, b, p, tau)

# Swapping the ordered plane basis reverses n and the affine coordinate.
swapped = invariants(b, a, p, -tau)
assert swapped[0] == base[0]
assert swapped[1] == base[1]
assert swapped[2] == -base[2]
assert swapped[3] == -base[3]
assert swapped[4] == base[4]
assert swapped[2] ** 2 + swapped[1] == base[2] ** 2 + base[1]
assert swapped[3] * swapped[2] == base[3] * base[2]

# A cyclic coordinate permutation is an orientation-preserving orthogonal
# transport.
def orth_plus(v):
    return (v[2], v[0], v[1])


transported = invariants(orth_plus(a), orth_plus(b), orth_plus(p), tau)
assert transported == base

# An orientation-reversing orthogonal transport flips the pseudovector n.
# The same physical ell therefore uses -tau; w and N are both odd.
def orth_minus(v):
    return (v[2], -v[0], v[1])


reflected = invariants(orth_minus(a), orth_minus(b), orth_minus(p), -tau)
assert reflected[0] == base[0]
assert reflected[1] == base[1]
assert reflected[2] == -base[2]
assert reflected[3] == -base[3]
assert reflected[4] == base[4]
assert reflected[3] * reflected[2] == base[3] * base[2]

# Under common scaling lambda, R and w^2 have weight 6; Nw and C_p also
# have weight 6. The affine parameter has weight -1.
lam = F(3, 2)
scaled = invariants(scale(lam, a), scale(lam, b), scale(lam, p), tau / lam)
assert scaled[0] == lam**4 * base[0]
assert scaled[1] == lam**6 * base[1]
assert scaled[2] == lam**3 * base[2]
assert scaled[3] == lam**3 * base[3]
assert scaled[4] == lam**6 * base[4]

result = {
    "schema": "marici.cosmology.rank_two_kummer_naturality.v1",
    "basis_swap": {"w_character": -1, "normal_character": -1, "selector_character": 1},
    "ambient_SO3_transport": "invariant",
    "ambient_orientation_reversal": {"w_character": -1, "normal_character": -1},
    "scaling_weights": {"Delta": 4, "R": 6, "w": 3, "N": 3, "C_p": 6},
    "paired_selector_weight": 6,
    "passed": True,
}
out = Path(__file__).with_name("results") / "rank-two-kummer-naturality.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
