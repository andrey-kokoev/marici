"""Exact bulk-scalar stabilization versus boundary-ratio audit."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
s, epsilon, C, v0, vpi = sp.symbols("s epsilon C v_0 v_pi", positive=True)

# Leading stiff-boundary Goldberger-Wise form. Its unique stationary minimum
# is conditional on the two independently supplied boundary values.
potential = C * (vpi - v0 * sp.exp(-epsilon * s)) ** 2
s_star = sp.log(v0 / vpi) / epsilon
stationary_residual = sp.simplify(sp.diff(potential, s).subs(s, s_star))
curvature = sp.simplify(sp.diff(potential, s, 2).subs(s, s_star))

# Grant the favorable common-scale relation a=epsilon*s_star=log(r), so no
# extra wall/warp scale ratio remains. Compose with WP758.
r = sp.symbols("r", positive=True)
a_star = sp.log(r)
portal_contrast_hyperbolic = sp.tanh(a_star) ** 2 / 2
portal_contrast = sp.factor(portal_contrast_hyperbolic.rewrite(sp.exp))
algebraic_contrast = sp.factor((r**2 - 1) ** 2 / (2 * (r**2 + 1) ** 2))
contrast_r2 = sp.simplify(portal_contrast.subs(r, 2))
contrast_r3 = sp.simplify(portal_contrast.subs(r, 3))
Delta = sp.symbols("Delta", positive=True)
r_inverse = sp.sqrt((1 + sp.sqrt(2 * Delta)) / (1 - sp.sqrt(2 * Delta)))

checks = {
    "stabilized_separation_is_log_boundary_ratio_over_epsilon": stationary_residual == 0,
    "conditional_stationary_point_has_positive_curvature": curvature == 2 * C * epsilon**2 * vpi**2,
    "log_hyperbolic_map_rewrites_exactly_to_algebraic_form": sp.simplify(portal_contrast_hyperbolic.rewrite(sp.exp) - algebraic_contrast) == 0,
    "boundary_ratio_two_gives_nine_fiftieths": contrast_r2 == sp.Rational(9, 50),
    "boundary_ratio_three_gives_eight_twenty_fifths": contrast_r3 == sp.Rational(8, 25),
    "same_stabilization_law_has_nonzero_boundary_data_fiber": sp.simplify(contrast_r3 - contrast_r2) == sp.Rational(7, 50),
    "every_submaximal_positive_contrast_has_boundary_ratio_preimage": sp.simplify(portal_contrast.subs(r, r_inverse) - Delta) == 0,
    "portal_contrast_varies_with_boundary_ratio": sp.simplify(sp.diff(portal_contrast, r)) != 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP759",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "a stiff-boundary bulk-scalar interval stabilizer with positive C and epsilon, boundary values v0>vpi>0, and the favorable common-scale identification a=epsilon*s_star",
    "faithful_coordinate": "the stabilized separation together with the independently specified boundary-value ratio r=v0/vpi and labelled wall orientation",
    "source_authorized_operation": "bulk-scalar variational equation and its induced radion potential",
    "stabilization_result": "s_star=log(v0/vpi)/epsilon with positive curvature 2*C*epsilon^2*vpi^2",
    "composed_portal_readout": "Delta(r)=(r^2-1)^2/[2*(r^2+1)^2] under the favorable common-scale grant",
    "contextual_partition": "the variational law selects one separation for each boundary packet but does not select among boundary packets",
    "classification": "conditional separation selector and local stabilizer, but not a source selector of the portal magnitude",
    "smallest_exact_falsifier": "r=2 and r=3 obey the same source equations and have stable minima but predict portal contrasts 9/50 and 8/25",
    "strong_grant": "the wall-width/stabilizer scale ratio is set to one; a generic model retains that additional continuous ratio",
    "sign_gate": "boundary ordering and wall orientation must still be fixed independently to assign the labelled sign",
    "rg_threshold_gate": "boundary values and bulk mass parameter require their own renormalized source law; stabilization alone does not protect the portal across wall, radion, and KK thresholds",
    "instrument_gate": "the stabilized overlap remains a formal coupling until embedded in a labelled, detector-calibrated process",
    "deutschian_status": "the stabilizer explains why a radius has a minimum, but its numerical answer is easy to vary through boundary data not explained by the mechanism",
    "next_source_gate": "derive the boundary-value ratio and orientation from quantized source data or a unique vacuum, rather than treating them as brane inputs",
}
(ROOT / "results" / "wp759_bulk_scalar_stabilization_boundary_ratio_fiber.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
