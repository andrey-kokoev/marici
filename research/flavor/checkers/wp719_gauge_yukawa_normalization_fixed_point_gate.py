"""Exact RG gate for gauge-Yukawa normalization of a Clebsch portal Gram."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
g, g0, t = sp.symbols("g g_0 t", positive=True)
b, b0, b1 = sp.symbols("b b_0 b_1", nonzero=True)
Cn, Cm = sp.symbols("C_n C_m", positive=True)

pn = g**2*Cn
pm = g**2*Cm
contrast = sp.factor(pn-pm)
beta_g_1 = b*g**3
beta_pn_1 = sp.factor(sp.diff(pn, g)*beta_g_1)
g2_solution = sp.factor(g0**2/(1-2*b*g0**2*t))
solution_residual = sp.factor(sp.diff(g2_solution, t)-2*b*g2_solution**2)

beta_g_2 = sp.factor(g**3*(b0+b1*g**2))
gstar2 = sp.factor(-b0/b1)
nonzero_fixed_residual = sp.factor((b0+b1*gstar2))
fixed_portal_contrast = sp.factor(gstar2*(Cn-Cm))
critical_exponent = sp.factor(sp.diff(beta_g_2, g).subs(g**2, gstar2))

g0a, g0b = sp.symbols("g_0a g_0b", positive=True)
flow_a = g0a**2/(1-2*b*g0a**2*t)
flow_b = g0b**2/(1-2*b*g0b**2*t)
hostile_boundary_difference = sp.factor(flow_a-flow_b)

checks = {
    "gauge_yukawa_relation_fixes_portal_ratio": sp.simplify(pn/pm-Cn/Cm) == 0,
    "clebsch_order_fixes_contrast_sign_conditionally": sp.simplify(contrast-g**2*(Cn-Cm)) == 0,
    "one_loop_flow_preserves_projective_ratio": sp.simplify(beta_pn_1/pn-2*b*g**2) == 0,
    "one_loop_solution_is_exact": solution_residual == 0,
    "one_loop_nonzero_fixed_point_is_absent": sp.solve(sp.Eq(beta_g_1, 0), g) == [],
    "distinct_boundary_values_remain_distinct_generically": hostile_boundary_difference != 0,
    "two_loop_nonzero_fixed_point_condition": nonzero_fixed_residual == 0,
    "two_loop_fixed_magnitude_and_exponent": fixed_portal_contrast == b0*(Cm-Cn)/b1 and critical_exponent == 2*b0**2/b1,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP719",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "representation-fixed Clebsch portal with gauge-Yukawa relation p_i=g^2 C_i and autonomous gauge running",
    "faithful_coordinate": "Clebsch invariants C_n,C_m plus the physical running gauge normalization g^2",
    "source_operation": "gauge-Yukawa identification of the auxiliary normalization",
    "classification": "fixes portal ratio and conditional contrast sign, but one-loop running does not select a nonzero magnitude",
    "smallest_exact_falsifier": "two distinct boundary values g_0a and g_0b obey the same source relation and remain distinct under the one-loop flow",
    "necessary_progressive_gate": "a source-fixed interacting zero of the completed beta system with the required attractive critical exponent",
    "two_loop_candidate": "g_*^2=-b_0/b_1, requiring opposite beta-coefficient signs and perturbative, scheme-stable completion",
    "remaining_gates": [
        "derive anomaly-free matter that fixes C_n,C_m,b_0,b_1 independently",
        "include every Yukawa and quartic direction and verify the full stability matrix",
        "derive a nondecoupling threshold map preserving the fixed relation",
        "construct representation-labelled calibrated channels whose response is injective on the portal contrast",
    ],
}
(ROOT / "results" / "wp719_gauge_yukawa_normalization_fixed_point_gate.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
