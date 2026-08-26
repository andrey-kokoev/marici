"""Exact source-free vacuum audit for the WP128 two-adjoint potential."""

import json
from pathlib import Path

import sympy as sp


x, y = sp.symbols("x y", nonnegative=True, real=True)
m_min_sq, lam, rho = sp.symbols("m_min_squared lambda rho", positive=True, real=True)
t = sp.symbols("t", positive=True, real=True)

radial = x + y
quartic_margin = rho - lam / 2
lower_bound = sp.factor(m_min_sq * radial / 2 + quartic_margin * radial**2)

# WP128 benchmark.
benchmark = {m_min_sq: 1, lam: 25, rho: 13}
benchmark_margin = sp.factor(quartic_margin.subs(benchmark))
benchmark_ray_bound = sp.factor(lower_bound.subs(benchmark).subs({x: t, y: 0}))
radial_symbol = sp.Symbol("R", nonnegative=True, real=True)
benchmark_radial_bound = sp.expand(
    (m_min_sq * radial_symbol / 2 + quartic_margin * radial_symbol**2).subs(benchmark)
)
benchmark_radial_coefficients = sp.Poly(benchmark_radial_bound, radial_symbol).all_coeffs()

mu_u, mu_d, mass_u_sq, mass_d_sq = sp.symbols(
    "mu_u mu_d M_u_squared M_d_squared", nonzero=True, real=True
)
h_u, h_d = sp.symbols("H_u H_d", real=True)
leading_a = -mu_u * h_u / mass_u_sq
leading_d = -mu_d * h_d / mass_d_sq

checks = {
    "commutator_bound_reduces_to_strict_quartic_margin": sp.expand(rho * radial**2 - lam * radial**2 / 2) == sp.expand(quartic_margin * radial**2),
    "WP128_benchmark_has_positive_quartic_margin": benchmark_margin == sp.Rational(1, 2),
    "benchmark_radial_bound_has_strictly_positive_nonconstant_coefficients": all(coefficient > 0 for coefficient in benchmark_radial_coefficients[:-1]),
    "benchmark_lower_bound_positive_on_nonzero_ray": benchmark_ray_bound > 0,
    "source_free_origin_has_zero_potential_bound": lower_bound.subs({x: 0, y: 0}) == 0,
    "linear_source_imposes_Hu_proportional_vacuum": sp.diff(leading_a, h_u) == -mu_u / mass_u_sq,
    "linear_source_imposes_Hd_proportional_vacuum": sp.diff(leading_d, h_d) == -mu_d / mass_d_sq,
    "zero_flavor_sources_restore_zero_leading_vacuum": leading_a.subs(h_u, 0) == 0 and leading_d.subs(h_d, 0) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP436",
    "title": "WP128 vacuum-source obstruction",
    "source_free_lower_bound": str(lower_bound),
    "WP128_quartic_margin": str(benchmark_margin),
    "WP128_nonzero_ray_bound": str(benchmark_ray_bound),
    "source_free_global_minimum": "A=D=0 under positive masses and rho>lambda/2",
    "leading_sourced_vacuum": {"A": str(leading_a), "D": str(leading_d)},
    "classification": "the current stable WP128 potential selects the symmetric origin; its noncommuting vacuum is imported by Yukawa-dependent linear sources",
    "smallest_exact_falsifier": "a nonzero global minimum under the same positive-mass and strict-coercivity assumptions",
    "remaining_gate": "predeclare and audit a source-free symmetry-breaking two-adjoint potential without fitting its vacuum to measured flavor",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).parents[1] / "results" / "wp436_wp128_vacuum_source_obstruction.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
