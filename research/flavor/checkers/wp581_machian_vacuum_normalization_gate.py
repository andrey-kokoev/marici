"""Exact WP581 dimensional normalization and single-source rank gate."""

import json
from pathlib import Path

import sympy as sp


rho, mass, scale, target = sp.symbols(
    "rho_vac M scale target", positive=True, real=True
)
eta = rho / mass**4
eta_rescaled = sp.simplify(rho / (scale * mass) ** 4)
mass_for_target = (rho / target) ** sp.Rational(1, 4)

eta_source = sp.symbols("eta", real=True)
z0, a, lambda_s0, b = sp.symbols(
    "z0 a lambda_s0 b", real=True
)
lambda_h = sp.symbols("lambda_H", positive=True, real=True)

z = z0 + a * eta_source
lambda_s = lambda_s0 + b * eta_source
readout = sp.Matrix([z, lambda_s * z**2 / lambda_h])
single_source_response = sp.simplify(readout.diff(eta_source))
two_setting_linear_design = sp.Matrix.hstack(
    single_source_response, 2 * single_source_response
)

half_mass = (2 * rho) ** sp.Rational(1, 4)

checks = {
    "vacuum_ratio_is_dimensionless_by_fourth_power": eta == rho / mass**4,
    "reference_rescaling_changes_ratio_by_fourth_power": sp.simplify(
        eta_rescaled - eta / scale**4
    ) == 0,
    "any_positive_target_can_be_encoded": sp.simplify(
        rho / mass_for_target**4 - target
    ) == 0,
    "one_half_is_encoded_by_M4_equal_two_rho": sp.simplify(
        rho / half_mass**4
    ) == sp.Rational(1, 2),
    "doubling_reference_divides_ratio_by_sixteen": sp.simplify(
        eta_rescaled.subs(scale, 2) - eta / 16
    ) == 0,
    "single_machian_scalar_has_one_response_column": single_source_response.cols == 1,
    "two_settings_of_same_scalar_are_rank_one": two_setting_linear_design.rank() == 1,
    "portal_response_has_two_rows_but_not_two_source_directions": single_source_response.rows == 2
    and single_source_response.cols == 1,
}
checks = {name: bool(value) for name, value in checks.items()}


def encode_matrix(matrix):
    return [[str(sp.simplify(matrix[row, col])) for col in range(matrix.cols)] for row in range(matrix.rows)]


result = {
    "work_package": "WP581",
    "classification": "no admitted Machian identification of h; a dimensionless vacuum ratio needs an independently fixed reference and one scalar source supplies at most rank one",
    "dimensionless_candidate": "eta=rho_vac/M^4",
    "reference_rescaling": "eta -> eta/scale^4",
    "reference_for_target": "M=(rho_vac/target)^(1/4)",
    "one_half_reference": "M^4=2*rho_vac",
    "single_scalar_portal_response": encode_matrix(single_source_response),
    "two_setting_same_scalar_design": encode_matrix(two_setting_linear_design),
    "smallest_exact_falsifier": "the same rho_vac with references M and 2M gives eta and eta/16",
    "contextual_partition": "unnormalized vacuum datum; relational normalized datum; rank-one Machian portal curve; absent two-source Machian surface",
    "reference_port_status": "choosing M creates a relational experiment and cannot be described as recovery of absolute vacuum energy",
    "remaining_gate": "derive the vacuum functional, reference scale, invariant source map, independent source rank, and calibrated instrument before assigning flavor meaning",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp581_machian_vacuum_normalization_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
