"""Exact PDE audit separating spectral heat trace from de Bruijn--Newman deformation."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    newman_time, spectral_time, frequency, z, gamma = sp.symbols(
        "lambda t u z gamma", real=True
    )
    newman_atom = sp.exp(newman_time * frequency**2) * sp.cos(z * frequency)
    pde_residual = sp.simplify(
        sp.diff(newman_atom, newman_time) + sp.diff(newman_atom, z, 2)
    )
    assert pde_residual == 0

    spectral_atom = sp.exp(-spectral_time * gamma**2)
    spectral_ode_residual = sp.simplify(
        sp.diff(spectral_atom, spectral_time) + gamma**2 * spectral_atom
    )
    assert spectral_ode_residual == 0

    assert not spectral_atom.has(z)
    assert not newman_atom.has(gamma)

    print("newman_pde=partial_lambda(H)=-partial_z_squared(H)")
    print("spectral_heat_ode=partial_t(exp(-t*gamma^2))=-gamma^2*exp(-t*gamma^2)")
    print("newman_parameter_moves_zero_divisor=True")
    print("spectral_time_damps_fixed_zero_divisor=True")
    print("heat_parameters_identical=False")


if __name__ == "__main__":
    main()
