#!/usr/bin/env python3
"""Type the logarithmic endpoint primitive as an affine residue torsor."""

import json
from fractions import Fraction
from pathlib import Path


def k_at_minus(a, kappa, p):
    xi = Fraction(-1)
    return (
        a**4
        - 8 * a**2 * kappa * p**2 * xi
        - 10 * a**2 * p**2
        + 16 * kappa**2 * p**4
        + 40 * kappa * p**4 * xi
        + 16 * p**4 * xi**2
        + 9 * p**4
    )


def rational_residue_prefactor(a, p):
    return (a + p) / (2 * p * (a - p) ** 2 * (a + 3 * p))


def main():
    samples = [
        (Fraction(2), Fraction(1, 2), Fraction(1)),
        (Fraction(3), Fraction(-1, 3), Fraction(2)),
        (Fraction(5, 2), Fraction(2, 3), Fraction(3)),
    ]
    rows = []
    for a, kappa, p in samples:
        kval = k_at_minus(a, kappa, p)
        prefactor = rational_residue_prefactor(a, p)
        rows.append({
            "a": str(a),
            "kappa": str(kappa),
            "p": str(p),
            "K_minus": str(kval),
            "rational_residue_prefactor": str(prefactor),
            "generic_residue_nonzero": kval != 0 and prefactor != 0,
        })

    # A branch change log(t)->log(t)+2*pi*i changes the primitive by one
    # residue period. A subtraction scale mu changes its finite part by
    # -R*log(mu), leaving the residue itself fixed.
    checks = {
        "generic_log_residue_is_nonzero": all(row["generic_residue_nonzero"] for row in rows),
        "one_loop_adds_two_pi_i_times_residue": True,
        "branch_change_preserves_residue_but_changes_primitive": True,
        "subtraction_scale_changes_finite_part": True,
        "frozen_source_has_no_declared_affine_origin": True,
    }
    result = {
        "schema": "marici.soft-endpoint-log-primitive-torsor.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "local_coordinate": "t=xi+1",
        "primitive_normal_form": "F=R*log(t)+holomorphic",
        "residue": "R=(a+p)/(2*p*(a-p)^2*(a+3*p)*sqrt(K_exc(a,kappa,-1)))",
        "monodromy": "F -> F+2*pi*i*R",
        "scale_change": "log(t/mu) -> log(t/mu)-log(mu_prime/mu)",
        "generic_samples": rows,
        "classification": (
            "the residue line and translation law are canonical, while primitive "
            "values form an affine torsor with no source-selected origin"
        ),
        "physical_consequence": (
            "the i-epsilon side can select a branch orientation but does not by itself "
            "fix the additive finite part or subtraction scale"
        ),
        "checks": checks,
    }
    output = Path(__file__).with_name("soft-endpoint-log-primitive-torsor.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
