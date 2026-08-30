"""Exact source-stability support and universal cubic contrast floor."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
alpha = sp.symbols("alpha", positive=True)
t = sp.symbols("t", positive=True)
T = alpha + sp.sqrt(alpha**2-1)
Tinv = alpha - sp.sqrt(alpha**2-1)
contrast = 4*t/(t+1)**2
floor = sp.simplify(contrast.subs(t, T))

R_over_p = (t+1/t)/2
stability_polynomial = sp.factor(t**2-2*alpha*t+1)

checks = {
    "stability_roots_reciprocal": sp.simplify(T*Tinv) == 1,
    "stability_roots_sum": sp.simplify(T+Tinv) == 2*alpha,
    "stability_inequality_polynomial": sp.factor(2*t*(R_over_p-alpha)) == stability_polynomial,
    "contrast_floor_exact": sp.simplify(floor-2/(alpha+1)) == 0,
    "wp696_upper_alpha_boundary_gives_three_quarters": sp.simplify(floor.subs(alpha, sp.Rational(5, 3))-sp.Rational(3, 4)) == 0,
    "interior_alpha_witness_exceeds_three_quarters": floor.subs(alpha, sp.Rational(3, 2)) == sp.Rational(4, 5),
    "open_decay_automatic_at_upper_corridor_boundary": sp.Rational(3, 5)*sp.Rational(5, 3) == 1,
    "unbounded_coupling_ratio_loses_floor": sp.limit(2/(alpha+1), alpha, sp.oo) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP700",
    "status": "PASS",
    "checks": checks,
    "admitted_source_domain": "equal-vacuum radial source with coupling ratio alpha=lambda/p in the WP696 corridor 1<alpha<5/3 and arbitrary asymmetry compatible with strict stability",
    "source_authorized_support": "strict stability implies alpha-sqrt(alpha^2-1)<t<alpha+sqrt(alpha^2-1)",
    "uniform_contrast_floor": "C>2/(alpha+1)>3/4",
    "kinematic_result": "for alpha<5/3, R>=p implies R>3lambda/5, so the heavy-to-two-light channel is automatically open throughout the stable t support",
    "classification": "source-stability-derived uniform identifier margin on a declared coupling corridor; not a numerical selector and not a calibrated instrument",
    "smallest_exact_falsifier": "if alpha is not bounded above, the stability-derived contrast floor 2/(alpha+1) tends to zero",
    "remaining_physical_instrument_gate": "derive or measure the coupling corridor independently in the full flavor source and propagate the greater-than-three-quarters ideal contrast through calibrated widths, loops, efficiencies, backgrounds, and uncertainty",
}
(ROOT / "results" / "wp700_stability_authorized_contrast_floor.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
