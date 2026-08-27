"""Exact stabilizer-groupoid typing of the radial mixing sign."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
s, mh2, mx2, kappa = sp.symbols("s mh2 mx2 kappa", real=True)

K_plus = sp.Matrix([[s - mh2, -kappa], [-kappa, s - mx2]])
K_minus = K_plus.subs(kappa, -kappa)
S = sp.diag(1, -1)
e_h = sp.Matrix([1, 0])
e_x = sp.Matrix([0, 1])
G_plus = sp.simplify(K_plus.inv())
G_minus = sp.simplify(K_minus.inv())

visible_plus = sp.simplify((e_h.T * G_plus * e_h)[0])
visible_minus = sp.simplify((e_h.T * G_minus * e_h)[0])
cross_plus = sp.simplify((e_h.T * G_plus * e_x)[0])
cross_minus = sp.simplify((e_h.T * G_minus * e_x)[0])

checks = {
    "sign_flip_is_hidden_basis_conjugation": K_minus == S * K_plus * S,
    "visible_port_is_fixed_by_stabilizer": S * e_h == e_h,
    "hidden_port_changes_orientation": S * e_x == -e_x,
    "visible_resolvent_is_invariant": sp.simplify(visible_minus - visible_plus) == 0,
    "cross_port_resolvent_is_odd": sp.simplify(cross_minus + cross_plus) == 0,
    "pole_polynomial_is_invariant": sp.simplify(K_minus.det() - K_plus.det()) == 0,
    "nonzero_cross_port_witness": cross_plus.subs({s: 5, mh2: 1, mx2: 2, kappa: 1}) == sp.Rational(1, 11),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP693",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "real two-radial-mode inverse propagators with the ordinary Higgs port as the sole admitted external port",
    "groupoid": "the visible-port stabilizer contains S=diag(1,-1), acting by K -> S K S while fixing the Higgs source vector",
    "contextual_partition": "kappa and -kappa are the same visible-port operational class; all visible poles and hh resolvents agree",
    "classification": "the WP692 sign pair is a contextual presentation ambiguity on the reduced two-point domain, not yet a pair of physically inequivalent physical16 points",
    "reference_port_result": "an admitted exit-sensitive port measures the cross resolvent, changes sign under S, and therefore defines a richer relational experiment over the smaller stabilizer groupoid",
    "smallest_exact_falsifier": "one nonzero calibrated Higgs-to-exit cross-port amplitude distinguishes the two representatives",
    "remaining_gate": "map the radial propagator parameters covariantly from the complete flavor source and decide whether any full-source invariant distinguishes portal-sign branches before detector projection",
}
(ROOT / "results" / "wp693_hidden_port_sign_groupoid.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
