"""Exact rational coefficient extraction for the elementary far Schwarzian."""

import json
from fractions import Fraction
from pathlib import Path


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def padd(left, right):
    size = max(len(left), len(right))
    return trim(
        [
            (left[index] if index < len(left) else Fraction(0))
            + (right[index] if index < len(right) else Fraction(0))
            for index in range(size)
        ]
    )


def pneg(poly):
    return [-value for value in poly]


def pmul(left, right):
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return trim(result)


def pder(poly):
    if len(poly) == 1:
        return [Fraction(0)]
    return trim([Fraction(index) * poly[index] for index in range(1, len(poly))])


def pdivmod(numerator, denominator):
    numerator = trim(numerator)
    denominator = trim(denominator)
    if denominator == [0]:
        raise ZeroDivisionError("polynomial division by zero")
    if len(numerator) < len(denominator):
        return [Fraction(0)], numerator
    quotient = [Fraction(0)] * (len(numerator) - len(denominator) + 1)
    remainder = list(numerator)
    while remainder != [0] and len(remainder) >= len(denominator):
        degree = len(remainder) - len(denominator)
        coefficient = remainder[-1] / denominator[-1]
        quotient[degree] += coefficient
        subtractor = [Fraction(0)] * degree + [
            coefficient * value for value in denominator
        ]
        remainder = padd(remainder, pneg(subtractor))
    return trim(quotient), trim(remainder)


def pgcd(left, right):
    left = trim(left)
    right = trim(right)
    while right != [0]:
        _, remainder = pdivmod(left, right)
        left, right = right, remainder
    if left == [0]:
        return [Fraction(1)]
    leading = left[-1]
    return [value / leading for value in left]


class Rat:
    def __init__(self, numerator, denominator=(Fraction(1),)):
        self.n = trim([Fraction(value) for value in numerator])
        self.d = trim([Fraction(value) for value in denominator])
        common = pgcd(self.n, self.d)
        if len(common) > 1 or common[0] != 1:
            self.n, n_remainder = pdivmod(self.n, common)
            self.d, d_remainder = pdivmod(self.d, common)
            if n_remainder != [0] or d_remainder != [0]:
                raise ArithmeticError("inexact polynomial gcd reduction")
        if self.d[-1] < 0:
            self.n = pneg(self.n)
            self.d = pneg(self.d)
        denominator_leading = self.d[-1]
        self.n = [value / denominator_leading for value in self.n]
        self.d = [value / denominator_leading for value in self.d]

    @staticmethod
    def constant(value):
        return Rat([Fraction(value)])

    def __add__(self, other):
        other = as_rat(other)
        return Rat(
            padd(pmul(self.n, other.d), pmul(other.n, self.d)),
            pmul(self.d, other.d),
        )

    def __neg__(self):
        return Rat(pneg(self.n), self.d)

    def __sub__(self, other):
        return self + (-as_rat(other))

    def __mul__(self, other):
        other = as_rat(other)
        return Rat(pmul(self.n, other.n), pmul(self.d, other.d))

    def reciprocal(self):
        return Rat(self.d, self.n)

    def __truediv__(self, other):
        return self * as_rat(other).reciprocal()

    def derivative(self):
        return Rat(
            padd(pmul(pder(self.n), self.d), pneg(pmul(self.n, pder(self.d)))),
            pmul(self.d, self.d),
        )

    def evaluate(self, value):
        def peval(poly):
            total = 0.0
            for coefficient in reversed(poly):
                total = total * value + float(coefficient)
            return total

        return peval(self.n) / peval(self.d)

    def serialize(self):
        def encode(poly):
            return [
                str(value.numerator)
                if value.denominator == 1
                else f"{value.numerator}/{value.denominator}"
                for value in poly
            ]

        return {
            "numerator_coefficients_ascending": encode(self.n),
            "denominator_coefficients_ascending": encode(self.d),
            "numerator_degree": len(self.n) - 1,
            "denominator_degree": len(self.d) - 1,
        }


def as_rat(value):
    return value if isinstance(value, Rat) else Rat.constant(value)


def eadd(left, right):
    size = max(len(left), len(right))
    return [
        (left[index] if index < len(left) else Rat.constant(0))
        + (right[index] if index < len(right) else Rat.constant(0))
        for index in range(size)
    ]


def emul(left, right):
    result = [Rat.constant(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] = result[i + j] + a * b
    return result


def escale(expression, scalar):
    return [coefficient * scalar for coefficient in expression]


def ederivative(expression, log_derivative):
    result = [Rat.constant(0)] * len(expression)
    for degree, coefficient in enumerate(expression):
        result[degree] = result[degree] + coefficient.derivative()
        if degree:
            result[degree - 1] = (
                result[degree - 1]
                + coefficient * degree * log_derivative
            )
    return result


r = Rat([0, 1])
log_derivative = Rat([2], [1, 2])
constant = Rat.constant(Fraction(3, 4)) + Rat([1], [0, 8])
log_coefficient = Rat([0, Fraction(1, 4)]) - Rat([1], [0, 16])
h0 = [constant, log_coefficient]


def dx(expression):
    return escale(ederivative(expression, log_derivative), Rat([1], [0, 2]))


h1 = dx(h0)
h2 = dx(h1)
h3 = dx(h2)
numerator = eadd(escale(emul(h1, h3), 2), escale(emul(h2, h2), -3))
numerator_at_log_one = numerator[0] + numerator[1] + numerator[2]

sample_radii = [20.0, 32.0, 100.0, 1000.0]
result = {
    "baseline": "H0=3/4+1/(8r)+(r/4-1/(16r))*L",
    "logarithm": "L=log((2r+1)/(4pi))",
    "schwarzian_numerator_degree_in_L": len(numerator) - 1,
    "baseline_x_jets_affine_in_L": {
        "H0_prime": [coefficient.serialize() for coefficient in h1],
        "H0_double_prime": [coefficient.serialize() for coefficient in h2],
        "H0_triple_prime": [coefficient.serialize() for coefficient in h3],
    },
    "coefficients": [coefficient.serialize() for coefficient in numerator],
    "numerator_at_log_one": numerator_at_log_one.serialize(),
    "coefficient_samples": [
        {
            "r": radius,
            "values": [coefficient.evaluate(radius) for coefficient in numerator],
        }
        for radius in sample_radii
    ],
    "exact_symbolic_extraction": True,
    "coefficient_signs_on_ray_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = (
        Path(__file__).parents[1]
        / "results"
        / "theta-far-schwarzian-exact-log-quadratic.json"
    )
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
