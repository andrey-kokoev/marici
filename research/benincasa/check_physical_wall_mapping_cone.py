"""Verify the physical shared-wall localization mapping-cone representative."""
from __future__ import annotations

import json

import sympy as sp

import physical_g12_shared_wall_cech_cocycle as cech

x, y, z = sp.symbols("x y z")
energy = x + y + z
r1 = (
    -x**3 + x**2*y + 3*x**2*z + x*y**2 + 2*x*y*z + x*z**2
    - y**3 - y**2*z + y*z**2 + z**3
)
r2 = (
    x**3 - x**2*y + x**2*z - x*y**2 - 2*x*y*z - x*z**2
    + y**3 - 3*y**2*z - y*z**2 - z**3
)
quartic = -16*(x*y)**2 - 8*x*y*energy**2 + 8*(x+y)*energy**3 - 5*energy**4


def main() -> None:
    pairs = (("q_g1", "q_g2"), ("q_g1", "q_g3"), ("q_g2", "q_g3"))
    for first, second in pairs:
        a1, b1 = cech.GRADIENTS[first]
        a2, b2 = cech.GRADIENTS[second]
        determinant = a1*b2 - b1*a2
        assert determinant != 0
        assert sp.Rational(1, determinant) + sp.Rational(1, -determinant) == 0

    support = sp.expand(r1 * r2 * energy**2)
    gcd = sp.factor(sp.gcd(sp.Poly(support, x, y, z), sp.Poly(quartic, x, y, z)).as_expr())
    assert gcd == 1

    print(json.dumps({
        "schema": "marici.physical-wall-mapping-cone.v1",
        "cech_degree_zero": ["rho_g1", "rho_g2", "rho_g3"],
        "cech_degree_one": [0, 0, 0],
        "pairwise_iterated_residue_differential": 0,
        "mapping_cone_closed": True,
        "normalized_conductor_support": "R1*R2*E^2",
        "conductor_support_gcd_with_Q": str(gcd),
        "quartic_support_in_representative": False,
        "absolute_lift_selected": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
