"""Exact affine theorem, without assigning instrument status to RG scale."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
a, b = sp.symbols("a b", real=True)
L1, L2 = sp.symbols("L1 L2", real=True)
response = sp.Matrix([a+b*L1, a+b*L2])
J = response.jacobian([a, b])
midpoint_boundary = -b*(L1+L2)/2
midpoint_response = sp.simplify(response.subs(a, midpoint_boundary))

# A concrete ordered-scale witness.
witness = {L1: 0, L2: 2, b: 3}

checks = {
    "two_scale_response_is_rank_two": sp.factor(J.det()) == L2-L1,
    "simultaneous_zero_requires_zero_running_or_equal_scales": sp.simplify(response[1]-response[0]-b*(L2-L1)) == 0,
    "midpoint_boundary_balances_residuals": midpoint_response == sp.Matrix([b*(L1-L2)/2, b*(-L1+L2)/2]),
    "minimax_witness_has_nonzero_floor": max(abs(v) for v in midpoint_response.subs(witness)) == 3,
    "single_scale_can_always_be_cancelled": response[0].subs(a, -b*L1) == 0,
    "second_scale_survives_first_scale_cancellation": sp.simplify(response[1].subs(a, -b*L1)-b*(L2-L1)) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP689",
    "status": "PASS",
    "checks": checks,
    "domain": "abstract affine response lambda(L)=a+bL with source-generated b>0; L must be a physical executable context to carry probe authority",
    "two_scale_jacobian": "det=difference L2-L1",
    "cancellation_no_go": "one boundary value a can cancel lambda at one scale but not at two distinct scales when b is nonzero",
    "uniform_two_context_floor": "min_a max(|lambda(L1)|,|lambda(L2)|)=b|L2-L1|/2",
    "optimal_boundary": "a=-b(L1+L2)/2",
    "classification": "affine comparison theorem only; renormalization-scale choices are not physical probes, while distinct executable physical contexts could remove the boundary cancellation algebraically",
    "smallest_exact_falsifier": "b=0 or L1=L2 collapses the two-scale determinant",
    "remaining_gate": "derive a finite-momentum same-channel response and bind two calibrated measurements at distinct physical momenta",
}
(ROOT / "results" / "wp689_two_scale_portal_cancellation_no_go.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
