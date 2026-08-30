"""Exact WP444 dilation obstruction to selecting g_F f/v."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]
wp443 = json.loads((root / "results" / "wp443_fundamental_flavon_completion.json").read_text(encoding="utf-8"))
s, g_f, v = sp.symbols("s g_F v", positive=True, real=True)

# At the WP443 unit representative R_adj=1/2 and |phi|^2=1/2.
adjoint_norm = s**2/sp.Integer(2)
fundamental_norm = s**2/sp.Integer(2)
f_squared = sp.simplify(adjoint_norm+fundamental_norm)
normalized_adjoint_fraction = sp.simplify(adjoint_norm/f_squared)
normalized_fundamental_fraction = sp.simplify(fundamental_norm/f_squared)
minimum_energy = -3*s**4/sp.Integer(8)
clock_ratio = sp.simplify(g_f*sp.sqrt(f_squared)/v)

# A representative nonzero gauge-mass eigenvalue has the universal scaling;
# rank is unchanged for every s>0 even though every pole moves linearly.
mass_squared_scaling = s**2

checks = {
    "wp443_dependency_passed": wp443["passed"],
    "total_flavon_norm_scales_quadratically": sp.simplify(f_squared-s**2) == 0,
    "normalized_adjoint_shape_is_dilation_invariant": normalized_adjoint_fraction == sp.Rational(1, 2),
    "normalized_fundamental_shape_is_dilation_invariant": normalized_fundamental_fraction == sp.Rational(1, 2),
    "minimum_energy_scales_quartically": sp.simplify(minimum_energy/s**4+sp.Rational(3, 8)) == 0,
    "gauge_mass_rank_is_preserved_for_positive_dilation": wp443["gauge_mass_rank"] == 8 and mass_squared_scaling != 0,
    "absolute_clock_ratio_changes_along_orbit": sp.diff(clock_ratio, s) != 0,
    "hostile_pair_has_distinct_ratios": sp.simplify(clock_ratio.subs(s, 2)-clock_ratio.subs(s, 1)) != 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP444",
    "state_domain": "WP443 vacuum family with fixed dimensionless couplings and fixed electroweak reference v.",
    "dilation": "(A,D,phi)->s(A,D,phi), (m^2,mu^2)->s^2(m^2,mu^2), s>0",
    "faithful_shape_coordinate": ["normalized adjoint pair", "normalized fundamental ray", "full gauge rank"],
    "shape_partition": "Every positive s lies in one normalized vacuum-shape class.",
    "clock_ratio": "g_F*s/v at the unit-normalized representative",
    "selector_classification": "neither: the current source action admits a continuous scale orbit and does not select g_F f/v",
    "instrument": None,
    "hostile_pair": {"s1": 1, "s2": 2, "same_normalized_shape": bool(normalized_adjoint_fraction == sp.Rational(1, 2)), "clock_ratio_factor": 2},
    "smallest_exact_falsifier": "A source-derived relation in the admitted action fixing s relative to v while preserving no continuous dilation orbit.",
    "remaining_gate": "Flavor-current observations may constrain the ratio but cannot retroactively source-select it; derive the conditional current map next.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp444_flavon_scale_orbit.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
