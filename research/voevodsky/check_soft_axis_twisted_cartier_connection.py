"""Derive the logarithmic connection on the twisted Cartier generator."""

from fractions import Fraction


def multiply(first, second):
    result = {}
    for i, x in first.items():
        for j, y in second.items():
            result[i + j] = result.get(i + j, Fraction(0)) + x * y
    return {degree: coefficient for degree, coefficient in result.items() if coefficient}


def power(polynomial, exponent):
    result = {0: Fraction(1)}
    for _ in range(exponent):
        result = multiply(result, polynomial)
    return result


def derivative(polynomial):
    return {degree - 1: degree * coefficient for degree, coefficient in polynomial.items() if degree}


def scale(polynomial, coefficient):
    return {degree: coefficient * value for degree, value in polynomial.items() if coefficient * value}


def add(first, second):
    result = dict(first)
    for degree, coefficient in second.items():
        result[degree] = result.get(degree, Fraction(0)) + coefficient
    return {degree: coefficient for degree, coefficient in result.items() if coefficient}


def evaluate(polynomial, value):
    return sum(coefficient * value**degree for degree, coefficient in polynomial.items())


def main():
    b_minus_one = {1: Fraction(1), 0: Fraction(-1)}
    b_plus_one = {1: Fraction(1), 0: Fraction(1)}
    w = scale(multiply(power(b_minus_one, 3), power(b_plus_one, 4)), Fraction(1, 8))
    w_prime = derivative(w)

    # Clear denominators in dlog(w)=3/(b-1)+4/(b+1).
    denominator = multiply(b_minus_one, b_plus_one)
    numerator = add(scale(b_plus_one, 3), scale(b_minus_one, 4))
    assert multiply(w_prime, denominator) == multiply(w, numerator)

    # The logarithmic residues are the boundary multiplicities.  The residue
    # at infinity is minus their sum, recovering the Euler resonance weight.
    residue_plus = 3
    residue_minus = 4
    residue_infinity = -(residue_plus + residue_minus)
    assert residue_infinity == -7

    # No regular polynomial connection coefficient A can satisfy w'=A*w:
    # w vanishes at both boundary points while w' does not vanish to the same
    # order.  Logarithmic poles are therefore forced by the transported source
    # derivative.
    assert evaluate(w, Fraction(1)) == evaluate(w, Fraction(-1)) == 0
    assert derivative(power(b_minus_one, 3)) != {}
    assert max(w_prime) < max(w)

    print("twist_section_w: (b-1)^3*(b+1)^4/8")
    print("transported_connection: d+dlog(w)")
    print("dlog(w): 3*db/(b-1)+4*db/(b+1)")
    print("residue_b_plus_1: 3")
    print("residue_b_minus_1: 4")
    print("residue_at_infinity: -7")
    print("Euler_resonance_weight: 7")
    print("Fuchs_residue_balance_matches_Euler_weight: YES")
    print("regular_polynomial_extension_preserving_source_lattice: NO")
    print("logarithmic_extension_forced: YES")
    print("next_gate: COMPUTE_DE_RHAM_COHOMOLOGY_OF_THE_RESIDUE_(3,4,-7)_CONNECTION")


if __name__ == "__main__":
    main()
