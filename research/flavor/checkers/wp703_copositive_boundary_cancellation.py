"""Exact test that radial stability permits affine portal cancellation."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
lh, lx, p_uv, dp = sp.symbols(
    "lambda_h lambda_x p_UV Delta_p", positive=False, real=True
)

p_low = p_uv + dp
copositive_margin_squared = lh * lx - p_uv**2
mixed_vacuum_determinant_margin = lh * lx - p_uv**2
witness = {lh: 2, lx: 2, p_uv: -1, dp: 1}

# Along y=h^2/x^2>=0, 4 V_4/x^4 = lambda_h y^2+2 p_UV y+lambda_x.
y = sp.symbols("y", nonnegative=True)
quartic_ray = lh * y**2 + 2 * p_uv * y + lx
witness_ray = sp.factor(quartic_ray.subs(witness))

general_cancellation = sp.simplify(p_low.subs(p_uv, -dp))
general_stability_margin = sp.factor(
    mixed_vacuum_determinant_margin.subs(p_uv, -dp)
)

checks = {
    "witness_quartic_positive_on_every_radial_ray": sp.expand(witness_ray) == 2*y**2-2*y+2 and sp.discriminant(witness_ray, y) < 0,
    "witness_uv_portal_is_negative": p_uv.subs(witness) < 0,
    "witness_copositivity_margin_is_positive": (sp.sqrt(lh*lx)+p_uv).subs(witness) == 1,
    "witness_mixed_vacuum_margin_is_positive": mixed_vacuum_determinant_margin.subs(witness) == 3,
    "witness_low_portal_cancels_exactly": p_low.subs(witness) == 0,
    "general_cancellation_preimage": general_cancellation == 0,
    "general_stability_reduces_to_threshold_bound": general_stability_margin == -dp**2+lh*lx,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP703",
    "status": "PASS",
    "checks": checks,
    "admitted_source_domain": "WP685 radial quartic source with free UV portal boundary, positive self-couplings, and additive finite portal threshold",
    "stability_conditions": {
        "quartic_copositivity": "lambda_h>0, lambda_x>0, p_UV>-sqrt(lambda_h lambda_x)",
        "mixed_vacuum_hessian": "lambda_h lambda_x-p_UV^2>0",
    },
    "contextual_partition": "stability retains both portal signs and the exact threshold-cancellation fiber",
    "classification": "stability is an admissibility rigidifier, not a selector of nonzero low-energy portal support or the WP700 ratio corridor",
    "smallest_exact_falsifier": "lambda_h=lambda_x=2, Delta_p=1, p_UV=-1 has positive copositivity and Hessian margins but p_low=0",
    "remaining_selector_gate": "derive a noninvertible UV boundary law stronger than copositivity; p_UV>=0 cannot be inserted without independent source authority",
}
(ROOT / "results" / "wp703_copositive_boundary_cancellation.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
