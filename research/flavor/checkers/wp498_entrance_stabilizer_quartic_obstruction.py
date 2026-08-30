"""Exact equal-entrance stabilizer quartic obstruction for WP498."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp492 = load("wp492_canonical_messenger_tensor_grammar.json")
wp497 = load("wp497_cyclic_row_quartic_census.json")

# Use an orthonormal row basis whose first axis is the normalized equal-
# entrance vector. Canonical row kinetics restrict internal symmetries to O(3).
h = sp.Matrix([1, 0, 0])
x = sp.Matrix(sp.symbols("a b c d e f", real=True))
a, b, c, d, e, f = x
R = sp.Matrix([[a, d, e], [d, b, f], [e, f, c]])


def symmetric_representation(generator):
    variation = sp.expand(generator * R + R * generator.T)
    components = sp.Matrix(
        [variation[0, 0], variation[1, 1], variation[2, 2],
         variation[0, 1], variation[0, 2], variation[1, 2]]
    )
    return components.jacobian(x)


J01 = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
J02 = sp.Matrix([[0, 0, -1], [0, 0, 0], [1, 0, 0]])
J12 = sp.Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]])
generators = [J01, J02, J12]
representations = [symmetric_representation(generator) for generator in generators]

m_symbols = sp.symbols("m0:21", real=True)
M = sp.zeros(6)
cursor = 0
for i in range(6):
    for j in range(i, 6):
        M[i, j] = M[j, i] = m_symbols[cursor]
        cursor += 1


def invariant_dimension(active_representations):
    equations = []
    for representation in active_representations:
        equations.extend(list(representation.T * M + M * representation))
    constraint_matrix, _ = sp.linear_eq_to_matrix(equations, m_symbols)
    return len(m_symbols) - constraint_matrix.rank()


stabilizer_dimension = invariant_dimension([representations[2]])
full_so3_dimension = invariant_dimension(representations)

# This reflection completes SO(2) to O(2).
reflection = sp.diag(1, 1, -1)
reflection_representation = sp.diag(1, 1, 1, 1, -1, -1)

trace_transverse = b + c
stabilizer_polynomials = [
    a**2,
    a * trace_transverse,
    trace_transverse**2,
    d**2 + e**2,
    (b - c) ** 2 + 4 * f**2,
]
stabilizer_matrices = [sp.hessian(polynomial, x) / 2 for polynomial in stabilizer_polynomials]


def flatten_symmetric(matrix):
    return [matrix[i, j] for i in range(6) for j in range(i, 6)]


stabilizer_basis_rank = sp.Matrix(
    [flatten_symmetric(matrix) for matrix in stabilizer_matrices]
).rank()
stabilizer_basis_is_continuously_invariant = all(
    representations[2].T * matrix + matrix * representations[2] == sp.zeros(6)
    for matrix in stabilizer_matrices
)
stabilizer_basis_is_reflection_invariant = all(
    reflection_representation.T * matrix * reflection_representation == matrix
    for matrix in stabilizer_matrices
)

radial_polynomial = sp.expand(sp.trace(R) ** 2)
frobenius_polynomial = sp.expand(sp.trace(R * R))
current_matrices = [
    sp.hessian(radial_polynomial, x) / 2,
    sp.hessian(frobenius_polynomial, x) / 2,
]
current_rank = sp.Matrix(
    [flatten_symmetric(matrix) for matrix in current_matrices]
).rank()
combined_rank = sp.Matrix(
    [flatten_symmetric(matrix) for matrix in current_matrices + stabilizer_matrices]
).rank()

u01, u02, u12 = sp.symbols("u01 u02 u12", real=True)
general_generator = u01 * J01 + u02 * J02 + u12 * J12
stabilizer_constraints, _ = sp.linear_eq_to_matrix(list(general_generator * h), [u01, u02, u12])
row_stabilizer_lie_dimension = 3 - stabilizer_constraints.rank()

checks = {
    "wp492_dependency_passed": wp492["passed"],
    "wp497_dependency_passed": wp497["passed"],
    "equal_entrance_stabilizer_lie_dimension_is_one": row_stabilizer_lie_dimension == 1,
    "stabilizer_generator_fixes_entrance": J12 * h == sp.zeros(3, 1),
    "two_full_so3_generators_move_entrance": J01 * h != sp.zeros(3, 1) and J02 * h != sp.zeros(3, 1),
    "o2_stabilizer_quartic_dimension_is_five": stabilizer_dimension == 5,
    "explicit_five_form_basis_is_independent": stabilizer_basis_rank == 5,
    "explicit_basis_is_so2_invariant": stabilizer_basis_is_continuously_invariant,
    "explicit_basis_is_reflection_invariant": stabilizer_basis_is_reflection_invariant,
    "current_radial_and_frobenius_rank_is_two": current_rank == 2,
    "current_plus_explicit_basis_spans_stabilizer_space": combined_rank == 5,
    "missing_stabilizer_quartic_codimension_is_three": stabilizer_dimension - current_rank == 3,
    "full_so3_quartic_dimension_is_two": full_so3_dimension == 2,
    "reflection_fixes_equal_entrance": reflection * h == h,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP498",
    "domain": "quartics quadratic in R=SS^T with canonical row kinetic normalization and the frozen nonzero equal-entrance vector",
    "equal_entrance_basis": "h=e0 after an orthogonal change of row basis",
    "maximal_orthogonal_stabilizer": "O(2)",
    "stabilizer_lie_dimension": int(row_stabilizer_lie_dimension),
    "o2_invariant_quartic_dimension": int(stabilizer_dimension),
    "explicit_o2_basis": [str(sp.expand(polynomial)) for polynomial in stabilizer_polynomials],
    "current_basis_rank": int(current_rank),
    "missing_o2_codimension": int(stabilizer_dimension - current_rank),
    "full_so3_invariant_quartic_dimension": int(full_so3_dimension),
    "authority": "The frozen nonzero entrance vector reduces row O(3) to its O(2) stabilizer. That largest compatible symmetry permits five connector quartics, so it cannot authorize the current two-coupling truncation. Full row SO(3) would give two invariants but forbids the existing nonzero entrance vertex unless a new source field or spurion is added.",
    "classification": "Exact source-symmetry obstruction: strengthening only the existing row symmetry cannot close the connector scalar action to its two retained quartics.",
    "selector": False,
    "rigidifier": False,
    "instrument": None,
    "smallest_exact_falsifier": "The maximal orthogonal stabilizer of the equal-entrance vector has a five-dimensional invariant connector-quartic space, while the retained radial and Frobenius forms have rank two.",
    "remaining_gate": "Either run at least the full five-coupling O(2)-invariant connector basis, or add an independently motivated dynamical entrance field transforming under full row SO(3) and recompute its vacuum, gauge quotient, messenger matching, Hessian, poles, residues, and widths.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp498_entrance_stabilizer_quartic_obstruction.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
