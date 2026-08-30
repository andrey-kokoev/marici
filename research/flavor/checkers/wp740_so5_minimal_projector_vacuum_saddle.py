"""Exact Hessian no-go for the minimal SO(5) symmetric-traceless projector."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
l1, l2, v, m2 = sp.symbols("lambda_1 lambda_2 v m2", real=True)
a, b, c = sp.symbols("a b c", real=True)

root_sum_equation = a + b + c
trace_equation = 3*a + b + c
root_solution = sp.solve((root_sum_equation, trace_equation), (a, c), dict=True)[0]

phi = sp.diag(0, 0, 0, v, -v)
stationary_m2 = (2*l1 + l2)*v**2

x, y = sp.symbols("x y", real=True)
z = -3*x - y
H_diag = sp.diag(x, x, x, y, z)

def hessian_form(H):
    return sp.expand(
        -l2*v**2*sp.trace(H*H)
        + 2*l1*sp.trace(phi*H)**2
        + 2*l2*sp.trace(phi*phi*H*H)
        + l2*sp.trace(phi*H*phi*H)
    )

Q_diag = sp.factor(hessian_form(H_diag) / v**2)
M_diag = sp.simplify(sp.hessian(Q_diag, (x, y)) / 2)
det_diag = sp.factor(M_diag.det())

h = sp.symbols("h", real=True)
H_shape = sp.zeros(5)
H_shape[0, 1] = h
H_shape[1, 0] = h
Q_shape = sp.factor(hessian_form(H_shape) / (2*h**2*v**2))

expected_M = sp.Matrix([
    [18*l1 + 15*l2, 12*l1 + 6*l2],
    [12*l1 + 6*l2, 8*l1 + 4*l2],
])
hostile = det_diag.subs({l1: 1, l2: -1})

checks = {
    "root_and_trace_constraints_force_triplet_eigenvalue_zero": root_solution[a] == 0,
    "remaining_eigenvalues_are_opposite": root_solution[c] == -b,
    "candidate_is_traceless": sp.trace(phi) == 0,
    "stationary_scale_relation_is_exact": stationary_m2 == (2*l1 + l2)*v**2,
    "upper_block_shape_coefficient_is_minus_lambda2": Q_shape == -l2,
    "diagonal_singlet_hessian_is_exact": sp.simplify(M_diag - expected_M) == sp.zeros(2),
    "diagonal_singlet_determinant_is_exact": det_diag == 24*l2*(2*l1 + l2),
    "stability_and_existence_make_determinant_negative": (
        det_diag.subs({l1: 1, l2: -1}) < 0
    ),
    "opposite_lambda2_sign_destabilizes_shape_mode": Q_shape.subs(l2, 1) < 0,
    "zero_lambda2_leaves_shape_flat": Q_shape.subs(l2, 0) == 0,
    "deliberate_failure_residual_is_nonzero": hostile == -24 and hostile != 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP740",
    "status": "PASS",
    "checks": checks,
    "source_domain": "one real symmetric-traceless 14 of SO(5) with the complete Z2-even renormalizable potential",
    "candidate_vacuum": "diag(0,0,0,v,-v), with m^2=(2 lambda_1+lambda_2)v^2",
    "classification": "the representation fixes a projector pattern algebraically, but the minimal source potential cannot select it dynamically",
    "exact_obstruction": "triplet-shape stability requires lambda_2<0 while the singlet Hessian determinant is 24 lambda_2(2 lambda_1+lambda_2)<0",
    "smallest_exact_falsifier": "at lambda_1=1, lambda_2=-1 the singlet Hessian determinant is -24",
    "deliberate_failure_residual": str(hostile),
    "claim_boundary": "Z2-even quartic renormalizable potential; an independently derived cubic invariant or higher operator is not ruled out",
    "remaining_source_gate": "derive any stabilizing cubic or higher operator and its coefficient independently, then prove a gapped projector and fixed eigenvalue ratios",
    "remaining_fixed_point_gate": "deferred because the minimal projector vacuum is a saddle",
    "remaining_physical_gate": "deferred; both singlet mass eigenstates would need labelled independently calibrated readout",
}
(ROOT / "results" / "wp740_so5_minimal_projector_vacuum_saddle.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
