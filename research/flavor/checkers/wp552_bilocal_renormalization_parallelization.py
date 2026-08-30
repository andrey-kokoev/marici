"""Exact operator-renormalization parallelization for the WP535 six-port map."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp535 = load("wp535_six_port_bilocal_instrument.json")
wp551 = load("wp551_omega_pole_width_residue_transfer.json")

mb, ms = sp.symbols("m_b m_s", nonzero=True)
mu2 = sp.symbols("mu2_1:7", nonzero=True)

ward = sp.zeros(6, 24)
for i, pole in enumerate(mu2):
    ward[i, 4 * i : 4 * i + 4] = sp.Matrix(
        [[1, -mb**2 / pole, -ms**2 / pole, 2 * mb * ms / pole]]
    )

# An exact, nontrivial operator mixing witness and a separate legal scheme
# transformation. Neither acts on the six source residues.
Z = sp.Matrix(
    [
        [1, 1, 0, 0],
        [0, 2, 1, 0],
        [0, 0, 3, 1],
        [1, 0, 0, 5],
    ]
)
S = sp.diag(2, 3, 5, 7)
Z24 = sp.kronecker_product(sp.eye(6), Z)
S24 = sp.kronecker_product(sp.eye(6), S)

h_bare = sp.Matrix(sp.symbols("h0:24"))
h_renormalized = Z24 * h_bare
ward_new_scheme = ward * S24.inv()
h_new_scheme = S24 * h_renormalized

amplitude = sp.simplify(ward * h_renormalized)
amplitude_new_scheme = sp.simplify(ward_new_scheme * h_new_scheme)
amplitude_wrong_parallelization = sp.simplify(ward * h_new_scheme)

residues = sp.Matrix(sp.symbols("r1:7"))
scalar = sp.simplify((residues.T * amplitude)[0])
scalar_new_scheme = sp.simplify((residues.T * amplitude_new_scheme)[0])

C_bare = sp.eye(24)
C_renormalized = sp.simplify(Z24 * C_bare * Z24.T)
single_pole_covariance = Z * Z.T
leading_principal_minors = [
    single_pole_covariance[:size, :size].det() for size in range(1, 5)
]

checks = {
    "dependencies_passed": bool(wp535["passed"] and wp551["passed"]),
    "operator_map_is_invertible": Z.det() != 0,
    "common_six_pole_operator_map_has_rank_twenty_four": Z24.rank() == 24,
    "ward_map_has_rank_six": ward.rank() == 6,
    "renormalized_ward_map_retains_rank_six": (ward * Z24).rank() == 6,
    "parallel_scheme_transport_preserves_all_amplitudes": amplitude_new_scheme
    == amplitude,
    "source_residues_need_no_scheme_transform": scalar_new_scheme == scalar,
    "unparallelized_scheme_change_is_detectably_wrong": amplitude_wrong_parallelization
    != amplitude,
    "covariance_transform_is_positive_definite": all(
        value.is_positive for value in leading_principal_minors
    )
    and C_renormalized.rank() == 24,
    "wp551_types_residues_as_dimensionless": wp551["quantity_types"][
        "signed_resolvent_residue"
    ]["mass_dimension"]
    == 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP552",
    "domain": "The six WP535 pole kernels, each with four bare bilocal operator channels, composed with one common invertible operator-mixing and subtraction map.",
    "factorization": {
        "source_residues": "Six dimensionless WP534 signed resolvent coefficients r_i.",
        "bare_estimators": "Twenty-four complex common-ensemble bilocal estimators h_bare.",
        "renormalization": "h_scheme=(I_6 tensor Z_scheme) h_bare.",
        "ward_contraction": "A_i=w_i^scheme h_i^scheme.",
        "experimental_scalar": "M_12,new=sum_i r_i A_i.",
    },
    "operator_map": {
        "single_pole_matrix": [[str(x) for x in row] for row in Z.tolist()],
        "single_pole_determinant": str(Z.det()),
        "six_pole_rank": Z24.rank(),
    },
    "scheme_covariance": {
        "basis_change": [[str(x) for x in row] for row in S.tolist()],
        "estimator_rule": "h_new=S h_old",
        "coefficient_rule": "w_new=w_old S^-1",
        "residue_rule": "r_i is unchanged",
        "all_six_amplitudes_invariant": bool(amplitude_new_scheme == amplitude),
        "scalar_invariant": bool(scalar_new_scheme == scalar),
    },
    "covariance": {
        "rule": "C_scheme=(I_6 tensor Z) C_bare (I_6 tensor Z)^T",
        "witness_rank": C_renormalized.rank(),
        "single_pole_leading_principal_minors": [
            str(x) for x in leading_principal_minors
        ],
        "authority": "The identity bare covariance is an exact structural witness only, not lattice data.",
    },
    "deletion_replay": "Deleting Z, its contact subtraction, or its covariance invalidates all six renormalized amplitudes and the scalar experimental composition. It leaves the source residues and Omega scale map unchanged.",
    "classification": "Exact source-estimator-scheme factorization and parallelization theorem; neither selector nor executed instrument calibration.",
    "selector": bool(wp551["selector"]),
    "rigidifier": bool((ward * Z24).rank() == 6),
    "instrument": "Requires a nonperturbatively determined four-channel mixing and subtraction matrix in a declared continuum scheme, shared across the six common-ensemble kernels with full covariance.",
    "smallest_exact_falsifier": "Apply h_new=S h_old but retain w_old. The exact checker finds A_new != A_old, violating scheme invariance.",
    "remaining_gate": "Compute Z and coincident-point subtraction nonperturbatively on the WP542 ensembles, match to a declared continuum scheme, propagate its joint covariance, and execute the six bilocal kernels. This identifies amplitudes but supplies no source selector.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp552_bilocal_renormalization_parallelization.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
