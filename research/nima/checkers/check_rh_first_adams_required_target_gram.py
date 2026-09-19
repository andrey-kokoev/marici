#!/usr/bin/env python3
"""Derive the unique theta target Gram required by the fixed Adams comparison."""

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa" / ".tmp_sympy"))
import sympy as s

a, b = s.symbols("a b", real=True)
u, v = s.symbols("u v", real=True)
z = u + s.I * v
G_st = s.Matrix([[a, z], [s.conjugate(z), b]])
Q = s.Matrix([[s.Rational(1, 2), s.Rational(1, 4)], [s.Rational(1, 2), -s.Rational(1, 4)]])
R = s.simplify(Q.inv())
G_required = s.simplify(R.conjugate().T * G_st * R)
pullback = s.simplify(Q.conjugate().T * G_required * Q)

expected = s.Matrix(
    [
        [a + 4 * b + 4 * u, a - 4 * b - 4 * s.I * v],
        [a - 4 * b + 4 * s.I * v, a + 4 * b - 4 * u],
    ]
)

checks = {
    "fixed_Q_inverse": R == s.Matrix([[1, 1], [2, -2]]),
    "required_target_formula": s.simplify(G_required - expected) == s.zeros(2),
    "pullback_recovers_stieltjes_gram": s.simplify(pullback - G_st) == s.zeros(2),
    "determinant_scaling": s.simplify(G_required.det() - 16 * G_st.det()) == 0,
}
assert all(checks.values())

payload = {
    "schema": "marici.nima.rh-first-adams-required-target-gram.v1",
    "fixed_linear_comparison_Q": [["1/2", "1/4"], ["1/2", "-1/4"]],
    "Q_inverse": [["1", "1"], ["2", "-2"]],
    "stieltjes_gram": [["a", "u+i*v"], ["u-i*v", "b"]],
    "required_theta_gram": [
        ["a+4*b+4*u", "a-4*b-4*i*v"],
        ["a-4*b+4*i*v", "a+4*b-4*u"],
    ],
    "determinant_relation": "det(G_theta_required)=16*det(G_St)",
    "checks": checks,
    "passed": True,
    "conclusion": "Because Q is fixed and invertible, the four target Green entries are uniquely prescribed by the Stieltjes Gram; no normalization freedom remains.",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()
out = Path(__file__).parents[1] / "results" / "rh-first-adams-required-target-gram.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
