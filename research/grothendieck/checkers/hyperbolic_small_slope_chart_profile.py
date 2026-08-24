"""Profile faithful polynomial coordinates on small-slope critical orbits."""

import json
import math

from hyperbolic_boundary_critical_curvature_sweep import state
from hyperbolic_boundary_unimodality_sweep import boundary_derivative


rows = []
for p in (0.99,0.9,0.7,0.5,0.3,0.2,1e-1,3e-2,1e-2,3e-3,1e-3,3e-4,1e-4,3e-5,1e-5):
    extrema = {
        "y_min": math.inf, "y_max": -math.inf,
        "d_min": math.inf, "d_max": -math.inf,
        "R_max": -math.inf, "holding_min": math.inf, "holding_max": -math.inf,
        "e_min": math.inf, "e_max": -math.inf,
        "Gc_min": math.inf, "Gc_max": -math.inf,
    }
    argmax = None
    for index in range(101):
        c = index / 100
        q = c * p
        lo, hi = 1e-12, 1.0
        while boundary_derivative(p, q, hi) > 0:
            hi *= 2
        for _ in range(70):
            mid = (lo + hi) / 2
            if boundary_derivative(p, q, mid) > 0:
                lo = mid
            else:
                hi = mid
        holding = (lo + hi) / 2
        t, r = state(p, q, holding)
        y = r / p
        d = (1 - t) / (p * p)
        e = 8*d - (1+c+2*y)
        # Exact affine coefficient in c, evaluated by endpoint difference.
        def chart_g(cc):
            pp, qq, rr = p, cc*p, p*y
            slope_sum, product = pp+qq, pp*qq
            nt = (4*t**3+2*t*product-2*t*(2+product)*rr*rr
                  -slope_sum*rr*(1-rr*rr))
            nr = (-t*slope_sum+2*(1-2*t*t-t*t*product)*rr
                  +3*t*slope_sum*rr*rr)
            return ((1-t*t)*nt+pp*(1-rr*rr)*nr)/(p*p)
        gc = chart_g(1)-chart_g(0)
        extrema["y_min"] = min(extrema["y_min"], y)
        extrema["y_max"] = max(extrema["y_max"], y)
        extrema["d_min"] = min(extrema["d_min"], d)
        extrema["d_max"] = max(extrema["d_max"], d)
        extrema["R_max"] = max(extrema["R_max"], r)
        extrema["holding_min"] = min(extrema["holding_min"], holding)
        extrema["holding_max"] = max(extrema["holding_max"], holding)
        extrema["e_min"] = min(extrema["e_min"],e)
        extrema["e_max"] = max(extrema["e_max"],e)
        extrema["Gc_min"] = min(extrema["Gc_min"],gc)
        extrema["Gc_max"] = max(extrema["Gc_max"],gc)
        if y == extrema["y_max"]:
            argmax = c
    rows.append({"p": p, "argmax_y_c": argmax, **extrema})

print(json.dumps(rows, indent=2))
