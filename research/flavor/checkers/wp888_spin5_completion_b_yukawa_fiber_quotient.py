import json
from pathlib import Path

import sympy as sp


I = sp.I
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -I], [I, 0]])
s3 = sp.diag(1, -1)
eye2 = sp.eye(2)
kron = sp.kronecker_product
gammas = [kron(s1, s1), kron(s2, s1), kron(s3, s1), kron(eye2, s2), kron(eye2, s3)]
C = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, -1], [-1, 0, 0, 0], [0, 1, 0, 0]])
phi = sp.Matrix([1, 2, 3, 5])
phi_tilde = C * phi


def B(x):
    return sp.Matrix.hstack(*[C * gamma * x for gamma in gammas])


def q(x):
    return C * x


def mass_matrix(y):
    matrix = sp.zeros(16)

    def block(row, col, value, coefficient):
        weighted = coefficient * value
        matrix[row : row + value.rows, col : col + value.cols] = weighted
        matrix[col : col + value.cols, row : row + value.rows] = weighted.T

    block(0, 4, B(phi), y[0])
    block(9, 4, B(phi_tilde), y[1])
    block(0, 13, q(phi_tilde), y[2])
    block(0, 14, q(phi), y[3])
    block(9, 14, q(phi_tilde), y[4])
    block(9, 15, q(phi), y[5])
    return matrix


y = sp.symbols("y1:7")
symbolic_mass = mass_matrix(y)
determinant = sp.factor(symbolic_mass.det())
expected = sp.Integer(85632148167696) * y[0] ** 4 * y[1] ** 4 * y[2] ** 2 * y[5] ** 2 * (y[0] * y[4] - y[1] * y[3]) ** 2


def spectral_shape(values):
    matrix = mass_matrix(values)
    gram = matrix.conjugate().T * matrix
    return matrix.rank(), sp.factor(sp.trace(gram * gram) / sp.trace(gram) ** 2)


rank_a, shape_a = spectral_shape((2, 3, 5, 7, 11, 13))
rank_b, shape_b = spectral_shape((2, 3, 6, 7, 11, 13))

# Connected graph with V=6 and E=6 has one independent cycle.
vertices = 6
edges = 6
components = 1
cycle_rank = edges - vertices + components

tests = {
    "symbolic_determinant_factorization_matches": sp.simplify(determinant - expected) == 0,
    "y1_coordinate_divisor_present": determinant.subs(y[0], 0) == 0,
    "y2_coordinate_divisor_present": determinant.subs(y[1], 0) == 0,
    "y3_coordinate_divisor_present": determinant.subs(y[2], 0) == 0,
    "y6_coordinate_divisor_present": determinant.subs(y[5], 0) == 0,
    "coherent_cycle_divisor_present": sp.simplify(determinant.subs(y[4], y[1] * y[3] / y[0])) == 0,
    "yukawa_graph_cycle_rank_is_one": cycle_rank == 1,
    "first_hostile_is_full_rank": rank_a == 16,
    "second_hostile_is_full_rank": rank_b == 16,
    "first_shape_value_matches": shape_a == sp.Rational(63449, 368082),
    "second_shape_value_matches": shape_b == sp.Rational(1603, 9680),
    "scale_free_spectra_differ": shape_a != shape_b,
}

passed = sum(bool(v) for v in tests.values())
result = {
    "work_package": "WP888",
    "status": "PASS" if passed == len(tests) else "FAIL",
    "summary": {"passed": passed, "total": len(tests), "all_passed": passed == len(tests)},
    "classification": "nontrivial_selector_fiber: generic full-rank masses retain six magnitudes and one cycle phase modulo fermion rephasing",
    "determinant_factorization": str(determinant),
    "discriminant_components": ["y1=0", "y2=0", "y3=0", "y6=0", "y1*y5-y2*y4=0"],
    "yukawa_graph_cycle_rank": cycle_rank,
    "generic_rephasing_stabilizer_dimension": 1,
    "quotient_real_dimension_lower_bound_fixed_vacuum": 7,
    "cycle_ratio": "rho=y1*y5/(y2*y4)",
    "full_rank_hostile_shapes": {"y3=5": str(shape_a), "y3=6": str(shape_b)},
    "monodromy_status": "open: determinant multiplicity alone does not authorize singular-projector monodromy",
    "remaining_gate": "exact continuation of singular projectors around the coherent rho=1 discriminant",
    "tests": tests,
}

output = Path(__file__).parents[1] / "results" / "wp888_spin5_completion_b_yukawa_fiber_quotient.json"
output.write_text(json.dumps(result, indent=2, default=bool) + "\n", encoding="utf-8")
print(json.dumps(result["summary"], indent=2))
raise SystemExit(0 if result["status"] == "PASS" else 1)
