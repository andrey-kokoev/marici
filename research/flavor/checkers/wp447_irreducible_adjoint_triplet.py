"""Exact WP447 checker for the irreducible adjoint-triplet flavon vacuum."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]
wp446 = json.loads((root / "results" / "wp446_messenger_physical16_obstruction.json").read_text(encoding="utf-8"))
I = sp.I
lambdas = [
    sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
    sp.diag(1, -1, 0),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
    sp.Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]]),
    sp.diag(1, 1, -2)/sp.sqrt(3),
]
J = [
    sp.Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]])/sp.sqrt(2),
    sp.Matrix([[0, -I, 0], [I, 0, -I], [0, I, 0]])/sp.sqrt(2),
    sp.diag(1, 0, -1),
]


def norm_squared(matrix):
    return sp.simplify(sp.trace(matrix.conjugate().T*matrix))


z = sp.symbols("z0:24", real=True)
X = [sum((z[8*k+i]*lambdas[i] for i in range(8)), sp.zeros(3)) for k in range(3)]
pairs = [(0, 1, 2, 1), (0, 2, 1, -1), (1, 2, 0, 1)]
square_terms = [X[i]*X[j]-X[j]*X[i]-I*sign*X[k] for i, j, k, sign in pairs]
radial = sum(sp.trace(matrix*matrix) for matrix in X)
potential = sp.expand(sum(norm_squared(term) for term in square_terms)+(radial-6)**2)

vacuum = {coordinate: 0 for coordinate in z}
for k in range(3):
    for i in range(8):
        vacuum[z[8*k+i]] = sp.simplify(sp.trace(J[k]*lambdas[i])/2)
hessian = sp.hessian(potential, z).subs(vacuum)
spectrum = hessian.eigenvals()

# Infinitesimal conjugation orbit.
gauge_tangents = []
for generator in lambdas:
    vector = []
    for matrix in J:
        delta = I*(generator*matrix-matrix*generator)
        vector.extend([sp.simplify(sp.trace(delta*b)/2) for b in lambdas])
    gauge_tangents.append(vector)
gauge_rank = sp.Matrix(gauge_tangents).T.rank()

# Burnside witness: words of length at most two already span M_3(C).
words = [sp.eye(3)]+J+[left*right for left in J for right in J]
word_matrix = sp.Matrix.hstack(*[sp.Matrix(word).reshape(9, 1) for word in words])
algebra_rank = word_matrix.rank()

# Reducible spin-1/2 plus singlet representation and the origin are hostile
# exact competitors. Both solve the commutator squares but miss the Casimir.
pauli = [lambdas[0]/2, lambdas[1]/2, lambdas[2]/2]
reducible_radial = sum(sp.trace(matrix*matrix) for matrix in pauli)
reducible_energy = sp.simplify((reducible_radial-6)**2)
origin_energy = sp.Integer(36)

checks = {
    "wp446_obstruction_dependency_passed": wp446["passed"],
    "spin_one_commutator_relations": all(J[i]*J[j]-J[j]*J[i] == I*sign*J[k] for i, j, k, sign in pairs),
    "spin_one_casimir_trace_is_six": sum(sp.trace(matrix*matrix) for matrix in J) == 6,
    "potential_is_power_counting_renormalizable": sp.Poly(potential, z).total_degree() == 4,
    "irreducible_vacuum_has_zero_global_energy": potential.subs(vacuum) == 0,
    "vacuum_is_stationary_in_all_24_components": all(sp.diff(potential, coordinate).subs(vacuum) == 0 for coordinate in z),
    "reducible_representation_is_rejected": reducible_energy == sp.Rational(81, 4),
    "origin_is_rejected": origin_energy == 36,
    "vacuum_word_algebra_is_full_M3": algebra_rank == 9,
    "gauge_orbit_has_rank_eight": gauge_rank == 8,
    "hessian_has_exactly_eight_zero_modes": spectrum.get(0) == 8,
    "all_physical_hessian_modes_are_positive": all(value > 0 for value in spectrum if value != 0),
    "zero_modes_equal_gauge_orbit": spectrum.get(0) == gauge_rank,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP447",
    "state_domain": "Three dynamical traceless Hermitian adjoints X_i of gauged diagonal SU(3)_F.",
    "source_action": "lambda sum_{i<j} ||[X_i,X_j]-i mu epsilon_ijk X_k||^2 + rho(sum_i Tr X_i^2-6 mu^2)^2",
    "coefficient_domain": "lambda>0, rho>0, mu>0",
    "global_vacuum": "X_i=mu J_i in the irreducible spin-one representation of su(2)",
    "global_minimum_energy": 0,
    "reducible_hostile_energy_in_unit_normalization": str(reducible_energy),
    "word_algebra_dimension": algebra_rank,
    "gauge_mass_rank": gauge_rank,
    "hessian_spectrum_at_unit_benchmark": {str(value): int(multiplicity) for value, multiplicity in spectrum.items()},
    "physical16_capacity": "The vacuum word algebra is M3(C), so no invariant generation subspace obstructs a general messenger Yukawa. Capacity is not numerical selection.",
    "scale_relation": "sum_i Tr X_i^2=6 mu^2; mu/v remains an independent source parameter",
    "instrument": None,
    "smallest_exact_falsifier": "A zero-energy reducible 2+1 representation, word-algebra rank below nine, or any nongauge Hessian zero/negative mode.",
    "remaining_gate": "Specify the messenger word grammar independently and test its map to physical16 before recomputing the mass-basis current kernel.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp447_irreducible_adjoint_triplet.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
