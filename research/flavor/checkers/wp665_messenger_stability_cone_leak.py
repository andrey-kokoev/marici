"""Exact failure of forward invariance for the disjoint-messenger stability cone."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
l, x, c, F = sp.symbols("l x c F", positive=True)
beta_l = 4*c**2+8*c*x+176*l**2+12*x**2-4*F
beta_x = 8*c**2+32*c*l+160*l*x+32*x**2
D = 4*l**2-x**2
beta_D = sp.expand(sp.diff(D, l)*beta_l+sp.diff(D, x)*beta_x)
positive_boundary_flow = sp.factor(beta_D.subs(x, 2*l))
negative_boundary_flow = sp.factor(beta_D.subs(x, -2*l))

checks = {
    "symmetric_submanifold_radial_flow_derived": beta_D == sp.expand(8*l*beta_l-2*x*beta_x),
    "positive_boundary_leaks_for_any_fermion_strength": positive_boundary_flow == -32*F*l,
    "positive_boundary_scalar_limit_is_tangent": positive_boundary_flow.subs(F, 0) == 0,
    "unit_hostile_boundary_points_outward": positive_boundary_flow.subs({F: 1, l: 1}) == -32,
    "opposite_boundary_is_not_the_same_gate": negative_boundary_flow != positive_boundary_flow,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP665", "status": "PASS", "checks": checks,
    "symmetric_domain": "lambda_n=lambda_m=lambda>0 with total disjoint fermion strength F=F_n+F_m",
    "radial_margin": "D=4lambda^2-lambda_x^2",
    "positive_boundary": "lambda_x=2lambda",
    "boundary_flow": "dD/dt=-32F lambda",
    "classification": "the full radial-stability cone is not forward invariant for any positive fixed disjoint-messenger strength",
    "smallest_exact_falsifier": "F=lambda=1 and lambda_x=2 gives D=0 but dD/dt=-32",
    "remaining_gate": "derive Yukawa running and threshold decoupling, then prove or refute invariance of a smaller scale-bounded domain",
}
(ROOT / "results" / "wp665_messenger_stability_cone_leak.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
