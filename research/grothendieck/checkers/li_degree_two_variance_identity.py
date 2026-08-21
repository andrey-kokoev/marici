"""Exact moment/variance meaning of the degree-two Li positivity channels."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    mass, first, second = sp.symbols("M m_1 m_2", real=True)
    c0 = mass
    c1 = first
    # cos(2 theta)=2 cos(theta)^2-1.
    c2 = 2 * second - mass

    odd = sp.factor(c0 - c2)
    coupled = sp.factor(c0 * (c0 + c2) - 2 * c1**2)

    expected_odd = 2 * (mass - second)
    expected_coupled = 2 * (mass * second - first**2)
    assert sp.expand(odd - expected_odd) == 0
    assert sp.expand(coupled - expected_coupled) == 0

    mean = first / mass
    variance = second / mass - mean**2
    assert sp.simplify(coupled - 2 * mass**2 * variance) == 0

    print("odd_channel=2*integral(sin(theta)^2)dmu")
    print("coupled_channel=2*M^2*variance_mu_normalized(cos(theta))")
    print("odd_identity_residual=0")
    print("variance_identity_residual=0")
    print("coupled_equality_condition=cos(theta)_constant_mu_almost_everywhere")


if __name__ == "__main__":
    main()
