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


def h1_energy(p, lo, hi):
    return integral(multiply(p, p), lo, hi) + integral(multiply(derivative(p), derivative(p)), lo, hi)


f = [F(3), F(-2), F(1), F(4)]
L = F(2)
M = F(3)
R = F(11)

whole = h1_energy(f, F(0), R)
seam_L = h1_energy(f, F(0), L)
tail_L = h1_energy(shift(f, L), F(0), R - L)
second_seam = h1_energy(shift(f, L), F(0), M)
tail_LM = h1_energy(shift(f, L + M), F(0), R - L - M)
combined_seam = h1_energy(f, F(0), L + M)

result = {
    "schema": "marici.grothendieck.h1_tail_seam_cut_isometry.v1",
    "checks": {
        "one_cut_energy_isometry": whole == seam_L + tail_L,
        "two_cut_energy_isometry": whole == seam_L + second_seam + tail_LM,
        "seams_concatenate_without_energy_loss": combined_seam == seam_L + second_seam,
        "interface_trace_matches": value(f, L) == value(shift(f, L), F(0)),
    },
    "cut_lengths": [str(L), str(M)],
}

assert all(result["checks"].values())
print(json.dumps(result, indent=2))
