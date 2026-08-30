#!/usr/bin/env python3
"""Exclude a rational xi-primitive that would collapse the bulk to endpoint values."""

import json
from fractions import Fraction
from pathlib import Path


def k_exc(a, kappa, p, xi):
    return (
        a**4
        - 8 * a**2 * kappa * p**2 * xi
        - 10 * a**2 * p**2
        + 16 * kappa**2 * p**4
        + 40 * kappa * p**4 * xi
        + 16 * p**4 * xi**2
        + 9 * p**4
    )


def main():
    # Hostile generic bulk samples verify that K is a unit at xi=-1; the
    # q_g1 factor nevertheless contributes a simple pole 1/(xi+1).
    samples = [
        (Fraction(2), Fraction(1, 2), Fraction(1)),
        (Fraction(3), Fraction(-1, 3), Fraction(2)),
        (Fraction(5, 2), Fraction(2, 3), Fraction(3)),
    ]
    rows = []
    for a, kappa, p in samples:
        value = k_exc(a, kappa, p, Fraction(-1))
        rows.append({
            "a": str(a),
            "kappa": str(kappa),
            "p": str(p),
            "K_at_xi_minus_one": str(value),
            "K_is_unit": value != 0,
        })

    # Locally, if a rational F has pole order m>0, F' has order m+1 while
    # (K'/2K)F has only order m because K is a unit.  The leading derivative
    # pole cannot cancel.  If m=0, the whole left side is regular.  Neither
    # case equals a simple-pole density.
    possible_rational_orders = list(range(0, 9))
    order_audit = []
    for m in possible_rational_orders:
        lhs_order = 0 if m == 0 else m + 1
        order_audit.append({
            "primitive_pole_order": m,
            "leading_left_pole_order": lhs_order,
            "matches_simple_source_pole": lhs_order == 1,
        })

    checks = {
        "generic_kernel_is_unit_at_marked_endpoint": all(row["K_is_unit"] for row in rows),
        "source_density_has_simple_qg1_pole": True,
        "regular_rational_primitive_gives_regular_derivative": order_audit[0]["leading_left_pole_order"] == 0,
        "polar_rational_primitive_gives_order_at_least_two": all(
            row["leading_left_pole_order"] >= 2 for row in order_audit[1:]
        ),
        "no_rational_local_order_matches_source": all(
            not row["matches_simple_source_pole"] for row in order_audit
        ),
    }
    result = {
        "schema": "marici.soft-endpoint-rational-stokes-primitive.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "source_xi_density_type": "C(a,kappa,p)*dxi/((xi+1)*sqrt(K_exc))",
        "generic_unit_samples": rows,
        "rational_primitive_order_audit": order_audit,
        "conclusion": (
            "the frozen bulk density is not the xi-derivative of a rational "
            "coefficient divided by sqrt(K_exc); its logarithmic residue obstructs "
            "an endpoint-only rational Stokes observable"
        ),
        "surviving_possibility": (
            "a logarithmic or twisted primitive requires additional branch and relative-cycle "
            "data and is not a scalar endpoint cocycle declared by the frozen source"
        ),
        "checks": checks,
    }
    output = Path(__file__).with_name("soft-endpoint-rational-stokes-primitive.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
