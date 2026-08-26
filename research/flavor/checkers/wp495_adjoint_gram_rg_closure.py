"""Exact adjoint port-Gram RG closure audit for WP495."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp447 = load("wp447_irreducible_adjoint_triplet.json")
wp494 = load("wp494_port_alignment_rg_closure.json")

T3 = sp.diag(1, -1, 0) / 2
T8 = sp.diag(1, 1, -2) / (2 * sp.sqrt(3))
zero = sp.zeros(3)


def invariants(matrices):
    gram = sp.Matrix(3, 3, lambda i, j: sp.simplify(sp.trace(matrices[i] * matrices[j])))
    radial = sp.factor(sp.trace(gram) ** 2)
    gram_square = sp.factor(sp.trace(gram * gram))
    commutator = sp.factor(
        sum(
            sp.trace(
                (matrices[i] * matrices[j] - matrices[j] * matrices[i]).conjugate().T
                * (matrices[i] * matrices[j] - matrices[j] * matrices[i])
            )
            for i in range(3)
            for j in range(i + 1, 3)
        )
    )
    return gram, radial, gram_square, commutator


parallel = [T3, T3, zero]
orthogonal = [T3, T8, zero]
gp, ap, bp, kp = invariants(parallel)
go, ao, bo, ko = invariants(orthogonal)

mu = sp.symbols("mu", positive=True)
J = [
    sp.Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]]) / sp.sqrt(2),
    sp.Matrix([[0, -sp.I, 0], [sp.I, 0, -sp.I], [0, sp.I, 0]]) / sp.sqrt(2),
    sp.diag(1, 0, -1),
]
vacuum_gram, vacuum_radial, vacuum_gram_square, vacuum_commutator = invariants([mu * matrix for matrix in J])
vacuum_port_gauge_shape = sp.factor(vacuum_radial - vacuum_gram_square)

# With Tr(T_a T_b)=delta_ab/2, the component-vector SO(3) contraction is four
# times this matrix-normalized invariant. Only support and independence are
# needed for the closure theorem.
parallel_port_shape = sp.factor(ap - bp)
orthogonal_port_shape = sp.factor(ao - bo)

checks = {
    "wp447_dependency_passed": wp447["passed"],
    "wp494_dependency_passed": wp494["passed"],
    "hostile_grams_are_distinct": gp != go,
    "hostile_pair_has_equal_radial_quartic": ap == ao == 1,
    "hostile_pair_has_zero_commutator_square": kp == ko == 0,
    "hostile_pair_has_distinct_gram_square": bp == 1 and bo == sp.Rational(1, 2),
    "port_gauge_shape_distinguishes_pair": parallel_port_shape == 0 and orthogonal_port_shape == sp.Rational(1, 2),
    "spin_one_vacuum_gram_is_isotropic": vacuum_gram == 2 * mu**2 * sp.eye(3),
    "spin_one_vacuum_radial_is_thirty_six": vacuum_radial == 36 * mu**4,
    "spin_one_vacuum_gram_square_is_twelve": vacuum_gram_square == 12 * mu**4,
    "spin_one_port_gauge_shape_is_twenty_four": vacuum_port_gauge_shape == 24 * mu**4,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP495",
    "domain": "three Hermitian SU(3)_F adjoints transforming as an SO(3)_P vector, with canonical generator normalization",
    "invariants": {
        "I_rad_X": "(Tr G_X)^2",
        "I_gram_X": "Tr(G_X^2)",
        "I_comm_X": "sum_{i<j} ||[X_i,X_j]||_F^2",
        "port_gauge_support": "4 (I_rad_X-I_gram_X) in component-vector normalization",
    },
    "hostile_pair": {
        "parallel": "X_1=T_3, X_2=T_3, X_3=0",
        "orthogonal": "X_1=T_3, X_2=T_8, X_3=0",
        "shared": {"I_rad_X": str(ap), "I_comm_X": str(kp)},
        "different": {"parallel_I_gram_X": str(bp), "orthogonal_I_gram_X": str(bo)},
    },
    "spin_one_vacuum": {
        "G_X": [[str(value) for value in row] for row in vacuum_gram.tolist()],
        "I_rad_X": str(vacuum_radial),
        "I_gram_X": str(vacuum_gram_square),
        "matrix_normalized_port_shape": str(vacuum_port_gauge_shape),
    },
    "new_compulsory_invariant": "Tr(G_X^2) with an independent running coefficient",
    "classification": "The WP447 radial-plus-commutator quartic basis is not closed under SO(3)_P gauge support after port gauging.",
    "selector": False,
    "rigidifier": False,
    "instrument": None,
    "smallest_exact_falsifier": "Parallel T_3,T_3 and orthogonal T_3,T_8 configurations have identical radial invariant one and commutator invariant zero, but Gram-square invariants one and one-half.",
    "remaining_gate": "Add Tr(G_X^2), complete the independent SU(3)_F single-trace quartic census and cyclic-row connector census, then recompute the vacuum Hessian and thresholds.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp495_adjoint_gram_rg_closure.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
