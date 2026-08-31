#!/usr/bin/env python3
"""Two-chart descent transition audit with adjoint-pairing preservation."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "rh_two_chart_adjoint_pairing_transition_audit.json"


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return [list(row) for row in zip(*A)]


def det2(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def symplectic_pair(u, v):
    return u[0] * v[1] - u[1] * v[0]

J = [[Fraction(0), Fraction(1)], [Fraction(-1), Fraction(0)]]

# Single-Weyl obstruction: a chart jump with nonzero density cannot equal an
# entire section.  Track only the coefficient of pi*i.
rho = Fraction(5)
weyl_jump = 2 * rho
transition_jump = -weyl_jump
formal_jump_cancels = weyl_jump + transition_jump == 0

# Formal scalar descent can cancel the analytic jump while failing the boundary
# adjoint pairing.  Bad T rescales only the source/value coordinate.
T_bad = [[Fraction(2), Fraction(0)], [Fraction(0), Fraction(1)]]
T_good = [[Fraction(2), Fraction(0)], [Fraction(0), Fraction(1, 2)]]

u = [Fraction(3), Fraction(1)]
v = [Fraction(1), Fraction(4)]
orig_pair = symplectic_pair(u, v)

def act(T, x):
    return [sum(T[i][j] * x[j] for j in range(2)) for i in range(2)]

bad_pair = symplectic_pair(act(T_bad, u), act(T_bad, v))
good_pair = symplectic_pair(act(T_good, u), act(T_good, v))

bad_preserves_pairing = matmul(matmul(transpose(T_bad), J), T_bad) == J
good_preserves_pairing = matmul(matmul(transpose(T_good), J), T_good) == J

# Even a symplectic diagonal transition is not automatically source-derived:
# the ratio a versus a^{-1} is a graph-topology datum.  Powers along a path grow
# if no path-length/source bound is supplied.
powers_norm_prefix = [Fraction(2) ** n for n in range(1, 8)]
unbounded_transition_products = all(powers_norm_prefix[i] < powers_norm_prefix[i + 1] for i in range(len(powers_norm_prefix) - 1))
source_path_bound_present = False

# Same jump cancellation admits a family T_a=diag(a,1/a).  It preserves the
# symplectic pairing but changes observer graph norms; jump data alone does not
# choose the chart topology.
a_values = [Fraction(2), Fraction(3), Fraction(5)]
observer_norms = [a * a + Fraction(1, a * a) for a in a_values]
transition_family_not_fixed_by_jump = len(set(observer_norms)) == len(observer_norms)

checks = {
    "single_weyl_jump_requires_two_chart_descent": weyl_jump != 0,
    "formal_transition_can_cancel_jump": formal_jump_cancels,
    "formal_jump_cancellation_does_not_preserve_adjoint_pairing": bad_pair != orig_pair and not bad_preserves_pairing,
    "symplectic_transition_preserves_adjoint_pairing": good_pair == orig_pair and good_preserves_pairing and det2(T_good) == 1,
    "jump_data_does_not_fix_observer_graph_norm": transition_family_not_fixed_by_jump,
    "unbounded_transition_products_need_source_path_bound": unbounded_transition_products and not source_path_bound_present,
}

payload = {
    "schema": "marici.strominger.rh_two_chart_adjoint_pairing_transition_audit.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "jump_data": {"rho": str(rho), "weyl_jump": f"{weyl_jump}*pi*i", "transition_jump": f"{transition_jump}*pi*i"},
    "pairing_test": {
        "u": [str(x) for x in u],
        "v": [str(x) for x in v],
        "original_pair": str(orig_pair),
        "bad_transition_pair": str(bad_pair),
        "good_transition_pair": str(good_pair),
    },
    "symplectic_family_observer_norms": {str(a): str(n) for a, n in zip(a_values, observer_norms)},
    "transition_power_norm_prefix": [str(x) for x in powers_norm_prefix],
    "verdict": (
        "The two-chart descent direction survives only as a stricter source "
        "contract. Formal jump cancellation is too weak: it can fail the adjoint "
        "boundary pairing. Symplectic transitions preserve the pairing, but the "
        "jump data do not determine their graph norm or bound path products. A "
        "valid RH descent transition must therefore provide all three data before "
        "fitting Xi: spectral-jump cancellation, symplectic/adjoint-pairing "
        "preservation, and source path bounds for transition compositions."
    ),
    "checks": checks,
    "gate_count": len(checks),
    "passed_gate_count": sum(checks.values()),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
