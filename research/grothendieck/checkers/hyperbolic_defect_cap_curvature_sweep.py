"""Hostile test on the concavity-cap enlargement of the source carrier."""

import json
import math
import random
import argparse

from hyperbolic_boundary_critical_curvature_sweep import directional_curvature


def g_value(t, r, p, q):
    slope_sum, product = p+q, p*q
    nt = (4*t**3+2*t*product-2*t*(2+product)*r*r
          -slope_sum*r*(1-r*r))
    nr = (-t*slope_sum+2*(1-2*t*t-t*t*product)*r
          +3*t*slope_sum*r*r)
    return (1-t*t)*nt+p*(1-r*r)*nr


parser = argparse.ArgumentParser()
parser.add_argument("--cap-multiplier", type=float, default=1.0)
parser.add_argument("--trials", type=int, default=200_000)
parser.add_argument("--absolute-defect-max", type=float)
arguments = parser.parse_args()

rng = random.Random(20260823)
trials = arguments.trials
roots = 0
failures = 0
largest = (-math.inf, None)
for _ in range(trials):
    p = 0.1+0.899999*rng.random()
    c = rng.random()
    q = c*p
    a, b = math.atanh(p), math.atanh(q)
    defect_cap = (a-b)*(p-q)/4
    if arguments.absolute_defect_max is None:
        defect = rng.random()*defect_cap*arguments.cap_multiplier
    else:
        defect = rng.random()*arguments.absolute_defect_max

    def evaluate(x):
        t = math.tanh(x)
        r = math.tanh(p*x-defect)
        return g_value(t,r,p,q)

    start = defect/p+1e-12
    previous_x, previous_g = start, evaluate(start)
    brackets = []
    for index in range(1, 121):
        current_x = start+12*index/120
        current_g = evaluate(current_x)
        if previous_g*current_g < 0:
            brackets.append((previous_x, current_x))
        previous_x, previous_g = current_x, current_g
    if not brackets:
        continue
    for lo, hi in brackets:
        sign_lo = evaluate(lo)
        for _ in range(70):
            mid = (lo+hi)/2
            if evaluate(mid)*sign_lo > 0:
                lo = mid
            else:
                hi = mid
        x = (lo+hi)/2
        t, r = math.tanh(x), math.tanh(p*x-defect)
        curvature = directional_curvature(t,r,p,q)
        roots += 1
        if curvature > largest[0]:
            largest = (curvature, (p,c,defect,defect_cap,x,t,r))
        if curvature >= 1e-10:
            failures += 1

print(json.dumps({
    "trials": trials,
    "cap_multiplier": arguments.cap_multiplier,
    "absolute_defect_max": arguments.absolute_defect_max,
    "roots": roots,
    "failures": failures,
    "largest_DG": largest,
}, indent=2))
