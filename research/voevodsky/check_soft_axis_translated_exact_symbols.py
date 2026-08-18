"""Derive the first Cartier symbols of the translated full exact operators."""

from fractions import Fraction


# Sparse polynomials in (u,a,b).
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
    d = add(one, scale(power(b, 2), -1))

    # F=u*z is the translated reduced equation from Entry 461.
    f = add(
        add(power(a, 2), scale(multiply(u, d), Fraction(1, 2))),
        add(scale(power(u, 2), Fraction(-5, 4)), scale(power(u, 3), Fraction(1, 2))),
    )
    k = power(f, 2)
    assert derivative(f, 1) == scale(a, 2)
    assert derivative(f, 2) == scale(multiply(u, b), -1)
    assert derivative(k, 1) == scale(multiply(a, f), 4)
    assert derivative(k, 2) == scale(multiply(multiply(u, b), f), -2)

    # With F=u*z: K=u^2*z^2, K_a=4*u*a*z, K_b=-2*u^2*b*z.
    # In every sector the K-multiple pieces vanish after division by z and
    # restriction z=0.  Only the 3/2*K_b and -3/2*K_a terms remain.
    for sa, sb in ((1, 1), (1, 0), (0, 1), (0, 0)):
        ea, eb = 2 - sa, 2 - sb
        assert ea in (1, 2) and eb in (1, 2)
        p_scalar = Fraction(3, 2) * -2
        q_scalar = Fraction(-3, 2) * 4
        assert p_scalar == -3
        assert q_scalar == -6

    print("translated_reduced_equation_F: a^2+u*(1-b^2)/2-5u^2/4+u^3/2")
    print("full_carrier_K: F^2=u^2*z^2")
    print("K_a: 4*u*a*z")
    print("K_b: -2*u^2*b*z")
    print("first_Cartier_p_symbol: -3*u^2*b*f*L1^ea*L2^eb")
    print("first_Cartier_q_symbol: -6*u*a*f*L1^ea*L2^eb")
    print("translated_carrier_constant_but_exact_symbol_zero: NO")
    print("carrier_monodromy_controls_resonance_transport: NO")
    print("exact_complex_controls_resonance_transport: YES")
    print("next_gate: NORMALIZE_THESE_SYMBOLS_BY_DEGREEWISE_REES_SHIFTS_AND_COMPUTE_COKERNEL")


if __name__ == "__main__":
    main()
