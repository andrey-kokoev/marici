"""Scout Burnol's pointwise multiplier at the c=sqrt(2) support boundary.

This is high-precision discovery evidence, not an interval certificate.
"""

import json

import mpmath as mp


mp.mp.dps = 80
LOG_TWO = mp.log(2)


def alpha(t):
    t = mp.mpf(t)
    return (
        8 * mp.sqrt(2) * mp.cos(LOG_TWO * t) / (1 + 4 * t * t)
        - mp.log(mp.pi)
        + mp.re(mp.digamma(mp.mpf(1) / 4 + mp.j * t / 2))
    )


grid_step = mp.mpf("0.001")
grid = [(i * grid_step, alpha(i * grid_step)) for i in range(20001)]
grid_min_t, _ = min(grid, key=lambda pair: pair[1])
critical = mp.findroot(
    lambda t: mp.diff(alpha, t),
    (grid_min_t - mp.mpf("0.01"), grid_min_t + mp.mpf("0.01")),
)

roots = []
for (left_t, left_v), (right_t, right_v) in zip(grid, grid[1:]):
    if left_v * right_v < 0:
        root = mp.findroot(alpha, (left_t, right_t))
        if not roots or abs(root - roots[-1]) > mp.mpf("1e-30"):
            roots.append(root)

result = {
    "schema": "marici.burnol-prime-two-boundary-multiplier.v1",
    "status": "pass",
    "scope": "high-precision scout; not a directed interval certificate",
    "formula": (
        "8*sqrt(2)*cos(t*log(2))/(1+4*t^2)-log(pi)"
        "+Re(digamma(1/4+i*t/2))"
    ),
    "alpha_at_zero": mp.nstr(alpha(0), 60),
    "global_grid_range": ["0", "20"],
    "grid_step": mp.nstr(grid_step, 10),
    "critical_t": mp.nstr(critical, 60),
    "critical_value": mp.nstr(alpha(critical), 60),
    "positive_axis_roots_through_20": [mp.nstr(root, 60) for root in roots],
    "pointwise_nonnegative_at_boundary": alpha(critical) >= 0,
    "interpretation": (
        "A negative multiplier rules out extending Burnol's proof to "
        "c=sqrt(2) by pointwise multiplier positivity alone. It does not "
        "falsify positivity on the Paley-Wiener/support-constrained subspace."
    ),
}

print(json.dumps(result, indent=2))

