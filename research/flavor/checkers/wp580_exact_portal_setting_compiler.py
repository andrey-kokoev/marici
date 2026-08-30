"""Exact WP580 finite portal-setting compiler and linearization hostile."""

import json
from pathlib import Path

import sympy as sp


z, lambda_h = sp.symbols("z lambda_H", positive=True, real=True)
lambda_s = sp.symbols("lambda_s", positive=True, real=True)
h = sp.symbols("h", real=True)


def invariant_map(z_value, lambda_s_value):
    return sp.Matrix([z_value, lambda_s_value * z_value**2 / lambda_h])


base = invariant_map(z, lambda_s)
setting_r = sp.Matrix([z + h, lambda_s * z**2 / (z + h) ** 2])
setting_q = sp.Matrix([z, lambda_s + lambda_h * h / z**2])

response_r = sp.simplify(invariant_map(setting_r[0], setting_r[1]) - base)
response_q = sp.simplify(invariant_map(setting_q[0], setting_q[1]) - base)
design = sp.Matrix.hstack(response_r, response_q)

linear_setting_r = sp.Matrix([z + h, lambda_s - 2 * lambda_s * h / z])
linear_response_r = sp.simplify(
    invariant_map(linear_setting_r[0], linear_setting_r[1]) - base
)
linear_q_contamination = sp.factor(linear_response_r[1])

hostile = {z: 1, lambda_s: 1, lambda_h: 1, h: sp.Rational(1, 2)}
hostile_exact_setting = setting_r.subs(hostile)
hostile_linear_setting = linear_setting_r.subs(hostile)
hostile_exact_response = response_r.subs(hostile)
hostile_linear_response = linear_response_r.subs(hostile)

checks = {
    "pure_r_setting_is_exact": response_r == sp.Matrix([h, 0]),
    "pure_q_setting_is_exact": response_q == sp.Matrix([0, h]),
    "finite_design_is_h_times_identity": design == h * sp.eye(2),
    "finite_design_determinant_is_h_squared": sp.factor(design.det()) == h**2,
    "linearized_r_setting_has_exact_contamination": linear_q_contamination
    == -lambda_s * h**2 * (3 * z + 2 * h) / (lambda_h * z),
    "hostile_exact_setting_is_three_halves_four_ninths": hostile_exact_setting
    == sp.Matrix([sp.Rational(3, 2), sp.Rational(4, 9)]),
    "hostile_exact_response_is_pure_r": hostile_exact_response
    == sp.Matrix([sp.Rational(1, 2), 0]),
    "hostile_linear_setting_is_three_halves_zero": hostile_linear_setting
    == sp.Matrix([sp.Rational(3, 2), 0]),
    "hostile_linear_response_contaminates_q_by_minus_one": hostile_linear_response
    == sp.Matrix([sp.Rational(1, 2), -1]),
}
checks = {name: bool(value) for name, value in checks.items()}


def encode_matrix(matrix):
    return [[str(sp.simplify(matrix[row, col])) for col in range(matrix.cols)] for row in range(matrix.rows)]


result = {
    "work_package": "WP580",
    "classification": "exact nonlinear source-coordinate compiler for orthogonal finite invariant portal settings; neither selector nor physical detector instrument",
    "base_invariants": encode_matrix(base),
    "pure_r_source_setting": encode_matrix(setting_r),
    "pure_q_source_setting": encode_matrix(setting_q),
    "pure_r_invariant_response": encode_matrix(response_r),
    "pure_q_invariant_response": encode_matrix(response_q),
    "finite_design": encode_matrix(design),
    "linearized_r_source_setting": encode_matrix(linear_setting_r),
    "linearized_r_invariant_response": encode_matrix(linear_response_r),
    "linearized_q_contamination": str(linear_q_contamination),
    "smallest_exact_falsifier": "at z=lambda_s=lambda_H=1 and h=1/2, exact setting (3/2,4/9) preserves q while the linearized setting (3/2,0) changes q by -1",
    "domain": "z>0, lambda_s>0, lambda_H>0, z+h>0, and lambda_s+lambda_H*h/z^2>0; symmetric r settings additionally require 0<h<z",
    "remaining_gate": "intersect exact settings with a declared viable source domain, then execute them through one publication-bound completed detector pipeline",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp580_exact_portal_setting_compiler.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
