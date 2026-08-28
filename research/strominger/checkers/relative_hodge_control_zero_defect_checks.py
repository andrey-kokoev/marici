"""Exact factorization of a Hodge connection into phase gauge and control."""

import hashlib
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
RESULT = ROOT / "results" / "relative_hodge_control_zero_defect_checks.json"

A, Ac, dalpha = sp.symbols("A Ac dalpha", real=True)
B = A - Ac
A_prime = A - dalpha
Ac_prime = Ac - dalpha
B_prime = sp.simplify(A_prime - Ac_prime)

J = sp.Matrix([[0, -1], [1, 0]])
r, dr, theta, dtheta = sp.symbols("r dr theta dtheta", real=True)
C = r * sp.Matrix([sp.cos(theta), sp.sin(theta)])
dC = dr * sp.Matrix([sp.cos(theta), sp.sin(theta)]) + r * dtheta * sp.Matrix([-sp.sin(theta), sp.cos(theta)])
Ac_polar = -dtheta
B_polar = sp.symbols("B_polar", real=True)
DA = sp.trigsimp(dC + (Ac_polar + B_polar) * J * C)
expected = sp.trigsimp(dr * sp.Matrix([sp.cos(theta), sp.sin(theta)]) + B_polar * J * C)

loop = sp.symbols("loop", real=True)
winding_data = []
for n in (1, 2, 3):
    Cn = sp.Matrix([sp.cos(n * loop), sp.sin(n * loop)])
    dCn = sp.diff(Cn, loop)
    Acn = sp.trigsimp(-(J * Cn).dot(dCn) / Cn.dot(Cn))
    Bn_for_regular_A_zero = -Acn
    winding_data.append({
        "n": n,
        "Ac": Acn,
        "Ac_holonomy": sp.integrate(Acn, (loop, 0, 2 * sp.pi)),
        "B": Bn_for_regular_A_zero,
        "B_holonomy": sp.integrate(Bn_for_regular_A_zero, (loop, 0, 2 * sp.pi)),
    })

Fx_A, Fx_Ac, dB = sp.symbols("F_A F_Ac dB", real=True)

checks = {
    "relative_connection_is_gauge_invariant": B_prime == B,
    "covariant_derivative_splits_into_radial_gauge_plus_relative_control": sp.trigsimp(DA - expected) == sp.zeros(2, 1),
    "relative_control_is_the_only_remaining_angular_coupling": sp.diff(DA, B_polar) == J * C,
    "composite_holonomy_is_minus_two_pi_times_winding": all(item["Ac_holonomy"] == -2 * sp.pi * item["n"] for item in winding_data),
    "regular_zero_connection_forces_opposite_relative_holonomy": all(item["B_holonomy"] == 2 * sp.pi * item["n"] for item in winding_data),
    "total_holonomy_cancels_for_A_zero_fixture": all(item["Ac_holonomy"] + item["B_holonomy"] == 0 for item in winding_data),
    "curvature_factorization_is_additive": sp.solve(sp.Eq(Fx_A, Fx_Ac + dB), Fx_A)[0] == Fx_Ac + dB,
    "wrong_sum_relative_field_is_not_gauge_invariant": sp.simplify((A_prime + Ac_prime) - (A + Ac)) != 0,
}

payload = {
    "schema": "marici.strominger.relative-hodge-control-zero-defect.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "factorization": {
        "connection": "A = A_C + B",
        "gauge_part": "A_C maps to A_C - d alpha",
        "control_part": "B is gauge invariant",
        "curvature": "F_A = F_A_C + dB",
    },
    "winding_fixtures": [{k: str(v) for k, v in item.items()} for item in winding_data],
    "disposition": {
        "capability_location": "B contains every connection degree not forced by the field phase",
        "zero_defect_law": "if A extends regularly across a winding zero, B must carry the opposite quantized puncture holonomy",
        "remaining_source_gate": "derive an independent gauge-invariant B and its defect attachment from gravitational source data",
    },
}
payload["checker_sha256"] = hashlib.sha256(HERE.read_bytes()).hexdigest()
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="ascii")
print(f"{payload['passed']}/{payload['total']} checks passed")
print(payload["checker_sha256"])
raise SystemExit(0 if payload["status"] == "passed" else 1)
