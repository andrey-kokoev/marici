"""Hostile sweep for the affine-denominator reachable wedge at G=0."""

import json
import math
import random

from hyperbolic_boundary_critical_curvature_sweep import state
from hyperbolic_boundary_unimodality_sweep import boundary_derivative


rng = random.Random(20260823)
trials = 50_000
minimum_lower = (math.inf, None)
minimum_upper = (math.inf, None)
failures = 0
for _ in range(trials):
    p = rng.random()
    q = rng.random() * p
    lo, hi = 1e-10, 1.0
    while boundary_derivative(p, q, hi) > 0:
        hi *= 2
    for _ in range(60):
        mid = (lo + hi) / 2
        if boundary_derivative(p, q, mid) > 0:
            lo = mid
        else:
            hi = mid
    holding = (lo + hi) / 2
    t, r = state(p, q, holding)
    z = r / t
    upper = (p + math.sqrt(p * p + 3.0)) / 3.0
    lower_margin = z - p
    upper_margin = upper - z
    package = (p, q, holding, t, z, upper)
    if lower_margin < minimum_lower[0]:
        minimum_lower = (lower_margin, package)
    if upper_margin < minimum_upper[0]:
        minimum_upper = (upper_margin, package)
    if lower_margin <= -1e-12 or upper_margin <= -1e-12:
        failures += 1

print(json.dumps({
    "trials": trials,
    "wedge_failures_beyond_1e-12": failures,
    "minimum_z_minus_p": minimum_lower,
    "minimum_upper_minus_z": minimum_upper,
}, indent=2))
