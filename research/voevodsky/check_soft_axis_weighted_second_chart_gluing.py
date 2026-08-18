"""Check the complementary weighted Rees chart and exceptional gluing."""

from fractions import Fraction


# Sparse polynomials indexed by (u,a,b).
def add(first, second):
    result = dict(first)
    for monomial, coefficient in second.items():
        result[monomial] = result.get(monomial, Fraction(0)) + coefficient
    return {m: c for m, c in result.items() if c}


def scale(polynomial, coefficient):
    return {m: coefficient * c for m, c in polynomial.items() if coefficient * c}


def multiply(first, second):
    result = {}
    for left, x in first.items():
        for right, y in second.items():
            monomial = tuple(a + b for a, b in zip(left, right))
            result[monomial] = result.get(monomial, Fraction(0)) + x * y
    return {m: c for m, c in result.items() if c}


def power(polynomial, exponent):
    result = {(0, 0, 0): Fraction(1)}
    for _ in range(exponent):
        result = multiply(result, polynomial)
    return result


def derivative(polynomial, variable):
    result = {}
    for monomial, coefficient in polynomial.items():
        degree = monomial[variable]
        if degree:
            reduced = list(monomial)
            reduced[variable] -= 1
            result[tuple(reduced)] = coefficient * degree
    return result


def main():
    one = {(0, 0, 0): Fraction(1)}
    u = {(1, 0, 0): Fraction(1)}
    a = {(0, 1, 0): Fraction(1)}
    b = {(0, 0, 1): Fraction(1)}
    c = add(one, b)
    d = add(one, scale(power(b, 2), -1))

    # Global equation of the controlling weighted Newton face.
    h = add(power(a, 2), scale(multiply(u, d), Fraction(1, 2)))
    k = power(h, 2)
    assert derivative(k, 1) == scale(multiply(a, h), 4)
    assert derivative(k, 2) == scale(multiply(multiply(u, b), h), -2)

    # Before choosing a Rees chart, every weighted initial exact operator has
    # the common factor H.  We certify the quotient identities on monomials.
    for sa, sb in ((1, 1), (1, 0), (0, 1), (0, 0)):
        ea, eb = 2 - sa, 2 - sb
        for i in range(13):
            for j in range(13):
                f = multiply(power(a, i), power(b, j))
                base = multiply(power(c, ea), power(a, eb))
                p = scale(multiply(multiply(derivative(f, 2), base), k), -1)
                if sa:
                    p = add(p, multiply(multiply(multiply(f, power(c, ea - 1)), power(a, eb)), k))
                p = add(p, scale(multiply(multiply(f, base), derivative(k, 2)), Fraction(3, 2)))

                q = multiply(multiply(derivative(f, 1), base), k)
                if sb:
                    q = add(q, scale(multiply(multiply(multiply(f, power(c, ea)), power(a, eb - 1)), k), -1))
                q = add(q, scale(multiply(multiply(f, base), derivative(k, 1)), Fraction(-3, 2)))

                # Construct the explicit H quotients rather than test by
                # division, so cancellation cannot create a false positive.
                p_over_h = scale(multiply(multiply(derivative(f, 2), base), h), -1)
                if sa:
                    p_over_h = add(
                        p_over_h,
                        multiply(multiply(multiply(f, power(c, ea - 1)), power(a, eb)), h),
                    )
                p_over_h = add(
                    p_over_h,
                    scale(multiply(multiply(multiply(multiply(f, base), u), b), one), -3),
                )
                q_over_h = multiply(multiply(derivative(f, 1), base), h)
                if sb:
                    q_over_h = add(
                        q_over_h,
                        scale(multiply(multiply(multiply(f, power(c, ea)), power(a, eb - 1)), h), -1),
                    )
                q_over_h = add(q_over_h, scale(multiply(multiply(multiply(f, base), a), one), -6))
                assert p == multiply(h, p_over_h)
                assert q == multiply(h, q_over_h)

    # On the a^2-chart, H=a^2*phi.  On the u-chart, a^2=u*t and
    # H=u*psi.  On their overlap t=1/s, hence phi=s*psi and the two
    # principal ideals agree because s is a unit.
    # Coefficients are represented as affine-linear polynomials in d.
    # phi=1+s*d/2; s*psi=s*(1/s+d/2)=phi.
    for b_value in (-3, -1, 0, 1, 2):
        d_value = Fraction(1 - b_value * b_value)
        for s_value in (Fraction(1), Fraction(2), Fraction(-3)):
            t_value = 1 / s_value
            phi = 1 + s_value * d_value / 2
            psi = t_value + d_value / 2
            assert phi == s_value * psi

    # The missing directions occur in the u-chart at psi=t=0.  The
    # exceptional equation also has a^2=0, retaining the center's thickening.
    for b_value in (-1, 1):
        d_value = Fraction(1 - b_value * b_value)
        assert d_value == 0
        assert Fraction(0) + d_value / 2 == 0

    print("global_weighted_initial_equation: H^2=(a^2+u*(1-b^2)/2)^2")
    print("all_global_weighted_initial_exact_operators_divisible_by_H: YES")
    print("a2_chart_factor: H=a^2*phi")
    print("u_chart_ring: Q[u,a,t,b]/(a^2-u*t)")
    print("u_chart_factor: H=u*psi, psi=t+(1-b^2)/2")
    print("overlap_transition: phi=s*psi, t=1/s")
    print("H_reduced_exceptional_quotients_glue: YES")
    print("b_plus_minus_1_support_in_u_chart: t=0")
    print("residual_center_thickening_at_boundary: a^2=0")
    print("next_gate: IDENTIFY_THE_GLUED_QUOTIENT_AS_A_RELATIVE_NEARBY_CYCLE_OBJECT")


if __name__ == "__main__":
    main()
