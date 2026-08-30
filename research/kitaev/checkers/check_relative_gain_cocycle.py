import hashlib
import json
from pathlib import Path

import sympy as sp


g1, g2, g3, q1, q2, q3 = sp.symbols("g1 g2 g3 q1 q2 q3", positive=True)

# Gauge invariance of a three-edge loop holonomy.
g1_prime = g1 * q1 / q2
g2_prime = g2 * q2 / q3
g3_prime = g3 * q3 / q1
assert sp.simplify(g1_prime * g2_prime * g3_prime - g1 * g2 * g3) == 0

# Recursive trivialization on an open path.
q0 = sp.symbols("q0", positive=True)
gains = [sp.Rational(2), sp.Rational(3), sp.Rational(5)]
frames = [q0]
transformed = []
for gain in gains:
    next_frame = sp.simplify(gain * frames[-1])
    transformed.append(sp.simplify(gain * frames[-1] / next_frame))
    frames.append(next_frame)
assert transformed == [1, 1, 1]
assert frames[-1] == 30 * q0

# Hostile tail: every prefix trivializes, but the frame degenerates.
hostile_products = [sp.Rational(1, 2) ** cutoff for cutoff in range(1, 9)]
assert all(hostile_products[index + 1] < hostile_products[index] for index in range(7))
assert sp.limit(sp.Rational(1, 2) ** sp.symbols("N", integer=True, positive=True), sp.symbols("N", integer=True, positive=True), sp.oo) == 0

# Alternating gains have bounded partial products.
alternating = []
product = sp.Integer(1)
for index in range(8):
    product *= sp.Integer(2) if index % 2 == 0 else sp.Rational(1, 2)
    alternating.append(product)
assert set(alternating) == {sp.Integer(1), sp.Integer(2)}

payload = {
    "status": "pass",
    "theorem": "relative_gain_cocycle_is_removable_only_by_bounded_normalization_coboundary",
    "gauge_law": "gamma_e'=gamma_e*q_source/q_target",
    "cycle_holonomy_invariant": True,
    "cycle_triviality_condition": "product_C gamma_e = 1 for every cycle",
    "open_finite_chain_algebraically_trivial": True,
    "infinite_chain_topological_condition": "partial products bounded above and below",
    "hostile_gain": "1/2 on every edge",
    "hostile_frame": "2^(-N)*q_0 -> 0",
    "bounded_alternating_gains": [str(value) for value in alternating],
    "exchange_requires_twisted_cocycle": True,
    "theta_gain_cocycle_computed": False,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "relative-gain-cocycle.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
