"""Exact full-source hostile pair collapsed by the visible two-point port."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
h, x = sp.symbols("h x", real=True)
lh, lx, p = sp.symbols("lambda_h lambda_x p", positive=True)
H2, X2 = sp.symbols("H2 X2", positive=True)

def potential(lp, muh2, mux2):
    return -muh2*h**2/2 - mux2*x**2/2 + lh*h**4/4 + lx*x**4/4 + lp*h**2*x**2/2

# Retune only quadratic source masses so both portal-sign branches have the
# same declared nonzero vacuum norms H2 and X2.
muh_plus = lh*H2 + p*X2
mux_plus = lx*X2 + p*H2
muh_minus = lh*H2 - p*X2
mux_minus = lx*X2 - p*H2
V_plus = potential(p, muh_plus, mux_plus)
V_minus = potential(-p, muh_minus, mux_minus)

subs_vac = {h**2: H2, x**2: X2}
H_plus = sp.Matrix([[2*lh*H2, 2*p*sp.sqrt(H2*X2)], [2*p*sp.sqrt(H2*X2), 2*lx*X2]])
H_minus = H_plus.subs(p, -p)
S = sp.diag(1, -1)
s = sp.symbols("s", real=True)
e_h = sp.Matrix([1, 0])
G_plus = (s*sp.eye(2) - H_plus).inv()
G_minus = (s*sp.eye(2) - H_minus).inv()
visible_difference = sp.simplify((e_h.T*(G_plus-G_minus)*e_h)[0])

witness = {lh: 3, lx: 3, p: 1, H2: 1, X2: 1}

checks = {
    "plus_branch_stationary_at_target_norms": sp.simplify(sp.diff(V_plus, h)/h).subs(subs_vac) == 0 and sp.simplify(sp.diff(V_plus, x)/x).subs(subs_vac) == 0,
    "minus_branch_stationary_at_target_norms": sp.simplify(sp.diff(V_minus, h)/h).subs(subs_vac) == 0 and sp.simplify(sp.diff(V_minus, x)/x).subs(subs_vac) == 0,
    "hessians_are_hidden_port_conjugate": H_minus == S*H_plus*S,
    "pole_polynomials_identical": sp.simplify(H_plus.charpoly().as_expr() - H_minus.charpoly().as_expr()) == 0,
    "visible_two_point_records_identical": visible_difference == 0,
    "mixed_quartic_source_invariant_differs": sp.diff(V_plus, h, h, x, x) - sp.diff(V_minus, h, h, x, x) == 4*p,
    "stable_positive_mass_witness": muh_minus.subs(witness) == 2 and mux_minus.subs(witness) == 2 and H_plus.det().subs(witness) == 32,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP694",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "minimal complete radial quartic source with positive target vacuum norms and stable portal-sign branches obtained by source-level quadratic-mass retuning",
    "hostile_pair": "lambda_p=+p with mu_h^2=lambda_h H2+p X2 and mu_x^2=lambda_x X2+p H2 versus lambda_p=-p with the signs reversed",
    "shared_readout": "same vacuum norms, scalar pole polynomial, and every visible hh two-point resolvent",
    "physical_difference": "the mixed fourth derivative of the source potential differs by 4p and is invariant under independent radial sign changes",
    "first_nonfaithful_arrow": "complete radial source -> visible two-point propagator packet",
    "classification": "visible Higgs two-point port is a contextual rigidifier/readout but not a faithful identifier of full scalar source constructors",
    "smallest_exact_falsifier": "the rational witness lambda_h=lambda_x=3, p=1, H2=X2=1 gives positive quadratic masses, stable determinant 32, identical visible propagators, and opposite portal quartics",
    "remaining_instrument_gate": "add a calibrated observable sensitive to the mixed quartic or cubic interference, derived from the same source and evaluated jointly with the two-point bins",
}
(ROOT / "results" / "wp694_full_source_visible_port_hostile_pair.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
