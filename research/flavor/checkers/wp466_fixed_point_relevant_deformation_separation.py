import json
from pathlib import Path

import sympy as sp


g, mu, v, c_u, c_d, s = sp.symbols("g mu v c_u c_d s", positive=True)
f = sp.sqrt(6) * mu
target = sp.simplify(g * f / v)

messenger_ratios = (sp.simplify(c_u * mu / mu), sp.simplify(c_d * mu / mu))
dilated_target = sp.simplify(target.subs(mu, s * mu))
dilated_ratios = (
    sp.simplify((s * c_u * mu) / (s * mu)),
    sp.simplify((s * c_d * mu) / (s * mu)),
)

hostile_one = sp.simplify(dilated_target.subs(s, 1))
hostile_two = sp.simplify(dilated_target.subs(s, 2))

assert messenger_ratios == (c_u, c_d)
assert dilated_ratios == messenger_ratios
assert sp.simplify(dilated_target / target) == s
assert sp.simplify(hostile_two / hostile_one) == 2
assert sp.simplify(hostile_two - hostile_one) != 0

result = {
    "work_package": "WP466",
    "granted_premise": "a unique complete dimensionless gauge-Yukawa-quartic fixed point",
    "fixed_vacuum_relation": "f=sqrt(6)*mu",
    "target": str(target),
    "dilation": {
        "mu": "s*mu",
        "M_U": "s*c_u*mu",
        "M_D": "s*c_d*mu",
        "preserved_threshold_ratios": [str(x) for x in dilated_ratios],
        "target_multiplier": str(sp.simplify(dilated_target / target)),
    },
    "hostile_pair": {
        "scale_factors": [1, 2],
        "target_values": [str(hostile_one), str(hostile_two)],
        "ratio": str(sp.simplify(hostile_two / hostile_one)),
    },
    "classification": "dimensionless fixed point may select g_F but cannot select g_F*f/v without a relevant common-clock constructor",
    "selector_admitted_for_target": sp.simplify(hostile_two - hostile_one) == 0,
    "smallest_exact_falsifier": "common flavor-scale dilation by two preserves all dimensionless fixed-point data and doubles g_F*f/v",
}

out = Path(__file__).parents[1] / "results" / "wp466_fixed_point_relevant_deformation_separation.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

