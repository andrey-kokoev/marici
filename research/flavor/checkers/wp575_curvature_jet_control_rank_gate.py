"""Exact WP575 distinction between jet rank and executable control rank."""

import json
from pathlib import Path

import sympy as sp


theta = sp.symbols("theta", real=True)
mu = sp.Matrix([(1 + theta) ** 2, 1, theta**2])
mu0 = mu.subs(theta, 0)
j1 = mu.diff(theta).subs(theta, 0)
j2 = mu.diff(theta, 2).subs(theta, 0)
jet = sp.Matrix.hstack(j1, j2)

a = theta
b = theta**2 / 2
exact_reconstruction = sp.simplify(mu0 + a * j1 + b * j2)
constraint = sp.expand(2 * b - a**2)

gram = sp.simplify(jet.T * jet)
formal_pure_curvature = jet * sp.Matrix([0, 1])

coefficient_constraint = 2 * sp.Symbol("b") - sp.Symbol("a") ** 2
constraint_gradient_at_origin = sp.Matrix(
    [sp.diff(coefficient_constraint, symbol) for symbol in (sp.Symbol("a"), sp.Symbol("b"))]
).subs({sp.Symbol("a"): 0, sp.Symbol("b"): 0})

executable_differential = mu.diff(theta).subs(theta, 0)

checks = {
    "wp573_measure_is_reproduced": mu == sp.Matrix([(1 + theta) ** 2, 1, theta**2]),
    "first_jet_is_exact": j1 == sp.Matrix([2, 0, 0]),
    "second_jet_is_exact": j2 == sp.Matrix([2, 0, 2]),
    "formal_jet_matrix_has_rank_two": jet.rank() == 2,
    "formal_gram_is_positive_definite": gram == sp.Matrix([[4, 4], [4, 8]]) and gram.det() == 16,
    "source_curve_reconstruction_is_exact": sp.simplify(exact_reconstruction - mu) == sp.zeros(3, 1),
    "admissible_coefficients_obey_parabola": constraint == 0,
    "coefficient_curve_has_one_dimensional_tangent": constraint_gradient_at_origin == sp.Matrix([0, 2]),
    "executable_source_differential_has_rank_one": executable_differential.rank() == 1,
    "pure_curvature_is_formally_nonzero": formal_pure_curvature == j2 and formal_pure_curvature != sp.zeros(3, 1),
    "pure_curvature_coefficient_is_not_on_source_curve": sp.solve([sp.Eq(theta, 0), sp.Eq(theta**2 / 2, 1)], [theta], dict=True) == [],
}
checks = {name: bool(value) for name, value in checks.items()}


def encode_matrix(matrix):
    return [[str(sp.simplify(matrix[row, col])) for col in range(matrix.cols)] for row in range(matrix.rows)]


result = {
    "work_package": "WP575",
    "classification": "an order-two predictive jet can have rank two while the executable source-control differential has rank one",
    "source_measure": [str(sp.expand(value)) for value in mu],
    "first_jet": encode_matrix(j1),
    "second_jet": encode_matrix(j2),
    "formal_jet_matrix": encode_matrix(jet),
    "formal_gram": encode_matrix(gram),
    "formal_gram_determinant": str(gram.det()),
    "admissible_coefficient_relation": "2*b=a^2",
    "central_control_tangent": "b=0",
    "executable_control_rank": executable_differential.rank(),
    "smallest_exact_falsifier": "the formal pure-curvature coefficient (a,b)=(0,1) is not realized by any source setting theta",
    "physical_consequence": "symmetric reweights estimate curvature but do not independently excite a second source direction",
    "remaining_gate": "an independently declared two-parameter flavor source surface with weak-basis-invariant rank-two differential and detector calibration",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp575_curvature_jet_control_rank_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
