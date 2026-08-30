import hashlib
import json
from pathlib import Path

import sympy as sp


D, L, alpha, p, eta = sp.symbols("D L alpha p eta", positive=True)

# Exponential hostile family.
W_exp = sp.exp(-alpha * D)
elasticity_exp = sp.simplify(-D * sp.diff(sp.log(W_exp), D))
assert elasticity_exp == alpha * D

block_exp = sp.simplify(D * W_exp - (D + L) * W_exp.subs(D, D + L))
small_D_block = sp.simplify(block_exp.subs({alpha: 1, D: sp.Rational(1, 2), L: 1}))
large_D_block = sp.simplify(block_exp.subs({alpha: 1, D: 2, L: 1}))
assert small_D_block < 0
assert large_D_block > 0

# Power family realizes the exact unit threshold.
W_power = D ** (-p)
elasticity_power = sp.simplify(-D * sp.diff(sp.log(W_power), D))
assert elasticity_power == p
block_p2 = sp.simplify((D * W_power - (D + L) * W_power.subs(D, D + L)).subs(p, 2))
block_p1 = sp.simplify((D * W_power - (D + L) * W_power.subs(D, D + L)).subs(p, 1))
block_phalf = sp.simplify((D * W_power - (D + L) * W_power.subs(D, D + L)).subs(p, sp.Rational(1, 2)))
assert block_p2.subs({D: 1, L: 1}) > 0
assert block_p1 == 0
assert block_phalf.subs({D: 1, L: 1}) < 0

# Uniform elasticity margin integrates to the advertised power modulus.
u = sp.symbols("u", positive=True)
integrated_margin = sp.integrate(eta / u, (u, D, D + L))
assert sp.simplify(integrated_margin - eta * sp.log((D + L) / D)) == 0

payload = {
    "status": "pass",
    "theorem": "remaining_boundary_block_is_controlled_by_sharp_decay_elasticity_threshold",
    "block": "D*W(D)-(D+L)*W(D+L)",
    "finite_interval_condition": "integral_D^(D+L) -d(log W) > log(1+L/D)",
    "elasticity": "-D*d_D log W(D)",
    "sharp_threshold": "elasticity > 1",
    "uniform_margin": "elasticity >= 1+eta",
    "uniform_block_modulus": "D*W(D)*[1-(D/(D+L))^eta]",
    "exponential_elasticity": "alpha*D",
    "exponential_small_D_fixture": str(small_D_block),
    "exponential_large_D_fixture": str(large_D_block),
    "power_threshold": {"p>1": "positive", "p=1": "zero", "0<p<1": "negative"},
    "theta_weight_identified": False,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "boundary-decay-elasticity.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
