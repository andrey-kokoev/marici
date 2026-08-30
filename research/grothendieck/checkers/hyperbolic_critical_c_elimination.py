"""Eliminate the affine slope ratio c=q/p from G=0 and DG."""

import sympy as sp
import random
import math

from hyperbolic_boundary_critical_curvature_sweep import state
from hyperbolic_boundary_unimodality_sweep import boundary_derivative

p, r, t, c = sp.symbols("p r T c")
q = c*p
s = p+q
product = p*q

nt = 4*t**3 + 2*t*product - 2*t*(2+product)*r**2 - s*r*(1-r**2)
nr = -t*s + 2*(1-2*t**2-t**2*product)*r + 3*t*s*r**2
vt = 1-t**2
vr = p*(1-r**2)
g = sp.expand(vt*nt + vr*nr)

ntt = sp.diff(nt, t)
ntr = sp.diff(nt, r)
nrr = sp.diff(nr, r)
dg = sp.expand(-2*t*vt*nt - 2*p*r*vr*nr + vt**2*ntt + 2*vt*vr*ntr + vr**2*nrr)

g0 = sp.expand(g.subs(c, 0))
g1 = sp.expand(sp.diff(g, c))
k0 = sp.expand(dg.subs(c, 0))
k1 = sp.expand(sp.diff(dg, c))
assert sp.expand(g - (g0+c*g1)) == 0
assert sp.expand(dg - (k0+c*k1)) == 0

# At a critical point c=-g0/g1, hence DG=(k0*g1-k1*g0)/g1.
numerator = sp.factor(k0*g1-k1*g0)
print("g1_factor=", sp.factor(g1))
print("eliminated_numerator_factor=", numerator)
print("degrees=", sp.Poly(numerator, p, r, t).degree_list())

functions = sp.lambdify((p, r, t), (g0, g1, numerator), "math")
rng = random.Random(20260823)
bracketed = 0
bad_slope = 0
bad_resultant = 0
closest_slope = (float("inf"), None)
closest_resultant = (float("inf"), None)
for _ in range(1_000_000):
    pv, rv, tv = rng.random(), rng.random(), rng.random()
    a, b, e = functions(pv, rv, tv)
    if a >= 0 and a+b <= 0:
        bracketed += 1
        if b >= 0:
            bad_slope += 1
        if e <= 0:
            bad_resultant += 1
        if -b < closest_slope[0]:
            closest_slope = (-b, (pv, rv, tv, a, a+b))
        if e < closest_resultant[0]:
            closest_resultant = (e, (pv, rv, tv, a, a+b))
print({
    "bracketed": bracketed,
    "bad_slope": bad_slope,
    "bad_resultant": bad_resultant,
    "closest_minus_g1": closest_slope,
    "closest_resultant": closest_resultant,
})

envelope_critical = 0
envelope_bad_slope = 0
envelope_bad_resultant = 0
envelope_bad_curvature = 0
envelope_closest = (float("inf"), None)
for _ in range(1_000_000):
    pv, tv, sv = rng.random(), rng.random(), rng.random()
    aa = (1-pv*pv)/3
    bb = (1-pv)*(2-pv)/3
    upper = pv*tv/(1-aa*tv*tv-bb*tv**4)
    rv = sv*upper
    a, b, e = functions(pv, rv, tv)
    if b == 0:
        continue
    cv = -a/b
    if 0 <= cv <= 1:
        envelope_critical += 1
        if b >= 0:
            envelope_bad_slope += 1
        if e <= 0:
            envelope_bad_resultant += 1
        if e/b >= 0:
            envelope_bad_curvature += 1
        if e < envelope_closest[0]:
            envelope_closest = (e, (pv, tv, rv, sv, cv, b))
print({
    "matched_rational_envelope_critical": envelope_critical,
    "bad_slope": envelope_bad_slope,
    "bad_resultant": envelope_bad_resultant,
    "bad_curvature_quotient": envelope_bad_curvature,
    "closest_resultant": envelope_closest,
})

gd = sp.lambdify((p, r, t, c), (g, dg), "math")
root_rows = []
for pv in (0.1, 0.2, 0.5, 0.9, 0.99):
    for cv in (0.0, 0.5, 1.0):
        lo, hi = 0.0, 1.0
        while boundary_derivative(pv, cv*pv, hi) > 0:
            hi *= 2
        for _ in range(70):
            mid = (lo+hi)/2
            if boundary_derivative(pv, cv*pv, mid) > 0:
                lo = mid
            else:
                hi = mid
        hv = (lo+hi)/2
        tv, rv = state(pv, cv*pv, hv)
        a, b, result = functions(pv, rv, tv)
        gv, curvature = gd(pv, rv, tv, cv)
        root_rows.append((pv, cv, hv, curvature, b, result, result/b))
print("root_rows=(p,c,L,DG,g1,resultant,resultant/g1)")
for row in root_rows:
    print(row)
