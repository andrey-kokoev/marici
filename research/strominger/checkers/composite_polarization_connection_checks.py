"""Exact audit of the composite polarization-phase connection."""

import hashlib
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
RESULT = ROOT / "results" / "composite_polarization_connection_checks.json"

x, y, dx, dy = sp.symbols("x y dx dy", real=True)
alpha, da = sp.symbols("alpha da", real=True)
r, dr, theta, dtheta, loop = sp.symbols("r dr theta dtheta loop", real=True)
J = sp.Matrix([[0, -1], [1, 0]])
C = sp.Matrix([x, y])
dC = sp.Matrix([dx, dy])
R = sp.cos(alpha) * sp.eye(2) + sp.sin(alpha) * J
dR = da * J * R


def composite_connection(field, derivative):
    return sp.simplify(-(J * field).dot(derivative) / field.dot(field))


A = composite_connection(C, dC)
C_prime = sp.simplify(R * C)
dC_prime = sp.simplify(R * dC + dR * C)
A_prime = sp.trigsimp(composite_connection(C_prime, dC_prime))

polar_C = r * sp.Matrix([sp.cos(theta), sp.sin(theta)])
polar_dC = (
    dr * sp.Matrix([sp.cos(theta), sp.sin(theta)])
    + r * dtheta * sp.Matrix([-sp.sin(theta), sp.cos(theta)])
)
polar_A = sp.trigsimp(composite_connection(polar_C, polar_dC))
polar_covariant_derivative = sp.trigsimp(polar_dC + polar_A * J * polar_C)
radial_derivative = dr * sp.Matrix([sp.cos(theta), sp.sin(theta)])

loop_C = sp.Matrix([sp.cos(loop), sp.sin(loop)])
loop_dC = sp.diff(loop_C, loop)
loop_A = sp.trigsimp(composite_connection(loop_C, loop_dC))
loop_holonomy = sp.integrate(loop_A, (loop, 0, 2 * sp.pi))

checks = {
    "composite_connection_has_required_local_formula": A == (y * dx - x * dy) / (x**2 + y**2),
    "composite_connection_transforms_as_A_minus_dalpha": sp.factor(sp.together(A_prime - (A - da))) == 0,
    "polar_connection_is_minus_phase_derivative": polar_A == -dtheta,
    "covariant_derivative_erases_phase_variation": sp.trigsimp(polar_covariant_derivative - radial_derivative) == sp.zeros(2, 1),
    "unit_winding_has_nonzero_holonomy": loop_A == -1 and loop_holonomy == -2 * sp.pi,
    "connection_denominator_vanishes_at_field_zero": (x**2 + y**2).subs({x: 0, y: 0}) == 0,
    "zero_field_has_no_defined_phase_connection": sp.denom(A).subs({x: 0, y: 0}) == 0,
    "wrong_sign_fails_required_gauge_law": sp.factor(sp.together(-A_prime - (-A - da))) != 0,
}

payload = {
    "schema": "marici.strominger.composite-polarization-connection.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "connection": str(A),
    "transformed_connection": str(A_prime),
    "polar_covariant_derivative": [str(v) for v in polar_covariant_derivative],
    "unit_winding_holonomy": str(loop_holonomy),
    "disposition": {
        "local_result": "the field constructs the required connection on its nonzero locus",
        "geometric_cost": "the covariant derivative removes polarization phase variation",
        "global_obstruction": "zeros make the connection singular and winding gives nontrivial holonomy",
        "authority_result": "the composite connection is a gauge quotient of the existing state, not an independent active control",
    },
}
payload["checker_sha256"] = hashlib.sha256(HERE.read_bytes()).hexdigest()
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="ascii")
print(f"{payload['passed']}/{payload['total']} checks passed")
print(payload["checker_sha256"])
raise SystemExit(0 if payload["status"] == "passed" else 1)
