"""Exact WP606 audit of reverse construction from physical16 to a relative channel."""

import json
from pathlib import Path

import sympy as sp


g_phi, g_psi, mass, kappa, visibility, background = sp.symbols(
    "g_phi g_psi M kappa nu B", real=True
)

gamma_phi = g_phi**2
gamma_psi = g_psi**2
relative_arc = g_phi * g_psi
j16 = -kappa * relative_arc / mass**2

record_plus = background + gamma_phi + gamma_psi + 2 * visibility * relative_arc
record_minus = background + gamma_phi + gamma_psi - 2 * visibility * relative_arc

port_sum = sp.simplify((record_plus + record_minus) / 2)
port_difference = sp.simplify((record_plus - record_minus) / (4 * visibility))

# Same calibrated boundary record and relative arc, but different norm channels.
source_a = {g_phi: 1, g_psi: 1, mass: 1, kappa: 1}
source_b = {g_phi: 2, g_psi: sp.Rational(1, 2), mass: 1, kappa: 1}

# Same boundary record, but different arcs when the portal normalization is not fixed.
calibration_a = {g_phi: 1, g_psi: 1, mass: 1, kappa: 1}
calibration_b = {g_phi: 1, g_psi: sp.Rational(1, 2), mass: 1, kappa: 2}

# The WP558 linear hostile direction: low-energy record fixed, threshold norm changes.
linear_map = sp.Matrix([[1, 1, 1]])
threshold_metric = sp.eye(3)
kernel_direction = sp.Matrix([1, -1, 0])

checks = {
    "phase_flipped_average_erases_arc": port_sum
    == background + gamma_phi + gamma_psi,
    "phase_flipped_difference_recovers_arc_conditionally": port_difference
    == relative_arc,
    "zero_visibility_erases_port_difference": sp.simplify(
        (record_plus - record_minus).subs(visibility, 0)
    )
    == 0,
    "same_j16_for_norm_hostile_pair": sp.simplify(
        j16.subs(source_a) - j16.subs(source_b)
    )
    == 0,
    "norm_hostile_pair_has_different_width_packets": (
        gamma_phi.subs(source_a), gamma_psi.subs(source_a)
    )
    != (gamma_phi.subs(source_b), gamma_psi.subs(source_b)),
    "same_j16_for_calibration_hostile_pair": sp.simplify(
        j16.subs(calibration_a) - j16.subs(calibration_b)
    )
    == 0,
    "calibration_hostile_pair_has_different_arcs": sp.simplify(
        relative_arc.subs(calibration_a) - relative_arc.subs(calibration_b)
    )
    != 0,
    "wp558_direction_is_in_low_energy_kernel": linear_map * kernel_direction
    == sp.zeros(1, 1),
    "wp558_direction_changes_threshold_norm": (
        kernel_direction.T * threshold_metric * kernel_direction
    )[0]
    == 2,
    "source_reachability_holds_identically": sp.simplify(
        relative_arc**2 - gamma_phi * gamma_psi
    )
    == 0,
}

if not all(checks.values()):
    raise SystemExit(f"WP606 check failed: {checks}")

result = {
    "work_package": "WP606",
    "status": "PASS",
    "checks": {key: bool(value) for key, value in checks.items()},
    "admitted_state_domain": "reachable real one-mediator coupling packets with separately supplied mass, portal calibration, coherent detector visibility, and background",
    "faithful_quotient_coordinate": "physical16; the audited boundary component is J16=-kappa*I/M^2",
    "source_authorized_probe_family": [
        "sector norms Gamma_phi and Gamma_psi",
        "two phase-flipped shared-channel records R_plus and R_minus",
    ],
    "contextual_partition": "R_plus and R_minus recover I only conditional on one shared coherent final state and independently calibrated nonzero visibility; J16 alone has larger fibers",
    "classification": "physical16 is a conditional boundary readout, neither a constructor of the relative-channel experiment nor a source identifier",
    "smallest_exact_falsifier": "(g_phi,g_psi)=(1,1) and (2,1/2), with M=kappa=1, have identical J16=-1 but different width packets",
    "calibration_falsifier": "(kappa,I)=(1,1) and (2,1/2), with M=1, have identical J16=-1 but different coherent arcs",
    "first_nonfaithful_arrow": "projection from the mediator source packet to the single physical16 boundary component",
    "remaining_physical_instrument_gate": "derive a common coherent final state, executable phase-flipped settings, nonzero visibility, calibrated background, finite-width support, and the portal normalization from one admitted mediator grammar",
    "descent_disposition": "a supplied invariant portal descends from the source experiment to physical16; no constructor-independent reverse map from physical16 to threshold records exists",
}

out = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "wp606_physical16_relative_channel_construction_audit.json"
)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
