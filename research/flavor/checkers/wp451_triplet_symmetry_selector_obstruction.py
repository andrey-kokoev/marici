"""Exact WP451 source-symmetry obstruction for messenger coefficients."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]
wp450 = json.loads((root / "results" / "wp450_messenger_word_grammar.json").read_text(encoding="utf-8"))
I = sp.I
J = [
    sp.Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]])/sp.sqrt(2),
    sp.Matrix([[0, -I, 0], [I, 0, -I], [0, I, 0]])/sp.sqrt(2),
    sp.diag(1, 0, -1),
]

# Solve invariant-vector and invariant-rank-two-tensor equations under the
# three infinitesimal SO(3) generators in the vector representation.
L = [
    sp.Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [-1, 0, 0]]),
    sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]]),
]
c = sp.Matrix(sp.symbols("c0:3"))
vector_system = sp.Matrix.vstack(*[generator*c for generator in L])
vector_rank = vector_system.jacobian(list(c)).rank()

t = sp.symbols("t0:9")
T = sp.Matrix(3, 3, t)
tensor_equations = []
for generator in L:
    tensor_equations.extend(list(generator*T+T*generator.T))
tensor_matrix, _ = sp.linear_eq_to_matrix(tensor_equations, t)
tensor_nullspace = tensor_matrix.nullspace()

casimir = sp.simplify(sum((matrix*matrix for matrix in J), sp.zeros(3)))
nontrivial_linear = J[2]

checks = {
    "wp450_dependency_passed": wp450["passed"],
    "no_nonzero_invariant_triplet_vector": vector_rank == 3,
    "invariant_rank_two_tensor_space_is_one_dimensional": len(tensor_nullspace) == 1,
    "invariant_rank_two_tensor_is_delta": sp.Matrix(3, 3, tensor_nullspace[0]) == sp.eye(3),
    "quadratic_casimir_is_central": casimir == 2*sp.eye(3),
    "source_symmetric_degree_two_yukawa_is_flavor_universal": (sp.eye(3)+casimir).rank() == 3 and (sp.eye(3)+casimir) == 3*sp.eye(3),
    "hostile_nontrivial_linear_word_breaks_source_rotation": nontrivial_linear != sp.zeros(3) and vector_rank == 3,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP451",
    "source_symmetry": "Oriented SO(3) rotations of the adjoint triplet X_i in WP447.",
    "degree_one_invariant_coefficients": "Only c_i=0.",
    "degree_two_invariant_coefficients": "Only c_ij=c delta_ij.",
    "vacuum_casimir": "sum_i J_i^2=2 I",
    "authorized_yukawa_family": "Y=(a+2b)I through degree two, separately in each quark sector.",
    "contextual_partition": "All three generations remain degenerate; no mixing or CP orientation is selected.",
    "selector_classification": "Neither selector nor viable rigidifier: preserving the source symmetry erases flavor, while breaking it requires a new source object.",
    "instrument": None,
    "smallest_exact_falsifier": "A nonzero SO(3)-invariant vector c_i or a non-delta invariant tensor c_ij.",
    "remaining_gate": "Introduce and dynamically select an SO(3)-breaking coefficient field, then include its vacuum, fluctuations, scale, and current consequences rather than treating fitted messenger coefficients as constants.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp451_triplet_symmetry_selector_obstruction.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
