#!/usr/bin/env python3
"""Exact formal audit of the conductor jet-residue constructor."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "benincasa" / "results" / "rank26-conductor-jet-residue-constructor.json"


def residue_of_shifted_series(coefficients: list[Fraction], pole_order: int) -> Fraction:
    """Residue of sum c_n R^n dR / R^pole_order."""
    target = pole_order - 1
    return coefficients[target] if target < len(coefficients) else Fraction(0)


def derivative_laurent(series: dict[int, Fraction]) -> dict[int, Fraction]:
    result: dict[int, Fraction] = {}
    for power, coefficient in series.items():
        if power:
            result[power - 1] = coefficient * power
    return result


coefficients = [Fraction(3), Fraction(-2), Fraction(5), Fraction(7), Fraction(-11), Fraction(13)]
jet_rows = []
for k in (0, 1, 2):
    pole_order = 2 * k + 1
    value = residue_of_shifted_series(coefficients, pole_order)
    derivative_value = coefficients[2 * k]  # f^(2k)(0)/(2k)! in coefficient form
    jet_rows.append({
        "k_pole": k,
        "normal_pole_order": pole_order,
        "required_jet_order": 2 * k,
        "residue": str(value),
        "jet_coefficient": str(derivative_value),
        "matches": value == derivative_value,
    })

# Formal residues annihilate exact normal derivatives for arbitrary Laurent
# series.  This is the local descent check underlying the de Rham quotient.
exact_seed = {-4: Fraction(2), -1: Fraction(5), 0: Fraction(7), 3: Fraction(-11)}
exact_derivative = derivative_laurent(exact_seed)
exact_residue = exact_derivative.get(-1, Fraction(0))

checks = {
    "k0_uses_value": jet_rows[0]["required_jet_order"] == 0 and jet_rows[0]["matches"],
    "k1_uses_second_jet": jet_rows[1]["required_jet_order"] == 2 and jet_rows[1]["matches"],
    "k2_uses_fourth_jet": jet_rows[2]["required_jet_order"] == 4 and jet_rows[2]["matches"],
    "formal_residue_annihilates_exact_normal_derivatives": exact_residue == 0,
}
payload = {
    "schema": "marici.rank26-conductor-jet-residue-constructor.v1",
    "physical_local_power": "R^(-1-2*k+2*epsilon)",
    "constructor": "J_k(f)=coefficient of R^(2*k) in f = f^(2*k)(0)/(2*k)!",
    "supported_k_depths": [0, 1, 2],
    "jet_rows": jet_rows,
    "exact_derivative_residue": str(exact_residue),
    "checks": checks,
    "passed": all(checks.values()),
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
if not payload["passed"]:
    raise SystemExit(1)
