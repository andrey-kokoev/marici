import hashlib
import json
from pathlib import Path

import sympy as sp


x, L, alpha, beta = sp.symbols("x L alpha beta", positive=True)
R = beta - alpha * x

entrance = sp.solve_univariate_inequality(R > 0, x)
assert entrance == (x < beta / alpha)

integrated = sp.integrate(R, (x, 0, L))
assert sp.simplify(integrated - (beta * L - alpha * L**2 / 2)) == 0

ratio = sp.symbols("r", positive=True)
integrated_by_ratio = sp.simplify(integrated.subs(beta, ratio * alpha) / (alpha * L))
assert integrated_by_ratio == ratio - L / 2

# Exact fixtures separate pointwise and integrated positivity.
fixture = {alpha: 1, beta: sp.Rational(3, 4), L: 1}
assert R.subs(fixture).subs(x, 1) < 0
assert integrated.subs(fixture) > 0
assert integrated.subs({alpha: 1, beta: 0, L: 1}) < 0

# Weighted-average threshold never exceeds the pointwise supremum in a finite packet.
J_values = [sp.Rational(1), sp.Rational(2), sp.Rational(1)]
K_values = [sp.Rational(1), sp.Rational(1), sp.Rational(3)]
x_values = [sp.Rational(0), sp.Rational(1), sp.Rational(2)]
w_values = [sp.Rational(1), sp.Rational(2), sp.Rational(1)]
pointwise = max(xi * ki / ji for xi, ki, ji in zip(x_values, K_values, J_values))
integrated_threshold = sp.simplify(
    sum(wi * xi * ki for wi, xi, ki in zip(w_values, x_values, K_values))
    / sum(wi * ji for wi, ji in zip(w_values, J_values))
)
assert integrated_threshold <= pointwise

payload = {
    "status": "pass",
    "theorem": "conditional_residual_is_controlled_by_projective_port_ratio",
    "residual": "beta*J(x)-alpha*x*K(x)",
    "projective_coordinate": "beta/alpha",
    "pointwise_threshold": "sup_I x*K(x)/J(x)",
    "integrated_threshold": "integral w*x*K / integral w*J",
    "minimal_fixture_pointwise_threshold": "L",
    "minimal_fixture_integrated_threshold": "L/2",
    "integration_can_repair_pointwise_failure": True,
    "beta_zero_strict_positivity": False,
    "finite_weighted_threshold": str(integrated_threshold),
    "finite_pointwise_threshold": str(pointwise),
    "required_source_input": "cutoff-independent lower bound on beta/alpha",
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "projective-port-ratio.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
