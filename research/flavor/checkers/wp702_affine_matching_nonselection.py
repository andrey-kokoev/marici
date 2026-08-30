"""Exact no-go for selection by additive threshold matching with free boundaries."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
lam_uv, p_uv = sp.symbols("lambda_UV p_UV", real=True)
dlam, dp = sp.symbols("Delta_lambda Delta_p", real=True)
lam_target, p_target = sp.symbols("lambda_target p_target", real=True)

low = sp.Matrix([lam_uv+dlam, p_uv+dp])
boundary = sp.Matrix([lam_uv, p_uv])
jacobian = low.jacobian(boundary)
preimage = sp.Matrix([lam_target-dlam, p_target-dp])

inside_target = {lam_target: sp.Rational(3, 2), p_target: 1}
outside_target = {lam_target: 2, p_target: 1}
zero_target = {p_target: 0}

checks = {
    "matching_map_is_invertible": jacobian.det() == 1,
    "every_low_energy_target_has_preimage": sp.simplify(low.subs({lam_uv: preimage[0], p_uv: preimage[1]})-sp.Matrix([lam_target, p_target])) == sp.zeros(2, 1),
    "zero_portal_target_has_preimage": sp.simplify(low[1].subs(p_uv, -dp)) == 0,
    "inside_corridor_target_reachable": sp.simplify(low.subs({lam_uv: preimage[0], p_uv: preimage[1]}).subs(inside_target)-sp.Matrix([sp.Rational(3, 2), 1])) == sp.zeros(2, 1),
    "outside_corridor_target_reachable": sp.simplify(low.subs({lam_uv: preimage[0], p_uv: preimage[1]}).subs(outside_target)-sp.Matrix([2, 1])) == sp.zeros(2, 1),
    "positive_threshold_does_not_exclude_zero_total": low[1].subs({p_uv: -1, dp: 1}) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP702",
    "status": "PASS",
    "checks": checks,
    "admitted_source_domain": "two independently free renormalized UV quartic boundaries with finite additive source-derived threshold and transport corrections",
    "matching_map": "(lambda_UV,p_UV) -> (lambda_UV+Delta_lambda,p_UV+Delta_p)",
    "nonselection_result": "the map is an affine bijection, so it reaches the high-contrast corridor, stable points outside it, and the zero-portal stratum",
    "classification": "radiative matching supplies operator support and rigidification but no proper-subspace selector while both UV boundaries remain free",
    "smallest_exact_falsifier": "p_UV=-Delta_p produces p_low=0 even when the source-derived threshold Delta_p is strictly positive",
    "remaining_selector_gate": "a noninvertible source boundary condition, fixed point with an independently admitted basin, positivity domain excluding the cancellation preimage, or other UV constructor must remove boundary freedom before matching can select",
}
(ROOT / "results" / "wp702_affine_matching_nonselection.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
