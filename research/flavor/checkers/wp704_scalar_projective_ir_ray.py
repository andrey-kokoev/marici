"""Exact projective-ray analysis of the closed WP662 scalar subspace."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
a, b, r, s = sp.symbols("a b r s", real=True)
C = sp.symbols("C", positive=True)

beta_a = 176*a**2 + 12*b**2
beta_b = 160*a*b + 32*b**2
beta_r = sp.factor((beta_a*b-a*beta_b)/b**2)
beta_r_projective = sp.factor(beta_r.subs(a, r*b)/(4*b))
radial_determinant = sp.factor((4*a**2-b**2).subs(a, r*b))
ray_polynomial = sp.factor(beta_r_projective)
rays = sp.solve(ray_polynomial, r)

implicit_ratio = (2*r-3)/(2*r-1)
implicit_derivative = sp.factor(
    sp.diff(implicit_ratio, r)*beta_r_projective
)

def ratio_at(clock, constant):
    q = constant*sp.exp(4*clock)
    return sp.simplify((3-q)/(2*(1-q)))

r_c1 = ratio_at(s, sp.Rational(1, 4))
r_c2 = ratio_at(s, sp.Rational(1, 2))

checks = {
    "symmetric_projective_beta_factorizes": sp.factor(beta_r.subs(a, r*b)) == 4*b*(2*r-1)*(2*r-3),
    "exact_projective_rays": rays == [sp.Rational(1, 2), sp.Rational(3, 2)],
    "stability_determinant_factorizes": radial_determinant == b**2*(2*r-1)*(2*r+1),
    "lower_ray_is_stability_boundary": radial_determinant.subs(r, sp.Rational(1, 2)) == 0,
    "upper_ray_is_strictly_stable": radial_determinant.subs({r: sp.Rational(3, 2), b: 1}) == 8,
    "implicit_solution_has_exponential_projective_clock": implicit_derivative == 4*implicit_ratio,
    "stable_basin_ir_limit_is_three_halves": sp.limit(ratio_at(s, C), s, -sp.oo) == sp.Rational(3, 2),
    "finite_clock_retains_trajectory_constant": sp.simplify(r_c1-r_c2) != 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP704",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "WP662 closed scalar subspace lambda_n=lambda_m=a, lambda_c=0, lambda_x=b>0 with strict radial stability",
    "faithful_coordinate": "the finite-scale projective ratio r=a/b together with its trajectory constant C",
    "source_authorized_operation": "the exact WP662 scalar one-loop beta flow restricted to its invariant symmetric subspace",
    "contextual_partition": "finite projective time preserves distinct C fibers; the Gaussian infrared limit collapses the strictly stable basin to tangent ratio r=3/2",
    "classification": "asymptotic selector on the scalar-truncation tangent cone; finite-scale rigidifier/transport; not yet a physical16 selector",
    "smallest_exact_falsifier": "C=1/4 and C=1/2 give distinct ratios at every finite s despite sharing the infrared ratio 3/2",
    "remaining_instrument_gate": "derive the ray and basin in the full gauge-Yukawa-messenger-threshold completion, bound finite matching error, and attach a calibrated portal readout",
}
(ROOT / "results" / "wp704_scalar_projective_ir_ray.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
