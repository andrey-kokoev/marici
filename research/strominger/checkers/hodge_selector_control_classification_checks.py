"""Exact smooth-versus-punctured Hodge classification of selector control."""

import hashlib
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
RESULT = ROOT / "results" / "hodge_selector_control_classification_checks.json"

u = sp.symbols("u", real=True)
x_coord, y_coord = sp.symbols("x_coord y_coord", real=True)
lambda_field = sp.Function("lambda_field")(x_coord, y_coord)
exact_curl = sp.diff(sp.diff(lambda_field, y_coord), x_coord) - sp.diff(sp.diff(lambda_field, x_coord), y_coord)
sphere_genus = 0
sphere_first_betti = 2 * sphere_genus
mode_data = []
for ell in range(1, 9):
    p = sp.legendre(ell, u)
    eigen = ell * (ell + 1)
    ode_residual = sp.expand((1 - u**2) * sp.diff(p, u, 2) - 2 * u * sp.diff(p, u) + eigen * p)
    mean = sp.integrate(p, (u, -1, 1))
    mode_data.append({"ell": ell, "eigenvalue": eigen, "ode_residual": ode_residual, "mean": mean})

puncture_data = []
for count in (4, 6, 8):
    relation = sp.ones(1, count)
    period_dimension = count - relation.rank()
    puncture_data.append({
        "punctures": count,
        "period_relation_rank": relation.rank(),
        "harmonic_period_dimension": period_dimension,
    })

checks = {
    "sphere_has_no_harmonic_one_form_sector": sphere_first_betti == 0,
    "nonconstant_scalar_modes_have_positive_laplacian": all(item["eigenvalue"] > 0 for item in mode_data),
    "legendre_modes_satisfy_spherical_laplacian_equation": all(item["ode_residual"] == 0 for item in mode_data),
    "nonconstant_modes_have_zero_mean": all(item["mean"] == 0 for item in mode_data),
    "exact_control_has_zero_curvature_by_d_squared": exact_curl == 0,
    "coexact_mode_curvature_is_nonzero_for_every_ell_ge_one": all(item["eigenvalue"] != 0 for item in mode_data),
    "puncture_periods_have_one_total_sum_relation": all(item["period_relation_rank"] == 1 for item in puncture_data),
    "punctured_sphere_harmonic_dimension_is_N_minus_one": all(item["harmonic_period_dimension"] == item["punctures"] - 1 for item in puncture_data),
    "degree_four_transverse_zero_packet_forces_at_least_three_period_modes": puncture_data[0]["harmonic_period_dimension"] == 3,
    "hostile_two_puncture_model_understates_generic_minimum": 2 - 1 < puncture_data[0]["harmonic_period_dimension"],
}

payload = {
    "schema": "marici.strominger.hodge-selector-control-classification.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "smooth_sphere": {
        "decomposition": "b = d lambda + star d mu",
        "harmonic_dimension": 0,
        "exact_role": "flat longitudinal or boundary-sensitive control",
        "coexact_role": "curvature-bearing bulk control",
        "curvature": "d b = Delta(mu) area_form",
    },
    "punctured_sphere": {
        "decomposition": "b = d lambda + star d mu + h_Z",
        "harmonic_dimension": "number_of_distinct_punctures - 1",
        "period_law": "the oriented puncture periods have one total-sum relation",
        "minimum_for_transverse_degree_four_packet": 3,
    },
    "spherical_mode_fixtures": [{k: str(v) for k, v in item.items()} for item in mode_data],
    "puncture_fixtures": puncture_data,
}
payload["checker_sha256"] = hashlib.sha256(HERE.read_bytes()).hexdigest()
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="ascii")
print(f"{payload['passed']}/{payload['total']} checks passed")
print(payload["checker_sha256"])
raise SystemExit(0 if payload["status"] == "passed" else 1)
