import hashlib
import json
from pathlib import Path

import sympy as sp


n = 3
omega = sp.exp(2 * sp.pi * sp.I / n)
X = sp.zeros(n)
for column in range(n):
    X[(column + 1) % n, column] = 1
Z = sp.diag(*[omega**j for j in range(n)])
assert sp.simplify(Z * X - omega * X * Z) == sp.zeros(n)

B1 = sp.Matrix([[1, 0, 1], [-1, 1, 0], [0, -1, -1]])
B2 = sp.Matrix([[1], [1], [-1]])
assert B1 * B2 == sp.zeros(3, 1)

z_error = sp.Matrix([1, 0, 0])
x_error_first = sp.Matrix([1, 0, 0])
x_error_reversed = sp.Matrix([0, 0, 1])
electric = (B1 * z_error).applyfunc(lambda value: int(value) % n)
magnetic_first = (B2.T * x_error_first).applyfunc(lambda value: int(value) % n)
magnetic_reversed = (B2.T * x_error_reversed).applyfunc(lambda value: int(value) % n)
assert electric == sp.Matrix([1, 2, 0])
assert magnetic_first == sp.Matrix([1])
assert magnetic_reversed == sp.Matrix([2])

# Every star/plaquette commutator exponent vanishes.
commutator_exponents = (B1 * B2).applyfunc(lambda value: int(value) % n)
assert commutator_exponents == sp.zeros(3, 1)

payload = {
    "status": "pass",
    "theorem": "generalized_toric_syndromes_are_commutator_characters",
    "qudit_dimension": n,
    "pauli_convention": "Z*X = omega*X*Z",
    "electric_syndrome_formula": "partial_1*z mod n",
    "magnetic_syndrome_formula": "partial_2^T*x mod n",
    "unit_Z_edge_error_syndrome": [1, 2, 0],
    "unit_X_first_edge_flux": [1],
    "unit_X_reversed_edge_flux": [2],
    "star_plaquette_commutator_exponents": [0, 0, 0],
    "orientation_required_beyond_qubits": True,
    "decoder_selected_by_syndrome": False,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "generalized-toric-syndromes.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
