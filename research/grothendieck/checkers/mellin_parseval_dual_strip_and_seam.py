import json
from fractions import Fraction as F
from math import comb


def derivative(p):
    return [F(k) * p[k] for k in range(1, len(p))]


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


def value(p, x):
    return sum(pk * x**k for k, pk in enumerate(p))


def integral(p, lo, hi):
    return sum(pk * (hi ** (k + 1) - lo ** (k + 1)) / F(k + 1) for k, pk in enumerate(p))


f = [F(2), F(-1), F(3), F(1)]
g = [F(-2), F(4), F(1)]
L = F(2)
R = F(7)

green_left = integral(multiply(derivative(f), g), F(0), R) + integral(multiply(f, derivative(g)), F(0), R)
green_right = value(f, R) * value(g, R) - value(f, F(0)) * value(g, F(0))
wall_left = integral(multiply([F(0)] + f, g), F(0), R)
wall_right = integral(multiply(f, [F(0)] + g), F(0), R)
translation_left = integral(multiply(shift(f, L), g), F(0), R - L)
translation_right = integral(multiply(f, shift(g, -L)), L, R)

result = {
    "schema": "marici.grothendieck.mellin_parseval_dual_strip_and_seam.v1",
    "checks": {
        "green_endpoint_identity": green_left == green_right,
        "wall_multiplication_is_self_adjoint": wall_left == wall_right,
        "right_translation_adjoint_is_truncated_backward_translation": translation_left == translation_right,
    },
    "seam_interval": [str(F(0)), str(L)],
}

assert all(result["checks"].values())
print(json.dumps(result, indent=2))
