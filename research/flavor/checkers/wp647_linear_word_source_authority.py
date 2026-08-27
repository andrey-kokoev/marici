"""Exact WP647 source-authority test for the WP646 linear-word window."""
import json
import runpy
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp646 = runpy.run_path(str(ROOT / "checkers" / "wp646_nonaligned_word_response_ladder.py"))
I = sp.I
J = wp646["J"]

# Real triplet generators. Infinitesimal invariance requires L_i c = 0.
L = [
    sp.Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [-1, 0, 0]]),
    sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]]),
]
stacked = sp.Matrix.vstack(*L)

# Rank-two invariants solve L_i A - A L_i = 0.
a = sp.symbols("a0:9")
A = sp.Matrix(3, 3, a)
commutator_system = sp.Matrix.vstack(*[(Li*A-A*Li).reshape(9, 1) for Li in L])
commutator_matrix, _ = sp.linear_eq_to_matrix(list(commutator_system), a)

reference_words = [sp.eye(3), J[2]]
reference_response = wp646["response"](reference_words)
casimir = sp.simplify(sum((Ji*Ji for Ji in J), sp.zeros(3)))

checks = {
    "triplet_invariance_system_has_full_rank": stacked.rank() == 3,
    "invariant_vector_space_is_zero": len(stacked.nullspace()) == 0,
    "rank_two_commutant_is_one_dimensional": len(commutator_matrix.nullspace()) == 1,
    "rank_two_invariant_is_scalar_identity": (
        sp.Matrix(3, 3, commutator_matrix.nullspace()[0]).is_diagonal()
        and len(set(sp.Matrix(3, 3, commutator_matrix.nullspace()[0]).diagonal())) == 1
    ),
    "spin_one_casimir_is_two_identity": casimir == 2*sp.eye(3),
    "single_reference_response_shape_is_ten_by_eight": reference_response.shape == (10, 8),
    "single_reference_response_rank_is_six": reference_response.rank() == 6,
    "single_reference_does_not_recover_rank_nine": reference_response.rank() < 9,
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP647",
    "status": "PASS",
    "checks": checks,
    "original_groupoid": "oriented SO(3) triplet source symmetry",
    "source_authorized_linear_coefficient_dimension": 0,
    "source_authorized_quadratic_invariant_dimension": 1,
    "quadratic_readout": "spin-one Casimir 2I; flavor-universal",
    "reference_extension": {
        "resource": "one declared oriented triplet n",
        "stabilizer_groupoid": "SO(2)_n",
        "word_family_per_sector": ["I", "J_n"],
        "real_control_dimension": 8,
        "exact_hostile_witness_response_rank": 6,
    },
    "classification": "original source: neither selector nor rank-nine carrier; one-port extension: relational rigidifier with rank-six response",
    "smallest_exact_falsifier": "a nonzero vector fixed by all three SO(3) generators",
    "remaining_gate": "derive a dynamical symmetry-breaking tensor and its vacuum independently; then test its induced coefficients on all 1210 sheets",
}
(ROOT / "results" / "wp647_linear_word_source_authority.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
