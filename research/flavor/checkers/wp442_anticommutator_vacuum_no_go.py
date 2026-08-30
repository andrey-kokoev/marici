"""Exact WP442 no-go for full breaking in the WP440 unstable region."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]
wp441 = json.loads((root / "results" / "wp441_charged_instability_threshold.json").read_text(encoding="utf-8"))
I = sp.I
basis = [
    sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
    sp.diag(1, -1, 0),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
    sp.Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]]),
    sp.diag(1, 1, -2),
]


def norm_squared(matrix):
    return sp.simplify(sp.trace(matrix.conjugate().T * matrix))


z = sp.symbols("z0:16", real=True)
A = sum((z[i]*basis[i] for i in range(8)), sp.zeros(3))
D = sum((z[8+i]*basis[i] for i in range(8)), sp.zeros(3))
R = sp.trace(A*A + D*D)
C = A*D-D*A
Q = A*D+D*A
V = -R/2 + 5*R**2 - norm_squared(C) - 4*norm_squared(Q)

branch = {q: 0 for q in z}
branch[z[2]] = sp.sqrt(sp.Rational(1, 208))
branch[z[5]] = sp.sqrt(sp.Rational(1, 104))
branch[z[8]] = sp.sqrt(sp.Rational(1, 208))
branch[z[11]] = sp.sqrt(sp.Rational(1, 104))
branch_hessian = sp.hessian(V, z).subs(branch)

commuting = {q: 0 for q in z}
commuting[z[2]] = sp.sqrt(sp.Rational(1, 48))
commuting[z[10]] = sp.sqrt(sp.Rational(1, 48))
A0, D0 = A.subs(commuting), D.subs(commuting)
mass_gram = sp.Matrix([
    [
        sp.trace((basis[i]*A0-A0*basis[i]).conjugate().T*(basis[j]*A0-A0*basis[j]))
        + sp.trace((basis[i]*D0-D0*basis[i]).conjugate().T*(basis[j]*D0-D0*basis[j]))
        for j in range(8)
    ] for i in range(8)
])
commuting_hessian = sp.hessian(V, z).subs(commuting)

u = sp.symbols("u0:8", real=True)
X = sum((u[i]*basis[i] for i in range(8)), sp.zeros(3))
cayley_trace_identity = sp.expand(sp.trace(X**4)-sp.trace(X**2)**2/2)

checks = {
    "wp441_dependency_passed": wp441["passed"],
    "traceless_three_by_three_fourth_trace_identity": cayley_trace_identity == 0,
    "branch_is_stationary": all(sp.diff(V, q).subs(branch) == 0 for q in z),
    "branch_is_commuting": C.subs(branch) == sp.zeros(3),
    "branch_has_nongauge_negative_mode": branch_hessian.eigenvals().get(sp.Rational(-16, 13)) == 1,
    "commuting_saturator_is_stationary": all(sp.diff(V, q).subs(commuting) == 0 for q in z),
    "commuting_saturator_reaches_global_bound": sp.simplify(V.subs(commuting)+sp.Rational(1, 48)) == 0,
    "commuting_saturator_has_gauge_rank_six": mass_gram.rank() == 6,
    "commuting_saturator_has_no_negative_hessian_mode": all(value >= 0 for value in commuting_hessian.eigenvals()),
    "global_saturator_beats_branch": V.subs(commuting) < V.subs(branch),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP442",
    "theorem": "For eta>lambda, every global minimizer of WP440 is commuting; therefore gauge-mass rank is at most six.",
    "global_bound": "V >= -m^2 R/2 + (rho-eta/2) R^2",
    "equality_reason": "lambda C + eta Q <= eta(C+Q) <= eta R^2/2; equality with eta>lambda forces C=0.",
    "hostile_point": {"m_squared": 1, "lambda": 1, "eta": 4, "rho": 5},
    "branch_energy": str(sp.simplify(V.subs(branch))),
    "global_commuting_energy": str(sp.simplify(V.subs(commuting))),
    "branch_hessian_spectrum": {str(k): int(v) for k, v in branch_hessian.eigenvals().items()},
    "commuting_hessian_spectrum": {str(k): int(v) for k, v in commuting_hessian.eigenvals().items()},
    "global_gauge_mass_rank": mass_gram.rank(),
    "classification": "The WP440 anticommutator completion destabilizes WP438 but selects a commuting rank-six global vacuum, not full flavor breaking.",
    "smallest_exact_falsifier": "At (1,1,4,5), a configuration below energy -1/48 or a rank above six for the commuting saturator.",
    "remaining_gate": "A full-breaking successor needs a genuinely different source-authorized invariant grammar or additional representation; g_F f/v remains unsourced.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp442_anticommutator_vacuum_no_go.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
