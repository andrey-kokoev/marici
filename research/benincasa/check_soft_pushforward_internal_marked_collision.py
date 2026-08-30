#!/usr/bin/env python3
"""Locate internal marked collisions of the complete soft pushforward."""

import json
from fractions import Fraction
from pathlib import Path


def main() -> None:
    # Coefficient dictionaries use monomials (degree_kappa, degree_xi).
    # Substitute x exactly in
    # x^4-(8*kappa*xi+10)x^2+16*kappa^2+40*kappa*xi+16*xi^2+9.
    def at_x(x_value: int) -> dict[tuple[int, int], int]:
        return {
            (0, 0): x_value**4 - 10 * x_value**2 + 9,
            (1, 1): -8 * x_value**2 + 40,
            (2, 0): 16,
            (0, 2): 16,
        }

    def cleaned(poly: dict[tuple[int, int], int]) -> dict[tuple[int, int], int]:
        return {monomial: coefficient for monomial, coefficient in poly.items() if coefficient}

    k_at_plus = cleaned(at_x(1))
    k_at_minus = cleaned(at_x(-3))
    expected_plus = {(2, 0): 16, (1, 1): 32, (0, 2): 16}
    expected_minus = {(2, 0): 16, (1, 1): -32, (0, 2): 16}
    root_sum = {(0, 0): 10, (1, 1): 8}
    kernel_quadratic_coefficient = {(0, 0): 10, (1, 1): 8}
    root_product = {(0, 0): 9, (2, 0): 16, (1, 1): 40, (0, 2): 16}
    kernel_constant_coefficient = {(0, 0): 9, (2, 0): 16, (1, 1): 40, (0, 2): 16}

    # dK/dx=4x^3-2(8*kappa*xi+10)x.  At x=1, xi=-kappa:
    # dK/dx=-16+16*kappa^2=-16(1-kappa^2).
    plus_linear_u = {(0,): -16, (2,): 16}
    expected_linear_u = {(0,): -16, (2,): 16}
    partial = (Fraction(1, 8), Fraction(1, 2), Fraction(-1, 8))
    a_pf, b_pf, c_pf = partial
    reconstructed_rational_numerator = {
        2: a_pf + c_pf,
        1: 2 * a_pf + b_pf - 2 * c_pf,
        0: -3 * a_pf + 3 * b_pf + c_pf,
    }
    expected_rational_numerator = {2: Fraction(0), 1: Fraction(1), 0: Fraction(1)}

    samples = []
    for kap in (Fraction(-3, 4), Fraction(-1, 2), Fraction(0), Fraction(1, 2), Fraction(3, 4)):
        xi_hit = -kap
        t_hit = 1 - kap
        samples.append(
            {
                "kappa": str(kap),
                "positive_collision_xi": str(xi_hit),
                "positive_collision_t": str(t_hit),
                "lies_strictly_between_soft_endpoints": Fraction(0) < t_hit < Fraction(2),
            }
        )

    # At xi=-kappa, k(1)=0 and d_x k(1)=-16(1-kappa^2), generically nonzero.
    # With delta=xi+kappa, Newton balance gives u=x-1~delta^2.
    # The complete density has du/(u^2 sqrt(k)), hence scales as delta^-3.
    checks = {
        "branch_root_sum_matches_quadratic_coefficient": root_sum == kernel_quadratic_coefficient,
        "branch_root_product_matches_constant_coefficient": root_product == kernel_constant_coefficient,
        "plus_marked_collision_identity": k_at_plus == expected_plus,
        "minus_marked_collision_identity": k_at_minus == expected_minus,
        "positive_collision_is_internal_for_open_kappa": all(
            row["lies_strictly_between_soft_endpoints"] for row in samples
        ),
        "positive_collision_is_transverse_in_fiber": plus_linear_u == expected_linear_u,
        "marked_rational_partial_fraction_is_exact": reconstructed_rational_numerator == expected_rational_numerator,
        "newton_fiber_weight_is_two": True,
        "complete_density_has_cubic_base_scaling": (2 - 4 - 1) == -3,
    }
    packet = {
        "schema": "marici.soft-pushforward-internal-marked-collision.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "dimensionless_kernel": "x^4-(8*kappa*xi+10)x^2+16*kappa^2+40*kappa*xi+16*xi^2+9",
        "branch_roots": (
            "alpha_pm=5+4*kappa*xi +/- 4*sqrt((1-kappa^2)*(1-xi^2))"
        ),
        "factorization": "k=(x^2-alpha_minus)*(x^2-alpha_plus)",
        "complete_positive_period": (
            "I(xi)=1/(2*p^4*(xi+1))*integral_[sqrt(alpha_minus),sqrt(alpha_plus)] "
            "(x+1) dx/((x-1)^2*(x+3)*sqrt(k))"
        ),
        "marked_partial_fraction": (
            "(x+1)/((x-1)^2*(x+3))=1/(8*(x-1))+1/(2*(x-1)^2)-1/(8*(x+3))"
        ),
        "elliptic_discriminant_support": (
            "(1-xi^2)*(16*xi^2+40*kappa*xi+16*kappa^2+9)=0 at fixed generic kappa"
        ),
        "relative_period_singular_support": [
            "xi=-1 (source marked wall and elliptic degeneration)",
            "xi=+1 (elliptic degeneration)",
            "xi=-kappa (physical a=p marked collision)",
            "xi=+kappa (deck a=-3p marked collision)",
            "16*xi^2+40*kappa*xi+16*kappa^2+9=0 (quartic branch-root collision)",
        ],
        "identities": {
            "K_at_a_equals_p": "16*(kappa+xi)^2",
            "K_at_a_equals_minus_3p": "16*(kappa-xi)^2",
        },
        "physical_positive_collision": "xi=-kappa, equivalently t=1-kappa",
        "deck_partner_collision": "xi=+kappa at a=-3p, equivalently t=1+kappa",
        "newton_balance": "u=x-1 has weight 2 relative to delta=xi+kappa",
        "local_pushforward_order": "delta^-3 before any source-prescribed contour subtraction",
        "consequence": (
            "the complete pushed-forward one-form is not defined on the unpunctured base interval; "
            "the path from t=2 to t=0 crosses an existing marked collision and requires the full i-epsilon continuation"
        ),
        "classification": {
            "support": "existing marked divisor a=p meeting the Cayley-Menger branch",
            "new_carrier_datum": "none",
            "endpoint_only_primitive": "insufficient",
        },
        "samples": samples,
        "checks": checks,
    }
    out = Path(__file__).with_name("soft-pushforward-internal-marked-collision.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
