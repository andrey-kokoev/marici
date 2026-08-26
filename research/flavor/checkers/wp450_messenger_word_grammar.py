"""Exact WP450 audit of the degree-two messenger word grammar."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]
wp447 = json.loads((root / "results" / "wp447_irreducible_adjoint_triplet.json").read_text(encoding="utf-8"))
I = sp.I
J = [
    sp.Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]])/sp.sqrt(2),
    sp.Matrix([[0, -I, 0], [I, 0, -I], [0, I, 0]])/sp.sqrt(2),
    sp.diag(1, 0, -1),
]

linear_words = [sp.eye(3)]+J
all_degree_two_words = linear_words+[left*right for left in J for right in J]
basis_names = ["I", "J1", "J2", "J3", "J1J1", "J1J2", "J1J3", "J2J2", "J2J3"]
basis_words = [sp.eye(3), J[0], J[1], J[2], J[0]*J[0], J[0]*J[1], J[0]*J[2], J[1]*J[1], J[1]*J[2]]

def word_matrix(words):
    return sp.Matrix.hstack(*[matrix.reshape(9, 1) for matrix in words])


linear_rank = word_matrix(linear_words).rank()
degree_two_rank = word_matrix(all_degree_two_words).rank()
basis_map = word_matrix(basis_words)

# Hostile matrix entry forbidden to the linear grammar but reconstructed
# uniquely by the frozen degree-two basis.
E13 = sp.zeros(3)
E13[0, 2] = 1
hostile_coefficients = sp.simplify(basis_map.inv()*E13.reshape(9, 1))
hostile_reconstruction = sum((hostile_coefficients[i]*basis_words[i] for i in range(9)), sp.zeros(3))

checks = {
    "wp447_dependency_passed": wp447["passed"],
    "linear_word_grammar_has_rank_four": linear_rank == 4,
    "degree_two_word_grammar_has_rank_nine": degree_two_rank == 9,
    "frozen_nine_word_basis_is_invertible": basis_map.det() != 0,
    "hostile_E13_is_not_in_linear_span": word_matrix(linear_words).row_join(E13.reshape(9, 1)).rank() > linear_rank,
    "hostile_E13_is_exactly_reconstructed_at_degree_two": hostile_reconstruction == E13,
    "coefficient_map_is_injective": basis_map.nullspace() == [],
    "one_complex_coefficient_per_basis_word": len(basis_words) == 9,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP450",
    "frozen_word_basis": basis_names,
    "operator_grammar": "For each quark sector, I is dimension four, J_i insertions arise from one vectorlike-messenger stage, and J_i J_j insertions from two stages.",
    "linear_span_dimension": linear_rank,
    "degree_two_span_dimension": degree_two_rank,
    "complex_coefficients_per_yukawa": len(basis_words),
    "hostile_E13_coefficients": {basis_names[i]: str(hostile_coefficients[i]) for i in range(9)},
    "contextual_partition": "The nine complex coefficients uniquely label literal 3x3 Yukawa matrices at the fixed vacuum, but physical quotienting and current orientation remain separate.",
    "selector_classification": "Universal carrier/rigidifier, not selector: arbitrary coefficients reproduce every complex Yukawa matrix and no source law fixes them.",
    "instrument": None,
    "smallest_exact_falsifier": "A complex 3x3 matrix outside the degree-two word span, or a nonzero coefficient null vector.",
    "remaining_gate": "A source symmetry or dynamics must reduce and select the messenger coefficients before the resulting current orientation can count as a prediction rather than a fit.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp450_messenger_word_grammar.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
