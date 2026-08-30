"""Exact symmetric principal-part decomposition of Li rational-square tests."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    s, z = sp.symbols("s z")
    u = (s - 1) / s

    for degree in range(0, 7):
        coefficients = sp.symbols(f"a0:{degree + 1}")
        polynomial = sum(coefficients[j] * z**j for j in range(degree + 1))
        test = sp.cancel(
            polynomial.subs(z, u)
            * polynomial.subs(z, 1 / u)
            / (s * (1 - s))
        )

        # Coefficients of the principal part at zero.
        scaled = sp.cancel(s ** (degree + 1) * test)
        principal = []
        for k in range(1, degree + 2):
            derivative_order = degree + 1 - k
            coefficient = sp.simplify(
                sp.diff(scaled, s, derivative_order).subs(s, 0)
                / sp.factorial(derivative_order)
            )
            principal.append(coefficient)

        reconstruction = sum(
            principal[k - 1] * (s ** (-k) + (1 - s) ** (-k))
            for k in range(1, degree + 2)
        )
        residual = sp.cancel(test - reconstruction)
        assert residual == 0

        jets = sp.symbols(f"ell0:{degree + 1}")
        local_log_derivative = sum(jets[j] * s**j for j in range(degree + 1))
        residue = sp.residue(test * local_log_derivative, s, 0)
        jet_pairing = sum(
            principal[k - 1] * jets[k - 1] for k in range(1, degree + 2)
        )
        assert sp.simplify(residue - jet_pairing) == 0

        print(
            f"degree={degree} basis_size={degree + 1} "
            "reconstruction_residual=0 residue_jet_residual=0"
        )

    print("unique_symmetric_principal_part_basis=True")
    print("basis_element_k=s^-k+(1-s)^-k")
    print("pair_normalized_energy=-sum_k(A_k*L_jet_(k-1))")


if __name__ == "__main__":
    main()
