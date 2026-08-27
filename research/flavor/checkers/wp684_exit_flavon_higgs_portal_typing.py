"""Exact invariant-typing audit for a Higgs portal to the messenger exit flavon."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

# Standard generators of rotations on the SO(3) vector representation.
J1 = sp.Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]])
J2 = sp.Matrix([[0, 0, 1], [0, 0, 0], [-1, 0, 0]])
J3 = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
w1, w2, w3 = sp.symbols("w1 w2 w3")
w = sp.Matrix([w1, w2, w3])
linear_invariants = sp.linsolve(list(J1*w)+list(J2*w)+list(J3*w), (w1, w2, w3))

# The Euclidean quadratic is invariant under all infinitesimal rotations.
delta = sp.eye(3)
quadratic_invariant = all(J.T*delta+delta*J == sp.zeros(3) for J in (J1, J2, J3))

# Expansion of lambda (H^dag H)(X.X) about X=x0+chi.
lam, h2 = sp.symbols("lambda_p h2", real=True)
x01, x02, x03, c1, c2, c3 = sp.symbols("x01 x02 x03 chi1 chi2 chi3", real=True)
x0 = sp.Matrix([x01, x02, x03])
chi = sp.Matrix([c1, c2, c3])
portal = sp.expand(lam*h2*((x0+chi).dot(x0+chi)))
linear_chi = sp.expand(2*lam*h2*x0.dot(chi))

checks = {
    "so3_vector_has_no_linear_singlet": linear_invariants == {(0, 0, 0)},
    "so3_dot_is_quadratic_invariant": quadratic_invariant,
    "quadratic_portal_induces_mixing_only_after_vev": all(sp.expand(portal).coeff(ci, 1).subs({c1: 0, c2: 0, c3: 0}) == sp.expand(linear_chi).coeff(ci, 1) for ci in (c1, c2, c3)),
    "zero_exit_vev_removes_induced_linear_portal": linear_chi.subs({x01: 0, x02: 0, x03: 0}) == 0,
    "zero_mixed_quartic_removes_induced_linear_portal": linear_chi.subs(lam, 0) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP684",
    "status": "PASS",
    "checks": checks,
    "field_typing": "messenger exit X_i is an SU(3)_F adjoint and SO(3)_P vector",
    "linear_portal": "H^dag H times X_i is forbidden: the SO(3)_P vector has no invariant linear functional; the flavor adjoint also has no trace singlet",
    "lowest_portal": "lambda_p (H^dag H)(X_i dot X_i)",
    "conditional_mixing": "after a declared exit vev x0, the quadratic portal contains 2 lambda_p (H^dag H)(x0 dot chi)",
    "authority_result": "the source registry does not admit the complete mixed potential, lambda_p, or the required common-frame vacuum direction, so this is not a current coherent reference",
    "classification": "typed candidate repair, presently unauthorized",
    "smallest_exact_falsifier": "lambda_p=0 or x0=0 removes the induced linear Higgs-exit mixing exactly",
    "remaining_gate": "derive the complete invariant mixed scalar potential and its vacuum, then compute the same-channel reference amplitude without borrowing a fitted portal angle",
}
(ROOT / "results" / "wp684_exit_flavon_higgs_portal_typing.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
