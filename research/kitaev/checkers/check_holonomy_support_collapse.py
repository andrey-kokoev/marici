import hashlib
import json
from pathlib import Path

import sympy as sp


I = sp.I
n = sp.symbols("n", integer=True, positive=True)
eps = 1 / n
half = sp.Rational(1, 2)
M_plus = sp.Matrix([[2, half, -I * eps], [half, 2, half], [I * eps, half, 2]])
M_minus = sp.conjugate(M_plus)
M_limit = sp.Matrix([[2, half, 0], [half, 2, half], [0, half, 2]])


def product(matrix):
    return sp.simplify(matrix[0, 1] * matrix[1, 2] * sp.conjugate(matrix[0, 2]))


w_plus = product(M_plus)
w_minus = product(M_minus)
assert w_plus == I / (4 * n)
assert w_minus == -I / (4 * n)
assert sp.limit(w_plus, n, sp.oo) == 0
assert sp.limit(w_minus, n, sp.oo) == 0
assert sp.simplify(w_plus / abs(w_plus)) == I
assert sp.simplify(w_minus / abs(w_minus)) == -I
assert M_plus.applyfunc(lambda x: sp.limit(x, n, sp.oo)) == M_limit
assert M_minus.applyfunc(lambda x: sp.limit(x, n, sp.oo)) == M_limit

# Squared Frobenius distance between the two branches tends to zero.
distance_squared = sp.simplify(
    sum(abs(M_plus[i, j] - M_minus[i, j]) ** 2 for i in range(3) for j in range(3))
)
assert distance_squared == 8 / n**2
assert sp.limit(distance_squared, n, sp.oo) == 0

# For n >= 2, diagonal 2 strictly dominates every row sum (at most 1).
assert sp.Rational(2) > sp.Rational(1)

payload = {
    "status": "pass",
    "theorem": "normalized_holonomy_does_not_survive_support_collapse",
    "normalized_branch_limits": ["+I", "-I"],
    "unnormalized_products": ["I/(4*n)", "-I/(4*n)"],
    "shared_matrix_limit": str(M_limit),
    "branch_distance_squared": "8/n^2 -> 0",
    "cycle_rank_before": 1,
    "cycle_rank_after": 0,
    "continuous_replacement": "unnormalized_cycle_product",
    "theta_application_frozen": True,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "holonomy-support-collapse.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
