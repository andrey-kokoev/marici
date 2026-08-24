"""Hostile comparison of D=G_q and G zero locations on exact orbits."""

import json
import math
import random

from hyperbolic_boundary_critical_curvature_sweep import state
from hyperbolic_boundary_unimodality_sweep import boundary_derivative


def denominator(p, q, holding):
    t, r = state(p, q, holding)
    z = r / t
    x = t * t
    return p - z + x * (-2*p*p*z + 3*p*z*z - 2*p + z)


def first_root(function, p, q):
    grid = [10.0 ** (-8 + 12 * i / 239) for i in range(240)]
    previous_x = grid[0]
    previous = function(p, q, previous_x)
    for current_x in grid[1:]:
        current = function(p, q, current_x)
        if previous == 0 or previous * current < 0:
            lo, hi = previous_x, current_x
            for _ in range(60):
                mid = (lo + hi) / 2
                if function(p, q, lo) * function(p, q, mid) <= 0:
                    hi = mid
                else:
                    lo = mid
            return (lo + hi) / 2
        previous_x, previous = current_x, current
    return None


rng = random.Random(20260823)
trials = 20_000
both = 0
ordering_failures = 0
minimum_gap = (math.inf, None)
for _ in range(trials):
    p = rng.random()
    q = rng.random() * p
    d_root = first_root(denominator, p, q)
    g_root = first_root(boundary_derivative, p, q)
    if d_root is None or g_root is None:
        continue
    both += 1
    gap = g_root - d_root
    if gap < minimum_gap[0]:
        minimum_gap = (gap, (p, q, d_root, g_root))
    if gap <= -1e-10:
        ordering_failures += 1

print(json.dumps({
    "trials": trials,
    "pairs_with_both_roots": both,
    "failures_of_D_root_before_G_root": ordering_failures,
    "minimum_LG_minus_LD": minimum_gap,
}, indent=2))
