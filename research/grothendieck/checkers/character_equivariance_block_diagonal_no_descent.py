import json
from pathlib import Path

import sympy as sp


a0, a1, a2, a3 = sp.symbols("a0 a1 a2 a3")
i = sp.I

# Regular representation of C4 and its general equivariant commutant.
shift = sp.Matrix([[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])
operator = a0 * sp.eye(4) + a1 * shift + a2 * shift**2 + a3 * shift**3
fourier = sp.Matrix([[i ** (-j * k) for k in range(4)] for j in range(4)]) / 2
diagonalized = sp.simplify(fourier * operator * fourier.conjugate().T)
off_diagonal = diagonalized - sp.diag(*[diagonalized[j, j] for j in range(4)])

trivial = sp.Matrix([1, 1, 1, 1])
nontrivial = sp.Matrix([1, i, -1, -i])

checks = {
    "operator_commutes_with_unit_action": sp.simplify(operator * shift - shift * operator) == sp.zeros(4),
    "character_fourier_transform_is_unitary": sp.simplify(fourier * fourier.conjugate().T - sp.eye(4)) == sp.zeros(4),
    "equivariant_operator_is_character_diagonal": sp.simplify(off_diagonal) == sp.zeros(4),
    "trivial_and_nontrivial_characters_are_orthogonal": (trivial.conjugate().T * nontrivial)[0] == 0,
    "no_cross_character_matrix_element": sp.simplify((trivial.conjugate().T * operator * nontrivial)[0]) == 0,
}

result = {
    "schema": "marici.grothendieck.character-equivariance-block-diagonal-no-descent.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "interpretation": "Every unit-equivariant comparison is diagonal in character space. Nontrivial twists cannot constrain the trivial Riemann block without an independently sourced symmetry-breaking or symmetry-extending incidence map.",
}

out = Path(__file__).parents[1] / "results" / "character_equivariance_block_diagonal_no_descent.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
