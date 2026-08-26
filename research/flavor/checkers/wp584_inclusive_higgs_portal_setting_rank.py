"""Exact WP584 rank audit of WP580 settings through inclusive Higgs readout."""

import json
from pathlib import Path

import sympy as sp


z, lambda_s, lambda_h, h = sp.symbols(
    "z lambda_s lambda_H h", positive=True, real=True
)


def readout(z_value, lambda_s_value):
    del lambda_s_value
    return 1 - z_value


r_minus = (z - h, lambda_s * z**2 / (z - h) ** 2)
r_plus = (z + h, lambda_s * z**2 / (z + h) ** 2)
q_minus = (z, lambda_s - lambda_h * h / z**2)
q_plus = (z, lambda_s + lambda_h * h / z**2)

responses = {
    "r_minus": sp.simplify(readout(*r_minus) - readout(z, lambda_s)),
    "r_plus": sp.simplify(readout(*r_plus) - readout(z, lambda_s)),
    "q_minus": sp.simplify(readout(*q_minus) - readout(z, lambda_s)),
    "q_plus": sp.simplify(readout(*q_plus) - readout(z, lambda_s)),
}

jacobian = sp.Matrix([readout(z, lambda_s)]).jacobian([z, lambda_s])
gram = sp.simplify(jacobian.T * jacobian)

hostile = {z: sp.Rational(1, 4), lambda_s: 1, lambda_h: 1, h: sp.Rational(1, 32)}
hostile_q_minus = tuple(sp.simplify(x.subs(hostile)) for x in q_minus)
hostile_q_plus = tuple(sp.simplify(x.subs(hostile)) for x in q_plus)

checks = {
    "inclusive_higgs_jacobian_has_rank_one": jacobian.rank() == 1,
    "lambda_s_column_is_zero": jacobian[:, 1] == sp.zeros(1, 1),
    "gram_determinant_is_zero": sp.det(gram) == 0,
    "r_minus_changes_readout_by_plus_h": responses["r_minus"] == h,
    "r_plus_changes_readout_by_minus_h": responses["r_plus"] == -h,
    "q_minus_is_detector_blind": responses["q_minus"] == 0,
    "q_plus_is_detector_blind": responses["q_plus"] == 0,
    "hostile_q_minus_is_one_quarter_one_half": hostile_q_minus
    == (sp.Rational(1, 4), sp.Rational(1, 2)),
    "hostile_q_plus_is_one_quarter_three_halves": hostile_q_plus
    == (sp.Rational(1, 4), sp.Rational(3, 2)),
    "hostile_readouts_are_three_quarters": readout(*hostile_q_minus)
    == readout(*hostile_q_plus)
    == sp.Rational(3, 4),
}

if not all(checks.values()):
    raise SystemExit(f"WP584 check failed: {checks}")

checks = {key: bool(value) for key, value in checks.items()}
result = {
    "work_package": "WP584",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "0<z<1, lambda_s>0, lambda_H>0",
    "faithful_source_coordinate": "(r,q)=(z,lambda_s*z^2/lambda_H)",
    "physical_instrument": "inclusive Higgs production/coupling readout kappa_t^2=1-z",
    "contextual_partition": "fixed-z classes with unrestricted positive lambda_s fiber",
    "response_rank": 1,
    "classification": "physical readout; separates r settings, is blind to q settings; neither selector nor rigidifier",
    "smallest_exact_falsifier": "at z=1/4, lambda_s=lambda_H=1, h=1/32, q-minus=(1/4,1/2) and q-plus=(1/4,3/2) both read kappa_t^2=3/4",
    "remaining_instrument_gate": "a publication-bound completed detector channel with nonzero calibrated derivative along q at fixed z",
}

out = Path(__file__).resolve().parents[1] / "results" / "wp584_inclusive_higgs_portal_setting_rank.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
