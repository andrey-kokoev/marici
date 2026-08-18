"""Determine the first-order Gauss--Manin lift obstruction at the soft fibre."""

from fractions import Fraction


def add(first, second):
    result = dict(first)
    for monomial, coefficient in second.items():
        result[monomial] = result.get(monomial, Fraction(0)) + coefficient
    return {m: c for m, c in result.items() if c}


def multiply(first, second):
    result = {}
    for (a1, b1), x in first.items():
        for (a2, b2), y in second.items():
            monomial = (a1 + a2, b1 + b2)
            result[monomial] = result.get(monomial, Fraction(0)) + x * y
    return {m: c for m, c in result.items() if c}


def scale(polynomial, coefficient):
    return {m: coefficient * c for m, c in polynomial.items() if coefficient * c}


def reduce_mod_a_power(polynomial, power):
    return {m: c for m, c in polynomial.items() if m[0] < power}


def main():
    # Entry 447 gives K_0=a^4 and dK/du|_0=a^2(1-b^2).
    k0 = {(4, 0): Fraction(1)}
    k_a = {(3, 0): Fraction(4)}
    k_b = {}
    k_u = {(2, 0): Fraction(1), (2, 2): Fraction(-1)}

    # The first-order deformation class lies in the hypersurface T1 module.
    # Since (K_0,K_a,K_b)=(a^3), reduction modulo the Jacobian ideal leaves a
    # nonzero class a^2(1-b^2), killed by multiplication by a.
    t1_class = reduce_mod_a_power(k_u, 3)
    assert t1_class == k_u
    assert t1_class != {}
    a = {(1, 0): Fraction(1)}
    assert reduce_mod_a_power(multiply(a, t1_class), 3) == {}

    # No regular polynomial vertical field V d/da + W d/db can lift d/du:
    # V*K_a has a-order at least three and W*K_b=0, whereas K_u has order two.
    regular_jacobian_orders = {monomial[0] for monomial in k_a}
    deformation_orders = {monomial[0] for monomial in k_u}
    assert min(regular_jacobian_orders) == 3
    assert min(deformation_orders) == 2

    # The unique lowest-a-order cancellation is meromorphic:
    # V=(b^2-1)/(4a), for which K_u+V*K_a=0.
    meromorphic_v = {(-1, 2): Fraction(1, 4), (-1, 0): Fraction(-1, 4)}
    assert add(k_u, multiply(meromorphic_v, k_a)) == {}
    assert min(a_degree for a_degree, _ in meromorphic_v) == -1

    # The obstruction vanishes only on the two coefficient directions b=+/-1.
    def evaluate_b(polynomial, value):
        result = {}
        for (a_degree, b_degree), coefficient in polynomial.items():
            result[a_degree] = result.get(a_degree, Fraction(0)) + coefficient * value**b_degree
        return {degree: coefficient for degree, coefficient in result.items() if coefficient}

    assert evaluate_b(t1_class, 1) == {}
    assert evaluate_b(t1_class, -1) == {}
    assert evaluate_b(t1_class, 0) == {2: Fraction(1)}

    print("soft_fiber_hypersurface_Jacobian_ideal: (a^3)")
    print("first_Kodaira_Spencer_class: [a^2*(1-b^2)]_mod_a^3")
    print("first_Kodaira_Spencer_class_nonzero: YES")
    print("first_Kodaira_Spencer_class_annihilator_contains: a")
    print("regular_polynomial_Gauss_Manin_lift: IMPOSSIBLE")
    print("minimal_vertical_correction: (b^2-1)/(4a)*d_da")
    print("minimal_correction_pole_order_along_a0: 1")
    print("exceptional_coefficient_directions_b_plus_minus_1: OBSTRUCTION_ZERO")
    print("next_gate: BLOW_UP_MIXED_IDEAL_(u,a)_AND_DERIVE_LOG_RELATIVE_CONNECTION")


if __name__ == "__main__":
    main()
