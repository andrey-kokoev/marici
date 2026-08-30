"""Separate hierarchy-forced from ratio-selected flavor purity.

Dependency-free audit of the WP49 physical purity functions on the S1
chart.  It deliberately tests limits and hostile CKM rays, not fitted sheets.
"""

import cmath
import json
import math

YU2, YC2, YT2 = (7.04e-6) ** 2, (3.56e-3) ** 2, 0.967**2
YD2, YS2, YB2 = (1.54e-5) ** 2, (3.06e-4) ** 2, (1.630e-2) ** 2
S12 = 0.22517
S13 = 0.003763
S23 = 0.04189
DELTA = math.radians(66.4)


def ckm(s13, s23, s12=S12, delta=DELTA):
    c12 = math.sqrt(1 - s12 * s12)
    c13 = math.sqrt(1 - s13 * s13)
    c23 = math.sqrt(1 - s23 * s23)
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


def purity(s13, s23):
    v = ckm(s13, s23)
    a = [[abs(z) for z in row] for row in v]
    ratio = -(v[0][0] * v[0][2].conjugate()) / (v[1][0] * v[1][2].conjugate())
    sin_gamma = abs(math.sin(cmath.phase(ratio)))
    dd = (YB2 - YS2) * (YB2 - YD2) * (YS2 - YD2)
    out = {}
    for name, row_index in (("u", 0), ("c", 1), ("t", 2)):
        edge02, edge12 = invert(v[row_index], (YD2, YS2, YB2))
        if name == "u":
            gap, scale, triple = YT2 - YC2, YT2, a[0][0] * a[0][2] * a[1][0]
        elif name == "c":
            gap, scale, triple = YT2 - YU2, YT2, a[0][0] * a[1][0] * a[1][2]
        else:
            gap, scale = YC2 - YU2, YC2
            triple = a[0][0] * a[1][0] * a[1][2] ** 2 * sin_gamma
        out[name] = gap * dd * triple / (scale * edge02 * math.sqrt(edge12))
    return out


observed = purity(S13, S23)
ray = S13 / S23
limit = purity(ray * 1e-5, 1e-5)
grid = [(0.02 + i * 0.00005) for i in range(3601)]
samples = [(r, purity(r * 1e-5, 1e-5)["t"]) for r in grid]
best_r, best_t = max(samples, key=lambda item: item[1])
hostile = {str(r): purity(r * 1e-5, 1e-5)["t"] for r in (0.03, 0.18)}

checks = {
    "observed_reproduced": abs(observed["t"] - 0.99148538) < 2e-7,
    "u_limit_is_mass_ratio": abs(limit["u"] - (1 - YC2 / YT2)) < 1e-8,
    "c_limit_is_one": abs(limit["c"] - 1) < 1e-8,
    "t_limit_not_one": best_t < 0.999,
    "observed_ratio_near_t_optimum": abs(ray - best_r) < 0.003,
    "hostile_rays_break_near_unity": min(hostile.values()) < 0.95,
}

report = {
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "observed": observed,
    "fixed_ratio_limit": limit,
    "observed_ratio": ray,
    "t_valley": {"best_ratio": best_r, "best_value": best_t},
    "hostile_t_values": hostile,
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(0 if all(checks.values()) else 1)
