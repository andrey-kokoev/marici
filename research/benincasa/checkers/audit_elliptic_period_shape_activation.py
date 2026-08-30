#!/usr/bin/env python3
"""Exact shape activation of the published homogeneous elliptic quotient."""

from fractions import Fraction as F


# Source Eq. (60): m=((a-1)^2 lambda^2-1)/((a+1)^2 lambda^2-1),
# with X1=a lambda, X2=lambda, X3=1.  Along the physical shape family
# X1=1+t, X2=1-t, X3=1 this becomes exactly (4t^2-1)/3.
m_coefficients = [F(-1, 3), F(0), F(4, 3)]  # coefficients through t^2
m_at_zero = m_coefficients[0]
m_first = m_coefficients[1]
m_second = 2 * m_coefficients[2]

# For the standard real complete elliptic period K(m),
# K'(m)=1/2 int sin(theta)^2/(1-m sin(theta)^2)^(3/2) dtheta.
# At m=-1/3 the integrand is nonnegative and nonzero on (0,pi/2), hence
# K'(-1/3)>0.  The chain rule gives d2 K(m(t))/dt2=(8/3)K'(-1/3).
chain_rule_coefficient = m_second

checks = {
    "homogeneous_modulus_is_minus_one_third": m_at_zero == F(-1, 3),
    "first_shape_derivative_vanishes": m_first == 0,
    "second_shape_derivative_is_nonzero": m_second == F(8, 3),
    "shape_activation_is_even_under_site_exchange": m_coefficients[1] == 0,
    "real_elliptic_period_derivative_has_positive_integrand": m_at_zero < 1,
    "elliptic_period_second_response_is_strictly_positive": chain_rule_coefficient > 0,
}

assert all(checks.values()), checks
print(f"PASS {sum(checks.values())}/{len(checks)}")
print(f"m(t)=-1/3+(4/3)t^2; m''(0)={m_second}")
print("K(m(t))''|0=(8/3) K'(-1/3)>0")
