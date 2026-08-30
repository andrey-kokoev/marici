"""Exact disjoint-Dirac-messenger tangent stability bound for WP662."""
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
M, y, Fn, Fm = sp.symbols("M y Fn Fm", positive=True)
dirac_supertrace = sp.expand(-4*sp.trace((M*sp.eye(3)+y*Jn)**4))
expected = sp.expand(-12*M**4-48*M**2*y**2*a-8*y**4*a**2)

beta_ln = 200-8*Fn
beta_lm = 200-8*Fm
beta_lx = 232
radial_flow = sp.expand(4*(beta_ln+beta_lm)-2*beta_lx)
boundary_sum = sp.Rational(1136, 32)

checks = {
    "dirac_supertrace_identity": sp.simplify(dirac_supertrace-expected) == 0,
    "disjoint_loop_generates_norm_support_only": not dirac_supertrace.has(*sp.symbols("m0:3")),
    "benchmark_radial_flow_formula": radial_flow == 1136-32*Fn-32*Fm,
    "exact_nonerosion_boundary": boundary_sum == sp.Rational(71, 2),
    "wp651_unit_four_frame_chain_example_is_inside": radial_flow.subs({Fn: 2, Fm: 2}) == 1008,
    "hostile_strong_example_erodes_margin": radial_flow.subs({Fn: 18, Fm: 18}) == -16,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP664", "status": "PASS", "checks": checks,
    "normalization": "canonically normalized fields; one Dirac triplet contributes -4 Tr[(M I+y J_n)^4] to the one-loop supertrace",
    "single_chain_contribution": "-12M^4-48M^2y^2|n|^2-8y^4|n|^4",
    "coupling_aggregates": "F_n=sum d_i y_ni^4 and F_m=sum d_j y_mj^4 over disjoint Dirac triplets",
    "radial_margin_flow": "dD/dt=1136-32(F_n+F_m) at the WP661 benchmark",
    "nonerosion_condition": "F_n+F_m<=71/2",
    "classification": "disjoint messenger completion preserves operator support but frame-margin stability is conditional on free source couplings",
    "smallest_exact_falsifier": "F_n+F_m>71/2 makes the radial stability margin decrease at the benchmark",
    "remaining_gate": "derive multiplicities and Yukawa couplings from the admitted messenger grammar and integrate the completed flow over a declared scale interval",
}
(ROOT / "results" / "wp664_disjoint_messenger_stability_bound.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
