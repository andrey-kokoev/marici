"""Exact port-symmetry versus messenger-entrance obstruction for WP482."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp479 = load("wp479_triplet_portal_port_rank.json")
wp481 = load("wp481_coupled_fixed_ray_acceptance.json")

# Real vector generators of the connected oriented triplet symmetry.
L1 = sp.Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]])
L2 = sp.Matrix([[0, 0, 1], [0, 0, 0], [-1, 0, 0]])
L3 = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
so3_generators = [L1, L2, L3]
stacked_generators = sp.Matrix.vstack(*so3_generators)
so3_invariant_vectors = stacked_generators.nullspace()

w11, w22, w33, w12, w13, w23 = sp.symbols("w11 w22 w33 w12 w13 w23")
w_variables = [w11, w22, w33, w12, w13, w23]
W = sp.Matrix([[w11, w12, w13], [w12, w22, w23], [w13, w23, w33]])


def commutant_solution_dimension(generators):
    equations = []
    for generator in generators:
        equations.extend(list(W * generator - generator * W))
    coefficient_matrix, _ = sp.linear_eq_to_matrix(equations, w_variables)
    return len(w_variables) - coefficient_matrix.rank()


so3_symmetric_commutant_dimension = commutant_solution_dimension(so3_generators)

# Reducible permutation representation of S3.
P12 = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
P123 = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
s3_generators = [P12, P123]
s3_invariance_matrix = sp.Matrix.vstack(*[generator - sp.eye(3) for generator in s3_generators])
s3_invariant_vectors = s3_invariance_matrix.nullspace()
s3_symmetric_commutant_dimension = commutant_solution_dimension(s3_generators)
ones = sp.ones(3, 1)
ones_gram = ones * ones.T

checks = {
    "wp479_dependency_passed": wp479["passed"],
    "wp481_dependency_passed": wp481["passed"],
    "oriented_triplet_has_no_invariant_vector": so3_invariant_vectors == [],
    "oriented_triplet_symmetric_commutant_is_one_dimensional": so3_symmetric_commutant_dimension == 1,
    "identity_commutes_with_oriented_triplet": all(sp.eye(3) * generator == generator * sp.eye(3) for generator in so3_generators),
    "permutation_triplet_has_one_invariant_vector": len(s3_invariant_vectors) == 1,
    "permutation_invariant_vector_is_all_ones": s3_invariant_vectors[0].cross(ones) == sp.zeros(3, 1),
    "permutation_symmetric_commutant_is_two_dimensional": s3_symmetric_commutant_dimension == 2,
    "ones_gram_is_allowed_by_permutations": all(ones_gram * generator == generator * ones_gram for generator in s3_generators),
    "ones_gram_is_not_isotropic": ones_gram != sp.eye(3),
    "permutation_entrance_sees_only_rank_one_singlet": ones_gram.rank() == 1,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP482",
    "minimal_chain": "Qbar H U_R + Ubar_L X_i u_R + Ubar_L M U_R with external Q,H,u singlets under the adjoint-label symmetry",
    "irreducible_oriented_triplet": {
        "invariant_vector_dimension": len(so3_invariant_vectors),
        "symmetric_gram_commutant_dimension": so3_symmetric_commutant_dimension,
        "consequence": "The symmetry enforces W proportional to I_3 but forbids the Qbar H U_R entrance and any invariant singlet-triplet mass intertwiner.",
    },
    "reducible_permutation_triplet": {
        "invariant_vector_dimension": len(s3_invariant_vectors),
        "invariant_vector": [1, 1, 1],
        "symmetric_gram_commutant_dimension": s3_symmetric_commutant_dimension,
        "general_form": "a*I_3+b*1*1^T",
        "consequence": "The singlet entrance exists, but symmetry permits a second Gram coefficient and the entrance alone probes only the rank-one singlet direction.",
    },
    "one_stage_no_go": {
        "statement": "With exact irreducible triplet symmetry and singlet external quarks/Higgs, no one-stage vectorlike messenger representation has both an invariant entrance and an invariant flavon exit connected by a symmetry-preserving mass.",
        "reason": "The entrance needs a trivial messenger component; the flavon exit needs a triplet component; exact invariant masses cannot mix inequivalent irreducible components.",
    },
    "classification": "The symmetry that would source-enforce the isotropic Gram is incompatible with the minimal executable messenger entrance; the permutation repair restores entrance but not isotropy.",
    "selector": False,
    "rigidifier": False,
    "reference_port_required": bool(so3_invariant_vectors == []),
    "reference_port_typing": "An added dynamical connector or prepared port vector changes the source field content and stabilizer groupoid; it does not reveal an absolute triplet orientation.",
    "instrument": None,
    "smallest_exact_falsifier": "Hom_SO(3)(1,3)=0 while the symmetric commutant of 3 is one-dimensional; switching to the permutation 1+2 representation makes Hom nonzero but enlarges the commutant to dimension two.",
    "remaining_gate": "Declare a renormalizable connector sector that prepares the messenger entrance, state its changed stabilizer groupoid, and prove that integrating it out yields W=kappa I_3 without new free Gram ratios.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp482_port_symmetry_entrance_obstruction.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
