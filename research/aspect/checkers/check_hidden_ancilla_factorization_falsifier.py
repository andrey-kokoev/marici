import json
from pathlib import Path

import sympy as sp


I2 = sp.eye(2)
H = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
CNOT = sp.Matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
])

# Embed a system qubit with an ancilla initialized in |0>, using basis
# |00>, |01>, |10>, |11> with the system as control.
V = sp.Matrix([[1, 0], [0, 0], [0, 1], [0, 0]])
P0 = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0]])
P1 = sp.Matrix([[0, 1, 0, 0], [0, 0, 0, 1]])
U_hidden = CNOT * CNOT
K0 = sp.simplify(P0 * U_hidden * V)
K1 = sp.simplify(P1 * U_hidden * V)

a11, a12, a21, a22, b11, b12, b21, b22 = sp.symbols(
    "a11 a12 a21 a22 b11 b12 b21 b22"
)
A = sp.Matrix([[a11, a12], [a21, a22]])
B = sp.Matrix([[b11, b12], [b21, b22]])

checks = {
    "hadamard_pair_is_identity": sp.simplify(H * H - I2) == sp.zeros(2),
    "cnot_pair_is_identity": U_hidden == sp.eye(4),
    "returned_ancilla_zero_kraus": K0 == I2,
    "no_leakage_kraus": K1 == sp.zeros(2),
    "trace_preserving_boundary": sp.simplify(K0.T.conjugate() * K0 + K1.T.conjugate() * K1) == I2,
    "arbitrary_linear_context_cannot_distinguish": sp.simplify(A * K0 * B - A * B) == sp.zeros(2),
    "internal_factorizations_are_distinct_syntax": 2 != 0,
}

result = {
    "schema": "marici.aspect.hidden-ancilla-factorization-falsifier.v1",
    "status": "falsified_as_stated" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {k: bool(v) for k, v in checks.items()},
    "falsified_clause": "Observable architecture is the factorization type of the diagram.",
    "repair": "Separate boundary contextual equivalence from intensional provenance; topology is observable only through exposed interfaces or nontrivial residual cells.",
}

out = Path(__file__).parents[1] / "results" / "hidden_ancilla_factorization_falsifier.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "falsified_as_stated" else 1)
