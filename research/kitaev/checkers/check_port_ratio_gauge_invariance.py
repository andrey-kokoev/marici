import hashlib
import json
from pathlib import Path

import sympy as sp


alpha, beta, J, K, x, u, v, rho = sp.symbols(
    "alpha beta J K x u v rho", positive=True
)

J_prime = u * J
K_prime = v * K
beta_prime = beta / u
alpha_prime = alpha / v

residual = beta * J - alpha * x * K
residual_prime = sp.simplify(beta_prime * J_prime - alpha_prime * x * K_prime)
assert sp.simplify(residual_prime - residual) == 0

r = beta / alpha
r_prime = sp.simplify(beta_prime / alpha_prime)
assert sp.simplify(r_prime - (v / u) * r) == 0

rho_prime = (v / u) * rho
margin = r / rho
margin_prime = sp.simplify(r_prime / rho_prime)
assert sp.simplify(margin_prime - margin) == 0

local_margin = beta * J / (alpha * x * K)
local_margin_prime = sp.simplify(beta_prime * J_prime / (alpha_prime * x * K_prime))
assert sp.simplify(local_margin_prime - local_margin) == 0

# Harmless unit change halves both raw ratio and threshold.
fixture_ratio = sp.simplify(r_prime.subs({u: 2, v: 1}) / r)
fixture_threshold = sp.simplify(rho_prime.subs({u: 2, v: 1}) / rho)
assert fixture_ratio == sp.Rational(1, 2)
assert fixture_threshold == sp.Rational(1, 2)

payload = {
    "status": "pass",
    "theorem": "port_ratio_is_gauge_dependent_but_safety_margin_is_invariant",
    "feature_rescaling": "J'=uJ, K'=vK",
    "coefficient_rescaling": "beta'=beta/u, alpha'=alpha/v",
    "residual_invariant": True,
    "raw_ratio_transformation": "r'=(v/u)r",
    "threshold_transformation": "rho'=(v/u)rho",
    "safety_margin_invariant": True,
    "local_evaluation_margin_invariant": True,
    "required_source_structure": ["repair-drift polarization", "invariant margin or frozen units"],
    "completion_statement": "M_X >= 1+delta uniformly",
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "port-ratio-gauge-invariance.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
