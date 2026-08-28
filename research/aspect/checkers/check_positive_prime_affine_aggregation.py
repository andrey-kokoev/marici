import json
from pathlib import Path

import mpmath as mp
import sympy as sp


u, ell, z, tau, f = sp.symbols("u ell z tau f", positive=True, real=True)
a = sp.Rational(1, 2) + z
b = sp.Rational(1, 2) - z
closed = f * ((1 - sp.exp(-b * ell)) / b - (1 - sp.exp(-a * ell)) / a)
integrand = 2 * f * sp.exp(-ell / 2) * sp.sinh(z * ell)
seam = sp.simplify(closed.subs(z, sp.I * tau))

primes = [2, 3, 5, 7, 11]
weights = [1, 2, 3, 5, 7]


def local_current(p, x):
    length = mp.log(p)
    return 2 * mp.quad(lambda q: mp.exp(-q / 2) * mp.sinh(x * q), [0, length])


grid = [mp.mpf(k) / 100 for k in range(1, 50)]
positive_grid = all(
    sum(w * local_current(p, x) for p, w in zip(primes, weights)) > 0
    for x in grid
)
negative_grid = all(
    sum(w * local_current(p, -x) for p, w in zip(primes, weights)) < 0
    for x in grid
)
frequency_grid = [mp.mpf(k) / 10 for k in range(1, 10001)]


def seam_quadrature(p, t):
    length = mp.log(p)
    return (
        t - mp.exp(-length / 2) * (t * mp.cos(t * length) + mp.sin(t * length) / 2)
    ) / (t**2 + mp.mpf(1) / 4)


positive_seam_grid = all(
    sum(
        w * seam_quadrature(p, t)
        for p, w in zip(primes, weights)
    ) > 0
    for t in frequency_grid
)

checks = {
    "closed_form_has_zero_initial_value": sp.simplify(closed.subs(ell, 0)) == 0,
    "closed_form_derivative_is_positive_integrand": sp.simplify(
        sp.diff(closed, ell).rewrite(sp.exp) - integrand.rewrite(sp.exp)
    ) == 0,
    "reciprocal_reversal_is_odd": sp.simplify(closed.subs(z, -z) + closed) == 0,
    "positive_prime_aggregate_has_positive_real_strip_grid": positive_grid,
    "negative_real_strip_grid_reverses_sign": negative_grid,
    "critical_seam_current_is_purely_imaginary": sp.simplify(sp.re(seam)) == 0,
    "positive_prime_aggregate_has_positive_seam_quadrature_grid": positive_seam_grid,
    "archimedean_normalized_current_vanishes": sp.limit(closed / (1 - sp.exp(-ell)), ell, 0) == 0,
}

result = {
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "primes": primes,
    "weights": weights,
    "real_strip_grid_points": len(grid),
    "positive_frequency_grid_points": len(frequency_grid),
    "seam_current": str(seam),
}
out = Path(__file__).resolve().parents[1] / "results" / "positive_prime_affine_aggregation.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
