"""Exact one-loop invariant support for the exit-flavon Higgs portal."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
h, x = sp.symbols("h x", real=True)
yq, yX, MB = sp.symbols("y_q y_X M_B", real=True)

# Rows (q_L,B_L), columns (q_R,B_R). The two source-authorized vertices share
# q_R: ordinary q_L-H-q_R and messenger B_L-X-q_R.
M = sp.Matrix([[yq*h, 0], [yX*x, MB]])
K = sp.expand(sp.trace((M*M.T)**2))
mixed = sp.expand(K).coeff(h, 2).coeff(x, 2)

# Deleting either source edge removes the additive portal support.
checks = {
    "fermion_invariant_contains_mixed_quartic": mixed == 2*yq**2*yX**2,
    "ordinary_yukawa_is_required": mixed.subs(yq, 0) == 0,
    "exit_yukawa_is_required": mixed.subs(yX, 0) == 0,
    "messenger_mass_does_not_create_the_mixed_coefficient": sp.diff(mixed, MB) == 0,
    "three_colors_preserve_nonzero_support": sp.simplify(3*mixed-6*yq**2*yX**2) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP686",
    "status": "PASS",
    "checks": checks,
    "source_vertices": ["q_L-H-q_R Standard Model Yukawa", "B_L-X-q_R exit Yukawa"],
    "one_loop_invariant": "Tr[(M M^dagger)^2]",
    "mixed_coefficient_per_color": "2 y_q^2 y_X^2 h^2 x^2",
    "renormalization_result": "the H^dag H times X dot X counterterm is required; lambda_p=0 is not an RG-invariant truncation when y_q y_X is nonzero",
    "selection_limit": "running generates portal support generically but does not select its renormalized numerical value; a boundary counterterm can cancel it at one chosen scale",
    "classification": "source-generated operator support and radiative rigidification, not numerical flavor selection",
    "smallest_exact_falsifier": "y_q=0 or y_X=0 deletes the mixed invariant",
    "remaining_gate": "derive the full one-scheme beta coefficient and finite threshold matching, then prove a nonzero uncertainty-stable portal at the experimental scale",
}
(ROOT / "results" / "wp686_radiative_exit_higgs_portal.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
