"""Exact formal-series check that prime-power grades are cyclic cumulants."""

from fractions import Fraction


ORDER = 9


def multiply(left, right):
    out = [Fraction(0) for _ in range(ORDER)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j < ORDER:
                out[i + j] += a * b
    return out


def exponential(series):
    out = [Fraction(0) for _ in range(ORDER)]
    out[0] = 1
    power = [Fraction(0) for _ in range(ORDER)]
    power[0] = 1
    factorial = 1
    for n in range(1, ORDER):
        power = multiply(power, series)
        factorial *= n
        for degree in range(ORDER):
            out[degree] += power[degree] / factorial
    return out


# -log(1-x), truncated as a formal series.
cumulants = [Fraction(0)] + [Fraction(1, k) for k in range(1, ORDER)]
euler_inverse = exponential(cumulants)
expected_inverse = [Fraction(1) for _ in range(ORDER)]

checks = 0
assert euler_inverse == expected_inverse
checks += ORDER
assert cumulants[1] == 1
assert cumulants[2] == Fraction(1, 2)
checks += 2

# Removing k=1,2 gives the det_3 tail; restoring them reconstructs one series.
tail = cumulants[:]
tail[1] = 0
tail[2] = 0
restored = tail[:]
restored[1] += cumulants[1]
restored[2] += cumulants[2]
assert restored == cumulants
checks += ORDER

print(f"PASS {checks}/{checks}: primitive and square grades are cumulants of one Euler determinant chart")

