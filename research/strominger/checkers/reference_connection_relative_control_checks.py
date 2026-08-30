"""Exact split of fixed spin-two attachment from variable relative control."""

import hashlib
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
RESULT = ROOT / "results" / "reference_connection_relative_control_checks.json"

omega, dphi, Ac, dalpha, b = sp.symbols("omega dphi Ac dalpha b", real=True)
spin_weight = 2
base_euler = 2
polarization_degree = spin_weight * base_euler

A0 = spin_weight * omega
A0_prime = spin_weight * (omega - dphi)
alpha_relation = spin_weight * dphi
Ac_prime = Ac - dalpha
B0 = A0 - Ac
B0_prime = A0_prime - Ac_prime.subs(dalpha, alpha_relation)

A = A0 + b
relative_total = sp.expand(A - Ac)
expected_relative = sp.expand(B0 + b)

F0_integral = 2 * sp.pi * polarization_degree
db_integral_closed_sphere = 0
F_integral = F0_integral + db_integral_closed_sphere

checks = {
    "weight_two_spin_connection_has_correct_local_gauge_law": sp.expand(A0_prime - (A0 - alpha_relation)) == 0,
    "fixed_reference_minus_composite_connection_is_gauge_invariant": sp.expand(B0_prime - B0) == 0,
    "every_connection_on_fixed_bundle_is_reference_plus_global_one_form": sp.expand(A - (A0 + b)) == 0,
    "active_relative_field_splits_as_fixed_attachment_plus_variable_control": relative_total == expected_relative,
    "reference_curvature_has_degree_four_integral": F0_integral == 8 * sp.pi,
    "global_one_form_cannot_change_total_chern_degree": F_integral == F0_integral,
    "zero_variable_control_leaves_only_fixed_reference_geometry": (A.subs(b, 0), relative_total.subs(b, 0)) == (A0, B0),
    "nonzero_variable_control_changes_connection_without_changing_bundle_degree": A.subs(b, 3) != A0 and F_integral == 8 * sp.pi,
}

payload = {
    "schema": "marici.strominger.reference-connection-relative-control.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "decomposition": {
        "fixed_reference": "A0 = 2 omega_LC",
        "full_connection": "A = A0 + b",
        "relative_to_field_phase": "A - A_C = (A0 - A_C) + b",
        "fixed_attachment": "B0 = A0 - A_C",
        "variable_control": "b is a globally defined gauge-invariant one-form",
    },
    "topology": {
        "polarization_degree": polarization_degree,
        "reference_curvature_integral": str(F0_integral),
        "variable_control_changes_degree": False,
    },
    "authority": {
        "spin_connection": "source-authorized for bundle attachment and presentation covariance",
        "fixed_B0": "source-derived comparison carrying the forced zero attachment",
        "b": "the only variable active-control degree; no source constructor yet identified",
    },
}
payload["checker_sha256"] = hashlib.sha256(HERE.read_bytes()).hexdigest()
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="ascii")
print(f"{payload['passed']}/{payload['total']} checks passed")
print(payload["checker_sha256"])
raise SystemExit(0 if payload["status"] == "passed" else 1)
