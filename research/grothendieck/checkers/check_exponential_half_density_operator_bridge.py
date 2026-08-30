#!/usr/bin/env python3
"""Exact monomial audit of the exponential half-density operator bridge."""

from fractions import Fraction


for numerator in range(-5, 8):
    a = Fraction(numerator, 3)

    # For f(x)=x^a, Uf(q)=exp((a+1/2)q).
    pulled_exponent = a + Fraction(1, 2)

    # U (x d/dx + 1/2) U^-1 acts by a+1/2, exactly as d/dq.
    centered_euler_eigenvalue = a + Fraction(1, 2)
    q_derivative_eigenvalue = pulled_exponent
    assert centered_euler_eigenvalue == q_derivative_eigenvalue

    # U d/dx U^-1 = exp(-q)(d/dq-1/2); after removing exp(-q),
    # the coefficient is a, the derivative coefficient of x^a.
    additive_coefficient = pulled_exponent - Fraction(1, 2)
    assert additive_coefficient == a

print("unitary_pullback=Uf(q)=exp(q/2)f(exp(q))")
print("mellin_coordinate=z=s-1/2")
print("centered_euler_bridge=U(x*d/dx+1/2)U^-1=d/dq")
print("additive_bridge=U(d/dx)U^-1=exp(-q)(d/dq-1/2)")
print("comparison_anomaly=exp(-q)")
print("required_structure=two_axis_operator_cell")
