#!/usr/bin/env python3
"""Verify the Sobolev zero forger and its infinity-trace rejection."""

import cmath
import math


z = complex(0.3, 0.8)

# Exact source f(q)=exp(-q).
g_plus_0 = 1.0 / (1.0 - z)
g_minus_0 = 1.0 / (1.0 + z)
x_value = g_plus_0 + g_minus_0
homogeneous_coefficient = -x_value

forged_readout = g_plus_0 + homogeneous_coefficient + g_minus_0

# The added mode belongs to H1 for Re(z)>0.
homogeneous_l2_norm_sq = abs(homogeneous_coefficient) ** 2 / (2.0 * z.real)
homogeneous_derivative_norm_sq = abs(z) ** 2 * homogeneous_l2_norm_sq

# Its weighted infinity trace is exactly its coefficient.
infinity_trace = homogeneous_coefficient

# A sharp cutoff after R converges in H1 because the homogeneous tail decays.
def tail_graph_bound(radius: float) -> float:
    # Bounds both the removed tail and a unit-width cutoff derivative term.
    return (
        abs(homogeneous_coefficient) ** 2
        * math.exp(-2.0 * z.real * radius)
        * (1.0 + abs(z) ** 2 + 2.0 * z.real)
        / (2.0 * z.real)
    )


checks = {
    "homogeneous_mode_is_h1": homogeneous_l2_norm_sq > 0.0 and homogeneous_derivative_norm_sq > 0.0,
    "homogeneous_mode_forges_zero": abs(forged_readout) < 1.0e-14,
    "source_infinity_trace_rejects_forger": abs(infinity_trace) > 1.0,
    "cutoff_sequence_converges_in_graph_norm": tail_graph_bound(80.0) < 1.0e-18,
    "weighted_trace_is_not_graph_closed": abs(infinity_trace) > 0.0 and tail_graph_bound(80.0) < 1.0e-18,
}

failed = [name for name, passed in checks.items() if not passed]
print(
    {
        "passed": len(checks) - len(failed),
        "total": len(checks),
        "failed": failed,
        "original_readout": x_value,
        "forged_readout": forged_readout,
        "infinity_trace": infinity_trace,
        "cutoff_graph_bound_R80": tail_graph_bound(80.0),
    }
)

if failed:
    raise SystemExit(1)

