"""Exact audit of the single-spurion correlated-Higgsing acceptance condition."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
a, b, gstar2, v2, E2 = sp.symbols(
    "a b g_star_squared v_squared E_squared", positive=True
)

vector_mass2 = a * gstar2 * v2
soft_mass2 = b * gstar2 * v2
epsilon = sp.cancel(soft_mass2 / (vector_mass2 + soft_mass2))
contrast = sp.factor(gstar2 * epsilon / 2)
threshold_margin = sp.factor(vector_mass2 - E2)

# Same fixed coupling and spurion scale, but two admissible coefficient packets.
witness_11 = sp.factor(contrast.subs({a: 1, b: 1}))
witness_13 = sp.factor(contrast.subs({a: 1, b: 3}))
coefficient_residual = sp.factor(witness_13 - witness_11)

checks = {
    "common_spurion_cancels_from_epsilon": sp.diff(epsilon, v2) == 0,
    "epsilon_is_dimensionless_coefficient_ratio": epsilon == b / (a + b),
    "common_spurion_cancels_from_portal_contrast": sp.diff(contrast, v2) == 0,
    "portal_contrast_has_selected_positive_sign": contrast.is_positive is True,
    "portal_contrast_retains_fixed_gauge_normalization": sp.diff(contrast, gstar2) != 0,
    "portal_contrast_depends_on_vector_coefficient": sp.diff(contrast, a) != 0,
    "portal_contrast_depends_on_soft_coefficient": sp.diff(contrast, b) != 0,
    "threshold_support_retains_the_spurion_clock": sp.diff(threshold_margin, v2) != 0,
    "equal_coefficients_give_quarter_strength": witness_11 == gstar2 / 4,
    "one_to_three_coefficients_give_three_eighths_strength": witness_13 == 3 * gstar2 / 8,
    "hostile_coefficient_pair_has_nonzero_residual": coefficient_residual == gstar2 / 8,
    "deliberate_failure_residual_is_nonzero": coefficient_residual != 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP749",
    "status": "PASS",
    "checks": checks,
    "admitted_domain": "positive a, b, g_star_squared, v_squared with correlated vector and soft masses M_V^2=a g_*^2 v^2 and m_soft^2=b g_*^2 v^2",
    "exact_threshold_factor": "epsilon=b/(a+b)",
    "exact_portal_contrast": "Delta=g_*^2 b/(2(a+b))",
    "positive_result": "one correlated spurion cancels the common dimensionful clock from the dimensionless nondecoupling portal magnitude and preserves its positive ordered sign",
    "coefficient_fiber": "the ratio b/a remains free unless the source theory fixes both representation-response coefficients",
    "threshold_support_fiber": "E^2<a g_*^2 v^2 still depends on the spurion scale v",
    "smallest_exact_falsifier": "at the same g_* and v, (a,b)=(1,1) gives Delta=g_*^2/4 while (a,b)=(1,3) gives Delta=3g_*^2/8; residual g_*^2/8",
    "classification": "conditional magnitude selector and common-clock canceller, but not yet a source principle, threshold-survival theorem, or physical instrument",
    "deutschian_status": "not yet a hard-to-vary explanation because the coefficient packet and its source constructor can be varied without changing the mechanism",
    "claim_boundary": "algebraic acceptance theorem only; no microscopic spurion dynamics, ordered embedding theorem, fixed-point model, finite threshold spectrum, physical16 descent, or calibrated instrument is supplied",
    "next_source_gate": "derive a unique positive coefficient ray (a:b), the ordered embedding, and g_* from one independently required anomaly-free source theory",
    "remaining_physical_gate": "derive threshold support and a calibrated physical16 response from the same source-defined experiment",
}
(ROOT / "results" / "wp749_single_spurion_correlated_higgsing_acceptance.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
