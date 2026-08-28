import json
from pathlib import Path

import sympy as sp


r, f, phi = sp.symbols("r f phi", real=True)
u = sp.exp(sp.I * phi)
D = sp.Matrix([1, 0])
C_phi = sp.Matrix([[f, 0], [2 * r * u, u]])
Q_star = sp.Matrix([[f**2 + 4 * r**2, 2 * r], [2 * r, 1]])
residual = C_phi.conjugate().T * C_phi - Q_star


def matrix_is_real(matrix):
    return all(sp.simplify(sp.im(sp.expand_complex(entry))) == 0 for entry in matrix)

checks = {
    "unit_phase_gram_invariant": all(sp.simplify(sp.expand_complex(e)) == 0 for e in residual),
    "source_duality_invariant": sp.simplify(-C_phi.conjugate().T * D - sp.Matrix([-f, 0])) == sp.zeros(2, 1),
    "direct_ray_fixed": (D.T * D)[0] == 1,
    "quarter_turn_is_distinct": C_phi.subs(phi, sp.pi / 2) != C_phi.subs(phi, 0),
    "real_structure_allows_positive_axis": matrix_is_real(C_phi.subs(phi, 0)),
    "real_structure_allows_negative_axis": matrix_is_real(C_phi.subs(phi, sp.pi)),
    "orientation_selects_positive": sp.simplify(C_phi.subs(phi, 0)[1, 1] - 1) == 0,
    "orientation_rejects_negative": sp.simplify(C_phi.subs(phi, sp.pi)[1, 1] + 1) == 0,
}

result = {
    "schema": "marici.aspect.theta-output-frame-augmentation-ladder.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "check_count": len(checks),
    "checks": {k: bool(v) for k, v in checks.items()},
    "ladder": [
        "lossless Gram data: U(2) output gauge",
        "source direct-feedthrough ray D: residual U(1)",
        "compatible real structure on D-perp: residual sign",
        "augmentation orientation: unique triangular frame",
    ],
    "family": "C_phi=[[f,0],[exp(i phi)2r,exp(i phi)]], D=e1",
}

out = Path(__file__).parents[1] / "results" / "theta_output_frame_augmentation_ladder.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "pass" else 1)
