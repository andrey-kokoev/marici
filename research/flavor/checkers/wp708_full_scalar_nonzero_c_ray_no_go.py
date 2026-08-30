"""Exact full-projective no-go for stable WP662 rays with lambda_c nonzero."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
x, y, z = sp.symbols("x y z", real=True)

beta_n = 4*z**2 + 8*z + 176*x**2 + 12
beta_m = 4*z**2 + 8*z + 176*y**2 + 12
beta_x = 8*z**2 + 16*z*(x+y) + 80*(x+y) + 32
beta_c_over_c = 40*z + 32*x + 32*y + 64

equations = [
    sp.expand(beta_n-x*beta_x),
    sp.expand(beta_m-y*beta_x),
    sp.expand(beta_c_over_c-beta_x),
]
groebner = sp.groebner(equations, z, y, x, order="lex")
eliminant = sp.factor(groebner.polys[-1].as_expr())
expected_eliminant = (2*x-1)**3*(6*x**2-3*x+1)*(9702*x**2-3157*x+513)

real_x = sp.Rational(1, 2)
back_equations = [sp.factor(eq.subs(x, real_x)) for eq in equations]
back_solutions = sp.solve_poly_system(back_equations, y, z)
radial_margin = 4*x*y-1

checks = {
    "full_projective_eliminant_factorizes": eliminant == expected_eliminant,
    "first_extra_factor_has_no_real_root": sp.discriminant(6*x**2-3*x+1, x) == -15,
    "second_extra_factor_has_no_real_root": sp.discriminant(9702*x**2-3157*x+513, x) == -9941855,
    "only_real_nonzero_c_rays": back_solutions == [(sp.Rational(1, 2), 1), (sp.Rational(1, 2), 2)],
    "first_real_ray_is_radially_marginal": radial_margin.subs({x: real_x, y: sp.Rational(1, 2)}) == 0,
    "both_real_rays_share_same_radial_margin": all(radial_margin.subs({x: real_x, y: sy}) == 0 for sy, _ in back_solutions),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP708",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "the complete four-quartic WP662 scalar one-loop beta field with lambda_x>0 and lambda_c nonzero",
    "faithful_coordinate": "full projective coupling triple (lambda_n/lambda_x, lambda_m/lambda_x, lambda_c/lambda_x)",
    "source_authorized_operation": "exact projective fixed-ray equations of the complete scalar beta field",
    "contextual_partition": "the two real nonzero-correlation rays are distinct in z but both lie on the same radially marginal boundary stratum",
    "classification": "neither stable selector nor rigidifier on the admitted strict-stability domain; no real nonzero-correlation fixed ray enters its interior",
    "smallest_exact_falsifier": "both real rays have x=y=1/2 and exact radial margin 4xy-1=0",
    "remaining_gate": "derive full gauge-Yukawa-messenger or new-field beta contributions that displace a ray into the strict stability interior, then retest its complete transverse basin and finite matching",
}
(ROOT / "results" / "wp708_full_scalar_nonzero_c_ray_no_go.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
