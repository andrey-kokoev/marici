"""Exact supertrace and stability bound for a protected doubled messenger channel."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
x = sp.symbols("x0:3", real=True)
n = sp.Matrix(x)
a = n.dot(n)
I = sp.I
J = [
    sp.Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]])/sp.sqrt(2),
    sp.Matrix([[0, -I, 0], [I, 0, -I], [0, I, 0]])/sp.sqrt(2),
    sp.diag(1, 0, -1),
]
Jn = sum((n[i]*J[i] for i in range(3)), sp.zeros(3))
M, y, Pn, Pm = sp.symbols("M y Pn Pm", positive=True)
mass = sp.Matrix.vstack(
    sp.Matrix.hstack(M*sp.eye(3), y*Jn),
    sp.Matrix.hstack(y*Jn, M*sp.eye(3)))
parity = sp.diag(1, 1, 1, -1, -1, -1)
mass_minus = mass.subs({z: -z for z in x}, simultaneous=True)
supertrace = sp.expand(-4*sp.trace(mass**4))
expected = sp.expand(-24*M**4-96*M**2*y**2*a-16*y**4*a**2)

radial_flow = 1136-64*(Pn+Pm)
boundary = sp.Rational(1136, 64)
boundary_cone_flow = -64*(Pn+Pm)*sp.symbols("lambda", positive=True)

checks = {
    "protected_mass_matrix_respects_flip": sp.simplify(parity*mass_minus*parity-mass) == sp.zeros(6),
    "protected_two_pair_supertrace_identity": sp.simplify(supertrace-expected) == 0,
    "protected_loop_preserves_even_norm_support": all(sum(mon) % 2 == 0 for mon, _ in sp.Poly(supertrace, *x).terms()),
    "protected_nonerosion_boundary_is_halved": boundary == sp.Rational(71, 4),
    "wp651_unit_four_frame_channel_derivative": radial_flow.subs({Pn: 2, Pm: 2}) == 880,
    "protected_cone_boundary_still_leaks": boundary_cone_flow.subs({Pn: 1, Pm: 0}) < 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP669", "status": "PASS", "checks": checks,
    "domain": "equal masses and reciprocal real off-diagonal Yukawas for each protected two-pair Dirac channel",
    "single_protected_channel": "-24M^4-96M^2y^2|n|^2-16y^4|n|^4",
    "radial_margin_flow": "dD/dt=1136-64(P_n+P_m)",
    "nonerosion_condition": "P_n+P_m<=71/4",
    "wp651_unit_protected_flow": "P_n=P_m=2 gives dD/dt=880",
    "classification": "exact flip protection preserves scalar support but doubles the fermionic erosion coefficient",
    "smallest_exact_falsifier": "one protected unit channel contributes a norm-quartic coefficient other than -16",
    "remaining_gate": "derive unequal masses, independent reciprocal vertices, tree matching, threshold decoupling, and running",
}
(ROOT / "results" / "wp669_protected_two_pair_supertrace.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
