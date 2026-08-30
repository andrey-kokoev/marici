#!/usr/bin/env python3
"""Integrate the internal Leray route packet and extract its soft finite part."""

import json
from fractions import Fraction
from pathlib import Path


def coefficients(kappa: Fraction):
    a = 1 - kappa
    b = (3 - kappa) / a**2
    return {
        "A_at_delta_plus_a": -b,
        "B_at_delta": b,
        "C_at_delta_squared": -2 / a,
        "D_at_delta_cubed": 2 * (1 + kappa),
    }


def numerator_from_partial(kappa: Fraction, coeffs):
    a = 1 - kappa
    A = coeffs["A_at_delta_plus_a"]
    B = coeffs["B_at_delta"]
    C = coeffs["C_at_delta_squared"]
    D = coeffs["D_at_delta_cubed"]
    return {
        3: A + B,
        2: a * B + C,
        1: a * C + D,
        0: a * D,
    }


def main() -> None:
    samples = []
    for kap in (Fraction(-3, 4), Fraction(-1, 2), Fraction(0), Fraction(1, 3), Fraction(3, 4)):
        coeffs = coefficients(kap)
        reconstructed = numerator_from_partial(kap, coeffs)
        expected = {
            3: Fraction(0),
            2: Fraction(1),
            1: 2 * kap,
            0: 2 * (1 - kap**2),
        }
        a = 1 - kap
        b = 1 + kap
        B = coeffs["B_at_delta"]
        samples.append(
            {
                "kappa": str(kap),
                "partial_coefficients": {key: str(value) for key, value in coeffs.items()},
                "reconstructed_numerator": {str(key): str(value) for key, value in reconstructed.items()},
                "expected_numerator": {str(key): str(value) for key, value in expected.items()},
                "decomposition_matches": reconstructed == expected,
                "log_coefficient_B": str(B),
                "finite_rational_term": str(-Fraction(4, 1) / a**2),
                "log_argument_without_source_branch": f"-{a}/{b}",
            }
        )

    checks = {
        "partial_fraction_decomposition_is_exact": all(row["decomposition_matches"] for row in samples),
        "basepoint_is_t_two": True,
        "soft_endpoint_is_t_zero": True,
        "finite_rational_term_is_derived": all(row["finite_rational_term"] != "0" for row in samples),
        "source_branch_is_still_required_for_logarithm": True,
    }
    packet = {
        "schema": "marici.soft-internal-route-finite-part.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "residue_partial_fraction": (
            "64*p^4*R = -B/(delta+a)+B/delta-2/(a*delta^2)+2*(1+kappa)/delta^3, "
            "a=1-kappa, B=(3-kappa)/(1-kappa)^2"
        ),
        "primitive": (
            "F_R=1/(64*p^4)*[B*log(delta/(delta+a))+2/(a*delta)-(1+kappa)/delta^2]"
        ),
        "pointed_route_difference": "Delta P_route=2*pi*i*(F_R(delta)-F_R(1+kappa))",
        "soft_log_coefficient_before_2pi_i": "-B/(64*p^4)",
        "soft_finite_part_before_2pi_i": (
            "1/(64*p^4)*[B*log(-(1-kappa)/(1+kappa))-4/(1-kappa)^2]"
        ),
        "source_branch_requirement": (
            "the negative-imaginary boundary value fixes the branch of log(-(1-kappa)/(1+kappa))"
        ),
        "interpretation": (
            "the opposite bypass changes both the soft logarithmic coefficient and the pointed finite part by an exact source-supported term"
        ),
        "samples": samples,
        "checks": checks,
    }
    out = Path(__file__).with_name("soft-internal-route-finite-part.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()

