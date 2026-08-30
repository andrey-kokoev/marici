#!/usr/bin/env python3
"""Derive the pure Cayley-Menger endpoint vanishing-cycle covector."""

import json
from fractions import Fraction
from pathlib import Path


def main():
    # Remove the common factor pi*i/p. Squared local covector entries are
    # 1/(5-4*kappa) at xi=-1 and 1/(5+4*kappa) at xi=+1.
    sample_kappas = (Fraction(-3, 4), Fraction(-1, 2), Fraction(0), Fraction(1, 2), Fraction(3, 4))
    samples = []
    for kappa in sample_kappas:
        c_minus_sq = Fraction(1, 1) / (5 - 4 * kappa)
        c_plus_sq = Fraction(1, 1) / (5 + 4 * kappa)
        samples.append({
            "kappa": str(kappa),
            "c_minus_squared_without_common_factor": str(c_minus_sq),
            "c_plus_squared_without_common_factor": str(c_plus_sq),
            "equal": c_minus_sq == c_plus_sq,
        })
    checks = {
        "collision_roots_positive_on_physical_open_interval": all(5 - 4*k > 0 and 5 + 4*k > 0 for k in sample_kappas),
        "endpoint_covectors_equal_only_on_symmetric_slice": [record["equal"] for record in samples] == [False, False, True, False, False],
        "generic_equal_weight_cancellation_is_broken": all(not record["equal"] for record in samples if record["kappa"] != "0"),
    }
    result = {
        "schema": "marici.soft-endpoint-vanishing-covector.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "quadratic_variable": "A=a^2",
        "double_roots": {
            "xi=-1": "A_minus=(5-4*kappa)*p^2",
            "xi=+1": "A_plus=(5+4*kappa)*p^2",
        },
        "positive_sheet_local_periods": {
            "xi=-1": "pi*i/(p*sqrt(5-4*kappa))",
            "xi=+1": "pi*i/(p*sqrt(5+4*kappa))",
        },
        "derivation": "dA=2a da and the standard quadratic-root vanishing period integral dA/w=2*pi*i give integral da/w=pi*i/sqrt(A0)",
        "samples": samples,
        "scope": "pure Cayley-Menger vanishing-cycle covector only; the marked rational source factor, especially its xi=-1 pole, is not included",
        "checks": checks,
    }
    output = Path(__file__).with_name("soft-endpoint-vanishing-covector.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
