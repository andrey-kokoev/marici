#!/usr/bin/env python3
"""Exact zero-stratum audit of the total-energy/defect Jacobian."""

import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent.parent


def main():
    x = sp.symbols("X1 X2 X3")
    p = sp.symbols("P1 P2 P3")
    outputs = (sum(x),) + tuple(p[i] ** 2 - x[i] ** 2 for i in range(3))
    jacobian = sp.Matrix(outputs).jacobian(x + p)

    rows = []
    failures = []
    # The matrix rank depends only on which X_i and P_i vanish.  Assign a
    # distinct exact nonzero integer to every nonvanishing coordinate.
    values = (2, 3, 5, 7, 11, 13)
    for zero_bits in itertools.product((False, True), repeat=6):
        substitution = {
            variable: (0 if is_zero else value)
            for variable, is_zero, value in zip(x + p, zero_bits, values)
        }
        rank = int(jacobian.subs(substitution).rank())
        all_p_zero = all(zero_bits[3:])
        coordinate_origin = any(zero_bits[i] and zero_bits[i + 3] for i in range(3))
        predicted_drop = all_p_zero or coordinate_origin
        observed_drop = rank < 4
        if observed_drop != predicted_drop:
            failures.append({"zero_bits": zero_bits, "rank": rank})
        rows.append(
            {
                "zero": [str(v) for v, flag in zip(x + p, zero_bits) if flag],
                "rank": rank,
                "predicted_drop": predicted_drop,
            }
        )

    checks = {
        "all_64_zero_strata_match": not failures,
        "generic_rank_is_four": jacobian.rank() == 4,
        "all_momentum_soft_has_rank_at_most_three":
            jacobian.subs({p[0]: 0, p[1]: 0, p[2]: 0}).rank() == 3,
        "each_coordinate_origin_forces_rank_drop": all(
            jacobian.subs({x[i]: 0, p[i]: 0}).rank() == 3 for i in range(3)
        ),
    }
    packet = {
        "schema": "marici.total_energy_defect_rank_drop.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "rank_drop_locus": (
            "V(P1,P2,P3) union V(X1,P1) union V(X2,P2) union V(X3,P3)"
        ),
        "checks": checks,
        "zero_strata": rows,
        "failures": failures,
        "scope_warning": (
            "This is the rank-drop locus of the kinematic coordinate map. "
            "It does not itself construct a coefficient or physical-cycle map."
        ),
    }
    output = ROOT / "results" / "total-energy-defect-rank-drop.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": packet["status"], "checks": checks}, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
