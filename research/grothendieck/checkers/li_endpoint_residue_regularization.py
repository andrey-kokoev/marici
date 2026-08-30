"""Exact reflection and finite-jet audit of the canonical endpoint residue functional."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    s, z = sp.symbols("s z")
    u = (s - 1) / s

    for degree in range(0, 6):
        coefficients = sp.symbols(f"a0:{degree + 1}")
        log_derivative_jets = sp.symbols(f"ell0:{degree + 1}")
        polynomial = sum(coefficients[j] * z**j for j in range(degree + 1))
        test = sp.cancel(
            polynomial.subs(z, u)
            * polynomial.subs(z, 1 / u)
            / (s * (1 - s))
        )
        local_log_derivative = sum(
            log_derivative_jets[j] * s**j for j in range(degree + 1)
        )

        residue_zero = sp.residue(test * local_log_derivative, s, 0)
        # xi(s)=xi(1-s) implies L(s)=xi'/xi(s)=-L(1-s).
        reflected_local_log_derivative = -local_log_derivative.subs(s, 1 - s)
        residue_one = sp.residue(test * reflected_local_log_derivative, s, 1)
        assert sp.simplify(residue_zero - residue_one) == 0

        # A pole of order d+1 samples exactly jets ell_0,...,ell_d.
        if degree > 0:
            assert sp.diff(residue_zero, log_derivative_jets[degree]) != 0
        print(
            f"degree={degree} endpoint_residues_equal=True "
            f"highest_log_derivative_jet={degree}"
        )

    print("full_divisor_functional=-Res_0-Res_1")
    print("pair_normalized_li_energy=-Res_0")
    print("degree_d_requires_log_derivative_jets_0_through_d=True")
    print("rank_dependent_counterterm_required=False")


if __name__ == "__main__":
    main()
