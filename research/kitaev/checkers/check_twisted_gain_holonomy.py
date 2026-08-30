import hashlib
import json
from pathlib import Path

import sympy as sp


l1, l2, q, x = sp.symbols("l1 l2 q x", real=True)


def affine_matrix(log_gain, parity):
    return sp.Matrix([[parity, log_gain], [0, 1]])


preserve_1 = affine_matrix(l1, 1)
preserve_2 = affine_matrix(l2, 1)
exchange_1 = affine_matrix(l1, -1)
exchange_2 = affine_matrix(l2, -1)

assert preserve_2 * preserve_1 == affine_matrix(l2 + l1, 1)
assert exchange_2 * exchange_1 == affine_matrix(l2 - l1, 1)
assert exchange_1 * exchange_1 == sp.eye(2)

# Conjugation by a frame translation leaves even translation fixed and shifts odd displacement.
frame = affine_matrix(q, 1)
frame_inverse = affine_matrix(-q, 1)
even_conjugate = sp.simplify(frame * preserve_1 * frame_inverse)
odd_conjugate = sp.simplify(frame * exchange_1 * frame_inverse)
assert even_conjugate == preserve_1
assert odd_conjugate == affine_matrix(l1 + 2 * q, -1)

# Repeated fixed exchange has period two on log margin.
first = -x + l1
second = sp.simplify(-first + l1)
assert second == x

# Unequal alternating exchanges translate every two steps.
second_unequal = sp.simplify(-first + l2)
assert second_unequal == x + l2 - l1

payload = {
    "status": "pass",
    "theorem": "ray_exchanging_constructors_carry_affine_twisted_gain_holonomy",
    "action": "x -> epsilon*x + ell",
    "composition": "(ell2,eps2)o(ell1,eps1)=(ell2+eps2*ell1,eps2*eps1)",
    "two_exchange_gain": "ell2-ell1",
    "even_loop_obstruction": "nonzero log translation",
    "odd_loop_obstruction": "ray-exchange parity",
    "odd_reflection_fixed_point": "ell/2",
    "repeated_equal_exchange_period": 2,
    "mixed_tail_requires_affine_recurrence": True,
    "orientation_double_cover_required_for_ordered_frame": True,
    "theta_transport_parity_computed": False,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "twisted-gain-holonomy.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
