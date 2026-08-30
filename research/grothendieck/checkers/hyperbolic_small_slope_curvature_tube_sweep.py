"""Hostile test of DG<0 on the proposed faithful small-slope tube."""

import json
import random

from hyperbolic_boundary_critical_curvature_sweep import directional_curvature


rng = random.Random(20260823)
trials = 1_000_000
largest = (-float("inf"), None)
largest_lower_face_g = (-float("inf"),None)
positive = 0
for _ in range(trials):
    p = 0.1+0.899999*rng.random()
    c = rng.random()
    # Sample R compactly, with R>=2p equivalent to y>=2.
    r = rng.random()
    y = r/p
    e = -2.5*rng.random()
    d = (1+c+2*y+e)/8
    t = 1-p*p*d
    if not (0<t<1):
        continue
    value = directional_curvature(t,r,p,c*p)/(p*p)
    # Evaluate G/p^2 at the lower tube face e=-0.3.
    eface=-2.5;dface=(1+c+2*y+eface)/8;tface=1-p*p*dface
    q=c*p;slope_sum,product=p+q,p*q
    nt=(4*tface**3+2*tface*product-2*tface*(2+product)*r*r
        -slope_sum*r*(1-r*r))
    nr=(-tface*slope_sum+2*(1-2*tface*tface-tface*tface*product)*r
        +3*tface*slope_sum*r*r)
    gface=((1-tface*tface)*nt+p*(1-r*r)*nr)/(p*p)
    if gface>largest_lower_face_g[0]:
        largest_lower_face_g=(gface,(p,c,r,y))
    if value > largest[0]:
        largest = (value,(p,c,r,y,e,d,t))
    if value > 1e-12:
        positive += 1

print(json.dumps({
    "trials": trials,
    "positive_beyond_1e-12": positive,
    "largest_DG_over_p2": largest,
    "largest_G_over_p2_at_e_minus_0.3":largest_lower_face_g,
},indent=2))
