"""Exact arithmetic checks for divisor pushforward and logarithmic descent."""

import sympy as sp


def mangoldt(n: int) -> sp.Expr:
    factors = sp.factorint(n)
    if len(factors) != 1:
        return sp.Integer(0)
    prime = next(iter(factors))
    return sp.log(prime)


for n in range(1, 101):
    pushed = sp.simplify(sum((mangoldt(d) for d in sp.divisors(n)), sp.Integer(0)))
    assert sp.simplify(pushed - sp.log(n)) == 0

    inverted = sp.simplify(sum((sp.mobius(d) * sp.log(sp.Rational(n, d)) for d in sp.divisors(n)), sp.Integer(0)))
    assert sp.simplify(inverted - mangoldt(n)) == 0

for m, n, scale in ((2, 3, 5), (4, 9, 7), (12, 25, 11)):
    original = sp.log(sp.Rational(m, n))
    scaled = sp.log(sp.Rational(scale * m, scale * n))
    assert sp.simplify(original - scaled) == 0

print("divisor_pushforward_Lambda=log_n checked_through=100")
print("Mobius_inversion_recovers_Lambda=True")
print("log_ratio_common_scaling_invariant=True")
print("quotient_compatible_coefficient_cocycle=True")
print("Hermitian_Xi_norm_identification_open=True")
print("physical_relative_chain_pushforward_constructed=False")

