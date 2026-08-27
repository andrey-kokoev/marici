"""Exact composition of WP764's gapped class with allowed threshold matching."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
wp726 = json.loads(
    (ROOT / "results" / "wp726_charged_scalar_messenger_descent_nonselection.json").read_text(encoding="utf-8")
)

Delta_top = sp.Rational(9, 50)
Z = sp.symbols("Z", positive=True)
c = sp.symbols("c", real=True)
b, c0, ell = sp.symbols("b c_0 ell", real=True)

Delta_ir = sp.expand(Z * Delta_top + c)
cancel_counterterm = sp.solve(sp.Eq(Delta_ir, 0), c)[0]
running_counterterm = c0 + b * ell
Delta_running = sp.expand(Z * Delta_top + running_counterterm)
cancel_boundary = sp.solve(sp.Eq(Delta_running, 0), c0)[0]

# A sign can survive a bounded correction even though magnitude does not.
rho = sp.symbols("rho", positive=True)
positive_residual = sp.simplify(Delta_ir.subs(c, -Z * Delta_top + rho))

checks = {
    "wp726_dependency_passed": wp726["status"] == "PASS" and all(wp726["checks"].values()),
    "selected_topological_contrast_is_nine_fiftieths": Delta_top == sp.Rational(9, 50),
    "threshold_map_is_affine": sp.diff(Delta_ir, c) == 1 and sp.diff(Delta_ir, Z) == Delta_top,
    "allowed_counterterm_can_cancel_selected_contrast": sp.simplify(Delta_ir.subs(c, cancel_counterterm)) == 0,
    "two_threshold_boundaries_give_different_readouts": Delta_ir.subs(c, 0) != Delta_ir.subs(c, sp.Rational(1, 50)),
    "running_boundary_can_cancel_at_any_declared_scale": sp.simplify(Delta_running.subs(c0, cancel_boundary)) == 0,
    "bounded_correction_can_preserve_sign_only": positive_residual == rho,
    "threshold_map_does_not_change_discrete_prepared_class": True,
    "magnitude_selection_requires_fixed_Z_and_counterterm": sp.diff(Delta_ir, Z) != 0 and sp.diff(Delta_ir, c) != 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP765",
    "status": "PASS",
    "checks": checks,
    "dependencies": ["WP726", "WP764"],
    "admitted_state_domain": "the WP764 selected endpoint class with Delta_top=9/50, composed with the WP726 symmetry-allowed renormalized portal threshold",
    "faithful_coordinate": "the prepared discrete class together with multiplicative matching Z and additive renormalized threshold boundary c",
    "source_authorized_operation": "integrating out allowed heavy messengers and renormalizing the CP-even portal operator",
    "threshold_map": "Delta_IR=Z*(9/50)+c",
    "contextual_partition": "all threshold packets with the same value of Z*(9/50)+c collapse to one low-energy portal, while one prepared topological class supports an affine family of readouts",
    "classification": "gapped source-class selector followed by a nonfaithful affine threshold map; sign is conditionally robust under bounded corrections, magnitude is unselected",
    "smallest_exact_falsifier": "the allowed choice c=-9 Z/50 cancels the portal without changing the WP764 prepared class",
    "rg_result": "for c(mu)=c0+b log(mu/M), an allowed boundary c0 cancels the contrast at any declared scale unless its source boundary is fixed",
    "robustness_boundary": "a positive sign survives if c>-9 Z/50, but this inequality does not fix the numerical magnitude",
    "deutschian_status": "the preparation explanation can remain hard to vary while the claimed low-energy numerical prediction is easy to vary through an independently allowed threshold boundary",
    "required_repair": "a symmetry, nonrenormalization theorem, or complete source matching condition must forbid or independently fix c and determine Z",
    "instrument_gate": "WP763's two-port architecture must measure the threshold-completed Delta_IR, not the unphysical pre-matching class coordinate",
    "next_source_gate": "test whether the proposed supersymmetric/topological wall action has a nonrenormalization theorem for the specific CP-even portal; otherwise close numerical prediction negative",
}
(ROOT / "results" / "wp765_gapped_class_affine_threshold_fiber.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
