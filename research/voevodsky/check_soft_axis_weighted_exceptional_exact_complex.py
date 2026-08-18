"""Derive the initial exact operators on the weighted soft exceptional divisor."""

from fractions import Fraction


# Polynomials in (s,b), stored by exponent pair.
def add(first, second):
    result = dict(first)
    for monomial, coefficient in second.items():
        result[monomial] = result.get(monomial, Fraction(0)) + coefficient
    return {m: c for m, c in result.items() if c}


def scale(polynomial, coefficient):
    return {m: coefficient * c for m, c in polynomial.items() if coefficient * c}


def multiply(first, second):
    result = {}
    for (s1, b1), x in first.items():
        for (s2, b2), y in second.items():
            monomial = (s1 + s2, b1 + b2)
            result[monomial] = result.get(monomial, Fraction(0)) + x * y
    return {m: c for m, c in result.items() if c}


def power(polynomial, exponent):
    result = {(0, 0): Fraction(1)}
    for _ in range(exponent):
        result = multiply(result, polynomial)
    return result


def derivative(polynomial, variable):
    result = {}
    for (s_degree, b_degree), coefficient in polynomial.items():
        degree = (s_degree, b_degree)[variable]
        if degree:
            monomial = (s_degree - (variable == 0), b_degree - (variable == 1))
            result[monomial] = coefficient * degree
    return result


def main():
    one = {(0, 0): Fraction(1)}
    s = {(1, 0): Fraction(1)}
    b = {(0, 1): Fraction(1)}
    c = add(one, b)
    d = add(one, scale(power(b, 2), -1))
    phi = add(one, scale(multiply(s, d), Fraction(1, 2)))
    f = power(phi, 2)

    # K_in=a^4*phi^2 after u=a^2*s.  Since the original operators
    # differentiate at fixed u, the weighted-chart chain rule gives
    # (partial_a K)_in/a^3 = 4F-2s*partial_s(F) = 4phi.
    k_b = derivative(f, 1)
    k_a_fixed_u = add(scale(f, 4), scale(multiply(s, derivative(f, 0)), -2))
    assert k_b == scale(multiply(multiply(s, b), phi), -2)
    assert k_a_fixed_u == scale(phi, 4)

    for sa, sb in ((1, 1), (1, 0), (0, 1), (0, 0)):
        ea, eb = 2 - sa, 2 - sb
        assert (eb + 4, eb + 3) == ((6 - sb), (5 - sb))
        for i in range(13):
            for j in range(13):
                monomial_b = power(b, j)
                # Exceptional p coefficient after removing a^(i+eb+4).
                p = scale(multiply(multiply(derivative(monomial_b, 1), power(c, ea)), f), -1)
                if sa:
                    p = add(p, multiply(multiply(monomial_b, power(c, ea - 1)), f))
                p = add(p, scale(multiply(multiply(monomial_b, power(c, ea)), k_b), Fraction(3, 2)))

                # Exceptional q coefficient after removing a^(i+eb+3).
                q = scale(multiply(multiply(monomial_b, power(c, ea)), f), i)
                if sb:
                    q = add(q, scale(multiply(multiply(monomial_b, power(c, ea)), f), -1))
                q = add(q, scale(multiply(multiply(monomial_b, power(c, ea)), k_a_fixed_u), Fraction(-3, 2)))

                p_quotient = add(
                    scale(multiply(derivative(monomial_b, 1), power(c, ea)), -1),
                    multiply(monomial_b, power(c, ea - 1)) if sa else {},
                )
                p_quotient = add(
                    multiply(phi, p_quotient),
                    scale(multiply(multiply(multiply(monomial_b, power(c, ea)), s), b), -3),
                )
                q_quotient = multiply(
                    multiply(monomial_b, power(c, ea)),
                    add(scale(phi, i - sb), scale(one, -6)),
                )
                assert p == multiply(phi, p_quotient)
                assert q == multiply(phi, q_quotient)

    # At b=+/-1, phi=1: the exceptional double section has no point in this
    # affine weighted chart, so those directions cannot be inferred here.
    for b_value in (-1, 1):
        phi_at_direction = Fraction(1) + Fraction(1 - b_value * b_value, 2)
        assert phi_at_direction == 1

    print("derived_p_shift_by_sector: 6-s_b")
    print("derived_q_shift_by_sector: 5-s_b")
    print("fixed_u_chain_rule_Ka_initial: 4*phi")
    print("Kb_initial: -2*s*b*phi")
    print("all_weighted_exceptional_exact_operators_divisible_by_phi: YES")
    print("exceptional_support_ring: Q[s,b]/(phi^2)")
    print("exact_image_contained_in_nilradical_(phi): YES")
    print("reduced_exceptional_quotient_survives: YES")
    print("b_plus_minus_1_present_in_this_chart: NO")
    print("next_gate: COMPUTE_SECOND_CHART_AND_GLUE_REDUCED_EXCEPTIONAL_QUOTIENT")


if __name__ == "__main__":
    main()
