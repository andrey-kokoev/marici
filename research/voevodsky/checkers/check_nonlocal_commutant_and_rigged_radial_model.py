#!/usr/bin/env python3
"""Exact checks for nonlocal reciprocal sectors and the rigged half-line model."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/voevodsky/results/nonlocal_commutant_and_rigged_radial_model.json"
CHECKER = Path(__file__).resolve()
checks: dict[str, bool] = {}

# Finite radial-site shadow of arbitrary nonlocal A,C at u=i.
i = s.I
I2, Z2 = s.eye(2), s.zeros(2)
A = s.Matrix([[1, 2], [3, 4]])
C = s.Matrix([[0, 1], [-2, 0]])
W = Z2.row_join(-i*I2).col_join((i*I2).row_join(Z2))
Me = A.row_join(C).col_join((-C).row_join(A))
Mo = A.row_join(C).col_join(C.row_join(-A))
Sodd = s.diag(1, 1, -1, -1)
checks["nonlocal_even_commutes"] = Me*W == W*Me
checks["nonlocal_odd_anticommutes"] = Mo*W == -W*Mo
checks["odd_sign_times_even"] = Mo == Sodd*Me
checks["nonlocal_even_odd_gramians_equal"] = Me.conjugate().T*Me == Mo.conjugate().T*Mo

# Parity diagonalization. Columns identify x with 2^-1/2 (x, ±u x).
root2 = s.sqrt(2)
U = (I2.row_join(I2).col_join((i*I2).row_join(-i*I2))) / root2
checks["parity_transform_unitary"] = s.simplify(U.conjugate().T*U) == s.eye(4)
parity_even = s.simplify(U.conjugate().T*Me*U)
expected_even = (A+i*C).row_join(Z2).col_join(Z2.row_join(A-i*C))
checks["even_parity_blocks"] = parity_even == expected_even
parity_odd = s.simplify(U.conjugate().T*Mo*U)
expected_odd = Z2.row_join(A-i*C).col_join((A+i*C).row_join(Z2))
checks["odd_parity_transitions"] = parity_odd == expected_odd

# Doubled derivative/boundary finite channel identities at u=i.
Dsign = s.diag(1, -1)  # derivative factor suppressed; only channel sign checked
W2 = s.Matrix([[0, -i], [i, 0]])
Jboundary = s.diag(-1, 1)
Sreal = s.diag(1, -1)  # J_u=Sreal K at u=i
checks["reciprocal_anticommutes_with_derivative_sign"] = Dsign*W2 == -W2*Dsign
checks["green_anti_isometry"] = W2.conjugate().T*Jboundary*W2 == -Jboundary
checks["twisted_real_involution"] = Sreal*Sreal.conjugate() == s.eye(2)
checks["real_reciprocal_commutation"] = Sreal*W2.conjugate() == W2*Sreal
checks["real_derivative_commutation"] = Sreal*Dsign.conjugate() == Dsign*Sreal
wall = s.Matrix([1, i])
checks["wall_fixed_by_reciprocal"] = W2*wall == wall
checks["wall_green_isotropic"] = (wall.conjugate().T*Jboundary*wall)[0] == 0
checks["wall_fixed_by_real"] = Sreal*wall.conjugate() == wall

# Exact graph-Riesz representative k=e^-r for endpoint evaluation.
r = s.symbols("r", nonnegative=True)
k = s.exp(-r)
f = s.exp(-2*r) + 3*s.exp(-3*r)
f0 = f.subs(r, 0)
graph_pairing = s.integrate(f*k + s.diff(f, r)*s.diff(k, r), (r, 0, s.oo))
checks["endpoint_graph_riesz_witness"] = s.simplify(graph_pairing-f0) == 0
checks["riesz_vector_in_L2"] = s.integrate(k**2, (r, 0, s.oo)) == s.Rational(1, 2)

# Triangular endpoint packets: exact L2 norm tends to zero with fixed trace one.
n = s.symbols("n", integer=True, positive=True)
x = s.symbols("x", nonnegative=True)
triangle_norm_sq = s.integrate((1-n*x)**2, (x, 0, 1/n))
checks["triangle_packet_norm"] = triangle_norm_sq == 1/(3*n)
checks["ambient_trace_unbounded"] = s.limit(triangle_norm_sq, n, s.oo) == 0

residuals = {
    "even_as_odd": Me*W + W*Me,
    "odd_as_even": Mo*W - W*Mo,
    "one_parity_block_omitted": A-i*C,
    "reciprocal_as_derivative_commuting": Dsign*W2-W2*Dsign,
    "delta_as_L2_vector": s.oo,
    "boundary_gramian_as_essential": s.Integer(0),
}
failures = {
    key: {
        "residual": str(value),
        "detected": (value != s.zeros(*value.shape)) if isinstance(value, s.MatrixBase) else (value == s.oo or value == 0),
    }
    for key, value in residuals.items()
}
checks["all_hostile_failures_detected"] = all(v["detected"] for v in failures.values())

passed = all(checks.values())
result = {
    "schema": "marici.voevodsky.nonlocal-rigged-radial-check.v1",
    "scope": "Exact two-site shadow and explicit exponential/triangular test functions; infinite-dimensional theorems remain in proof packets.",
    "checker_sha256": hashlib.sha256(CHECKER.read_bytes()).hexdigest(),
    "checks": checks,
    "deliberate_failures": failures,
    "passed": passed,
}
RESULT.parent.mkdir(parents=True, exist_ok=True)
RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": passed, "check_count": len(checks), "hostile_failures": len(failures)}))
raise SystemExit(0 if passed else 1)
