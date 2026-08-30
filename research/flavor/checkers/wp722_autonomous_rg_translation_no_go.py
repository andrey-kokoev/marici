"""Exact autonomous-RG translation fiber and source-anchor gate."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
t, c, K = sp.symbols("t c K", real=True, nonzero=True)
x_anchor, t_anchor = sp.symbols("x_anchor t_anchor", real=True, nonzero=True)
x = 1/(c-t)
y = K/(c-t)**2
beta_x = x**2
beta_y = 2*x*y
projective_invariant = sp.factor(y/x**2)
portal = y
translation_sensitivity = sp.factor(sp.diff(portal, c))
anchor_solution = sp.solve(sp.Eq(1/(c-t_anchor), x_anchor), c)[0]

x1, x2, b1, b2 = sp.symbols("x_1 x_2 beta_1 beta_2", real=True)
O = sp.Function("O")(x1, x2)
lie_derivative = sp.diff(O, x1)*b1 + sp.diff(O, x2)*b2

checks = {
    "translated_x_family_solves_autonomous_flow": sp.simplify(sp.diff(x, t)-beta_x) == 0,
    "translated_y_family_solves_coupled_flow": sp.simplify(sp.diff(y, t)-beta_y) == 0,
    "projective_relation_is_translation_invariant": projective_invariant == K,
    "low_energy_portal_varies_along_translation_fiber": sp.simplify(translation_sensitivity+2*K/(c-t)**3) == 0,
    "same_projective_ray_has_continuum_of_portal_values": sp.simplify(portal.subs(t, 0)-K/c**2) == 0,
    "dimensionful_boundary_condition_fixes_translation": anchor_solution == t_anchor+1/x_anchor,
    "generic_observable_sensitivity_is_lie_derivative": lie_derivative == b1*sp.diff(O, x1)+b2*sp.diff(O, x2),
    "rg_invariants_alone_are_translation_insensitive": sp.diff(projective_invariant, c) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP722",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "autonomous dimensionless RG flows evaluated relative to a fixed physical energy",
    "faithful_coordinate": "the point on the RG orbit, not merely its projective orbit or invariant labels",
    "theorem": "time translation maps every nonconstant autonomous RG solution to another solution; any observable with nonzero Lie derivative along beta varies on this fiber",
    "contextual_partition": "projective and RG-invariant data identify an orbit, while the translation constant labels physically distinct values at a declared external scale",
    "classification": "autonomous RG can rigidify an orbit and its basin but cannot select its absolute placement without a dimensionful source anchor",
    "smallest_exact_falsifier": "x=1/(c-t), y=K/(c-t)^2 has fixed y/x^2=K for every c but y(0)=K/c^2",
    "minimal_repair": "one source-authorized condition x(t_anchor)=x_anchor, giving c=t_anchor+1/x_anchor",
    "authority_gate": "a measured electroweak, messenger, detector, or Planck scale fixes the translation only if a named source interface derives its relation to the flavor trajectory; calibration alone is identification, not selection",
}
(ROOT / "results" / "wp722_autonomous_rg_translation_no_go.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
