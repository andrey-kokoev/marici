"""Exact degree-12 falsifier for integral-sampling Mellin orientation."""

from fractions import Fraction as F
import json
from pathlib import Path


def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def divrem(a, b):
    a, b = trim(a[:]), trim(b[:])
    while len(a) >= len(b) and any(a):
        q = a[-1] / b[-1]
        shift = len(a) - len(b)
        for i, value in enumerate(b):
            a[i + shift] -= q * value
        trim(a)
    return a


def derivative(p):
    return [F(i) * p[i] for i in range(1, len(p))] or [F(0)]


def sturm(p):
    seq = [trim(p[:]), derivative(p)]
    while any(seq[-1]):
        remainder = divrem(seq[-2], seq[-1])
        if not any(remainder):
            break
        seq.append([-x for x in remainder])
    return seq


def infinity_sign(p, positive):
    sign = 1 if p[-1] > 0 else -1
    return sign if positive or (len(p) - 1) % 2 == 0 else -sign


def variations(signs):
    return sum(a != b for a, b in zip(signs, signs[1:]))


# Fourier images of (pi*x^2)^j exp(-pi*x^2), as polynomials in t=pi*x^2.
images = [
    [F(1)],
    [F(1, 2), F(-1)],
    [F(3, 4), F(-3), F(1)],
    [F(15, 8), F(-45, 4), F(15, 2), F(-1)],
    [F(105, 16), F(-105, 2), F(105, 2), F(-14), F(1)],
    [F(945, 32), F(-4725, 16), F(1575, 4), F(-315, 2), F(45, 2), F(-1)],
    [F(10395, 64), F(-31185, 16), F(51975, 16), F(-3465, 2), F(1485, 4), F(-33), F(1)],
]

F4 = [F(0), F(-6), F(4)]
Q8 = [F(0), F(105, 8), F(0), F(-7), F(1)]
R12 = [F(0), F(-31185, 32), F(0), F(3465, 8), F(0), F(-33, 2), F(1)]


def fourier(coefficients):
    out = [F(0)] * len(images)
    for coefficient, image in zip(coefficients, images):
        for degree, value in enumerate(image):
            out[degree] += coefficient * value
    return trim(out)


def pad(p):
    return p + [F(0)] * (7 - len(p))


carrier = [a + F(13, 20) * b + F(1, 160) * c
           for a, b, c in zip(pad(F4), pad(Q8), pad(R12))]

# carrier = t*S(t)/5120.  Positivity for integer samples follows from
# pi*n^2 > 3, S(3)>0, and S' having no real root with positive leading sign.
S = [F(-18225), F(20480), F(-9436), F(3328), F(-528), F(32)]
D = derivative(S)
sturm_sequence = sturm(D)
root_count = variations([infinity_sign(p, False) for p in sturm_sequence]) - variations(
    [infinity_sign(p, True) for p in sturm_sequence]
)
S_at_3 = sum(value * F(3) ** degree for degree, value in enumerate(S))

# After removing r(2r-1), the Mellin window is
# H(y)=(256*y^2+5920*y+87325)/81920, y=(r-1/4)^2.
discriminant = F(5920) ** 2 - 4 * F(256) * F(87325)

checks = {
    "quartic_direction_fourier_fixed": fourier(pad(F4)) == trim(F4[:]),
    "degree8_direction_fourier_fixed": fourier(pad(Q8)) == trim(Q8[:]),
    "degree12_direction_fourier_fixed": fourier(pad(R12)) == trim(R12[:]),
    "hostile_carrier_fourier_fixed": fourier(carrier) == trim(carrier[:]),
    "vacuum_sample_zero": carrier[0] == 0,
    "derivative_has_no_real_roots": root_count == 0,
    "sample_polynomial_increasing_above_three": D[-1] > 0 and root_count == 0,
    "sample_polynomial_positive_at_three": S_at_3 == 13155,
    "mellin_y_discriminant_negative": discriminant == -F(54374400),
}

result = {
    "schema": "marici.theta-degree12-sampling-falsifier.v1",
    "carrier_coefficients_t_basis": [str(x) for x in carrier],
    "sample_polynomial_S": [str(x) for x in S],
    "S_at_3": str(S_at_3),
    "derivative_real_root_count": root_count,
    "mellin_y_discriminant": str(discriminant),
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "verdict": "Fourier self-duality, vacuum nullity, and positive integer samples do not force critical-line Mellin-window zeros at degree twelve.",
}

out = Path(__file__).resolve().parents[1] / "results" / "theta_degree12_sampling_falsifier.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
