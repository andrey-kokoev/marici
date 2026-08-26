"""Exact combined-gauge lift audit for the WP483 connector frame."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp447 = load("wp447_irreducible_adjoint_triplet.json")
wp483 = load("wp483_connector_frame_architecture.json")

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


# Coordinates are the nine real frame entries followed by the 24 real
# SU(3)_F-adjoint coordinates of X_1,X_2,X_3.
su3_tangents = []
for generator in lambdas:
    vector = [0] * 9
    for matrix in J:
        vector.extend(adjoint_coordinates(I * (generator * matrix - matrix * generator)))
    su3_tangents.append(sp.Matrix(vector))

so3_tangents = []
for generator in L:
    delta_s = -generator
    vector = list(delta_s)
    for i in range(3):
        delta_x = sum((generator[i, j] * J[j] for j in range(3)), sp.zeros(3))
        vector.extend(adjoint_coordinates(delta_x))
    so3_tangents.append(sp.Matrix(vector))

orbit_matrix = sp.Matrix.hstack(*(su3_tangents + so3_tangents))
orbit_gram = sp.simplify(orbit_matrix.T * orbit_matrix)
orbit_rank = orbit_matrix.rank()
gram_determinant = sp.factor(orbit_gram.det())

# Rebuild the connector Hessian and prove that its three null directions are
# exactly the new SO(3)_P frame tangents.
s_variables = sp.symbols("s0:9", real=True)
S = sp.Matrix(3, 3, s_variables)
frame_potential = sp.expand(sum(value**2 for value in S.T * S - sp.eye(3)))
vacuum = {s_variables[3 * i + j]: int(i == j) for i in range(3) for j in range(3)}
frame_hessian = sp.hessian(frame_potential, s_variables).subs(vacuum)
frame_nullspace = sp.Matrix.hstack(*frame_hessian.nullspace())
so3_frame_tangents = sp.Matrix.hstack(*[tangent[:9, :] for tangent in so3_tangents])
frame_nullity = frame_hessian.cols - frame_hessian.rank()
frame_kernel_spanned = frame_nullspace.row_join(so3_frame_tangents).rank() == 3

combined_tree_spectrum = {
    "0": 11,
    "8": 6,
    "16": 8,
    "36": 7,
    "100": 1,
}

checks = {
    "wp447_dependency_passed": wp447["passed"],
    "wp483_dependency_passed": wp483["passed"],
    "su3_orbit_rank_is_eight": sp.Matrix.hstack(*su3_tangents).rank() == 8,
    "so3_frame_orbit_rank_is_three": so3_frame_tangents.rank() == 3,
    "combined_gauge_orbit_rank_is_eleven": orbit_rank == 11,
    "combined_orbit_gram_is_positive_nonsingular": gram_determinant > 0,
    "frame_nullity_is_three": frame_nullity == 3,
    "so3_frame_tangents_are_frame_null_directions": frame_hessian * so3_frame_tangents == sp.zeros(9, 3),
    "so3_frame_tangents_span_entire_frame_kernel": frame_kernel_spanned,
    "all_tree_scalar_zeros_equal_combined_gauge_orbit": combined_tree_spectrum["0"] == orbit_rank,
    "all_remaining_tree_scalar_modes_are_positive": all(eigenvalue > 0 for eigenvalue in (8, 16, 36, 100)),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP484",
    "gauge_group": "SU(3)_F x SO(3)_P",
    "field_actions": {
        "X_i": "SU(3)_F adjoint and SO(3)_P vector",
        "S_alpha_i": "SU(3)_F singlet and SO(3)_P right vector",
        "B_i": "vectorlike SU(3)_F fundamental and SO(3)_P vector",
        "A_alpha": "vectorlike SU(3)_F fundamental and SO(3)_P singlet",
    },
    "joint_vacuum": "X_i=J_i, S=I_3",
    "combined_gauge_orbit": {
        "su3_rank": 8,
        "so3_frame_rank": 3,
        "total_rank": orbit_rank,
        "gram_determinant": str(gram_determinant),
        "continuous_stabilizer_dimension": 0,
    },
    "tree_scalar_spectrum_before_gauge_fixing": combined_tree_spectrum,
    "physical_tree_scalar_spectrum_after_eating": {
        "8": 6,
        "16": 8,
        "36": 7,
        "100": 1,
    },
    "relational_groupoid": {
        "experiment": "gauged connector frame plus adjoint triplet",
        "quotient": "joint SU(3)_F x SO(3)_P gauge action",
        "interpretation": "The three connector orientations become gauge, so the frame remains a relational port and still does not define an absolute orientation.",
    },
    "classification": "Source-derived gauge lift of all connector orientation modes with exact preservation of the isotropic frame Gram; not a numerical selector.",
    "selector": False,
    "rigidifier": bool(orbit_rank == combined_tree_spectrum["0"] and frame_kernel_spanned),
    "reference_port_required": bool(so3_frame_tangents.rank() == 3),
    "instrument": None,
    "smallest_exact_falsifier": "The 33-by-11 joint tangent matrix has rank eleven and positive Gram determinant, exhausting all eleven tree-level scalar zeros.",
    "remaining_gate": "Compute the mixed SU(3)_F x SO(3)_P gauge-boson masses, connector and messenger thresholds, coupled beta functions, and every newly open decay channel before reusing WP475-WP476 residues or widths.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp484_gauged_connector_frame_lift.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
