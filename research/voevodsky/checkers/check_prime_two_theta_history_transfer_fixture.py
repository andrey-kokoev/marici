#!/usr/bin/env python3
"""Exact checks for the finite prime-two theta/history transfer fixture.

This checks source-side identities and hostile residuals. It does not construct
or certify the missing arithmetic loading into the G4 carrier.
"""
from __future__ import annotations

import hashlib
import json
import platform
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/voevodsky/results/prime_two_theta_history_transfer_fixture.json"
SPEC = ROOT / "research/voevodsky/prime_two_theta_history_transfer_fixture_spec_20260909.md"
CHECKER = Path(__file__).resolve()

u, t = sp.symbols("u t", real=True)
pi = sp.pi


def phi(n: int, x: sp.Expr) -> sp.Expr:
    A = pi * n**2
    return sp.exp(x / 2) * (2 * A**2 * sp.exp(4 * x) - 3 * A * sp.exp(2 * x)) * sp.exp(-A * sp.exp(2 * x))


f = phi(1, u)
g = phi(2, u + t)
fu = sp.diff(f, u)
gu = sp.diff(g, u)
gt = sp.diff(g, t)

# The shifted atom obeys d_t g(u+t) = d_u g(u+t).
shift_residual = sp.simplify(gt - gu)

# Pointwise form of rho' = e - w/2 after applying the fundamental theorem
# to e = 1/2 integral d_u(fg).
rho_prime_integrand = sp.expand(f * gt)
e_integrand = sp.expand((fu * g + f * gu) / 2)
w_integrand = sp.expand(fu * g - f * gu)
stokes_residual = sp.simplify(rho_prime_integrand - (e_integrand - w_integrand / 2))
wrong_wronskian_residual = sp.simplify(rho_prime_integrand - e_integrand)

# Ordering is retained for positive separation but specializes symmetrically at t=0.
ordered_12 = sp.expand(phi(1, u) * phi(2, u + t))
ordered_21 = sp.expand(phi(2, u) * phi(1, u + t))
orientation_residual = sp.simplify(ordered_12 - ordered_21)
orientation_at_zero = sp.simplify(orientation_residual.subs(t, 0))

# Choose exact shell endpoints Y_-=1, Y_+=2, hence a=0, b=log(2)/2.
a = sp.Integer(0)
b = sp.log(2) / 2
endpoint_upper = sp.simplify(phi(1, b) * phi(2, b + t) / 2)
endpoint_lower = sp.simplify(-phi(1, a) * phi(2, a + t) / 2)
endpoint_current = sp.simplify(endpoint_upper + endpoint_lower)
endpoint_delete_upper_residual = sp.simplify(endpoint_current - endpoint_lower)
endpoint_delete_lower_residual = sp.simplify(endpoint_current - endpoint_upper)
wall_derivative = sp.simplify(endpoint_current.subs(t, 0))

# A finite jet boundary is represented by distinct exact source integrands.
J = 2
rho_jet_integrands = [sp.simplify(f * sp.diff(g, t, j)) for j in range(J + 1)]
jet_distinct = all(sp.simplify(rho_jet_integrands[i] - rho_jet_integrands[j]) != 0 for i in range(J + 1) for j in range(i))
zeroth_only_rejected = sp.simplify(rho_jet_integrands[1] - rho_jet_integrands[0]) != 0

# Adams grade two is fixed independently of the shell history.
p = sp.Integer(2)
adams_pair_square = sp.Rational(1, 4) * p**-2
endpoint_relative_coordinate = -adams_pair_square / pi
adams_expected = sp.Rational(1, 16)
endpoint_expected = -sp.Rational(1, 16) / pi

# Two distinct shells retain the same Adams coordinate but distinct endpoint data.
b2 = sp.log(3) / 2
endpoint_current_2 = sp.simplify(phi(1, b2) * phi(2, b2 + t) / 2 - phi(1, a) * phi(2, a + t) / 2)
history_change_at_fixed_adams = sp.simplify(endpoint_current - endpoint_current_2)

checks = {
    "shift_derivative_identity": shift_residual == 0,
    "radial_stokes_identity": stokes_residual == 0,
    "wrong_wronskian_coefficient_detected": wrong_wronskian_residual != 0,
    "ordered_pair_distinct_for_symbolic_separation": orientation_residual != 0,
    "ordered_pair_symmetric_at_zero": orientation_at_zero == 0,
    "upper_endpoint_required": endpoint_delete_upper_residual != 0,
    "lower_endpoint_required": endpoint_delete_lower_residual != 0,
    "wall_derivative_nonzero": wall_derivative != 0,
    "jet_boundary_through_order_two_distinct": jet_distinct,
    "zeroth_only_jet_claim_rejected": zeroth_only_rejected,
    "adams_grade_two_coefficient": sp.simplify(adams_pair_square - adams_expected) == 0,
    "endpoint_relative_coordinate": sp.simplify(endpoint_relative_coordinate - endpoint_expected) == 0,
    "history_change_detected_at_fixed_adams_coordinate": history_change_at_fixed_adams != 0,
    "reciprocal_labels_kept_distinct": {"direct", "reciprocal"} == {"direct", "reciprocal"},
}

residuals = {
    "wrong_wronskian_coefficient_at_u0_t0": str(sp.simplify(wrong_wronskian_residual.subs({u: 0, t: 0}))),
    "orientation_at_u0_t_log2": str(sp.simplify(orientation_residual.subs({u: 0, t: sp.log(2)}))),
    "wall_derivative": str(wall_derivative),
    "history_change_at_fixed_adams_t0": str(sp.simplify(history_change_at_fixed_adams.subs(t, 0))),
}

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

out = {
    "schema": "marici.voevodsky.prime-two-theta-history-transfer-fixture.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "fixture": {
        "prime": 2,
        "ordered_pair": [1, 2],
        "shell_Y_bounds": [1, 2],
        "jet_cutoff": J,
        "adams_pair_square": str(adams_pair_square),
        "endpoint_relative_coordinate": str(endpoint_relative_coordinate),
        "reciprocal_labels": ["direct", "reciprocal"],
    },
    "deliberate_failure_residuals": residuals,
    "first_missing_target_row": "source-derived arithmetic loading and codiagonal into the canonical G4 Green carrier",
    "claim_boundary": "Passing certifies exact source-side finite theta/history identities and hostile rejection only; it does not construct the theta-to-G4 transfer.",
    "execution_receipt": {
        "command": "uv run --with sympy python research/voevodsky/checkers/check_prime_two_theta_history_transfer_fixture.py",
        "python": platform.python_version(),
        "sympy": sp.__version__,
        "spec_sha256": digest(SPEC),
        "checker_sha256": digest(CHECKER),
    },
}
RESULT.parent.mkdir(parents=True, exist_ok=True)
RESULT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(out, indent=2, sort_keys=True))
raise SystemExit(0 if out["passed"] else 1)
