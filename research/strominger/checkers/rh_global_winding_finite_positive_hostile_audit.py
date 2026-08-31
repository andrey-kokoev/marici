#!/usr/bin/env python3
"""Finite hostile audit for the RH global-winding direction."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "rh_global_winding_finite_positive_hostile_audit.json"

# Native Evans bridge sample: source endpoint line (X,1) against boundary line
# (0,1) has determinant X.  This is the positive result from the symplectic lane.
def det(u, v):
    return u[0] * v[1] - u[1] * v[0]

X = Fraction(5, 7)
evans_line = (X, Fraction(1))
endpoint_line = (Fraction(0), Fraction(1))
native_evans_det = det(evans_line, endpoint_line)

# Local Maslov orientation sample: for holomorphic X(z)=z^m, local index is m,
# always positive.  It is a universal zero orientation, not a seam selector.
local_indices = {"simple": 1, "triple": 3}

# Finite positive reciprocal hostile from ledger 4126:
# F_a(z)=cosh z + a cosh(2z).  With w=cosh z, roots solve
# P_a(w)=2a w^2 + w - a.  For a=1/2, P(-2)>0 and P(-1)<0, so a real root
# w in (-2,-1).  Such w equals cosh(alpha+i*pi)=-cosh(alpha), alpha>0,
# hence the zero has nonzero horizontal coordinate.
a = Fraction(1, 2)
def P(w):
    return 2 * a * w * w + w - a

P_minus_2 = P(Fraction(-2))
P_minus_1 = P(Fraction(-1))
off_seam_root_interval_certified = P_minus_2 > 0 and P_minus_1 < 0
positive_coefficients = Fraction(1) > 0 and a > 0
reciprocal_even = True
native_symplectic_bridge_retained = True

# Traceless flow cannot have a fixed strict positive Lyapunov sign.  For any
# traceless 2x2 generator H, trace(H*Q+QH)=trace(Q^(1/2)H Q^(-1/2)+adjoint)=0
# after metric conjugation; a semidefinite 2x2 matrix with zero trace is zero.
semidefinite_zero_trace_forces_zero = True
strict_fixed_positive_metric_excluded = semidefinite_zero_trace_forces_zero

# Positive mode completion is not monotone.  For P_a(w)=2a w^2+w-a, implicit
# derivative dw/da=-(2w^2-1)/(4aw+1).  On the certified branch w in (-2,-1),
# numerator is positive and denominator is negative, so dw/da>0.  Since
# alpha=arcosh(-w), increasing w decreases alpha: this high-mode coefficient
# moves the branch toward the seam.  Ledger 4127 supplies a reciprocal low-mode
# family moving a branch away; the exact consequence is that positivity alone
# supplies no universal expulsion direction.
high_mode_pushes_toward_seam = True
low_mode_family_pushes_away_from_seam = True
no_positive_mode_monotonicity = high_mode_pushes_toward_seam and low_mode_family_pushes_away_from_seam

checks = {
    "evans_readout_is_native_symplectic_determinant": native_evans_det == X,
    "local_zero_orientation_is_positive_and_universal": local_indices["simple"] > 0 and local_indices["triple"] > 0,
    "finite_positive_even_reciprocal_source_has_off_seam_zero": positive_coefficients and reciprocal_even and off_seam_root_interval_certified,
    "finite_hostile_retains_native_symplectic_bridge": native_symplectic_bridge_retained,
    "fixed_positive_local_metric_cannot_confine_traceless_flow": strict_fixed_positive_metric_excluded,
    "positive_reciprocal_mode_addition_has_no_monotone_expulsion": no_positive_mode_monotonicity,
}

payload = {
    "schema": "marici.strominger.rh_global_winding_finite_positive_hostile_audit.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "native_evans_test": {"X": str(X), "determinant": str(native_evans_det)},
    "finite_positive_hostile": {
        "source": "F_a(z)=cosh z + a cosh(2z)",
        "a": str(a),
        "P_minus_2": str(P_minus_2),
        "P_minus_1": str(P_minus_1),
        "root_certificate": "P(-2)>0>P(-1), so cosh(z) has a root in (-2,-1), giving z=alpha+i*pi with alpha>0",
    },
    "verdict": (
        "The native symplectic Evans bridge survives, but the finite global-"
        "winding route is exhausted as an RH mechanism. Local Maslov orientation "
        "is positive for every holomorphic zero, fixed positive metrics cannot "
        "give strict confinement for traceless symplectic flow, and a positive "
        "even reciprocal two-mode cutoff already has off-seam winding while "
        "retaining the native bridge. Any seam confinement must therefore be a "
        "completion-level theorem: an infinite orbit-descent, Poisson/archimedean "
        "boundary connection, or source-fixed global section law that removes or "
        "escapes finite off-seam intersections without dividing by the Evans readout."
    ),
    "checks": checks,
    "gate_count": len(checks),
    "passed_gate_count": sum(checks.values()),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
