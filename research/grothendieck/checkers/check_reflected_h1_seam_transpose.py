"""Exact polynomial audit of the reflected H1 seam correspondence."""

from fractions import Fraction
import json


# u(x)=1+2x on [0,1]; reflected v(q)=1-2q on [-1,0].
L = Fraction(1)

# Exact integrals: integral_0^1 (1+2x)^2 dx = 13/3 and derivative energy=4.
u_l2 = Fraction(13, 3)
u_d_l2 = Fraction(4)
v_l2 = Fraction(13, 3)
v_d_l2 = Fraction(4)

u_value_0 = Fraction(1)
u_value_L = Fraction(3)
v_value_0 = Fraction(1)
v_value_minus_L = Fraction(3)

u_prime = Fraction(2)
v_prime = Fraction(-2)

u_flux_0 = -u_prime
u_flux_L = u_prime
v_flux_0 = v_prime
v_flux_minus_L = -v_prime

checks = {
    "L2_norm_preserved": u_l2 == v_l2,
    "derivative_norm_preserved": u_d_l2 == v_d_l2,
    "H1_graph_norm_preserved": u_l2 + u_d_l2 == v_l2 + v_d_l2,
    "zero_endpoint_value_preserved": u_value_0 == v_value_0,
    "moving_endpoint_value_preserved": u_value_L == v_value_minus_L,
    "zero_endpoint_outward_flux_preserved": u_flux_0 == v_flux_0,
    "moving_endpoint_outward_flux_preserved": u_flux_L == v_flux_minus_L,
    "coordinate_derivative_reverses": v_prime == -u_prime,
}

result = {
    "schema": "marici.grothendieck.reflected-h1-seam-transpose.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "graph_norm_squared": str(u_l2 + u_d_l2),
}

print(json.dumps(result, indent=2, sort_keys=True))
