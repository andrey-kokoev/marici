#!/usr/bin/env python3
"""Exact finite-matrix tests for nonunitary observer transport."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/voevodsky/results/nonunitary_comparison_condition_numbers.json"
CHECKER = Path(__file__).resolve()

checks: dict[str, bool] = {}

# A diagonal model saturating lower, upper, and condition-number bounds.
C = s.diag(2, s.Rational(1, 3))
T = s.diag(3, 5)
Tp = T * C.inv()
source_lower, source_upper = s.Integer(3), s.Integer(5)
C_norm, Cinv_norm = s.Integer(2), s.Integer(3)
target_lower, target_upper = s.Rational(3, 2), s.Integer(15)
checks["transport_formula"] = Tp == s.diag(s.Rational(3, 2), 15)
checks["lower_bound_sharp"] = target_lower == source_lower / C_norm
checks["upper_bound_sharp"] = target_upper == source_upper * Cinv_norm
checks["condition_number_bound_sharp"] = (
    target_upper / target_lower
    == (C_norm * Cinv_norm) * (source_upper / source_lower)
)
checks["gramian_congruence"] = (
    Tp.conjugate().T * Tp
    == C.inv().conjugate().T * (T.conjugate().T * T) * C.inv()
)
checks["exact_margin_not_invariant"] = target_lower != source_lower

# Kernel and finite repair transport through a nonunitary shear.
Cs = s.Matrix([[1, 2], [0, 1]])
D = s.Matrix([[1, 0]])
K = s.Matrix([[0, 1]])
Dp = D * Cs.inv()
Kp = K * Cs.inv()
source_kernel = D.nullspace()[0]
target_kernel = Dp.nullspace()[0]
checks["kernel_transports"] = target_kernel.row_join(Cs * source_kernel).rank() == 1
checks["source_repair_injective"] = K * source_kernel != s.zeros(1, 1)
checks["target_repair_injective"] = Kp * target_kernel != s.zeros(1, 1)
checks["repaired_row_invertible"] = Dp.col_join(Kp).det() != 0

# Green form transport: C is not Hilbert unitary, but transported J is exact.
J = s.diag(-1, 1)
Jp = Cs.inv().conjugate().T * J * Cs.inv()
checks["nonunitary"] = Cs.conjugate().T * Cs != s.eye(2)
checks["transported_green_identity"] = Cs.conjugate().T * Jp * Cs == J
checks["fixed_green_identity_fails"] = Cs.conjugate().T * J * Cs != J

# Standard conjugation transported through a complex shear.
Cc = s.Matrix([[1, s.I], [0, 1]])
R_linear_part = Cc * Cc.conjugate().inv()  # R'=S K
checks["transported_real_involution"] = (
    s.simplify(R_linear_part * R_linear_part.conjugate()) == s.eye(2)
)
checks["fixed_standard_real_fails"] = Cc != Cc.conjugate()

# Similarity by a nonunitary matrix is not a star map.
A = s.Matrix([[0, 1], [0, 0]])
phi_Astar = Cs * A.conjugate().T * Cs.inv()
phi_A_star = (Cs * A * Cs.inv()).conjugate().T
checks["nonunitary_similarity_not_star_map"] = phi_Astar != phi_A_star

# Hostile assertions each retain an exact nonzero residual.
residuals = {
    "claim_exact_lower_invariance": target_lower - source_lower,
    "claim_exact_upper_invariance": target_upper - source_upper,
    "claim_fixed_green_compatibility": Cs.conjugate().T * J * Cs - J,
    "claim_fixed_real_compatibility": Cc - Cc.conjugate(),
    "claim_similarity_is_star_map": phi_Astar - phi_A_star,
    "forget_to_transport_repair": K * target_kernel,
}
deliberate_failures = {
    key: {"residual": str(value), "nonzero": value != 0 and value != s.zeros(*value.shape) if isinstance(value, s.MatrixBase) else value != 0}
    for key, value in residuals.items()
}
checks["all_hostile_residuals_nonzero"] = all(x["nonzero"] for x in deliberate_failures.values())

passed = all(checks.values())
result = {
    "schema": "marici.voevodsky.nonunitary-condition-number-check.v1",
    "scope": "Exact finite matrices; infinite-dimensional Calkin transport remains theorem-level.",
    "checker_sha256": hashlib.sha256(CHECKER.read_bytes()).hexdigest(),
    "checks": checks,
    "sharp_model": {
        "C": str(C), "T": str(T), "T_prime": str(Tp),
        "source_bounds": [str(source_lower), str(source_upper)],
        "target_bounds": [str(target_lower), str(target_upper)]
    },
    "deliberate_failures": deliberate_failures,
    "passed": passed,
}
RESULT.parent.mkdir(parents=True, exist_ok=True)
RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": passed, "check_count": len(checks), "hostile_residuals": len(deliberate_failures)}))
raise SystemExit(0 if passed else 1)
