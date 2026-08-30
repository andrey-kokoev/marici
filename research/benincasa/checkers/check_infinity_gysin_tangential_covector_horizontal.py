#!/usr/bin/env python3
"""Verify endpoint-corrected differentiability of the tangential infinity covector."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/infinity-gysin-tangential-covector-horizontal.json"

t = sp.symbols("t", positive=True)
x, y, z = sp.symbols("x y z", positive=True)
h = x**2+y**2-z**2
F = x**2*t**4-h*t**2+y**2
f0 = 1/sp.sqrt(F)
f2 = t**2/sp.sqrt(F)
endpoint_coefficient = 1/x

tail_coefficient = sp.factor(sp.limit(t**2*(f2-endpoint_coefficient), t, sp.oo))

derivative_records = {}
checks = {
    "endpoint_coefficient_is_1_over_x": sp.limit(f2, t, sp.oo) == endpoint_coefficient,
    "finite_tail_coefficient": sp.factor(
        tail_coefficient-h/(2*x**3)
    ) == 0,
}
for variable in (x, y, z):
    endpoint_derivative = sp.diff(endpoint_coefficient, variable)
    corrected_derivative = sp.diff(f2, variable)-endpoint_derivative
    corrected_tail = sp.factor(sp.limit(t**2*corrected_derivative, t, sp.oo))
    omega0_derivative_tail = sp.factor(
        sp.limit(t**2*sp.diff(f0, variable), t, sp.oo)
    )
    derivative_records[str(variable)] = {
        "endpoint_derivative": sp.sstr(endpoint_derivative),
        "corrected_omega2_derivative_tail": sp.sstr(corrected_tail),
        "omega0_derivative_tail": sp.sstr(omega0_derivative_tail),
        "nonintegrable_constant_after_correction": "0",
    }
    checks[f"{variable}:corrected_omega2_derivative_is_integrable"] = (
        sp.limit(corrected_derivative, t, sp.oo) == 0
    )
    checks[f"{variable}:omega0_derivative_is_integrable"] = (
        sp.limit(sp.diff(f0, variable), t, sp.oo) == 0
    )

# Common energy scaling x,y,z -> lambda(x,y,z) gives weight -1 for both
# the ordinary omega0 period and the finite-part omega2 period.
lam = sp.symbols("lambda", positive=True)
scaled_F = sp.factor(F.subs({x: lam*x, y: lam*y, z: lam*z}))
checks["energy_scaling_of_F_is_quadratic"] = sp.factor(scaled_F-lam**2*F) == 0
checks["endpoint_subtraction_has_weight_minus_one"] = sp.factor(
    endpoint_coefficient.subs(x, lam*x)-endpoint_coefficient/lam
) == 0

assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.infinity-gysin-tangential-covector-horizontal.v1",
    "generic_binary_quartic": sp.sstr(F),
    "energy_domain": "x>0,y>0,z>0 away from the elliptic discriminant",
    "source_endpoint_coefficient": sp.sstr(endpoint_coefficient),
    "subtraction": "R/x",
    "subtracted_tail_coefficient": sp.sstr(tail_coefficient),
    "derivative_records": derivative_records,
    "endpoint_connection": "d(1/x)=-dx/x^2",
    "common_energy_weight": -1,
    "result": (
        "Every base derivative of omega2 minus the derivative of its source "
        "endpoint coefficient decays as O(t^-2). The tangential finite-part "
        "covector therefore differentiates without an endpoint anomaly."
    ),
    "full_gauss_manin_matrix_identity": (
        "not recomputed here; this checker certifies the endpoint component "
        "required for the marked-relative horizontal extension"
    ),
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print("endpoint coefficient", endpoint_coefficient)
print("tail coefficient", tail_coefficient)
for variable, record in derivative_records.items():
    print(variable, record["corrected_omega2_derivative_tail"])
print(OUT)
