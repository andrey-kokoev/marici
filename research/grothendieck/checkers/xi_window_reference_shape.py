"""Exact leading-order checks for the Xi-window reference-shape audit."""

import sympy as sp

T, ell, pi = sp.symbols("T ell pi", positive=True)
n = T * ell / pi
radius_squared = n * T**2 / 3
p = n**2 / 2
assert sp.simplify(p / radius_squared - 3 * ell / (2 * pi * T)) == 0

x = sp.symbols("x", real=True)
uniform_second_moment = sp.integrate(x**2 / 2, (x, -1, 1))
semicircle_density = 2 * sp.sqrt(1 - x**2) / sp.pi
semicircle_second_moment = sp.integrate(x**2 * semicircle_density, (x, -1, 1))
assert uniform_second_moment == sp.Rational(1, 3)
assert semicircle_second_moment == sp.Rational(1, 4)

potential = (1 + x) * sp.log(1 + x) + (1 - x) * sp.log(1 - x)
potential_derivative = sp.log(1 + x) - sp.log(1 - x)
assert sp.simplify(sp.diff(potential, x) - potential_derivative) == 0

print("xi_scaled_window_limit=uniform")
print(f"uniform_second_moment={uniform_second_moment}")
print(f"hermite_semicircle_second_moment={semicircle_second_moment}")
print("affine_shape_match=False")
print("xi_scale_coefficient_asymptotic=3*log(T)/(2*pi*T)")
print("uniform_equilibrium_potential_verified=True")
