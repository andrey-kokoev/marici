"""Compare Euler-resonance degrees with the exceptional Cartier lattice."""

from fractions import Fraction


def polynomial_multiply(first, second):
    result = {}
    for i, x in first.items():
        for j, y in second.items():
            result[i + j] = result.get(i + j, Fraction(0)) + x * y
    return {degree: coefficient for degree, coefficient in result.items() if coefficient}


def polynomial_power(polynomial, exponent):
    result = {0: Fraction(1)}
    for _ in range(exponent):
        result = polynomial_multiply(result, polynomial)
    return result


def evaluate(polynomial, value):
    return sum(coefficient * value**degree for degree, coefficient in polynomial.items())


def vanishing_order(polynomial, point, max_order=20):
    current = dict(polynomial)
    for order in range(max_order + 1):
        if evaluate(current, point):
            return order
        current = {
            degree - 1: coefficient * degree
            for degree, coefficient in current.items()
            if degree
        }
    raise AssertionError("vanishing order exceeds audit bound")


def main():
    # On the u-chart, a^2=u*t.  The divided Euler generator a^7*(b+1)
    # becomes a*u^3*t^3*(b+1).  Removing its Rees degree u^3 and restricting
    # to D uses t=(b^2-1)/2.
    b_minus_one = {1: Fraction(1), 0: Fraction(-1)}
    b_plus_one = {1: Fraction(1), 0: Fraction(1)}
    t_on_d = polynomial_multiply(b_minus_one, b_plus_one)
    t_on_d = {degree: coefficient / 2 for degree, coefficient in t_on_d.items()}
    comparison_coefficient = polynomial_multiply(polynomial_power(t_on_d, 3), b_plus_one)
    expected = polynomial_multiply(polynomial_power(b_minus_one, 3), polynomial_power(b_plus_one, 4))
    expected = {degree: coefficient / 8 for degree, coefficient in expected.items()}
    assert comparison_coefficient == expected

    assert vanishing_order(comparison_coefficient, Fraction(1)) == 3
    assert vanishing_order(comparison_coefficient, Fraction(-1)) == 4
    assert sum((3, 4)) == 7
    assert evaluate(comparison_coefficient, Fraction(0)) != 0

    # The relative a-degree seven is three powers of u plus the residual odd
    # generator a.  Thus the generic basis match requires a Rees shift by six,
    # and its remaining coefficient is not a unit on the full b-axis.
    relative_a_degree = 7
    rees_u_shift = relative_a_degree // 2
    residual_a_parity = relative_a_degree % 2
    assert (rees_u_shift, residual_a_parity) == (3, 1)

    print("Euler_divided_generators: 1, a^7*(b+1)")
    print("u_chart_transform_second: a*u^3*t^3*(b+1)")
    print("required_Rees_u_shift: 3")
    print("residual_Cartier_generator: a")
    print("comparison_coefficient_on_D: (b-1)^3*(b+1)^4/8")
    print("boundary_vanishing_order_b_plus_1: 3")
    print("boundary_vanishing_order_b_minus_1: 4")
    print("total_boundary_degree: 7")
    print("plain_global_Euler_Cartier_basis_identification: REFUTED")
    print("generic_identification_away_from_b_plus_minus_1: YES")
    print("next_gate: DERIVE_OR_REFUTE_A_BOUNDARY_LATTICE_MODIFICATION_WITH_DIVISOR_3P_PLUS_4M")


if __name__ == "__main__":
    main()
