"""Exact audit for the three-site absolute-Q falsifier.

The script uses a tiny integer polynomial/rational-function implementation,
so it has no third-party dependencies.  It checks the identities used to
separate the absolute degree-two-del-Pezzo Gysin system from marked/relative
Q-support, and it checks the A/B versus B/A Legendre normalization against
the published coefficient of the second-order operator L2.
"""

from __future__ import annotations

import json


class Poly:
    """Sparse integer polynomial in a fixed number of variables."""

    def __init__(self, nvars: int, terms=None):
        self.nvars = nvars
        self.terms = {
            tuple(exponents): int(coefficient)
            for exponents, coefficient in (terms or {}).items()
            if coefficient
        }

    @classmethod
    def constant(cls, nvars: int, coefficient: int):
        if coefficient == 0:
            return cls(nvars)
        return cls(nvars, {(0,) * nvars: coefficient})

    @classmethod
    def variable(cls, nvars: int, index: int):
        exponents = [0] * nvars
        exponents[index] = 1
        return cls(nvars, {tuple(exponents): 1})

    def _coerce(self, other):
        if isinstance(other, Poly):
            assert other.nvars == self.nvars
            return other
        return Poly.constant(self.nvars, other)

    def __add__(self, other):
        other = self._coerce(other)
        terms = dict(self.terms)
        for exponents, coefficient in other.terms.items():
            terms[exponents] = terms.get(exponents, 0) + coefficient
        return Poly(self.nvars, terms)

    __radd__ = __add__

    def __neg__(self):
        return Poly(
            self.nvars,
            {exponents: -coefficient for exponents, coefficient in self.terms.items()},
        )

    def __sub__(self, other):
        return self + (-self._coerce(other))

    def __rsub__(self, other):
        return self._coerce(other) - self

    def __mul__(self, other):
        other = self._coerce(other)
        terms = {}
        for left_exp, left_coefficient in self.terms.items():
            for right_exp, right_coefficient in other.terms.items():
                exponents = tuple(
                    left + right for left, right in zip(left_exp, right_exp)
                )
                terms[exponents] = (
                    terms.get(exponents, 0)
                    + left_coefficient * right_coefficient
                )
        return Poly(self.nvars, terms)

    __rmul__ = __mul__

    def __pow__(self, exponent: int):
        assert exponent >= 0
        result = Poly.constant(self.nvars, 1)
        factor = self
        power = exponent
        while power:
            if power & 1:
                result = result * factor
            factor = factor * factor
            power >>= 1
        return result

    def derivative(self, index: int):
        terms = {}
        for exponents, coefficient in self.terms.items():
            degree = exponents[index]
            if degree:
                lowered = list(exponents)
                lowered[index] -= 1
                key = tuple(lowered)
                terms[key] = terms.get(key, 0) + degree * coefficient
        return Poly(self.nvars, terms)

    def evaluate(self, values):
        assert len(values) == self.nvars
        return sum(
            coefficient
            * product(value**degree for value, degree in zip(values, exponents))
            for exponents, coefficient in self.terms.items()
        )

    def __eq__(self, other):
        return self.terms == self._coerce(other).terms


class Rat:
    """Unsimplified rational function; equality is exact cross multiplication."""

    def __init__(self, numerator: Poly, denominator: Poly):
        assert numerator.nvars == denominator.nvars
        assert denominator.terms
        self.numerator = numerator
        self.denominator = denominator

    @classmethod
    def polynomial(cls, polynomial: Poly):
        return cls(polynomial, Poly.constant(polynomial.nvars, 1))

    def _coerce(self, other):
        if isinstance(other, Rat):
            return other
        if isinstance(other, Poly):
            return Rat.polynomial(other)
        return Rat.polynomial(Poly.constant(self.numerator.nvars, other))

    def __add__(self, other):
        other = self._coerce(other)
        return Rat(
            self.numerator * other.denominator
            + other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    __radd__ = __add__

    def __neg__(self):
        return Rat(-self.numerator, self.denominator)

    def __sub__(self, other):
        return self + (-self._coerce(other))

    def __rsub__(self, other):
        return self._coerce(other) - self

    def __mul__(self, other):
        other = self._coerce(other)
        return Rat(
            self.numerator * other.numerator,
            self.denominator * other.denominator,
        )

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self._coerce(other)
        return Rat(
            self.numerator * other.denominator,
            self.denominator * other.numerator,
        )

    def derivative(self, index: int):
        return Rat(
            self.numerator.derivative(index) * self.denominator
            - self.numerator * self.denominator.derivative(index),
            self.denominator**2,
        )

    def __eq__(self, other):
        other = self._coerce(other)
        return (
            self.numerator * other.denominator
            == other.numerator * self.denominator
        )


def product(values):
    result = 1
    for value in values:
        result *= value
    return result


def compactification_checks():
    nvars = 3
    x, y, z = (Poly.variable(nvars, index) for index in range(nvars))
    E = x + y + z
    h = x**2 + y**2 - z**2
    A = h - 2 * x * y
    B = h + 2 * x * y
    u = E**2 + y**2
    v = E**2 + x**2

    H = x**2 * u**2 - h * u * v + y**2 * v**2 + E**2 * A * B
    H_expected = z**2 * (E**4 - h * E**2 + x**2 * y**2)

    # Four times the two restricted quadratic-form determinants.  Clearing
    # the factor 1/4 keeps every identity integral.
    det_alpha_times_four = (
        4 * y**2 * (x**2 * u**2 + E**2 * A * B) - h**2 * u**2
    )
    det_beta_times_four = (
        4 * x**2 * (y**2 * v**2 + E**2 * A * B) - h**2 * v**2
    )

    checks = {
        "H_identity": H == H_expected,
        "binary_quadratic_determinant": 4 * x**2 * y**2 - h**2 == -A * B,
        "alpha_restriction_determinant": (
            det_alpha_times_four == -A * B * (E**2 - y**2) ** 2
        ),
        "beta_restriction_determinant": (
            det_beta_times_four == -A * B * (E**2 - x**2) ** 2
        ),
    }
    assert all(checks.values())
    return checks


def q_and_gysin_checks():
    # Total-energy normal expansion: variables are x, y, E and z=E-x-y.
    nvars = 3
    x, y, E = (Poly.variable(nvars, index) for index in range(nvars))
    z = E - x - y
    A = (x - y) ** 2 - z**2
    B = (x + y) ** 2 - z**2
    Q = 4 * A * B - (A + B - E**2) ** 2
    Q_expected = (
        -16 * x**2 * y**2
        - 8 * x * y * E**2
        + 8 * (x + y) * E**3
        - 5 * E**4
    )

    # Clear denominators in R_infinity(v_alg).
    c7 = (x**2 - y**2) * (x**2 * y**2 - E**4)
    c8 = 2 * x**2 * (E**2 + y**2)
    c9 = -2 * y**2 * (E**2 + x**2)
    gysin_row_one_times_two = (
        2 * c7 + (E**2 + y**2) * c8 + (E**2 + x**2) * c9
    )
    gysin_row_two_times_2y2 = (
        -y**2 * (E**2 + x**2) * c8
        - x**2 * (E**2 + y**2) * c9
    )

    checks = {
        "Q_total_energy_expansion": Q == Q_expected,
        "Q_first_normal_grade_zero": all(
            exponents[2] != 1 for exponents in Q.terms
        ),
        "Q_second_normal_grade": Q.terms.get((1, 1, 2)) == -8,
        "Gysin_kernel_row_one": gysin_row_one_times_two == 0,
        "Gysin_kernel_row_two": gysin_row_two_times_2y2 == 0,
    }
    assert all(checks.values())
    return checks


def slice_checks():
    nvars = 1
    lam = Poly.variable(nvars, 0)
    x, y, z = 2 * lam, lam, Poly.constant(nvars, 1)
    E = x + y + z
    A = (x - y) ** 2 - z**2
    B = (x + y) ** 2 - z**2
    Q = 4 * A * B - (A + B - E**2) ** 2
    expected = (
        35 * lam**4 + 12 * lam**3 - 70 * lam**2 - 36 * lam - 5
    )
    derivative_expected = (lam**2 - 1) * (140 * lam + 36)

    lo, hi = 1.0, 2.0
    for _ in range(100):
        midpoint = (lo + hi) / 2
        if expected.evaluate((midpoint,)) > 0:
            hi = midpoint
        else:
            lo = midpoint
    root = (lo + hi) / 2

    checks = {
        "Q_slice_polynomial": Q == expected,
        "Q_slice_derivative": Q.derivative(0) == derivative_expected,
        "P_at_1": expected.evaluate((1,)),
        "P_at_2": expected.evaluate((2,)),
        "unique_simple_root_interval": [1, 2],
        "root_approximation": root,
        "nonvanishing_factors_at_root": {
            "A": root**2 - 1,
            "B": 9 * root**2 - 1,
            "E2_minus_x2": (3 * root + 1) ** 2 - 4 * root**2,
            "E2_minus_y2": (3 * root + 1) ** 2 - root**2,
            "H": (
                (3 * root + 1) ** 2 * (4 * root**2 + 6 * root + 2)
                + 4 * root**4
            ),
        },
    }
    assert checks["Q_slice_polynomial"]
    assert checks["Q_slice_derivative"]
    assert checks["P_at_1"] == -64
    assert checks["P_at_2"] == 299
    assert all(value > 0 for value in checks["nonvanishing_factors_at_root"].values())
    return checks


def legendre_normalization_checks():
    # Variables are a and lambda.  Standard Legendre equation:
    # m(1-m)u_mm + (1-2m)u_m - u/4 = 0.
    nvars = 2
    a, lam = (Poly.variable(nvars, index) for index in range(nvars))
    one = Poly.constant(nvars, 1)
    A = (a - 1) ** 2 * lam**2 - 1
    B = (a + 1) ** 2 * lam**2 - 1

    def transformed_p(modulus_numerator, modulus_denominator, twist_divisor):
        m = Rat(modulus_numerator, modulus_denominator)
        m_prime = m.derivative(1)
        m_second = m_prime.derivative(1)
        legendre_p = (1 - 2 * m) / (m * (1 - m))
        # f=twist_divisor^(-1/2)u(m); the coefficient receives D'/D.
        return (
            legendre_p * m_prime
            - m_second / m_prime
            + Rat(twist_divisor.derivative(1), twist_divisor)
        )

    published_numerator = 5 * A * B + 2 * (A + B)
    published_p = Rat(published_numerator, lam * A * B)
    wrong_pair_numerator = 5 * A * B + 4 * A
    wrong_pair_p = Rat(wrong_pair_numerator, lam * A * B)

    B_twist_A_over_B = transformed_p(A, B, B)
    B_twist_B_over_A = transformed_p(B, A, B)
    A_twist_B_over_A = transformed_p(B, A, A)

    checks = {
        "B_twist_with_A_over_B_matches_published_L2": (
            B_twist_A_over_B == published_p
        ),
        "B_twist_with_B_over_A_fails_published_L2": not (
            B_twist_B_over_A == published_p
        ),
        "B_twist_with_B_over_A_gives_trial_coefficient": (
            B_twist_B_over_A == wrong_pair_p
        ),
        "A_twist_with_B_over_A_matches_published_L2": (
            A_twist_B_over_A == published_p
        ),
        "trial_minus_published_numerator": (
            wrong_pair_numerator - published_numerator == 2 * (A - B)
        ),
    }
    assert all(checks.values())
    return checks


def main():
    packet = {
        "status": "proved_exact_identities",
        "compactification": compactification_checks(),
        "Q_and_Gysin": q_and_gysin_checks(),
        "generic_Q_slice": slice_checks(),
        "Legendre_normalization": legendre_normalization_checks(),
        "interpretive_boundary": [
            "The determinant identities plus the coordinate-case analysis in the ledger show that the absolute compactified pair is smooth at the exhibited generic Q root.",
            "A rank-one rational gauge shifts logarithmic residues by integers and cannot turn trivial monodromy into the sign character of sqrt(-Q).",
            "The checks do not locate Q inside the marked/relative coefficient system.",
        ],
    }
    print(json.dumps(packet, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
