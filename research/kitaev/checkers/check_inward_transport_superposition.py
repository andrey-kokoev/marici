import hashlib
import json
from pathlib import Path

import sympy as sp


z = sp.symbols("z", real=True)

F1 = z - 10
G1 = sp.Integer(1)
F2 = z + 9
G2 = sp.Integer(-100)


def zero_and_velocity(F, G):
    roots = sp.solve(F, z)
    assert len(roots) == 1
    root = roots[0]
    velocity = sp.simplify(-G.subs(z, root) / sp.diff(F, z).subs(z, root))
    return root, velocity, sp.simplify(root * velocity)


r1, v1, product1 = zero_and_velocity(F1, G1)
r2, v2, product2 = zero_and_velocity(F2, G2)
rs, vs, product_sum = zero_and_velocity(F1 + F2, G1 + G2)

assert (r1, v1, product1) == (10, -1, -10)
assert (r2, v2, product2) == (-9, 100, -900)
assert (rs, vs, product_sum) == (sp.Rational(1, 2), sp.Rational(99, 2), sp.Rational(99, 4))
assert product1 < 0 and product2 < 0 and product_sum > 0

# A single linear generator exists on the labelled basis F1,F2.
A = sp.Matrix([[0, 0], [1, -100]])
assert A * sp.Matrix([1, 0]) == sp.Matrix([0, 1])
assert A * sp.Matrix([0, 1]) == sp.Matrix([0, -100])
assert A * sp.Matrix([1, 1]) == sp.Matrix([0, -99])

payload = {
    "status": "pass",
    "theorem": "inward_divisor_transport_is_not_closed_under_positive_superposition",
    "first_pair": {"zero": "10", "velocity": "-1", "product": "-10"},
    "second_pair": {"zero": "-9", "velocity": "100", "product": "-900"},
    "positive_sum": {"zero": "1/2", "velocity": "99/2", "product": "99/4"},
    "summands_move_inward": True,
    "sum_moves_inward": False,
    "inward_pair_class_is_convex": False,
    "common_linear_generator_on_labelled_span_exists": True,
    "theta_states_admitted": False,
    "required_repair": "nonconvex constructor orbit, correlated pair cone, or additive energy law",
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "inward-transport-superposition.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
