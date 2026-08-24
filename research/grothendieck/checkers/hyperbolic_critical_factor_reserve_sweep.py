"""Profile eliminated factor reserves on exact reachable G=0 orbits."""

import json
import math
import random

from hyperbolic_boundary_critical_curvature_sweep import state, directional_curvature
from hyperbolic_boundary_unimodality_sweep import boundary_derivative


rng = random.Random(20260823)
trials = 100_000
largest_d = (-math.inf, None)
largest_pfactor = (-math.inf, None)
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
    z, x = r / t, t * t
    d = p - z + x * (-2*p*p*z + 3*p*z*z - 2*p + z)
    dg = directional_curvature(t, r, p, q)
    pfactor = -dg * d / (2 * x)
    package = (p, q, holding, t, z)
    if d > largest_d[0]:
        largest_d = (d, package)
    if pfactor > largest_pfactor[0]:
        largest_pfactor = (pfactor, package)
    if d >= 1e-12 or pfactor >= 1e-12:
        failures += 1

print(json.dumps({
    "trials": trials,
    "nonnegative_factor_failures_beyond_1e-12": failures,
    "largest_D": largest_d,
    "largest_P": largest_pfactor,
}, indent=2))
