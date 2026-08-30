"""Exact full-grammar and pole-basis audit of the WP676 exchange candidate."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
rt2 = sp.sqrt(2)
swap = sp.Matrix([[0, 1], [1, 0]])
H = sp.Matrix([[1, 1], [1, -1]])/rt2

# Rows are the independently typed entrance and exit source currents; columns
# are the bare A and B messenger fields.
endpoint_incidence = sp.eye(2)
swapped_endpoints = endpoint_incidence*swap

# The balanced frame fluctuation has the same off-diagonal species tensor as
# the vev-induced mixing. In the physical pole basis it is diagonal.
native_n_vertex = swap
pole_n_vertex = sp.simplify(H.T*native_n_vertex*H)
entrance_poles = sp.simplify(H.T*sp.Matrix([1, 0]))
exit_poles = sp.simplify(H.T*sp.Matrix([0, 1]))

checks = {
    "internal_swap_is_exact_involution": swap**2 == sp.eye(2),
    "fixed_external_endpoints_break_swap": swapped_endpoints != endpoint_incidence,
    "endpoint_swap_would_repair_only_by_new_external_automorphism": swap*endpoint_incidence*swap == endpoint_incidence,
    "balanced_pole_transform_is_orthogonal": sp.simplify(H.T*H) == sp.eye(2),
    "frame_fluctuation_is_diagonal_in_pole_basis": pole_n_vertex == sp.diag(1, -1),
    "cross_pole_n_transition_vanishes": pole_n_vertex[0, 1] == 0 and pole_n_vertex[1, 0] == 0,
    "entrance_and_exit_reach_both_poles_with_relative_sign": entrance_poles == sp.Matrix([1, 1])/rt2 and exit_poles == sp.Matrix([1, -1])/rt2,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP681",
    "status": "PASS",
    "checks": checks,
    "full_grammar_result": "A<->B is not a symmetry with the independently typed entrance and exit currents held fixed",
    "repair_requirement": "one must also exchange the external entrance and exit source objects, which is not an admitted flavor automorphism",
    "pole_basis": "P_plus=(A+B)/sqrt(2), P_minus=(A-B)/sqrt(2)",
    "pole_vertex": "the balanced n fluctuation is diag(y,-y), so P_plus<->P_minus+n transitions vanish",
    "cascade_consequence": "the WP674 cross-species cascade cannot be transported into the exact balanced exchange theory",
    "correction_to_wp676": "exchange balance is a conditional internal-block rigidifier/minimizer, not a source-authorized selector of the full constructor",
    "smallest_exact_falsifier": "the endpoint incidence matrix I becomes the column-swapped matrix under A<->B",
    "remaining_gate": "a different source symmetry or an independently admitted external-current exchange constructor would be needed to select balance without closing the analyzer channel",
}
(ROOT / "results" / "wp681_full_grammar_exchange_audit.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
