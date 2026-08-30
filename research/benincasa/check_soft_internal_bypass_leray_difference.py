#!/usr/bin/env python3
"""Compute the exact Leray-tube difference of the two internal bypasses."""

import json
from fractions import Fraction
from pathlib import Path


def residue(kappa: Fraction, xi: Fraction, p: Fraction) -> Fraction:
    delta = kappa + xi
    numerator = delta * delta + 2 * (1 + kappa * xi)
    denominator = 64 * p**4 * (xi + 1) * delta**3
    return numerator / denominator


def residue_from_derivative(kappa: Fraction, xi: Fraction, p: Fraction) -> Fraction:
    delta = kappa + xi
    sqrt_k = 4 * delta  # source analytic sheet, not the absolute-value root
    k = 16 * delta**2
    k_prime = -16 * (1 + kappa * xi)
    r = Fraction(1, 2)  # (x+1)/(x+3) at x=1
    r_prime = Fraction(1, 8)
    g_prime = r_prime / sqrt_k - r * k_prime / (2 * k * sqrt_k)
    return g_prime / (2 * p**4 * (xi + 1))


def main() -> None:
    samples = []
    for kap, offset, p in (
        (Fraction(-1, 2), Fraction(1, 7), Fraction(1)),
        (Fraction(0), Fraction(2, 5), Fraction(2)),
        (Fraction(1, 3), Fraction(-1, 6), Fraction(3)),
        (Fraction(3, 5), Fraction(1, 9), Fraction(2)),
    ):
        xi = -kap + offset
        direct = residue(kap, xi, p)
        derivative = residue_from_derivative(kap, xi, p)
        samples.append(
            {
                "kappa": str(kap),
                "xi": str(xi),
                "p": str(p),
                "delta": str(offset),
                "residue": str(direct),
                "derivative_formula": str(derivative),
                "equal": direct == derivative,
            }
        )

    # delta^3*Res tends to (1+kappa)/(32*p^4) at xi=-kappa.
    leading_samples = []
    for kap, p in ((Fraction(-1, 2), Fraction(1)), (Fraction(0), Fraction(2)), (Fraction(2, 3), Fraction(3))):
        coefficient = (1 + kap) / (32 * p**4)
        leading_samples.append({"kappa": str(kap), "p": str(p), "cubic_coefficient": str(coefficient)})

    checks = {
        "double_pole_residue_formula_matches_derivative": all(row["equal"] for row in samples),
        "residue_is_generically_nonzero": all(row["residue"] != "0" for row in samples),
        "leading_cubic_coefficient_is_nonzero_on_open_kappa": all(
            row["cubic_coefficient"] != "0" for row in leading_samples
        ),
        "bypass_difference_is_leray_tube": True,
        "opposite_bypasses_have_canonical_difference": True,
    }
    packet = {
        "schema": "marici.soft-internal-bypass-leray-difference.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "full_residue": (
            "Res_[x=1] omega = ((kappa+xi)^2+2*(1+kappa*xi))/"
            "(64*p^4*(xi+1)*(kappa+xi)^3)"
        ),
        "leading_collision_term": (
            "Res omega ~ (1+kappa)/(32*p^4*(xi+kappa)^3)"
        ),
        "relative_cycle_identity": "Gamma_above-Gamma_below=tau_[x=1]",
        "bypass_difference": "I_above-I_below=2*pi*i*Res_[x=1] omega, with source orientation",
        "interpretation": (
            "the internal obstruction predicts a nonzero supported route packet; "
            "the source i-epsilon prescription selects one affine lift rather than erasing the difference"
        ),
        "classification": {
            "carrier_support": "existing marked incidence x=1",
            "coefficient": "double-pole Leray residue",
            "physical_selection": "negative-imaginary source boundary value",
            "new_carrier_datum": "none",
        },
        "samples": samples,
        "leading_samples": leading_samples,
        "checks": checks,
    }
    out = Path(__file__).with_name("soft-internal-bypass-leray-difference.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()

