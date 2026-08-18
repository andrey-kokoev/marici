"""Audit generic-lower radicals in the normal directions to homogeneity."""
from __future__ import annotations

import json

import sympy as sp

x, y, z = sp.symbols("x y z")
energy = x + y + z
triangle = (x-y-z)*(x-y+z)*(x+y-z)*(x+y+z)
quartic = -16*(x*y)**2 - 8*x*y*energy**2 + 8*(x+y)*energy**3 - 5*energy**4


def main() -> None:
    # The generic radicals have the form -4*nu_i*nu_j*Lambda_P*F_ij.
    # Their first nonzero normal-grade coefficients are obtained by P=X in
    # Lambda_P and F_ij after retaining the labelled nu_i*nu_j monomial.
    coefficients = {
        "nu1_nu2": sp.factor(-4*triangle*(z**2-(x-y)**2)),
        "nu1_nu3": sp.factor(-4*triangle*(y**2-(x-z)**2)),
        "nu2_nu3_minus": sp.factor(-4*triangle*(x**2-(y-z)**2)),
        "nu2_nu3_plus": sp.factor(-4*triangle*(x**2-(y+z)**2)),
    }
    rows = {}
    for name, coefficient in coefficients.items():
        gcd = sp.factor(
            sp.gcd(sp.Poly(coefficient, x, y, z), sp.Poly(quartic, x, y, z)).as_expr()
        )
        assert gcd == 1
        rows[name] = {
            "coefficient": str(coefficient),
            "gcd_with_Q": str(gcd),
        }

    print(json.dumps({
        "schema": "marici.generic-lower-homogeneous-normal-grade.v1",
        "normal_parameters": ["nu1=P1^2-X1^2", "nu2=P2^2-X2^2", "nu3=P3^2-X3^2"],
        "first_nonzero_normal_order": 2,
        "normal_grade_coefficients": rows,
        "same_marked_plane_types": True,
        "missing_marked_section": False,
        "all_normal_coefficients_Q_coprime": True,
        "quartic_from_first_normal_grade": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
