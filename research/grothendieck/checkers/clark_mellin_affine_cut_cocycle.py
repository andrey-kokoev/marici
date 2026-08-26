import json
from fractions import Fraction as F
from math import comb


def add(a, b):
    n = max(len(a), len(b))
    return [(a[k] if k < len(a) else 0) + (b[k] if k < len(b) else 0) for k in range(n)]


def multiply(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def shift(p, a):
    out = [F(0)] * len(p)
    for k, pk in enumerate(p):
        for r in range(k + 1):
            out[r] += pk * F(comb(k, r)) * a ** (k - r)
    return out


def integral(p, lo, hi):
    return sum(pk * (hi ** (k + 1) - lo ** (k + 1)) / F(k + 1) for k, pk in enumerate(p))


f = [F(2), F(-1), F(3), F(1)]
a = F(5, 7)
L = F(2)
M = F(3)
R = F(11)
tail = shift(f, L)
r = [F(0), F(1)]

global_clark_tail = multiply([F(1) - a * L, -a], tail)
local_clark_tail = multiply([F(1), -a], tail)
affine_repair = [-a * L * v for v in tail]
clark_identity = global_clark_tail == add(local_clark_tail, affine_repair)

moment_checks = []
for n in range(7):
    global_moment = integral(multiply(([F(0)] * n) + [F(1)], f), F(0), R)
    seam_moment = integral(multiply(([F(0)] * n) + [F(1)], f), F(0), L)
    global_kernel_on_tail = [F(comb(n, k)) * L ** (n - k) for k in range(n + 1)]
    tail_moment = integral(multiply(global_kernel_on_tail, tail), F(0), R - L)
    moment_checks.append(global_moment == seam_moment + tail_moment)

result = {
    "schema": "marici.grothendieck.clark_mellin_affine_cut_cocycle.v1",
    "checks": {
        "clark_affine_repair_identity": clark_identity,
        "mellin_moments_use_global_shifted_kernel": all(moment_checks),
        "two_cut_clark_cocycle_is_additive": -a * (L + M) == -a * L - a * M,
    },
    "affine_repair_coefficient": str(-a * L),
}

assert all(result["checks"].values())
print(json.dumps(result, indent=2))
