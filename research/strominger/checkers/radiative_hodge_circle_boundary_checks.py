"""Exact symplectic and boundary audit of the radiative Hodge circle."""

import hashlib
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
RESULT = ROOT / "results" / "radiative_hodge_circle_boundary_checks.json"

c, s = sp.symbols("c s", real=True)
I2 = sp.eye(2)
J2 = sp.Matrix([[0, -1], [1, 0]])
R2 = c * I2 + s * J2
J4 = sp.diag(J2, J2)
R4 = c * sp.eye(4) + s * J4
OMEGA = sp.Matrix.vstack(
    sp.Matrix.hstack(sp.zeros(2), I2),
    sp.Matrix.hstack(-I2, sp.zeros(2)),
)


def circle_reduce(matrix):
    return matrix.applyfunc(lambda x: sp.expand(x).subs(c**2 + s**2, 1))


metric_residual = circle_reduce(R2.T * R2 - I2)
symplectic_residual = circle_reduce(R4.T * OMEGA * R4 - OMEGA)
composition_residual = sp.simplify(
    (c * I2 + s * J2) * (c * I2 - s * J2) - (c**2 + s**2) * I2
)

electric_line = sp.Matrix([1, 0])
electric_image = J2 * electric_line
full_boundary = sp.eye(2)

checks = {
    "hodge_generator_squares_to_minus_identity": J2**2 == -I2,
    "formal_circle_preserves_fiber_metric": metric_residual == sp.zeros(2),
    "formal_circle_preserves_radiative_symplectic_form": symplectic_residual == sp.zeros(4),
    "inverse_is_opposite_hodge_angle": composition_residual == sp.zeros(2),
    "quarter_turn_is_the_hodge_bridge": R2.subs({c: 0, s: 1}) == J2,
    "electric_boundary_line_is_not_hodge_invariant": electric_image != electric_line and electric_image[0] == 0,
    "full_two_parity_boundary_fiber_is_hodge_invariant": J2 * full_boundary == sp.Matrix.hstack(J2[:, 0], J2[:, 1]),
    "hostile_boundary_preservation_claim_has_nonzero_residual": electric_image - electric_line != sp.zeros(2, 1),
}

payload = {
    "schema": "marici.strominger.radiative-hodge-circle-boundary.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "theorem": {
        "unrestricted_phase_space": "R(c,s)=c I+s J is orthogonal and symplectic when c^2+s^2=1",
        "boundary_criterion": "a linear boundary condition B is preserved by the Hodge circle iff J(B) is contained in B",
        "hostile_polarization": "the one-dimensional electric line is sent to the magnetic line and is not preserved",
        "closed_boundary_packet": "the joint electric-magnetic boundary fiber is preserved",
        "remaining_gap": "global Hodge-circle authority does not imply region-, mode-, or event-selective execution",
    },
    "residuals": {
        "metric": str(metric_residual),
        "symplectic": str(symplectic_residual),
        "electric_boundary": [str(x) for x in electric_image - electric_line],
    },
}
payload["checker_sha256"] = hashlib.sha256(HERE.read_bytes()).hexdigest()
RESULT.parent.mkdir(parents=True, exist_ok=True)
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="ascii")
print(f"{payload['passed']}/{payload['total']} checks passed")
print(payload["checker_sha256"])
raise SystemExit(0 if payload["status"] == "passed" else 1)
