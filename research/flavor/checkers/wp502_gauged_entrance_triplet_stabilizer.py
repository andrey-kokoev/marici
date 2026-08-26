"""Exact gauged entrance-triplet stabilizer audit for WP502."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp484 = load("wp484_gauged_connector_frame_lift.json")
wp501 = load("wp501_external_entrance_rank_theorem.json")

I = sp.I
lambdas = [
    sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
    sp.diag(1, -1, 0),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
    sp.Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]]),
    sp.diag(1, 1, -2) / sp.sqrt(3),
]
J = [
    sp.Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]]) / sp.sqrt(2),
    sp.Matrix([[0, -I, 0], [I, 0, -I], [0, I, 0]]) / sp.sqrt(2),
    sp.diag(1, 0, -1),
]
L = [
    sp.Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [-1, 0, 0]]),
    sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]]),
]


def adjoint_coordinates(matrix):
    return [sp.simplify(sp.trace(matrix * basis) / 2) for basis in lambdas]


def orbit_matrix(entrance_vevs):
    tail_zeros = [0] * (3 * len(entrance_vevs))

    su3_tangents = []
    for generator in lambdas:
        vector = [0] * 9
        for matrix in J:
            vector.extend(adjoint_coordinates(I * (generator * matrix - matrix * generator)))
        vector.extend(tail_zeros)
        su3_tangents.append(sp.Matrix(vector))

    port_tangents = []
    for generator in L:
        vector = list(-generator)
        for i in range(3):
            delta_x = sum((generator[i, j] * J[j] for j in range(3)), sp.zeros(3))
            vector.extend(adjoint_coordinates(delta_x))
        vector.extend(tail_zeros)
        port_tangents.append(sp.Matrix(vector))

    row_tangents = []
    for generator in L:
        vector = list(generator)
        vector.extend([0] * 24)
        for entrance_vev in entrance_vevs:
            vector.extend(list(generator * entrance_vev))
        row_tangents.append(sp.Matrix(vector))

    return sp.Matrix.hstack(*(su3_tangents + port_tangents + row_tangents))


h1 = sp.Matrix([0, 0, 1])
h2 = sp.Matrix([1, 0, 0])
orbit_zero = orbit_matrix([])
orbit_one = orbit_matrix([h1])
orbit_two = orbit_matrix([h1, h2])

rank_zero = orbit_zero.rank()
rank_one = orbit_one.rank()
rank_two = orbit_two.rank()
generator_count = orbit_two.cols
gram_two = sp.simplify(orbit_two.T * orbit_two)
gram_two_determinant = sp.factor(gram_two.det())

# The common diagonal row/port/spin-one flavor subgroup is the three-dimensional
# stabilizer before entrance vevs. One vector leaves its axial generator; two
# noncollinear vectors leave none.
row_on_one = sp.Matrix.hstack(*[generator * h1 for generator in L])
row_on_two = sp.Matrix.vstack(
    sp.Matrix.hstack(*[generator * h1 for generator in L]),
    sp.Matrix.hstack(*[generator * h2 for generator in L]),
)

checks = {
    "wp484_dependency_passed": wp484["passed"],
    "wp501_dependency_passed": wp501["passed"],
    "enlarged_gauge_generator_count_is_fourteen": generator_count == 14,
    "connector_and_adjoint_vacuum_orbit_rank_is_eleven": rank_zero == 11,
    "connector_and_adjoint_stabilizer_dimension_is_three": generator_count - rank_zero == 3,
    "one_entrance_vev_orbit_rank_is_thirteen": rank_one == 13,
    "one_entrance_vev_leaves_one_generator": generator_count - rank_one == 1,
    "one_row_vector_has_one_dimensional_rotational_stabilizer": 3 - row_on_one.rank() == 1,
    "two_noncollinear_entrance_vevs_orbit_rank_is_fourteen": rank_two == 14,
    "two_noncollinear_entrance_vevs_remove_continuous_stabilizer": generator_count - rank_two == 0,
    "two_row_vectors_have_trivial_rotational_stabilizer": 3 - row_on_two.rank() == 0,
    "fully_broken_orbit_gram_is_positive_nonsingular": gram_two_determinant > 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP502",
    "source_extension": {
        "gauge_group": "SU(3)_F x SO(3)_P x SO(3)_E",
        "entrance_fields": "two electroweak-doublet row triplets H_u_alpha and H_d_alpha",
        "renormalizable_vertices": [
            "y_Hu Qbar H_u_alpha A_Ru_alpha",
            "y_Hd Qbar H_d_alpha A_Rd_alpha",
        ],
        "row_charged_fermions": "A_L and A_R are vectorlike SO(3)_E vectors",
    },
    "joint_vacuum": "X_i=J_i, S=I_3, with zero, one, or two noncollinear row-triplet electroweak vevs",
    "gauge_orbit": {
        "generator_count": int(generator_count),
        "without_entrance_vev": {
            "rank": int(rank_zero),
            "continuous_stabilizer_dimension": int(generator_count - rank_zero),
        },
        "one_entrance_vev": {
            "rank": int(rank_one),
            "continuous_stabilizer_dimension": int(generator_count - rank_one),
        },
        "two_noncollinear_entrance_vevs": {
            "rank": int(rank_two),
            "continuous_stabilizer_dimension": int(generator_count - rank_two),
            "orbit_gram_determinant": str(gram_two_determinant),
        },
    },
    "groupoid_change": "The fixed entrance vector is replaced by dynamical row-triplet fields and the row action is gauged. Entrance directions become relational vevs in the enlarged quotient; they are not absolute channel axes.",
    "anomaly_posture": "The new scalars carry no fermion anomaly. The A messengers are vectorlike and use the real integer-spin SO(3) vector representation, so the extension introduces no perturbative cubic row-gauge anomaly.",
    "classification": "Conditional renormalizable gauge completion of the three-component entrance carrier. Two noncollinear entrance vevs are necessary and sufficient to remove the residual continuous diagonal gauge stabilizer in the declared vacuum.",
    "selector": False,
    "rigidifier": bool(rank_two == generator_count),
    "instrument": None,
    "smallest_exact_falsifier": "With no entrance vev the fourteen-generator orbit has rank eleven; with one row-vector vev it has rank thirteen. A massless diagonal gauge sector remains until two noncollinear row vectors are present.",
    "remaining_gate": "Construct the complete two-triplet electroweak potential and prove a stable noncollinear vacuum, derive all fourteen gauge masses and scalar poles, and show that three entrance components remain independently preparable and readable after gauge fixing, mixing, finite widths, and detector resolution.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp502_gauged_entrance_triplet_stabilizer.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
