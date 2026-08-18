"""Audit and certify all-order total-energy transport of wall pair residues."""
from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    E, x, y = sp.symbols("E x y")
    z = E - x - y
    Q = sp.factor(
        4 * (((x - y) ** 2 - z**2) * ((x + y) ** 2 - z**2))
        - (
            ((x - y) ** 2 - z**2)
            + ((x + y) ** 2 - z**2)
            - E**2
        )
        ** 2
    )

    norms = {
        "g1_g2": sp.factor(
            4
            * z**2
            / (
                (x - y - z) ** 4
                * (x - y + z) ** 4
                * E**2
                * (x + y + 3 * z) ** 2
            )
        ),
        "g1_g3": sp.factor(
            E**2
            / (
                4
                * (y + z) ** 4
                * (x - y - z) ** 4
                * (x + y - z) ** 2
                * (x + y + 3 * z) ** 2
            )
        ),
        "g2_g3": sp.factor(
            E**2
            / (
                4
                * (x + z) ** 4
                * (x - y + z) ** 4
                * (x + y - z) ** 2
                * (x + y + 3 * z) ** 2
            )
        ),
    }

    rows = {}
    for name, norm in norms.items():
        logarithmic_derivative = sp.factor(sp.diff(norm, E) / (2 * norm))
        ratio = sp.Integer(1)
        orders = []
        for order in range(1, 9):
            ratio = sp.factor(sp.diff(ratio, E) + logarithmic_derivative * ratio)
            denominator = sp.factor(sp.denom(sp.cancel(ratio)))
            gcd_q = sp.factor(
                sp.gcd(
                    sp.Poly(denominator, E, x, y),
                    sp.Poly(Q, E, x, y),
                ).as_expr()
            )
            assert gcd_q == 1
            orders.append(
                {
                    "order": order,
                    "derivative_over_original": str(ratio),
                    "denominator": str(denominator),
                    "gcd_denominator_Q": str(gcd_q),
                }
            )
        rows[name] = {
            "sheet_norm": str(norm),
            "logarithmic_derivative": str(logarithmic_derivative),
            "orders": orders,
        }

    result = {
        "schema": "marici.physical-wall-all-order-transport.v1",
        "pairs": rows,
        "audited_orders": 8,
        "all_audited_derivative_denominators_Q_coprime": True,
        "structural_induction": (
            "If eta'/eta lies in the localization by the irreducible factors "
            "of eta^2, then R_(n+1)=d_E R_n+(eta'/eta)R_n remains in the same localization."
        ),
        "all_orders_cech_closed": (
            "d_E^n eta_ji=-d_E^n eta_ij follows from eta_ji=-eta_ij"
        ),
        "all_orders_new_pole_divisors": False,
        "Q_supported_transport_from_static_pair_residues": False,
        "new_carrier_datum": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
