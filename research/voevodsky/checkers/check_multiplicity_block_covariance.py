#!/usr/bin/env python3
"""Exact hostile checks for multiplicity-valued reciprocal/Real block multipliers."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/voevodsky/results/multiplicity_block_covariance.json"
CHECKER = Path(__file__).resolve()

n = 2
I = s.I
I2 = s.eye(n)
Z2 = s.zeros(n)
u = I
u2 = -1

# Standard conjugation on K=C^2. A is real; C=iR is twisted-real: conjugate(C)=u^2 C.
A = s.Matrix([[1, 2], [0, 3]])
R = s.Matrix([[0, 1], [2, 0]])
C = I * R
checks: dict[str, bool] = {}
checks["A_and_C_do_not_commute"] = A * C != C * A
checks["A_real"] = A.conjugate() == A
checks["C_twisted_real"] = C.conjugate() == u2 * C

W = Z2.row_join((1/u) * I2).col_join((u * I2).row_join(Z2))
Sreal = I2.row_join(Z2).col_join(Z2.row_join(u2 * I2))
Sodd = I2.row_join(Z2).col_join(Z2.row_join(-I2))

M_even = A.row_join(C).col_join((u2 * C).row_join(A))
M_odd = A.row_join(C).col_join((-u2 * C).row_join(-A))

checks["reciprocal_involution"] = s.simplify(W * W) == s.eye(2*n)
checks["even_commutes_with_reciprocal"] = s.simplify(M_even * W - W * M_even) == s.zeros(2*n)
checks["odd_anticommutes_with_reciprocal"] = s.simplify(M_odd * W + W * M_odd) == s.zeros(2*n)
checks["even_fixed_fiber_real"] = s.simplify(M_even * Sreal - Sreal * M_even.conjugate()) == s.zeros(2*n)
checks["odd_fixed_fiber_real"] = s.simplify(M_odd * Sreal - Sreal * M_odd.conjugate()) == s.zeros(2*n)
checks["odd_is_unitary_sign_times_even"] = s.simplify(M_odd - Sodd * M_even) == s.zeros(2*n)
checks["even_odd_gramians_equal"] = s.simplify(M_even.conjugate().T * M_even - M_odd.conjugate().T * M_odd) == s.zeros(2*n)

# Diagonal subfamily recovers scalar-pattern parity with C=0.
M_diag_even = A.row_join(Z2).col_join(Z2.row_join(A))
M_diag_odd = A.row_join(Z2).col_join(Z2.row_join(-A))
checks["diagonal_even_recovered"] = M_diag_even * W == W * M_diag_even
checks["diagonal_odd_recovered"] = M_diag_odd * W == -W * M_diag_odd

# Hostile mutations must produce exact nonzero residuals.
M_bad_even_D = A.row_join(C).col_join(C.row_join(A))  # D=C instead of u^2 C=-C
M_bad_odd_B = A.row_join(C).col_join((-u2*C).row_join(A))  # B=A instead of -A
C_bad_real = R
M_bad_real = A.row_join(C_bad_real).col_join((u2*C_bad_real).row_join(A))

residuals = {
    "even_wrong_lower_left_phase": M_bad_even_D * W - W * M_bad_even_D,
    "odd_wrong_lower_right_sign": M_bad_odd_B * W + W * M_bad_odd_B,
    "off_diagonal_not_twisted_real": M_bad_real * Sreal - Sreal * M_bad_real.conjugate(),
    "even_as_odd_variance": M_even * W + W * M_even,
    "odd_as_even_variance": M_odd * W - W * M_odd,
}
deliberate_failures = {
    name: {"residual": str(s.simplify(value)), "nonzero": s.simplify(value) != s.zeros(2*n)}
    for name, value in residuals.items()
}
checks["all_hostile_residuals_nonzero"] = all(x["nonzero"] for x in deliberate_failures.values())

# Full ambient commutant is larger than pointwise multipliers: finite radial swap commutes with W
# but mixes radial sites, represented on radial_site tensor channel tensor multiplicity.
Rswap = s.Matrix([[0, 1], [1, 0]])
W_total = s.kronecker_product(s.eye(2), W)
nonlocal_commuter = s.kronecker_product(Rswap, s.eye(2*n))
checks["nonlocal_commutant_witness"] = nonlocal_commuter * W_total == W_total * nonlocal_commuter
checks["nonlocal_witness_moves_radial_sites"] = nonlocal_commuter != s.eye(4*n)

passed = all(checks.values())
result = {
    "schema": "marici.voevodsky.multiplicity-block-covariance-check.v1",
    "scope": "Exact C^2 multiplicity witness at u=i; general classification remains in the symbolic block proof packet.",
    "checker_sha256": hashlib.sha256(CHECKER.read_bytes()).hexdigest(),
    "checks": checks,
    "deliberate_failures": deliberate_failures,
    "passed": passed,
}
RESULT.parent.mkdir(parents=True, exist_ok=True)
RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": passed, "check_count": len(checks), "hostile_residuals": len(deliberate_failures)}))
raise SystemExit(0 if passed else 1)
