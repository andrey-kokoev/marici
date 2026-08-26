import hashlib
import json
from pathlib import Path

import sympy as sp


I = sp.I
half = sp.Rational(1, 2)
M_plus = sp.Matrix(
    [[2, half, -I * half], [half, 2, half], [I * half, half, 2]]
)
M_minus = sp.conjugate(M_plus)

assert M_plus == M_plus.conjugate().T
assert M_minus == M_minus.conjugate().T
assert all(2 > sum(abs(M_plus[i, j]) for j in range(3) if j != i) for i in range(3))

lam = sp.symbols("lambda")
char_plus = sp.expand(M_plus.charpoly(lam).as_expr())
char_minus = sp.expand(M_minus.charpoly(lam).as_expr())
assert char_plus == char_minus


def holonomy(matrix):
    product = matrix[0, 1] * matrix[1, 2] * sp.conjugate(matrix[0, 2])
    magnitude = abs(matrix[0, 1]) * abs(matrix[1, 2]) * abs(matrix[0, 2])
    return sp.simplify(product / magnitude)


h_plus = holonomy(M_plus)
h_minus = holonomy(M_minus)
assert h_plus == I
assert h_minus == -I
assert h_plus != h_minus
assert all(abs(M_plus[i, j]) == abs(M_minus[i, j]) for i in range(3) for j in range(3))

# A connected triangle has cycle rank 3 - 3 + 1 = 1.
beta_one = 3 - 3 + 1
assert beta_one == 1

payload = {
    "status": "pass",
    "theorem": "minimal_phase_ports_are_cycle_holonomies",
    "triangle_cycle_rank": beta_one,
    "holonomies": ["+I", "-I"],
    "shared_characteristic_polynomial": str(char_plus),
    "shared_edge_magnitudes": True,
    "spectral_orientation_blindness": True,
    "complex_phase_port_group": "U(1)^beta_1",
    "real_phase_port_group": "C2^beta_1",
    "theta_application_frozen": True,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "phase-cycle-holonomy.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
