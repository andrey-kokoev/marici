#!/usr/bin/env python3
"""Exact Jacobian certificate for generic independence of E and labelled defects."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent.parent


def main():
    x1, x2, x3, p1, p2, p3 = sp.symbols("X1 X2 X3 P1 P2 P3")
    variables = (x1, x2, x3, p1, p2, p3)
    outputs = (
        x1 + x2 + x3,
        p1**2 - x1**2,
        p2**2 - x2**2,
        p3**2 - x3**2,
    )
    jacobian = sp.Matrix(outputs).jacobian(variables)
    selected_columns = (0, 3, 4, 5)
    minor = jacobian[:, selected_columns]
    determinant = sp.factor(minor.det())
    expected = 8 * p1 * p2 * p3
    simple_soft_minors = {
        "P1=0": sp.factor(jacobian.subs(p1, 0)[:, (0, 1, 4, 5)].det()),
        "P2=0": sp.factor(jacobian.subs(p2, 0)[:, (1, 0, 3, 5)].det()),
        "P3=0": sp.factor(jacobian.subs(p3, 0)[:, (2, 0, 3, 4)].det()),
    }
    expected_soft_minors = {
        "P1=0": 8 * x1 * p2 * p3,
        "P2=0": -8 * x2 * p1 * p3,
        "P3=0": 8 * x3 * p1 * p2,
    }
    checks = {
        "selected_minor_is_exact": sp.expand(determinant - expected) == 0,
        "generic_rank_is_four": determinant != 0,
        "selected_minor_divisor_is_exact": sp.factor(determinant) == expected,
        "simple_soft_divisors_remain_rank_four_generically": all(
            sp.expand(simple_soft_minors[key] - expected_soft_minors[key]) == 0
            for key in simple_soft_minors
        ),
        "physical_locus_keeps_total_energy_free": all(
            sp.diff(outputs[0], variable) != 0 for variable in (x1, x2, x3)
        ),
    }
    packet = {
        "schema": "marici.total_energy_defect_independence.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "variables": [str(variable) for variable in variables],
        "outputs": [str(output) for output in outputs],
        "jacobian": [[str(value) for value in row] for row in jacobian.tolist()],
        "selected_columns": ["X1", "P1", "P2", "P3"],
        "selected_minor": [[str(value) for value in row] for row in minor.tolist()],
        "minor_determinant": str(determinant),
        "simple_soft_alternative_minors": {
            key: str(value) for key, value in simple_soft_minors.items()
        },
        "checks": checks,
        "conclusion": (
            "E and the three labelled defects are algebraically independent "
            "on a dense open set, and generic points of every simple soft "
            "divisor retain rank four. Generic kinematic incidence supplies "
            "no total-energy-to-defect Rees map."
        ),
        "scope_warning": (
            "This excludes a generic carrier-algebra map. It does not exclude "
            "coefficient-derived, physical-cycle, or deeper supported maps."
        ),
    }
    output = ROOT / "results" / "total-energy-defect-independence.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": packet["status"], "checks": checks}, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
