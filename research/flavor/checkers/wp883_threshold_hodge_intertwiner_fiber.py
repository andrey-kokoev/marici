import json
from pathlib import Path

import sympy as sp


H = sp.diag(-1, 1)
J = sp.Matrix([[0, -1], [1, 0]])
a, b, c, d, eta = sp.symbols("a b c d eta", real=True)
M = sp.Matrix([[a, b], [c, d]])

# Linear intertwiner spaces before orthogonality.
h_equations = list(M * H - H * M)
hodge_equations = h_equations + list(M * J - J * M)
h_solution = sp.linsolve(h_equations, (a, b, c, d))
hodge_solution = sp.linsolve(hodge_equations, (a, b, c, d))

Mp = sp.eye(2)
Mm = -sp.eye(2)
g = sp.symbols("g", nonzero=True, real=True)
G = g * H

tests = {
    "H_only_linear_commutant_is_diagonal": h_solution == {(a, 0, 0, d)},
    "H_only_orthogonal_fiber_has_four_signs": all((sp.diag(x, y).T * sp.diag(x, y) == sp.eye(2)) for x in (-1, 1) for y in (-1, 1)),
    "Hodge_linear_commutant_is_scalar": hodge_solution == {(d, 0, 0, d)},
    "Hodge_orthogonal_fiber_has_two_signs": Mp.T * Mp == sp.eye(2) and Mm.T * Mm == sp.eye(2),
    "positive_lift_intertwines_H": Mp * H == H * Mp,
    "negative_lift_intertwines_H": Mm * H == H * Mm,
    "positive_lift_intertwines_J": Mp * J == J * Mp,
    "negative_lift_intertwines_J": Mm * J == J * Mm,
    "central_lifts_have_same_H_conjugation": Mp * H * Mp.inv() == Mm * H * Mm.inv(),
    "central_lifts_have_same_G_conjugation": Mp * G * Mp.inv() == Mm * G * Mm.inv(),
    "eta_two_doubles_strength": sp.simplify((eta * G).subs(eta, 2) - 2 * (eta * G).subs(eta, 1)) == sp.zeros(2),
    "eta_two_quadruples_intensity": sp.simplify((eta**2).subs(eta, 2) / (eta**2).subs(eta, 1) - 4) == 0,
}

passed = sum(bool(v) for v in tests.values())
result = {
    "work_package": "WP883",
    "status": "PASS" if passed == len(tests) else "FAIL",
    "summary": {"passed": passed, "total": len(tests), "all_passed": passed == len(tests)},
    "classification": "rigidifier_not_selector: Hodge matching fixes adjoint transport while leaving a central lift and continuous gain-jump fiber",
    "H_only_orthogonal_fiber_size": 4,
    "H_and_J_orthogonal_fiber_size": 2,
    "adjoint_visible_lift_fiber_size": 1,
    "portal_gain_jump_dimension": 1,
    "matching_family": "M=sigma R_plus R_minus^T, sigma in {+1,-1}",
    "smallest_falsifiers": ["M versus -M", "eta=1 versus eta=2"],
    "remaining_gate": "completion-specific finite threshold action and, for lift sign, a declared relational reference experiment",
    "tests": tests,
}

output = Path(__file__).parents[1] / "results" / "wp883_threshold_hodge_intertwiner_fiber.json"
output.write_text(json.dumps(result, indent=2, default=bool) + "\n", encoding="utf-8")
print(json.dumps(result["summary"], indent=2))
raise SystemExit(0 if result["status"] == "PASS" else 1)
