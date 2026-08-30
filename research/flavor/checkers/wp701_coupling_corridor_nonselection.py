"""Exact no-go: stability does not select the WP700 coupling corridor."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
lam, p, v = sp.symbols("lambda p v", positive=True)

mL2 = 2*v**2*(lam-p)
mH2 = 2*v**2*(lam+p)
stability_margin = sp.factor(lam**2-p**2)
decay_margin = sp.factor(mH2-4*mL2)

inside = {lam: sp.Rational(3, 2), p: 1, v: 1}
outside = {lam: 2, p: 1, v: 1}

# The same grammar also admits an exactly decoupled positive quartic point.
l0, v0 = sp.symbols("lambda_0 v_0", positive=True)
zero_portal_hessian = 2*v0**2*sp.diag(l0, l0)

checks = {
    "stability_condition_only_requires_alpha_above_one": stability_margin.subs(inside) > 0 and stability_margin.subs(outside) > 0,
    "inside_corridor_decay_open": decay_margin.subs(inside) == 1,
    "outside_corridor_decay_closed": decay_margin.subs(outside) == -2,
    "outside_witness_strictly_stable": mL2.subs(outside) == 2 and mH2.subs(outside) == 6,
    "corridor_boundary_is_five_thirds": decay_margin.subs(lam, sp.Rational(5, 3)*p) == 0,
    "zero_portal_stable_source_allowed": zero_portal_hessian.det() == 4*l0**2*v0**4,
    "stability_does_not_imply_decay": sp.factor(decay_margin) == 2*v**2*(-3*lam+5*p),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP701",
    "status": "PASS",
    "checks": checks,
    "admitted_source_domain": "minimal symmetric radial potential with independently free positive self-coupling lambda and portal magnitude p, plus the legal p=0 stratum",
    "nonselection_result": "strict stability requires lambda/p>1 but does not impose lambda/p<5/3; the WP700 high-contrast open-decay corridor is a proper subset of stable sources",
    "inside_witness": "lambda/p=3/2 is stable and has open H-to-LL phase space",
    "smallest_exact_falsifier": "lambda/p=2 is strictly stable with masses squared {2,6} but H-to-LL phase space is closed",
    "zero_portal_falsifier": "the same source grammar admits p=0 with a positive diagonal Hessian and no branch contrast",
    "classification": "stability rigidifies support conditional on a chosen corridor but does not select the corridor or a portal branch",
    "remaining_selector_gate": "derive an independent source operation that restricts lambda/p to a proper predictive domain and excludes p=0 before using the cubic contrast as an instrument prediction",
}
(ROOT / "results" / "wp701_coupling_corridor_nonselection.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
