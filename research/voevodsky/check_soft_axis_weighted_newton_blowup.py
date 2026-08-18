"""Determine the Newton-adapted blowup of the full soft Cayley--Menger quartic."""

from fractions import Fraction


# Monomials are indexed by (u-degree, a-degree, b-degree).
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


def initial_form(weight_u, weight_a):
    weights = {
        monomial: weight_u * monomial[0] + weight_a * monomial[1]
        for monomial in K
    }
    minimum = min(weights.values())
    return minimum, {m: K[m] for m, weight in weights.items() if weight == minimum}


def substitute_u_equals_a_power_s(power):
    # Return exponents (a-degree, s-degree, b-degree).
    return {
        (a_degree + power * u_degree, u_degree, b_degree): coefficient
        for (u_degree, a_degree, b_degree), coefficient in K.items()
    }


def exceptional_after_division(transformed, exceptional_order):
    return {
        (s_degree, b_degree): coefficient
        for (a_degree, s_degree, b_degree), coefficient in transformed.items()
        if a_degree == exceptional_order
    }


def main():
    ordinary_order, ordinary_initial = initial_form(1, 1)
    assert ordinary_order == 2
    assert ordinary_initial == {
        (2, 0, 0): Fraction(1, 4),
        (2, 0, 2): Fraction(-1, 2),
        (2, 0, 4): Fraction(1, 4),
    }
    ordinary_chart = substitute_u_equals_a_power_s(1)
    ordinary_exceptional = exceptional_after_division(ordinary_chart, 2)
    assert ordinary_exceptional == {
        (2, 0): Fraction(1, 4),
        (2, 2): Fraction(-1, 2),
        (2, 4): Fraction(1, 4),
    }

    weighted_order, weighted_initial = initial_form(2, 1)
    assert weighted_order == 4
    assert len(weighted_initial) == 6
    weighted_chart = substitute_u_equals_a_power_s(2)
    weighted_exceptional = exceptional_after_division(weighted_chart, 4)
    assert weighted_exceptional == {
        (0, 0): Fraction(1),
        (1, 0): Fraction(1),
        (1, 2): Fraction(-1),
        (2, 0): Fraction(1, 4),
        (2, 2): Fraction(-1, 2),
        (2, 4): Fraction(1, 4),
    }

    # Coefficient comparison proves the weighted initial form is the square
    # (a^2 + u(1-b^2)/2)^2. In the u=a^2*s chart the exceptional equation is
    # (1+s(1-b^2)/2)^2.
    square_coefficients = {
        (0, 0): Fraction(1),
        (1, 0): Fraction(1),
        (1, 2): Fraction(-1),
        (2, 0): Fraction(1, 4),
        (2, 2): Fraction(-1, 2),
        (2, 4): Fraction(1, 4),
    }
    assert weighted_exceptional == square_coefficients

    # At generic b^2 != 1 the reduced exceptional direction is unique;
    # multiplicity two must be retained by normalization/nearby cycles.
    for b in (0, 2, 3):
        direction = Fraction(-2, 1 - b * b)
        value = (1 + direction * Fraction(1 - b * b, 2)) ** 2
        assert value == 0

    print("ordinary_(u,a)_blowup_exceptional_order: 2")
    print("ordinary_exceptional_equation: s^2*(1-b^2)^2/4")
    print("ordinary_blowup_adapted_to_Newton_face: NO")
    print("Newton_weights: wt(a)=1,wt(u)=2")
    print("weighted_initial_form: (a^2+u*(1-b^2)/2)^2")
    print("source_derived_Rees_ideal: (u,a^2)")
    print("weighted_chart_exceptional_equation: (1+s*(1-b^2)/2)^2")
    print("generic_reduced_exceptional_section: s=-2/(1-b^2)")
    print("exceptional_section_multiplicity: 2")
    print("b_plus_minus_1_directions: REQUIRE_SEPARATE_CHART_OR_FURTHER_BLOWUP")
    print("next_gate: PULL_EXACT_COMPLEX_TO_WEIGHTED_REES_SPACE_AND_RETAIN_DOUBLE_SECTION")


if __name__ == "__main__":
    main()
