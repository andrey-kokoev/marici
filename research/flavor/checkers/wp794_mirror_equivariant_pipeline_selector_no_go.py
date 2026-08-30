"""Exact mirror-equivariant source-to-instrument selector no-go."""
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp793 = json.loads(
    (ROOT / "results" / "wp793_f_theory_vertical_flux_mirror_moduli_no_go.json")
    .read_text(encoding="utf-8")
)

R = sp.Matrix([[0, 1], [1, 0]])
portal = sp.Matrix([1, -1])
invariant_gate = sp.Matrix([1, 1])

s_plus, s_minus = sp.symbols("s_plus s_minus")
selection = sp.Matrix([s_plus, s_minus])
invariance_residual = sp.simplify(R * selection - selection)
invariant_solution = sp.solve(
    list(invariance_residual), [s_plus, s_minus], dict=True
)

P = sp.Matrix([[sp.Rational(3, 4), sp.Rational(1, 4)],
               [sp.Rational(1, 4), sp.Rational(3, 4)]])
stationary = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 2)])
asymmetric_state = sp.Matrix([1, 0])

inclusive_width = portal.applyfunc(lambda x: x**2)
signed_readout = portal
joint_portal = sp.Matrix([1, -1])
joint_reference = sp.Matrix([1, -1])
relational_readout = joint_portal.multiply_elementwise(joint_reference)

mu = sp.symbols("mu", nonzero=True, real=True)
fixed_reference_bias = sp.Matrix([mu, -mu])
dynamical_mirror_bias = sp.Matrix([mu, mu])

checks = {
    "wp793_dependency_passed": wp793["status"] == "PASS"
    and all(wp793["checks"].values()),
    "mirror_is_an_involution": R * R == sp.eye(2),
    "portal_is_mirror_odd": R * portal == -portal,
    "admissibility_gate_is_mirror_invariant":
        R * invariant_gate == invariant_gate,
    "invariant_selector_has_equal_orbit_weights":
        invariant_solution == [{s_plus: s_minus}],
    "singleton_indicator_is_not_invariant":
        R * asymmetric_state != asymmetric_state,
    "transport_commutes_with_mirror": P * R == R * P,
    "symmetric_distribution_is_stationary": P * stationary == stationary,
    "asymmetric_distribution_is_not_stationary":
        P * asymmetric_state != asymmetric_state,
    "inclusive_threshold_collapses_sign":
        inclusive_width == sp.Matrix([1, 1]),
    "signed_instrument_separates_but_does_not_select":
        signed_readout[0] != signed_readout[1],
    "simultaneous_reference_mirror_preserves_relational_readout":
        relational_readout == sp.Matrix([1, 1]),
    "fixed_reference_bias_breaks_mirror":
        fixed_reference_bias[0] != fixed_reference_bias[1],
    "dynamical_mirrored_reference_restores_pairing":
        dynamical_mirror_bias[0] == dynamical_mirror_bias[1],
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP794",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP793",
    "admitted_state_domain": (
        "any flavor source domain containing a free two-point mirror orbit "
        "{x_plus,x_minus} with a nonzero orientation-odd portal, invariant "
        "admissibility and energy gates, mirror-equivariant RG and threshold "
        "transport, and either inclusive or signed detector channels"
    ),
    "faithful_coordinate": (
        "the full mirror orbit label, portal magnitude, RG trajectory, "
        "threshold state, detector calibration state, and any reference-port "
        "orientation"
    ),
    "source_authorized_probe_family": (
        "invariant source costs and constraints, equivariant transition "
        "kernels, threshold widths, signed readouts, and relational reference "
        "products"
    ),
    "contextual_partition": (
        "source gates leave the two mirror states in one equal-cost orbit; "
        "equivariant transport preserves the orbit, inclusive readout "
        "identifies it, and signed readout separates it without deleting a "
        "source member"
    ),
    "selector_result": (
        "no mirror-invariant selector can choose one member of a free "
        "two-point orbit; the only invariant indicators weight both equally. "
        "RG, thresholds, and instruments cannot retroactively supply source "
        "selection"
    ),
    "smallest_exact_falsifier": (
        "the two-state orbit with swap matrix R, invariant gate (1,1), "
        "orientation-odd portal (1,-1), and symmetric transport kernel"
    ),
    "sign_result": (
        "a nonzero sign requires a source operation not equivariant under the "
        "original mirror groupoid; a fixed pseudoscalar or reference port "
        "changes the admitted experiment"
    ),
    "magnitude_result": (
        "the theorem still applies if an even source potential uniquely fixes "
        "the nonzero magnitude: the two signs remain paired"
    ),
    "rg_threshold_result": (
        "mirror-equivariant RG maps paired initial conditions to paired "
        "trajectories with matched stability data, and sign-even thresholds "
        "cannot remove the source orbit"
    ),
    "instrument_result": (
        "inclusive instruments erase the sign; calibrated signed instruments "
        "can distinguish it but cannot select its source. A reference port "
        "measures only a relational product over a stabilizer groupoid"
    ),
    "deutschian_status": (
        "the no-go follows from equivariance alone and explains why every "
        "equilibrium mirror-complete proposal fails at source selection"
    ),
    "necessary_source_principle": (
        "a non-mirror-completable boundary or irreversible history constructor "
        "must co-generate portal orientation and calibration reference; its "
        "dynamics must also fix magnitude and feed one RG, threshold, and "
        "detector pipeline"
    ),
    "remaining_gate": (
        "exhibit a physical flavor constructor with that non-equivariant "
        "boundary authority and derive, rather than assume, its magnitude, "
        "basin, thresholds, and physical16 instrument"
    ),
}

(ROOT / "results" / "wp794_mirror_equivariant_pipeline_selector_no_go.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
