import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
wp472 = json.loads((root / "results" / "wp472_higgs_rate_width_gate.json").read_text(encoding="utf-8"))

y, a, g = sp.symbols("y a g", positive=True)
L = sp.Rational(2379, 2500)
d = sp.Matrix([sp.sqrt(3) * y, sp.sqrt(2 * a), 1])
norm2 = sp.simplify((d.T * d)[0])
P = sp.simplify(d * d.T / norm2)
dilation_higgs_residue = sp.simplify(P[1, 1])
orthogonal_higgs_budget = sp.simplify(1 - dilation_higgs_residue)

a_max = sp.solve(sp.Eq(orthogonal_higgs_budget, L), a)[0]
target = sp.sqrt(3) * g * y / sp.sqrt(a)
target_lower = sp.simplify(target.subs(a, a_max))
unit_ceiling = sp.simplify(orthogonal_higgs_budget.subs({a: 1, y: 1}))
unit_target_lower = sp.simplify(target_lower.subs(y, 1))

checks = {
    "wp472_dependency_passed": wp472["passed"],
    "dilation_projector_is_idempotent": sp.simplify(P * P - P) == sp.zeros(3),
    "dilation_higgs_residue_formula": dilation_higgs_residue == 2 * a / (3 * y**2 + 2 * a + 1),
    "orthogonal_budget_formula": orthogonal_higgs_budget == (3 * y**2 + 1) / (3 * y**2 + 2 * a + 1),
    "unit_geometry_ceiling_is_two_thirds": unit_ceiling == sp.Rational(2, 3),
    "unit_geometry_fails_rate_lower_edge": unit_ceiling < L,
    "escape_boundary_for_a_is_exact": a_max == 121 * (3 * y**2 + 1) / 4758,
    "unit_target_lower_bound_is_exact": unit_target_lower == g * sp.sqrt(sp.Rational(7137, 242)),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP473",
    "dilation_norm_squared": str(norm2),
    "dilation_higgs_residue": str(dilation_higgs_residue),
    "maximum_single_orthogonal_higgs_residue": str(orthogonal_higgs_budget),
    "unit_geometry_ceiling": str(unit_ceiling),
    "rate_working_lower_edge": str(L),
    "escape_condition": {"a_max": str(a_max)},
    "conditional_target_lower_bound": str(target_lower),
    "unit_y_target_lower_bound": {
        "exact": str(unit_target_lower),
        "coefficient_over_g": float(sp.N(unit_target_lower / g, 16)),
    },
    "classification": "projector-completeness no-go for unit geometry and exact rate-induced constraint on the selector family",
    "remaining_gate": "source-select an allowed coefficient ray or derive a new production channel, then recompute the full spectral and width packet",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp473_dilation_residue_sum_rule.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)

