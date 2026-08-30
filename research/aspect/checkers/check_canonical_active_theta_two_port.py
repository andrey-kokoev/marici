import json
from pathlib import Path

import sympy as sp


r, f = sp.symbols("r f", real=True, positive=True)
Q = sp.Matrix([[1, 2 * r], [2 * r, 1]])
b = sp.Matrix([-f, 0])
rho = sp.simplify((b.T * Q.inv() * b)[0])
delta = sp.simplify((rho - 1) / rho) * b * b.T
Q_active = sp.simplify(Q + delta)
C = sp.Matrix([[f, 0], [2 * r, 1]])
D = sp.Matrix([1, 0])
theta = sp.symbols("theta", real=True)
U = sp.Matrix([[sp.cos(theta), -sp.sin(theta)], [sp.sin(theta), sp.cos(theta)]])
C_rotated = U * C
D_rotated = U * D

checks = {
    "update_simplifies": delta == sp.diag(f**2 + 4 * r**2 - 1, 0),
    "active_balance": Q_active == sp.Matrix([[f**2 + 4 * r**2, 2 * r], [2 * r, 1]]),
    "determinant_equals_forcing_square": sp.simplify(Q_active.det() - f**2) == 0,
    "triangular_factor": C.T * C == Q_active,
    "source_duality": -C.T * D == b,
    "unit_feedthrough": (D.T * D)[0] == 1,
    "forcing_recovered_from_volume": sp.simplify(sp.sqrt(Q_active.det()) - f) == 0,
    "seam_witness_C": C.subs({r: 0, f: sp.sqrt(2)}) == sp.diag(sp.sqrt(2), 1),
    "output_rotation_is_unitary": sp.simplify(U.T * U) == sp.eye(2),
    "rotated_gram_is_invariant": sp.simplify(C_rotated.T * C_rotated - Q_active) == sp.zeros(2),
    "rotated_source_duality": sp.simplify(-C_rotated.T * D_rotated - b) == sp.zeros(2, 1),
    "rotated_feedthrough_is_unit": sp.simplify((D_rotated.T * D_rotated)[0] - 1) == 0,
    "triangular_frame_changes": C_rotated.subs(theta, sp.pi / 2) != C,
}

result = {
    "schema": "marici.aspect.active-theta-two-port-normal-form.v2",
    "status": "pass" if all(checks.values()) else "fail",
    "check_count": len(checks),
    "checks": {k: bool(v) for k, v in checks.items()},
    "response_normal_form": "C=[[f,0],[2r,1]] modulo common left-unitary output rotation",
    "direct_column": "D=(1,0)^T",
    "volume_law": "det(Q_active)=f^2",
    "claim_boundary": "The realization class is invariant; the triangular representative requires an output-frame choice.",
}

out = Path(__file__).parents[1] / "results" / "canonical_active_theta_two_port.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "pass" else 1)
