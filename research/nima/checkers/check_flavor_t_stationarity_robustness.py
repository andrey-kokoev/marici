"""One-sigma corner audit of the flavor t-purity stationary selector."""

import cmath
import itertools
import json
import math

CENTERS = {
    "yu": 7.04e-6, "yc": 3.56e-3, "yt": 0.967,
    "yd": 1.54e-5, "ys": 3.06e-4, "yb": 1.630e-2,
    "s12": 0.22517, "delta": math.radians(66.4),
}
SIGMAS = {
    "yu": 0.15e-6, "yc": 0.06e-3, "yt": 0.004,
    "yd": 0.02e-5, "ys": 0.04e-4, "yb": 0.009e-2,
    "s12": 0.00068, "delta": math.radians(2.8),
}
VUB, SVUB = 0.003763, 0.000088
VCB, SVCB = 0.04189, 0.00081


def ckm(s13, s23, s12, delta):
    c12, c13, c23 = (math.sqrt(1 - x * x) for x in (s12, s13, s23))
    phase = cmath.exp(1j * delta)
    return (
        (c12 * c13, s12 * c13, s13 / phase),
        (-s12 * c23 - c12 * s23 * s13 * phase,
         c12 * c23 - s12 * s23 * s13 * phase, s23 * c13),
        (s12 * s23 - c12 * c23 * s13 * phase,
         -c12 * s23 - s12 * c23 * s13 * phase, c23 * c13),
    )


def invert(row, masses):
    e1 = sum(masses)
    e2 = sum(masses[i] * masses[j] for i in range(3) for j in range(i + 1, 3))
    e3 = math.prod(masses)
    weights = [abs(z) ** 2 for z in row]
    d0 = sum(weights[i] * masses[i] for i in range(3))
    beta = e3 * sum(weights[i] / masses[i] for i in range(3))
    d1 = (beta * d0 - e3) / ((e1 - d0) * d0 - e2 + beta)
    p0 = math.prod(d0 - x for x in masses)
    p1 = math.prod(d1 - x for x in masses)
    return p0 / (d1 - d0), p1 / (d0 - d1)


def t_purity(r, p):
    s23, s13 = 1e-4, r * 1e-4
    v = ckm(s13, s23, p["s12"], p["delta"])
    a = [[abs(z) for z in row] for row in v]
    ratio = -(v[0][0] * v[0][2].conjugate()) / (v[1][0] * v[1][2].conjugate())
    sin_gamma = abs(math.sin(cmath.phase(ratio)))
    down = tuple(p[x] ** 2 for x in ("yd", "ys", "yb"))
    up = tuple(p[x] ** 2 for x in ("yu", "yc", "yt"))
    edge02, edge12 = invert(v[2], down)
    dd = (down[2] - down[1]) * (down[2] - down[0]) * (down[1] - down[0])
    triple = a[0][0] * a[1][0] * a[1][2] ** 2 * sin_gamma
    return (up[1] - up[0]) * dd * triple / (up[1] * edge02 * math.sqrt(edge12))


def maximize(p):
    lo, hi = 0.04, 0.14
    phi = (1 + math.sqrt(5)) / 2
    c, d = hi - (hi - lo) / phi, lo + (hi - lo) / phi
    for _ in range(55):
        if t_purity(c, p) > t_purity(d, p):
            hi, d = d, c
            c = hi - (hi - lo) / phi
        else:
            lo, c = c, d
            d = lo + (hi - lo) / phi
    return (lo + hi) / 2


keys = tuple(CENTERS)
stars = []
for signs in itertools.product((-1, 1), repeat=len(keys)):
    point = {key: CENTERS[key] + sign * SIGMAS[key] for key, sign in zip(keys, signs)}
    stars.append(maximize(point))

central_star = maximize(CENTERS)
one_at_time = {}
for key in keys:
    endpoints = []
    for sign in (-1, 1):
        point = dict(CENTERS)
        point[key] += sign * SIGMAS[key]
        endpoints.append(maximize(point))
    one_at_time[key] = {
        "minus": endpoints[0],
        "plus": endpoints[1],
        "span": abs(endpoints[1] - endpoints[0]),
    }
dominant = max(one_at_time, key=lambda key: one_at_time[key]["span"])

r_low = (VUB - SVUB) / (VCB + SVCB)
r_high = (VUB + SVUB) / (VCB - SVCB)
star_low, star_high = min(stars), max(stars)
checks = {
    "all_256_corners_finite": len(stars) == 256 and all(math.isfinite(x) for x in stars),
    "central_stationary_point_inside_observed_interval": r_low < central_star < r_high,
    "robust_containment_is_falsified": not (r_low < star_low < star_high < r_high),
    "robust_narrowness_is_falsified": star_high - star_low > r_high - r_low,
    "all_stationary_points_interior": 0.04 < star_low and star_high < 0.14,
}
report = {
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "corner_count": len(stars),
    "central_stationary_point": central_star,
    "stationary_interval": [star_low, star_high],
    "observed_ratio_1sigma_interval": [r_low, r_high],
    "interval_width_ratio": (star_high - star_low) / (r_high - r_low),
    "one_at_time": one_at_time,
    "dominant_one_at_time_input": dominant,
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(0 if all(checks.values()) else 1)
