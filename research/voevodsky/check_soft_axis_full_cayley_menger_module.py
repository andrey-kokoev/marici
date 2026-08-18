"""Construct the full soft-axis Cayley--Menger quotient before support loading."""

from fractions import Fraction


def add(first, second):
    result = dict(first)
    for monomial, coefficient in second.items():
        result[monomial] = result.get(monomial, Fraction(0)) + coefficient
    return {m: c for m, c in result.items() if c}


def scale(polynomial, coefficient):
    return {m: coefficient * c for m, c in polynomial.items() if coefficient * c}


def multiply(first, second):
    result = {}
    for left, a in first.items():
        for right, b in second.items():
            monomial = tuple(x + y for x, y in zip(left, right))
            result[monomial] = result.get(monomial, Fraction(0)) + a * b
    return {m: c for m, c in result.items() if c}


def power(polynomial, exponent):
    result = {(0, 0, 0): Fraction(1)}
    for _ in range(exponent):
        result = multiply(result, polynomial)
    return result


def derivative_u(polynomial):
    return {
        (u_degree - 1, a_degree, b_degree): coefficient * u_degree
        for (u_degree, a_degree, b_degree), coefficient in polynomial.items()
        if u_degree
    }


def specialize_u_zero(polynomial):
    return {
        (0, a_degree, b_degree): coefficient
        for (u_degree, a_degree, b_degree), coefficient in polynomial.items()
        if u_degree == 0
    }


def reduce_a(polynomial, relation_tail):
    """Reduce modulo a^4 + relation_tail using its unit leading coefficient."""
    result = dict(polynomial)
    while result and max(a_degree for _, a_degree, _ in result) >= 4:
        monomial = max((m for m in result if m[1] >= 4), key=lambda m: m[1])
        coefficient = result.pop(monomial)
        u_degree, a_degree, b_degree = monomial
        multiplier = {(u_degree, a_degree - 4, b_degree): -coefficient}
        result = add(result, multiply(multiplier, relation_tail))
    return result


def main():
    one = {(0, 0, 0): Fraction(1)}
    u = {(1, 0, 0): Fraction(1)}
    a = {(0, 1, 0): Fraction(1)}
    b = {(0, 0, 1): Fraction(1)}
    square = lambda polynomial: multiply(polynomial, polynomial)

    # Frozen chart X1=1, X2=u, v=2 used by the exact-form soft-axis audit.
    x = one
    y = scale(u, Fraction(1, 2))
    z = add(scale(u, Fraction(1, 2)), scale(one, -1))
    c = scale(u, -1)
    h = add(add(square(x), square(y)), scale(square(z), -1))
    ga = add(
        multiply(add(square(x), scale(square(c), -1)), add(add(square(x), scale(square(y), -1)), scale(square(z), -1))),
        scale(multiply(square(c), square(z)), -2),
    )
    gb = add(
        multiply(add(square(y), scale(square(c), -1)), add(add(square(y), scale(square(x), -1)), scale(square(z), -1))),
        scale(multiply(square(c), square(z)), -2),
    )
    hh = multiply(
        square(z),
        add(
            multiply(add(square(c), scale(square(y), -1)), add(square(c), scale(square(x), -1))),
            multiply(square(c), square(z)),
        ),
    )
    cayley_menger = {}
    for coefficient, monomial in (
        (square(x), power(a, 4)),
        (scale(h, -1), multiply(power(a, 2), power(b, 2))),
        (square(y), power(b, 4)),
        (ga, power(a, 2)),
        (gb, power(b, 2)),
        (hh, one),
    ):
        cayley_menger = add(cayley_menger, multiply(coefficient, monomial))

    assert cayley_menger[(0, 4, 0)] == 1
    assert all(a_degree <= 4 for _, a_degree, _ in cayley_menger)
    assert specialize_u_zero(cayley_menger) == {(0, 4, 0): Fraction(1)}

    first_normal = specialize_u_zero(derivative_u(cayley_menger))
    assert first_normal == {
        (0, 2, 0): Fraction(1),
        (0, 2, 2): Fraction(-1),
    }
    assert first_normal != {}

    leading = {(0, 4, 0): Fraction(1)}
    relation_tail = add(cayley_menger, scale(leading, -1))
    normal_forms = [reduce_a(power(a, exponent), relation_tail) for exponent in range(13)]
    assert all(all(a_degree < 4 for _, a_degree, _ in form) for form in normal_forms)
    assert normal_forms[:4] == [power(a, exponent) for exponent in range(4)]
    assert reduce_a(cayley_menger, relation_tail) == {}

    # Coefficientwise d/du does not descend to the quotient: it sends the
    # defining relation to a nonzero class at u=0. A Gauss--Manin correction
    # must therefore be derived from the relative de Rham geometry.
    assert reduce_a(first_normal, {}) == first_normal

    print("soft_axis_full_CM_relation_degree_in_a: 4_MONIC")
    print("soft_axis_special_fiber_relation: a^4")
    print("soft_axis_first_normal_relation: a^2*(1-b^2)")
    print("full_CM_quotient_basis_over_Q[u,b]: 1,a,a^2,a^3")
    print("full_CM_quotient_flat_rank_over_soft_base: 4")
    print("first_order_deformation: NONTRIVIAL")
    print("coefficientwise_soft_derivative_on_quotient: DOES_NOT_DESCEND")
    print("relative_Gauss_Manin_correction: REQUIRED")
    print("identification_with_exact_form_cokernel: NOT_YET_PROVED")
    print("physical_relative_support_class: NOT_YET_CONSTRUCTED")


if __name__ == "__main__":
    main()
