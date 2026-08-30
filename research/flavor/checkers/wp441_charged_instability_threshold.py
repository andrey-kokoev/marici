"""Exact WP441 threshold for loss of stability of the WP438 vacuum."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]
wp440 = json.loads((root / "results" / "wp440_charged_bifurcation_preregistration.json").read_text(encoding="utf-8"))

m2, lam, eta, rho = sp.symbols("m_squared lambda eta rho", positive=True, real=True)
charged_physical_eigenvalue = sp.factor(m2 * (3*lam-eta) / (2*rho-lam))
threshold = 3*lam
coercive_margin = rho-lam/2-eta

stable_point = {m2: 1, lam: 1, eta: 2, rho: 4}
unstable_point = {m2: 1, lam: 1, eta: 4, rho: 5}
threshold_point = {m2: 1, lam: 1, eta: 3, rho: 4}

checks = {
    "frozen_wp440_dependency_passed": wp440["passed"],
    "stable_hostile_point_is_inside_coercive_domain": coercive_margin.subs(stable_point) > 0,
    "stable_hostile_point_has_positive_charged_mode": charged_physical_eigenvalue.subs(stable_point) > 0,
    "unstable_hostile_point_is_inside_coercive_domain": coercive_margin.subs(unstable_point) > 0,
    "unstable_hostile_point_has_negative_charged_mode": charged_physical_eigenvalue.subs(unstable_point) < 0,
    "threshold_point_has_exact_zero_mode": charged_physical_eigenvalue.subs(threshold_point) == 0,
    "instability_region_is_open": (eta-threshold).subs(unstable_point) > 0 and coercive_margin.subs(unstable_point) > 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP441",
    "charged_block_spectrum": {"0": 4, str(charged_physical_eigenvalue): 4},
    "bifurcation_threshold": "eta=3*lambda",
    "stable_side": "eta<3*lambda",
    "unstable_side": "eta>3*lambda",
    "intersection_with_frozen_domain": "eta>3*lambda and rho>lambda/2+eta is a nonempty open region",
    "smallest_exact_falsifier": "At (m^2,lambda,eta,rho)=(1,1,4,5), the charged eigenvalue is +1/9 or the coercivity margin is nonpositive.",
    "remaining_gate": "Follow the departing branch without assuming its stabilizer; WP442 supplies the negative global disposition.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp441_charged_instability_threshold.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
