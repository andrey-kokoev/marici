from fractions import Fraction as Q
from itertools import permutations
import json
from pathlib import Path

def trim(a):
    while a and a[-1] == 0:
        a.pop()
    return a

def add(a, b):
    out = list(a) + [Q(0)] * max(0, len(b) - len(a))
    for i, x in enumerate(b):
        out[i] += x
    return trim(out)

def neg(a):
    return [-x for x in a]

def mul(a, b):
    if not a or not b:
        return []
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)

def sign(p):
    inversions = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return -1 if inversions % 2 else 1

def determinant(matrix):
    out = []
    for p in permutations(range(len(matrix))):
        term = [Q(sign(p))]
        for i, j in enumerate(p):
            term = mul(term, matrix[i][j])
        out = add(out, term)
    return out

zero = []
# Coefficients in v of 4*P6, D, and H; each coefficient is ascending in u.
p2 = [Q(1)]
p1 = [Q(-4), Q(2), Q(4), Q(-4)]
p0 = [Q(4), Q(-4), Q(-7), Q(4), Q(4)]
d2 = [Q(-1)]
d1 = [Q(4), Q(-6), Q(4)]
d0 = [Q(-4), Q(12), Q(-9)]
h1 = [Q(1), Q(2), Q(-1)]
h0 = [Q(-2), Q(-3), Q(0), Q(1)]

res_d = determinant([
    [p2, p1, p0, zero],
    [zero, p2, p1, p0],
    [d2, d1, d0, zero],
    [zero, d2, d1, d0],
])
res_h = add(add(mul(p2, mul(h0, h0)), neg(mul(p1, mul(h1, h0)))), mul(p0, mul(h1, h1)))

expected_d = [Q(0)] * 4 + [Q(16), Q(-160), Q(464), Q(-576), Q(320), Q(-64)]
expected_h = [Q(0)] * 3 + [Q(-8), Q(8), Q(8), Q(-4)]
assert res_d == expected_d
assert res_h == expected_h

packet = {
    "schema": "marici.p6_wall_resultants.v1",
    "normalization": "resultants of 4*P6 with D and H",
    "resultant_D": "16*u^4*(u-1)^2*(1-8*u+12*u^2-4*u^3)",
    "resultant_H": "4*u^3*(-2+2*u+2*u^2-u^3)",
    "exact_fraction_arithmetic": True,
}
Path("research/benincasa/results/p6-wall-resultants.json").write_text(
    json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(packet, sort_keys=True))
