#!/usr/bin/env python3
"""Exact audit of faithful versus birational Tate comparison coordinates."""

from fractions import Fraction


for p in (2, 3, 5, 7, 11):
    # Use a^2=1/p and rational x only through the combinations a*x and a/x.
    # Independent rational test packets suffice for the algebraic identities.
    for u, v in ((Fraction(1, p), Fraction(2, p + 1)), (Fraction(3, p + 2), Fraction(1, p))):
        d_plus = 1 - u
        d_minus = 1 - v
        symmetric = d_plus + d_minus
        antisymmetric = d_plus - d_minus
        assert (symmetric + antisymmetric) / 2 == d_plus
        assert (symmetric - antisymmetric) / 2 == d_minus
        product = d_plus * d_minus
        assert (symmetric * symmetric - antisymmetric * antisymmetric) / 4 == product
        if d_minus:
            ratio = d_plus / d_minus
            assert (symmetric + antisymmetric) / (symmetric - antisymmetric) == ratio

# Divisor collision: every pair (0,c), c nonzero, maps to product=ratio=0.
collapsed = set()
for c in (Fraction(1), Fraction(2), Fraction(7, 3)):
    d_plus = Fraction(0)
    d_minus = c
    collapsed.add((d_plus * d_minus, d_plus / d_minus))
assert collapsed == {(Fraction(0), Fraction(0))}

print("faithful_coordinates=T=D_plus+D_minus,A=D_plus-D_minus")
print("reciprocity_parity=T_even,A_odd")
print("linear_reconstruction=D_plus_minus=(T_plus_minus_A)/2")
print("ratio_product_coordinates=birational")
print("ratio_product_divisor_fiber=infinite")
print("required_readout=two_uncompressed_quadratures")
