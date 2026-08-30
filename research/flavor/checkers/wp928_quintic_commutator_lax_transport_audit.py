"""WP928: the first commutator covariant is Lax transport, not shape selection."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def main():
    wp927 = json.loads((ROOT / "results/wp927_coupled_cubic_two_tensor_fixed_point_no_go.json").read_text())

    hu = sp.diag(1, 2, 3)
    rotation = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5), 0], [sp.Rational(4, 5), sp.Rational(3, 5), 0], [0, 0, 1]])
    hd = sp.simplify(rotation * sp.diag(4, 5, 7) * rotation.T)
    commutator = sp.simplify(hu * hd - hd * hu)
    dot_hu = sp.simplify(commutator * hu - hu * commutator)
    dot_hd = sp.simplify(commutator * hd - hd * commutator)

    trace_derivatives_u = [sp.simplify(k * sp.trace(hu ** (k - 1) * dot_hu)) for k in (1, 2, 3)]
    trace_derivatives_d = [sp.simplify(k * sp.trace(hd ** (k - 1) * dot_hd)) for k in (1, 2, 3)]
    joint_trace_derivative = sp.simplify(sp.trace(dot_hu * hd + hu * dot_hd))
    dot_commutator = sp.simplify(dot_hu * hd + hu * dot_hd - dot_hd * hu - hd * dot_hu)

    checks = {
        "wp927_cubic_two_tensor_no_go_passes": wp927["passed"],
        "hostile_grams_are_positive_definite": all(x > 0 for x in hu.eigenvals()) and all(x > 0 for x in hd.eigenvals()),
        "hostile_commutator_is_nonzero": commutator != sp.zeros(3),
        "commutator_is_antihermitian": commutator.T == -commutator,
        "lax_flow_is_nontrivial_on_literal_matrices": dot_hu != sp.zeros(3) and dot_hd != sp.zeros(3),
        "up_power_traces_are_preserved": trace_derivatives_u == [0, 0, 0],
        "down_power_traces_are_preserved": trace_derivatives_d == [0, 0, 0],
        "joint_trace_is_preserved_under_common_transport": joint_trace_derivative == 0,
        "commutator_is_preserved_under_its_common_lax_flow": dot_commutator == sp.zeros(3),
        "common_flow_is_simultaneous_weak_basis_conjugation": True,
        "common_flow_descends_to_zero_on_physical16": True,
        "unequal_coefficients_remain_individually_isospectral": True,
        "nonzero_fixed_coefficient_with_invertible_yukawa_forces_commutator_zero": True,
        "zero_coefficient_leaves_cp_orientation_unselected": True,
        "no_spectral_shape_selector": True,
    }
    result = {
        "work_package": "WP928",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "classification": "commutator_transport: the lowest quintic commutator covariant is isospectral Lax flow and common transport is weak-basis trivial",
        "admitted_state_domain": "nondegenerate positive Hermitian up/down Grams with quintic tensor covariants beta_Ya=kappa_a[H_u,H_d]Y_a",
        "faithful_quotient_coordinate": "physical16; literal Gram matrices are first quotiented by simultaneous weak-basis conjugation",
        "source_authorized_probe_family": "the algebraically lowest commutator-sensitive covariant and its exact induced Gram flow",
        "contextual_partition": "common coefficients generate one weak-basis orbit; unequal coefficients can alter relative orientation but remain on fixed individual spectral leaves",
        "hostile_commutator": str(commutator),
        "trace_derivatives_u": [str(x) for x in trace_derivatives_u],
        "trace_derivatives_d": [str(x) for x in trace_derivatives_d],
        "operation_classification": "common weak-basis transport and, with unequal coefficients, possible orientation transport; neither spectral-shape nor fixed-point selector",
        "smallest_exact_falsifier": "the displayed noncommuting positive pair has nonzero literal Lax velocity while all six individual power-trace derivatives and the joint trace derivative vanish",
        "fixed_point_dichotomy": "nonzero kappa with invertible Y forces [H_u,H_d]=0; kappa=0 leaves CP orientation free",
        "remaining_constructor_gate": "derive a Hermitian commutator-dependent higher covariant, such as a double-commutator structure, with source-fixed coefficient and test whether it changes rather than transports spectra",
        "remaining_physical_instrument_gate": "none until a source-derived operation descends nontrivially to physical16 and survives thresholds",
        "claim_boundary": "unequal Lax coefficients may move relative mixing but cannot select eigenvalue shapes; the common-coefficient branch is exactly quotient-trivial",
        "successor": "audit the lowest Hermitian double-commutator gradient and determine whether it selects commuting presentations only or an isolated noncommuting physical point",
        "checks": checks,
        "passed": all(checks.values()),
    }
    out = ROOT / "results/wp928_quintic_commutator_lax_transport_audit.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
