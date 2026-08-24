"""Hostile scan of the polynomial critical barrier d=1/2."""

import json
import math

def state_from_chart(p, c, y, d):
    return 1 - p*p*d, p*y, p, c*p


maximum_g = (-math.inf, None)
for ip in range(101):
    p = 0.1 * ip / 100
    if p == 0:
        p = 1e-12
    for ic in range(101):
        c = ic / 100
        # The polynomial corrections decay once py is small; scan both a
        # dense finite collar and logarithmic y values up to the physical R<1.
        ys = [2 + 8 * iy / 160 for iy in range(161)]
        upper = min(0.999 / p, 1000.0)
        if upper > 10:
            ys += [math.exp(math.log(10) + (math.log(upper)-math.log(10))*j/80)
                   for j in range(81)]
        for y in ys:
            if p*y >= 1:
                continue
            t, r, pp, q = state_from_chart(p, c, y, 0.5)
            # Evaluate G directly at chart state.
            slope_sum, product = pp + q, pp*q
            nt = (4*t**3 + 2*t*product - 2*t*(2+product)*r*r
                  - slope_sum*r*(1-r*r))
            nr = (-t*slope_sum + 2*(1-2*t*t-t*t*product)*r
                  + 3*t*slope_sum*r*r)
            g = (1-t*t)*nt + pp*(1-r*r)*nr
            normalized = g/(p*p)
            if normalized > maximum_g[0]:
                maximum_g = (normalized, (p,c,y,t,r))

print(json.dumps({
    "domain": {"p": [0,0.1], "c": [0,1], "y_lower": 2, "R_strictly_below": 1},
    "maximum_sampled_G_over_p2_at_d_half": maximum_g,
    "all_sampled_strictly_negative": maximum_g[0] < 0,
}, indent=2))
