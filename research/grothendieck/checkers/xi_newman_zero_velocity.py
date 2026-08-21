"""Exact simple-zero velocity and spectral-heat derivative under backward heat flow."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    z, lam, t = sp.symbols("z lambda t", real=True)
    gamma = sp.Function("gamma")(lam)
    hz, hzz = sp.symbols("H_z H_zz", nonzero=True)

    # Implicit differentiation of H_lambda(gamma(lambda))=0 with
    # partial_lambda H=-partial_z^2 H gives gamma'=H_zz/H_z.
    gamma_velocity = hzz / hz
    heat_atom_derivative = sp.simplify(
        sp.diff(sp.exp(-t * gamma**2), lam).subs(sp.diff(gamma, lam), gamma_velocity)
    )
    expected_heat_derivative = -2 * t * gamma * gamma_velocity * sp.exp(-t * gamma**2)
    assert sp.simplify(heat_atom_derivative - expected_heat_derivative) == 0

    # Hostile finite model: two positive zero pairs +/-a, +/-b.
    a, b = sp.symbols("a b", positive=True)
    polynomial = (z**2 - a**2) * (z**2 - b**2)
    velocity_a = sp.factor(sp.diff(polynomial, z, 2).subs(z, a) / sp.diff(polynomial, z).subs(z, a))
    velocity_b = sp.factor(sp.diff(polynomial, z, 2).subs(z, b) / sp.diff(polynomial, z).subs(z, b))
    assert sp.simplify(velocity_a - (5 * a**2 - b**2) / (a * (a**2 - b**2))) == 0
    assert sp.simplify(velocity_b - (5 * b**2 - a**2) / (b * (b**2 - a**2))) == 0

    # The inner-zero velocity changes sign at b=sqrt(5)*a.
    assert sp.simplify(velocity_a.subs(b, 2 * a)) < 0
    assert sp.simplify(velocity_a.subs(b, 3 * a)) > 0

    print("simple_zero_velocity=H_zz/H_z")
    print("spectral_heat_lambda_derivative=-2*t*sum(gamma*gamma_prime*exp(-t*gamma^2))")
    print(f"two_pair_inner_velocity={velocity_a}")
    print(f"two_pair_outer_velocity={velocity_b}")
    print("inner_velocity_sign_fixed=False")
    print("spectral_heat_monotonicity_automatic=False")


if __name__ == "__main__":
    main()
