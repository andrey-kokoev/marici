"""Exact messenger-topology bifurcation behind the two-triplet scalar flow."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
x = sp.symbols("x0:6", real=True)
n, m = sp.Matrix(x[:3]), sp.Matrix(x[3:])
a, b, c = n.dot(n), m.dot(m), n.dot(m)
I = sp.I
J = [
    sp.Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]])/sp.sqrt(2),
    sp.Matrix([[0, -I, 0], [I, 0, -I], [0, I, 0]])/sp.sqrt(2),
    sp.diag(1, 0, -1),
]
Jn = sum((n[i]*J[i] for i in range(3)), sp.zeros(3))
Jm = sum((m[i]*J[i] for i in range(3)), sp.zeros(3))
M, yn, ym = sp.symbols("M yn ym", real=True)

shared_matrix = M*sp.eye(3)+yn*Jn+ym*Jm
shared_trace = sp.expand(sp.trace(shared_matrix**4))
radius = yn**2*a+ym**2*b+2*yn*ym*c
shared_expected = sp.expand(3*M**4+12*M**2*radius+2*radius**2)

separate_trace = sp.expand(
    sp.trace((M*sp.eye(3)+yn*Jn)**4)
    + sp.trace((M*sp.eye(3)+ym*Jm)**4))
separate_expected = sp.expand(
    6*M**4+12*M**2*(yn**2*a+ym**2*b)+2*(yn**4*a**2+ym**4*b**2))

A, B, C = sp.symbols("A B C", real=True)
unit_shared_invariants = sp.expand(3+12*(A+B+2*C)+2*(A+B+2*C)**2)
unit_separate_invariants = sp.expand(6+12*(A+B)+2*(A**2+B**2))
unit_shared = sp.expand(shared_expected.subs({M: 1, yn: 1, ym: 1}))
unit_separate = sp.expand(separate_expected.subs({M: 1, yn: 1, ym: 1}))
hostile_point = dict(zip(x, [1, 0, 0, 1, 0, 0]))

checks = {
    "spin_one_shared_trace_identity": sp.simplify(shared_trace-shared_expected) == 0,
    "separate_trace_identity": sp.simplify(separate_trace-separate_expected) == 0,
    "shared_generates_quadratic_cross_term": sp.Poly(unit_shared_invariants, A, B, C).coeff_monomial(C) == 24,
    "shared_generates_flip_odd_quartics": sp.Poly(unit_shared_invariants, A, B, C).coeff_monomial(A*C) == 8 and sp.Poly(unit_shared_invariants, A, B, C).coeff_monomial(B*C) == 8,
    "separate_has_no_cross_support": not unit_separate_invariants.has(C),
    "same_tree_word_capacity_different_loop_response": sp.simplify(
        unit_shared.subs(hostile_point)-unit_separate.subs(hostile_point)) != 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP663", "status": "PASS", "checks": checks,
    "shared_unit_trace": str(unit_shared_invariants),
    "separate_unit_trace": str(unit_separate_invariants),
    "shared_extra_support": ["n dot m", "|n|^2(n dot m)", "|m|^2(n dot m)"],
    "tree_level_equivalence": "both topologies can carry independently adjustable J_n and J_m word coefficients",
    "classification": "the matched word packet does not determine messenger-induced RG completion",
    "smallest_exact_falsifier": "a nonzero coefficient of n dot m in the claimed flip-even completion",
    "remaining_gate": "freeze one messenger topology and its symmetry charges independently, then derive its full gauge-Yukawa-scalar beta system",
}
(ROOT / "results" / "wp663_messenger_topology_rg_bifurcation.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
