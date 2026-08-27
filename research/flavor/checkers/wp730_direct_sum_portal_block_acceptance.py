"""Exact direct-sum portal-block fixed-point and relevant-mode acceptance theorem."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
a, b, c = sp.symbols("a b c", real=True)
qA, qB = sp.symbols("q_A q_B", positive=True)
M = sp.Matrix([[a, c], [c, b]])
source = sp.Matrix([4 * qA, 3 * qB])
D = sp.factor(M.det())
fixed = sp.simplify(M.inv() * source)
d = sp.Matrix([[1, -1]])
contrast = sp.factor((d * fixed)[0])
expected_contrast = sp.factor((4 * qA * (b + c) - 3 * qB * (a + c)) / D)
cancellation = sp.solve(sp.Eq(contrast, 0), qB)[0]

A = sp.Integer(1)
even = sp.Matrix([1, 1])
odd = sp.Matrix([1, -1])
safe_contrast_matrix = sp.Matrix([[A, -2], [-2, A]])
unsafe_contrast_matrix = sp.Matrix([[A, 2], [2, A]])

numeric_positive = sp.Matrix([[2, 1], [1, 3]])
numeric_fixed = numeric_positive.inv() * sp.Matrix([4, 3])

checks = {
    "mixed_portal_block_determinant": D == a * b - c**2,
    "unique_fixed_pair_is_exact": fixed == sp.Matrix([(4 * b * qA - 3 * c * qB) / D, (3 * a * qB - 4 * c * qA) / D]),
    "fixed_contrast_formula_is_exact": sp.simplify(contrast - expected_contrast) == 0,
    "cross_coupling_shifts_positive_cancellation_fiber": sp.simplify(cancellation - 4 * qA * (b + c) / (3 * (a + c))) == 0,
    "positive_definite_numeric_block_has_irrelevant_modes": numeric_positive.is_positive_definite is True,
    "positive_definite_numeric_block_has_unique_nonzero_contrast": numeric_fixed == sp.Matrix([sp.Rational(9, 5), sp.Rational(2, 5)]),
    "even_relevant_witness_has_exponents_minus_one_and_three": safe_contrast_matrix.eigenvals() == {-1: 1, 3: 1},
    "even_relevant_mode_is_contrast_invisible": d * even == sp.zeros(1, 1),
    "odd_mode_is_irrelevant_in_safe_witness": safe_contrast_matrix * odd == 3 * odd,
    "odd_relevant_witness_has_exponents_minus_one_and_three": unsafe_contrast_matrix.eigenvals() == {-1: 1, 3: 1},
    "odd_mode_is_relevant_in_unsafe_witness": unsafe_contrast_matrix * odd == -odd,
    "odd_relevant_mode_changes_contrast": (d * odd)[0] == 2,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP730",
    "status": "PASS",
    "checks": checks,
    "state_coordinate": "the ordered two-portal block of the simultaneous representation-labelled source",
    "fixed_contrast": "[4 q_A (b+c) - 3 q_B (a+c)]/(a b-c^2)",
    "cancellation_fiber": "q_B/q_A = 4(b+c)/[3(a+c)]",
    "full_irrelevance_gate": "the symmetric portal stability block must be positive definite: a>0 and a b-c^2>0",
    "partial_relevance_gate": "every relevant eigenvector must be annihilated by the contrast covector (1,-1)",
    "smallest_exact_falsifiers": [
        "the shifted positive cancellation fiber makes the fixed contrast zero",
        "a relevant odd eigenvector gives the contrast a free critical-surface amplitude",
    ],
    "claim_boundary": "the theorem gives acceptance conditions but does not derive the direct-sum beta coefficients",
    "remaining_source_gate": "compute a,b,c,q_A,q_B and the complete stability eigenvectors from the simultaneous anomaly-free action",
    "remaining_threshold_instrument_gate": "prove no external relevant direction enters contrast through finite matching and realize two calibrated labelled channels",
}
(ROOT / "results" / "wp730_direct_sum_portal_block_acceptance.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
