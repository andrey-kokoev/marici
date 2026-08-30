import hashlib
import json
from pathlib import Path

import sympy as sp


a, b, c, d = sp.symbols("a b c d", real=True)
A = sp.Matrix([[a, b], [c, d]])
R = sp.diag(1, -1)
I = sp.eye(2)
P_plus = (I + R) / 2
P_minus = (I - R) / 2

commutator = sp.simplify(A * R - R * A)
anticommutator = sp.simplify(A * R + R * A)
leakage = sp.simplify(P_plus * A * P_minus + P_minus * A * P_plus)

assert commutator == sp.Matrix([[0, -2 * b], [2 * c, 0]])
assert anticommutator == sp.Matrix([[2 * a, 0], [0, -2 * d]])
assert leakage == sp.Matrix([[0, b], [c, 0]])

commutator_frobenius_squared = sp.simplify(sum(entry**2 for entry in commutator))
leakage_frobenius_squared = sp.simplify(sum(entry**2 for entry in leakage))
assert sp.simplify(commutator_frobenius_squared - 4 * leakage_frobenius_squared) == 0

# Exact polarization preservation with collapsing relative-gain cocycle.
hostile = sp.diag(sp.Rational(1, 2), 1)
assert hostile * R - R * hostile == sp.zeros(2)
for cutoff in range(1, 9):
    product = hostile**cutoff
    assert product == sp.diag(sp.Rational(1, 2) ** cutoff, 1)

payload = {
    "status": "pass",
    "theorem": "source_involution_freezes_port_polarization_but_not_safety_margin",
    "involution": "diag(1,-1)",
    "commutator": "[[0,-2b],[2c,0]]",
    "commutation_equivalent_to_ordered_ray_preservation": True,
    "anticommutation_equivalent_to_ray_exchange": True,
    "commutator_norm_squared": "4*(b^2+c^2)",
    "leakage_norm_squared": "b^2+c^2",
    "hostile_constructor": "diag(1/2,1)",
    "hostile_commutator_zero": True,
    "safety_margin_after_N": "2^(-N)*M_0",
    "polarization_preservation_implies_margin_preservation": False,
    "required_completion_data": ["commutator control", "relative-gain cocycle control"],
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "port-polarization-involution.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
