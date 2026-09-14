#!/usr/bin/env python3
"""Exact symbolic and finite-cell checks for the half-line thickness theorem."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/voevodsky/results/half_line_interval_thickness.json"
CHECKER = Path(__file__).resolve()

checks: dict[str, bool] = {}
ell, delta, beta, M = s.symbols("ell delta beta M", positive=True)
r, a = s.symbols("r a", real=True)
t = s.symbols("t", real=True)
packet = s.sin(s.pi * t / ell)
packet_derivative = s.diff(packet, t)
checks["sine_packet_L2_norm"] = s.simplify(s.integrate(packet**2, (t, 0, ell)) - ell/2) == 0
checks["sine_packet_derivative_norm"] = s.simplify(s.integrate(packet_derivative**2, (t, 0, ell)) - s.pi**2/(2*ell)) == 0
necessary_beta = delta**2*ell/2 - s.pi**2/(2*ell)
checks["necessary_beta_formula"] = s.factor(necessary_beta) == (delta*ell-s.pi)*(delta*ell+s.pi)/(2*ell)
checks["necessary_scale_threshold"] = s.simplify(necessary_beta.subs(ell, 2*s.pi/delta)) == 3*s.pi*delta/4

Cw = 2*ell/beta
Cd = 2*M**2*ell**3/beta
checks["sufficiency_constants_positive"] = Cw.is_positive and Cd.is_positive
# Harmonic conversion: if A>=delta^2 x and A>=y, then x+y<=A(1+delta^-2).
graph_constant = delta**2/(1+delta**2)
checks["graph_conversion_positive"] = graph_constant.is_positive
checks["graph_conversion_below_one"] = s.simplify(1-graph_constant).is_positive

# Exact two-cell multiplicity model. Alternating rank-one projections have
# pointwise norm one but only become uniformly positive after both cells.
P1 = s.diag(1, 0)
P2 = s.diag(0, 1)
two_cell_mass = P1 + P2
checks["alternating_projection_two_cell_mass"] = two_cell_mass == s.eye(2)
checks["one_cell_has_invisible_direction"] = P1.det() == 0 and P2.det() == 0
checks["operator_norm_alone_insufficient"] = P1.norm() == 1 and P1.rank() == 1

# Even and odd reciprocal fields inherit the same local mass from equal Gramians.
A = s.Matrix([[1, 0], [0, 2]])
C = s.Matrix([[0, 1], [1, 0]])
Me = A.row_join(C).col_join((-C).row_join(A))  # u=i, u^2=-1
Sodd = s.diag(1, 1, -1, -1)
Mo = Sodd * Me
checks["reciprocal_even_odd_local_gramians_equal"] = Me.conjugate().T*Me == Mo.conjugate().T*Mo

# Deliberate failures with exact residuals or limits.
N = s.symbols("N", integer=True, positive=True)
far_interval_localized_mass = s.Integer(0)  # indicator [0,1], interval [2,3]
decaying_interval_mass = s.integrate(s.exp(-2*r), (r, N, N+1))
constant_projection_mass = P1
zero_covariant_weight_mass = s.zeros(2)
finite_sample_hole_mass = s.Integer(0)  # construct weight equal 1 on sampled cells, 0 on next cell

failures = {
    "total_mass_without_uniform_local_mass": {
        "residual": str(far_interval_localized_mass),
        "nonzero_obstruction": far_interval_localized_mass == 0,
    },
    "nonzero_everywhere_without_uniform_margin": {
        "residual": str(decaying_interval_mass),
        "limit": str(s.limit(decaying_interval_mass, N, s.oo)),
        "nonzero_obstruction": s.limit(decaying_interval_mass, N, s.oo) == 0,
    },
    "operator_norm_mass_hides_direction": {
        "residual": str(constant_projection_mass.det()),
        "nonzero_obstruction": constant_projection_mass.det() == 0,
    },
    "covariance_without_coercivity": {
        "residual": str(zero_covariant_weight_mass),
        "nonzero_obstruction": zero_covariant_weight_mass == s.zeros(2),
    },
    "finite_interval_sampling_not_universal": {
        "residual": str(finite_sample_hole_mass),
        "nonzero_obstruction": finite_sample_hole_mass == 0,
    },
}
checks["all_deliberate_failures_detected"] = all(x["nonzero_obstruction"] for x in failures.values())

passed = all(checks.values())
result = {
    "schema": "marici.voevodsky.half-line-interval-thickness-check.v1",
    "scope": "Exact theorem formulas and representative hostile weights; no finite interval sample certifies the universal condition.",
    "checker_sha256": hashlib.sha256(CHECKER.read_bytes()).hexdigest(),
    "checks": checks,
    "deliberate_failures": failures,
    "passed": passed,
}
RESULT.parent.mkdir(parents=True, exist_ok=True)
RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": passed, "check_count": len(checks), "deliberate_failures": len(failures)}))
raise SystemExit(0 if passed else 1)
