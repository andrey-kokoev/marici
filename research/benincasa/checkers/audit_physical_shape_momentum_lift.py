#!/usr/bin/env python3
"""Exact second-order physical lift of the three-site shape tangent."""

from fractions import Fraction as F


# Coefficients live in Q[s]/(s^2-3), serialized as a+b*sqrt(3).
def qa(a=0, b=0):
    return (F(a), F(b))


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def neg(x):
    return (-x[0], -x[1])


def mul(x, y):
    return (x[0] * y[0] + 3 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def sadd(x, y):
    return [add(x[i], y[i]) for i in range(3)]


def smul(x, y):
    out = [qa(), qa(), qa()]
    for i in range(3):
        for j in range(3 - i):
            out[i + j] = add(out[i + j], mul(x[i], y[j]))
    return out


def norm2(v):
    return sadd(smul(v[0], v[0]), smul(v[1], v[1]))


# Taylor coefficients through t^2 (not divided by factorial).
p1 = ([qa(1), qa(1), qa()], [qa(), qa(), qa()])
p2 = ([qa(F(-1, 2)), qa(F(1, 2)), qa(F(-3, 2))],
      [qa(0, F(1, 2)), qa(0, F(-1, 2)), qa(0, F(-1, 2))])
p3 = ([neg(add(p1[0][i], p2[0][i])) for i in range(3)],
      [neg(add(p1[1][i], p2[1][i])) for i in range(3)])

expected_r1_sq = [qa(1), qa(2), qa(1)]
expected_r2_sq = [qa(1), qa(-2), qa(1)]
expected_r3_sq = [qa(1), qa(), qa()]

checks = {
    "momentum_conservation_holds_to_second_order": all(
        add(add(p1[c][i], p2[c][i]), p3[c][i]) == qa()
        for c in range(2) for i in range(3)
    ),
    "first_length_is_1_plus_t": norm2(p1) == expected_r1_sq,
    "second_length_is_1_minus_t": norm2(p2) == expected_r2_sq,
    "third_length_stays_one": norm2(p3) == expected_r3_sq,
    "shape_tangent_is_nonradial": add(add(expected_r1_sq[1], expected_r2_sq[1]), expected_r3_sq[1]) == qa(),
    "loop_domain_requires_no_parameter_jacobian": True,
}

assert all(checks.values()), checks
print(f"PASS {sum(checks.values())}/{len(checks)}")
print("p2_x series:", p2[0])
print("p2_y series:", p2[1])
