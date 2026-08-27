"""Exact audit of a massive-vector D-term portal constructor."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
wp766 = json.loads(
    (ROOT / "results" / "wp766_holomorphy_protects_wrong_operator_class.json").read_text(
        encoding="utf-8"
    )
)

g, q_n, q_x, q_phi, v, c_k = sp.symbols(
    "g q_n q_x q_phi v c_K", nonzero=True, real=True
)
n2, x2 = sp.symbols("n2 x2", real=True)

# K(V)=M_V^2 V^2/2 + J V. Eliminating the auxiliary heavy vector gives
# K_eff=-J^2/(2 M_V^2).
J = 2 * g * (q_n * n2 + q_x * x2)
M2 = 2 * g**2 * q_phi**2 * v**2
K_eff = sp.expand(-J**2 / (2 * M2))
portal = sp.expand(K_eff).coeff(n2 * x2)
expected = -2 * q_n * q_x / (q_phi**2 * v**2)

portal_v1 = sp.simplify(portal.subs({q_n: 1, q_x: 1, q_phi: 1, v: 1}))
portal_v2 = sp.simplify(portal.subs({q_n: 1, q_x: 1, q_phi: 1, v: 2}))
completed = sp.simplify(portal + c_k)
cancel_boundary = sp.solve(sp.Eq(completed, 0), c_k)[0]

checks = {
    "wp766_dependency_passed": wp766["status"] == "PASS" and all(wp766["checks"].values()),
    "heavy_vector_elimination_is_exactly_quadratic": sp.simplify(K_eff + J**2 / (2 * M2)) == 0,
    "tree_portal_is_fixed_by_current_exchange": sp.simplify(portal - expected) == 0,
    "gauge_coupling_cancels_against_higgsed_mass": not portal.has(g),
    "equal_sign_charges_fix_negative_sign": portal_v1 < 0,
    "opposite_sign_charges_fix_positive_sign": sp.simplify(portal.subs({q_n: 1, q_x: -1, q_phi: 1, v: 1})) > 0,
    "higgs_scale_remains_in_portal": portal.has(v),
    "hostile_scale_pair_changes_magnitude": sp.simplify(portal_v1 - portal_v2) != 0,
    "hostile_scale_pair_has_factor_four": sp.simplify(portal_v1 / portal_v2) == 4,
    "allowed_Kahler_boundary_can_cancel_exchange": sp.simplify(completed.subs(c_k, cancel_boundary)) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP767",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP766",
    "admitted_state_domain": "two light N=1 current multiplets coupled to one source-defined Higgsed Abelian vector multiplet, with a positive vector mass and the symmetry-allowed Kahler completion",
    "faithful_coordinate": "the charge product q_n q_x, Higgs charge q_phi, Higgs scale v, and additive renormalized Kahler boundary c_K",
    "source_authorized_operation": "classical elimination of the unique massive vector current channel K(V)=M_V^2 V^2/2+JV",
    "tree_level_portal": "-2 q_n q_x/(q_phi^2 v^2)",
    "classification": "the current constructor fixes the tree-level sign once charge orientation is fixed and cancels the gauge coupling, but it leaves a continuous Higgs-scale fiber and an additive Kahler threshold fiber",
    "smallest_scale_falsifier": "at identical unit charges, v=1 gives -2 while v=2 gives -1/2",
    "smallest_threshold_falsifier": "c_K=2 q_n q_x/(q_phi^2 v^2) cancels the current-exchange portal",
    "deutschian_status": "hardens the sign explanation but not the magnitude, RG basin, threshold survival, or readout",
    "next_source_gate": "derive a quantized or dynamically isolated Higgs scale and a D-term Ward identity that forbids independent Kahler completion, then compose with a calibrated physical16 instrument",
    "instrument_gate": "the current exchange is a source operation, not yet a detector-calibrated flavor probe",
}
(ROOT / "results" / "wp767_massive_vector_current_exchange_scale_fiber.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
