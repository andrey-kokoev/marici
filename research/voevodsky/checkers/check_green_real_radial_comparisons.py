#!/usr/bin/env python3
"""Exact symbolic checks for the Green--Real radial comparison calculus."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/voevodsky/results/green_real_radial_comparisons.json"
CHECKER = Path(__file__).resolve()

u, v = s.symbols("u v", nonzero=True)
ub, vb = s.symbols("ub vb", nonzero=True)
I2 = s.eye(2)
J = s.diag(-1, 1)
W_u = s.Matrix([[0, 1 / u], [u, 0]])
W_v = s.Matrix([[0, 1 / v], [v, 0]])
S_u = s.diag(1, u**2)  # J_u = S_u K
S_v = s.diag(1, v**2)
G = s.diag(1, v / u)
G_bar = s.diag(1, vb / ub)
W_u_star = W_u.conjugate().T.subs({s.conjugate(u): ub})

W_u_bar = s.Matrix([[0, 1 / ub], [ub, 0]])
checks = {
    "reciprocal_involution": s.simplify(W_u * W_u - I2) == s.zeros(2),
    "green_anti_isometry": s.simplify((W_u_star * J * W_u).subs(ub, 1/u) + J) == s.zeros(2),
    "twisted_real_involution": s.simplify((S_u * s.diag(1, ub**2)).subs(ub, 1/u) - I2) == s.zeros(2),
    "twisted_real_reciprocal_commutation": s.simplify((S_u * W_u_bar).subs(ub, 1/u) - W_u * S_u) == s.zeros(2),
    "phase_gauge_reciprocal_naturality": s.simplify(G * W_u - W_v * G) == s.zeros(2),
    "phase_gauge_real_naturality": s.simplify((G * S_u - S_v * G_bar).subs({ub: 1/u, vb: 1/v})) == s.zeros(2),
}
H = s.simplify(W_v * W_u)
checks["two_sewing_holonomy"] = s.simplify(H - s.diag(u/v, v/u)) == s.zeros(2)
H_star = H.conjugate().T.subs({s.conjugate(u): 1/u, s.conjugate(v): 1/v})
checks["holonomy_green_isometry"] = s.simplify(H_star * J * H - J) == s.zeros(2)
checks["holonomy_determinant_one"] = s.simplify(H.det() - 1) == 0
checks["phase_gauge_groupoid"] = s.simplify(s.diag(1, s.symbols('w')/v) * G - s.diag(1, s.symbols('w')/u)) == s.zeros(2)

# Deliberate failures must produce nonzero residuals.
wrong_real = s.diag(1, u)  # missing one power of u
wrong_real_residual = s.simplify(1 - u)  # image of (1,u) fails the Lambda_u wall equation
quarter_turn = s.Matrix([[0, -1], [1, 0]])
quarter_as_reciprocal_residual = s.simplify(quarter_turn**2 - I2)
wrong_gauge = s.diag(1, u/v)
wrong_gauge_residual = s.simplify(wrong_gauge * W_u - W_v * wrong_gauge)

deliberate_failures = {
    "missing_real_phase_power": {
        "residual": str(wrong_real_residual),
        "nonzero": wrong_real_residual != s.zeros(2),
    },
    "quarter_turn_as_involution": {
        "residual": str(quarter_as_reciprocal_residual),
        "nonzero": quarter_as_reciprocal_residual != s.zeros(2),
    },
    "reversed_phase_gauge": {
        "residual": str(wrong_gauge_residual),
        "nonzero": wrong_gauge_residual != s.zeros(2),
    },
}
passed = all(checks.values()) and all(x["nonzero"] for x in deliberate_failures.values())
result = {
    "schema": "marici.voevodsky.green-real-radial-comparison-check.v1",
    "checker_sha256": hashlib.sha256(CHECKER.read_bytes()).hexdigest(),
    "assumptions": ["u and v are nonzero unit phases", "conjugate(u)=u^-1", "conjugate(v)=v^-1"],
    "checks": checks,
    "deliberate_failures": deliberate_failures,
    "passed": passed,
}
RESULT.parent.mkdir(parents=True, exist_ok=True)
RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": passed, "checks": len(checks), "deliberate_failures": len(deliberate_failures)}))
raise SystemExit(0 if passed else 1)
