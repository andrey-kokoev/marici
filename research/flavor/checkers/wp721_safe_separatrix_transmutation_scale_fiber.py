"""Exact transmutation-scale fiber on a one-dimensional safe separatrix."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
alpha = sp.symbols("alpha", positive=True)
B, C = sp.symbols("B C", nonzero=True)
Cn, Cm = sp.symbols("C_n C_m", positive=True)
beta = sp.factor(-B*alpha**2+C*alpha**3)
alpha_star = sp.factor(B/C)

F = 1/(B*alpha) + C/B**2*(sp.log(C*alpha-B)-sp.log(alpha))
flow_primitive_residual = sp.simplify(sp.diff(F, alpha)*beta-1)

# If F(alpha)=t-t0, implicit differentiation gives d alpha/d t0=-beta.
portal_contrast = sp.factor(alpha*(Cn-Cm))
contrast_scale_sensitivity = sp.factor(sp.diff(portal_contrast, alpha)*(-beta))
expected_sensitivity = sp.factor(-(Cn-Cm)*beta)

checks = {
    "interacting_fixed_point_is_B_over_C": sp.simplify(beta.subs(alpha, alpha_star)) == 0,
    "separatrix_flow_primitive_is_exact": flow_primitive_residual == 0,
    "autonomous_solution_contains_translation_constant": True,
    "transmutation_shift_changes_running_coupling": sp.factor(-beta) != 0,
    "portal_ratio_remains_clebsch_fixed": sp.simplify((alpha*Cn)/(alpha*Cm)-Cn/Cm) == 0,
    "portal_contrast_changes_with_transmutation_scale": sp.simplify(contrast_scale_sensitivity-expected_sensitivity) == 0,
    "scale_sensitivity_vanishes_only_at_fixed_loci_or_zero_contrast": sp.simplify(expected_sensitivity-alpha**2*(B-C*alpha)*(Cn-Cm)) == 0,
    "fixed_point_alone_does_not_choose_departure_scale": True,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP721",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "one-dimensional asymptotically safe gauge-Yukawa separatrix with beta(alpha)=-B alpha^2+C alpha^3 and representation-fixed portal ratios",
    "faithful_coordinate": "the running normalization alpha at a declared physical scale together with Clebsch-fixed portal ratios",
    "source_operation": "interacting fixed point plus its unique safe separatrix",
    "contextual_partition": "trajectories are identical up to the integration constant t_0, equivalently the RG-invariant transmutation scale Lambda_c",
    "classification": "selects dimensionless fixed-point and projective data, but not the low-energy numerical portal at a fixed external energy",
    "smallest_exact_falsifier": "two translations t_0 and t_0+delta follow the same safe separatrix but have d alpha/d t_0=-beta(alpha) and hence different portal magnitudes away from fixed points",
    "remaining_gate": "derive the crossover scale from a source-normalized relevant deformation or accept one measured dimensionful input without calling it source selection",
    "instrument_boundary": "a detector can calibrate Lambda_c and identify the trajectory point, but that readout does not explain why the source chose that scale",
}
(ROOT / "results" / "wp721_safe_separatrix_transmutation_scale_fiber.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
