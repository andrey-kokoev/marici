"""Exact common-scale commuting square for Ward-complete six-port rows."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp550 = load("wp550_omega_scale_setting_constructor.json")
wp552 = load("wp552_bilocal_renormalization_parallelization.json")

mb_hat, ms_hat, common_scale = sp.symbols(
    "m_b_hat m_s_hat k_common", nonzero=True
)
mu2_hat = sp.symbols("mu2_hat_1:7", nonzero=True)

Z = sp.Matrix([[sp.sympify(x) for x in row] for row in wp552["operator_map"]["single_pole_matrix"]])
Z24 = sp.kronecker_product(sp.eye(6), Z)
h = sp.Matrix(sp.symbols("h0:24"))


def ward_rows(mb, ms, poles_squared):
    rows = sp.zeros(6, 24)
    for i, pole_squared in enumerate(poles_squared):
        rows[i, 4 * i : 4 * i + 4] = sp.Matrix(
            [[1, -mb**2 / pole_squared, -ms**2 / pole_squared, 2 * mb * ms / pole_squared]]
        )
    return rows


lattice_ward = ward_rows(mb_hat, ms_hat, mu2_hat)
physical_ward = ward_rows(
    common_scale * mb_hat,
    common_scale * ms_hat,
    [common_scale**2 * pole for pole in mu2_hat],
)

amplitude_lattice_path = sp.simplify(lattice_ward * Z24 * h)
amplitude_physical_path = sp.simplify(physical_ward * Z24 * h)

kq, kp = sp.symbols("k_q k_p", nonzero=True)
split_ward = ward_rows(
    kq * mb_hat,
    kq * ms_hat,
    [kp**2 * pole for pole in mu2_hat],
)
hostile_split_ward = sp.simplify(split_ward.subs({kq: 2, kp: 1}))

scale_jacobian = sp.Matrix([[2, -2], [2, -2], [2, -2]])
common_scale_tangent = sp.Matrix([1, 1])
relative_scale_tangent = sp.Matrix([1, 0])

checks = {
    "dependencies_passed": bool(wp550["passed"] and wp552["passed"]),
    "common_scale_cancels_from_ward_rows": physical_ward == lattice_ward,
    "omega_and_operator_paths_commute": amplitude_physical_path
    == amplitude_lattice_path,
    "relative_scale_map_has_rank_one": scale_jacobian.rank() == 1,
    "common_scale_motion_is_kernel": scale_jacobian * common_scale_tangent
    == sp.zeros(3, 1),
    "relative_scale_motion_is_detected": scale_jacobian * relative_scale_tangent
    != sp.zeros(3, 1),
    "hostile_split_preserves_vector_coefficients": all(
        hostile_split_ward[i, 4 * i] == lattice_ward[i, 4 * i]
        for i in range(6)
    ),
    "hostile_split_multiplies_scalar_coefficients_by_four": all(
        sp.simplify(hostile_split_ward[i, 4 * i + j] - 4 * lattice_ward[i, 4 * i + j]) == 0
        for i in range(6)
        for j in range(1, 4)
    ),
    "hostile_split_changes_ward_rows": hostile_split_ward != lattice_ward,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP553",
    "domain": "The six WP535 Ward-complete pole rows, WP550 Omega scale architecture, and WP552 common four-channel operator map.",
    "scale_coordinates": ["log k_quark", "log k_pole"],
    "relative_scale_jacobian": [[str(x) for x in row] for row in scale_jacobian.tolist()],
    "rank": scale_jacobian.rank(),
    "kernel": [[str(x) for x in vector] for vector in scale_jacobian.nullspace()],
    "commuting_square": {
        "path_one": "Form m_b^2/mu_i^2, m_s^2/mu_i^2, and m_b*m_s/mu_i^2 in the shared lattice frame, then apply the operator map.",
        "path_two": "Apply one common Omega energy scale to quark and pole masses, form the ratios, then apply the operator map.",
        "exactly_equal": bool(amplitude_physical_path == amplitude_lattice_path),
    },
    "hostile_split_scale": {
        "k_quark": 2,
        "k_pole": 1,
        "vector_factor": 1,
        "scalar_factors": [4, 4, 4],
        "outcome": "Each packet remains internally scaled, but the Ward row changes because no common-frame interface joins them.",
    },
    "classification": "Exact common-scale interface and commuting-square theorem; identification rigidifier, neither selector nor executed calibration.",
    "selector": bool(wp552["selector"]),
    "rigidifier": bool(amplitude_physical_path == amplitude_lattice_path),
    "instrument": "Requires quark masses, Omega, pole kernels, and operator mixing/subtraction to be determined on a common ensemble and continuum scheme, or joined by an independently calibrated matching constructor with covariance.",
    "smallest_exact_falsifier": "Set k_quark=2*k_pole. The vector Ward coefficient is unchanged while all three scalar coefficients multiply by four.",
    "remaining_gate": "Execute one joint WP542 analysis containing same-ensemble quark-mass renormalization, a*m_Omega, six pole kernels, operator mixing and subtraction, continuum matching, timestamps, disturbances, and full covariance. Source selection remains independent.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp553_ward_common_scale_commuting_square.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
