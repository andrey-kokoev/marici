"""Exact first-order stability response of the regular WP708 marginal ray."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
x, y, z = sp.symbols("x y z", real=True)
N, M, X, C = sp.symbols("N M X C", real=True)

beta_n = 4*z**2 + 8*z + 176*x**2 + 12
beta_m = 4*z**2 + 8*z + 176*y**2 + 12
beta_x = 8*z**2 + 16*z*(x+y) + 80*(x+y) + 32
beta_c_over_c = 40*z + 32*x + 32*y + 64
F = sp.Matrix([
    beta_n-x*beta_x,
    beta_m-y*beta_x,
    beta_c_over_c-beta_x,
])
base = {x: sp.Rational(1, 2), y: sp.Rational(1, 2), z: 1}
J = F.jacobian((x, y, z)).subs(base)
source_correction = sp.Matrix([
    N-sp.Rational(1, 2)*X,
    M-sp.Rational(1, 2)*X,
    C-X,
])
displacement = sp.simplify(-J.inv()*source_correction)
dx, dy, dz = displacement
delta_margin = sp.factor(2*(dx+dy))

checks = {
    "regular_ray_projective_jacobian": J == sp.Matrix([[-8, -48, 0], [-48, -8, 0], [-64, -64, 8]]),
    "jacobian_is_invertible": J.det() == -17920,
    "radial_margin_response": sp.simplify(delta_margin-(M+N-X)/28) == 0,
    "correlation_correction_drops_out_of_radial_response": sp.diff(delta_margin, C) == 0,
    "positive_self_correction_opens_stability": delta_margin.subs({N: 1, M: 1, X: 0}) == sp.Rational(1, 14),
    "mixed_norm_correction_can_close_stability": delta_margin.subs({N: 0, M: 0, X: 1}) == -sp.Rational(1, 28),
    "pure_correction_is_radially_null": delta_margin.subs({N: 0, M: 0, X: 0, C: 1}) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP709",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "formal first-order completions of the regular WP708 ray (x,y,z)=(1/2,1/2,1)",
    "faithful_coordinate": "the full projective coupling displacement together with radial margin D=4xy-1",
    "source_authorized_probe_family": "linear response to separately named beta corrections (N,M,X,C); no correction sign is admitted as source data",
    "contextual_partition": "radial response sees only N+M-X and has a one-dimensional visible quotient with a three-dimensional first-order kernel",
    "classification": "acceptance functional and rigidifier for future source completions; neither selector nor physical instrument",
    "smallest_exact_falsifier": "N+M-X<=0 fails to move the marginal ray into strict stability at first order",
    "remaining_gate": "derive all correction components from one frozen source and scheme, establish positive margin with errors, then recompute transverse basin and finite threshold readout",
}
(ROOT / "results" / "wp709_beta_displacement_acceptance_functional.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
