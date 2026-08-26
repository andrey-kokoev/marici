"""Exact rational audit of the primitive far-wall flux coefficient."""

from __future__ import annotations

from fractions import Fraction as Q


def add(*polynomials: dict[int, Q]) -> dict[int, Q]:
    result: dict[int, Q] = {}
    for polynomial in polynomials:
        for degree, coefficient in polynomial.items():
            result[degree] = result.get(degree, Q(0)) + coefficient
    return result


def multiply(left: dict[int, Q], right: dict[int, Q]) -> dict[int, Q]:
    result: dict[int, Q] = {}
    for left_degree, left_coefficient in left.items():
        for right_degree, right_coefficient in right.items():
            degree = left_degree + right_degree
            result[degree] = result.get(degree, Q(0)) + left_coefficient * right_coefficient
    return result


def scale(polynomial: dict[int, Q], scalar: Q) -> dict[int, Q]:
    return {degree: scalar * coefficient for degree, coefficient in polynomial.items()}


def rising(value: Q, order: int) -> Q:
    result = Q(1)
    for index in range(order):
        result *= value + index
    return result


def expectation(polynomial: dict[int, Q], order: int) -> Q:
    shape = Q(order + 1)
    return sum(coefficient * rising(shape, degree) for degree, coefficient in polynomial.items())


def main() -> None:
    # log(F(a+y/(2c))/F(a)) = -y + A1/c + A2/c^2 + A3/c^3 + O(c^-4).
    a1 = {1: Q(9, 4), 2: Q(-1, 2)}
    a2 = {1: Q(3, 2), 3: Q(-1, 6)}
    a3 = {1: Q(9, 4), 2: Q(-3, 4), 4: Q(-1, 24)}
    w1 = a1
    w2 = add(a2, scale(multiply(a1, a1), Q(1, 2)))
    w3 = add(a3, multiply(a1, a2), scale(multiply(multiply(a1, a1), a1), Q(1, 6)))

    def coefficients(order: int) -> tuple[Q, Q, Q]:
        return tuple(expectation(weight, order) for weight in (w1, w2, w3))

    def ratio_coefficients(order: int) -> tuple[Q, Q, Q]:
        a_1, a_2, a_3 = coefficients(order - 1)
        b_1, b_2, b_3 = coefficients(order)
        r1 = a_1 - b_1
        r2 = a_2 - a_1 * b_1 + b_1 * b_1 - b_2
        r3 = a_3 - a_2 * b_1 + a_1 * (b_1 * b_1 - b_2) - b_1**3 + 2 * b_1 * b_2 - b_3
        return r1, r2, r3

    signs = {4: Q(-1), 6: Q(3), 8: Q(-3), 10: Q(1)}
    combined = [sum(signs[k] * ratio_coefficients(k)[j] for k in signs) for j in range(3)]
    # h_k=2c(1+r1/c+r2/c^2+r3/c^3+...), so the first survivor is 2*combined[2]/c^2.
    assert combined == [Q(0), Q(0), Q(32)]
    assert 2 * combined[2] == 64
    print({
        "combined_ratio_coefficients": [str(value) for value in combined],
        "first_surviving_flux_derivative_coefficient": "64",
        "asymptotic": "Omega'(a)=64/c^2+O(c^-3)",
    })


if __name__ == "__main__":
    main()
