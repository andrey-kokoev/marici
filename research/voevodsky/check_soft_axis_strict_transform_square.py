"""Factor the full Cayley--Menger relation on the weighted u-chart."""

from fractions import Fraction


# Full K from Entry 451, indexed by (u,a,b).
K = {
    (0, 4, 0): Fraction(1),
    (1, 2, 0): Fraction(1),
    (1, 2, 2): Fraction(-1),
    (2, 0, 0): Fraction(1, 4),
    (2, 0, 2): Fraction(-1, 2),
    (2, 0, 4): Fraction(1, 4),
    (2, 2, 0): Fraction(-5, 2),
    (3, 0, 0): Fraction(-5, 4),
    (3, 0, 2): Fraction(5, 4),
    (3, 2, 0): Fraction(1),
    (4, 0, 0): Fraction(33, 16),
    (4, 0, 2): Fraction(-1, 2),
    (5, 0, 0): Fraction(-5, 4),
    (6, 0, 0): Fraction(1, 4),
}


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


def main():
    # New indices are (u,t,b), using a^2=u*t and dividing by u^2.
    strict_transform = {}
    for (u_degree, a_degree, b_degree), coefficient in K.items():
        assert a_degree % 2 == 0
        transformed = (u_degree + a_degree // 2 - 2, a_degree // 2, b_degree)
        assert transformed[0] >= 0
        strict_transform[transformed] = strict_transform.get(transformed, Fraction(0)) + coefficient

    one = {(0, 0, 0): Fraction(1)}
    u = {(1, 0, 0): Fraction(1)}
    t = {(0, 1, 0): Fraction(1)}
    b2 = {(0, 0, 2): Fraction(1)}
    psi = add(t, scale(add(one, scale(b2, -1)), Fraction(1, 2)))
    translated_coordinate = add(add(psi, scale(u, Fraction(-5, 4))), {(2, 0, 0): Fraction(1, 2)})
    square = multiply(translated_coordinate, translated_coordinate)
    assert strict_transform == square

    # Translation by a polynomial in u is an automorphism over the u-base;
    # it identifies the full family with the constant doubled section z^2=0.
    special_translation = add(translated_coordinate, scale(psi, -1))
    assert special_translation == {(1, 0, 0): Fraction(-5, 4), (2, 0, 0): Fraction(1, 2)}

    print("full_u_chart_strict_transform: (psi-5u/4+u^2/2)^2")
    print("translated_coordinate: z=psi-5u/4+u^2/2")
    print("family_after_translation: z^2=0")
    print("carrier_family_over_u: ALGEBRAICALLY_TRIVIAL_DOUBLE_SECTION")
    print("reduced_carrier_monodromy: IDENTITY")
    print("standard_nearby_cycles_detect_nilpotent_thickening: NO")
    print("nontrivial_resonance_transport_must_come_from_exact_complex: YES")
    print("next_gate: CONJUGATE_THE_FULL_EXACT_OPERATORS_BY_THE_CARRIER_TRANSLATION")


if __name__ == "__main__":
    main()
