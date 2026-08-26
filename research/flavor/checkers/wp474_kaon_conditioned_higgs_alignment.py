import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
wp461 = json.loads((root / "results" / "wp461_kaon_conditioned_pole_width_reach.json").read_text(encoding="utf-8"))
wp473 = json.loads((root / "results" / "wp473_dilation_residue_sum_rule.json").read_text(encoding="utf-8"))

v_tev = sp.Rational(12311, 50000)
f_min_tev = sp.sympify(wp461["conditional_working_limits"]["f_min_TeV"])
a_current_max = sp.simplify(3 * (v_tev / f_min_tev) ** 2)
a_rate_max = sp.Rational(242, 2379)
rate_lower = sp.Rational(2379, 2500)

dilation_higgs_max = sp.simplify(a_current_max / (a_current_max + 2))
orthogonal_budget_min = sp.simplify(2 / (a_current_max + 2))
f_over_v_min = sp.simplify(f_min_tev / v_tev)
benchmark_target = sp.sympify(wp461["conditional_working_limits"]["g_F_f_over_v_benchmark"])

checks = {
    "wp461_dependency_passed": wp461["passed"],
    "wp473_dependency_passed": wp473["passed"],
    "current_a_ceiling_is_positive": a_current_max > 0,
    "current_a_ceiling_satisfies_rate_gate": a_current_max < a_rate_max,
    "dilation_higgs_residue_is_below_one_part_in_10_9": dilation_higgs_max < sp.Rational(1, 10**9),
    "orthogonal_budget_exceeds_rate_lower_edge": orthogonal_budget_min > rate_lower,
    "benchmark_target_remains_wp461_readout": benchmark_target == 2500 * sp.sqrt(6) / 123,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP474",
    "inherited_domain": "WP461 provisional kaon likelihood, threshold envelope, and 5-TeV vector-pole benchmark",
    "v_TeV": str(v_tev),
    "f_min_TeV": str(f_min_tev),
    "f_over_v_min": {"exact": str(f_over_v_min), "numeric": float(sp.N(f_over_v_min, 16))},
    "a_current_ceiling": {"exact": str(a_current_max), "numeric": float(sp.N(a_current_max, 16))},
    "a_rate_ceiling": str(a_rate_max),
    "maximum_dilation_higgs_residue": {
        "exact": str(dilation_higgs_max),
        "numeric": float(sp.N(dilation_higgs_max, 16)),
    },
    "minimum_orthogonal_higgs_budget": {
        "exact": str(orthogonal_budget_min),
        "numeric": float(sp.N(orthogonal_budget_min, 16)),
    },
    "benchmark_g_F_f_over_v": str(benchmark_target),
    "classification": "conditional flavor-current constraint drives the common-clock geometry into the Higgs-rate-compatible cone; no numerical source selection",
    "remaining_gate": "recompute hierarchical scalar poles and residues, calibrate or derive eta independently, and freeze all widths in the same threshold domain",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp474_kaon_conditioned_higgs_alignment.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
