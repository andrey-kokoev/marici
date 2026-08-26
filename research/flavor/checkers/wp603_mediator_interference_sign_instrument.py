"""Exact WP603 mediator-interference sign instrument."""

import json
from pathlib import Path

import sympy as sp


g_phi, g_psi, mass = sp.symbols("g_phi g_psi M", nonzero=True, real=True)
width_phi = g_phi**2
width_psi = g_psi**2
interference = g_phi * g_psi
effective_cross = -interference / mass**2

sign_states = ((1, 1), (1, -1), (-1, 1), (-1, -1))
width_partition = {}
joint_partition = {}
for state in sign_states:
    first, second = state
    width_record = (first**2, second**2)
    joint_record = (first**2, second**2, first * second)
    width_partition.setdefault(str(width_record), []).append(state)
    joint_partition.setdefault(str(joint_record), []).append(state)

global_sign_orbits = [
    {(1, 1), (-1, -1)},
    {(1, -1), (-1, 1)},
]
joint_classes = [set(states) for states in joint_partition.values()]

width_jacobian = sp.Matrix(
    [
        [sp.diff(width_phi, g_phi), sp.diff(width_phi, g_psi)],
        [sp.diff(width_psi, g_phi), sp.diff(width_psi, g_psi)],
    ]
)
joint_jacobian = sp.Matrix(
    [
        [sp.diff(width_phi, g_phi), sp.diff(width_phi, g_psi)],
        [sp.diff(width_psi, g_phi), sp.diff(width_psi, g_psi)],
        [sp.diff(interference, g_phi), sp.diff(interference, g_psi)],
    ]
)
joint_gram_determinant = sp.factor((joint_jacobian.T * joint_jacobian).det())

checks = {
    "widths_have_one_four_state_sign_class": len(width_partition) == 1
    and len(next(iter(width_partition.values()))) == 4,
    "physical_constructor_quotient_has_two_relative_sign_classes": len(
        global_sign_orbits
    )
    == 2,
    "widths_collapse_the_two_physical_constructor_classes": all(
        orbit.issubset(set(next(iter(width_partition.values()))))
        for orbit in global_sign_orbits
    ),
    "interference_recovers_exact_global_sign_orbits": len(joint_classes) == 2
    and all(orbit in joint_classes for orbit in global_sign_orbits),
    "width_jacobian_is_locally_rank_two_away_from_zero": width_jacobian.det()
    == 4 * g_phi * g_psi,
    "local_rank_does_not_remove_global_sign_fiber": len(width_partition) == 1,
    "joint_gram_is_positive_away_from_zero": sp.simplify(
        joint_gram_determinant
        - (4 * g_phi**4 + 16 * g_phi**2 * g_psi**2 + 4 * g_psi**4)
    )
    == 0,
    "tree_matching_consistency_relation_is_exact": sp.simplify(
        mass**2 * effective_cross + interference
    )
    == 0,
    "interference_magnitude_matches_partial_width_product": sp.simplify(
        interference**2 - width_phi * width_psi
    )
    == 0,
}

if not all(checks.values()):
    raise SystemExit(f"WP603 check failed: {checks}")

result = {
    "work_package": "WP603",
    "status": "PASS",
    "checks": {key: bool(value) for key, value in checks.items()},
    "source_domain": "one resolved mediator of mass M with two nonzero real source couplings g_phi and g_psi",
    "constructor_quotient": "coupling pairs modulo simultaneous global sign reversal",
    "ordinary_threshold_record": ["M", "Gamma_phi proportional to g_phi^2", "Gamma_psi proportional to g_psi^2"],
    "ordinary_contextual_partition": [["++", "+-", "-+", "--"]],
    "physical_constructor_partition": [["++", "--"], ["+-", "-+"]],
    "completed_probe": "a calibrated coherent shared-channel interference record I proportional to g_phi*g_psi",
    "completed_contextual_partition": [["++", "--"], ["+-", "-+"]],
    "classification": "widths are locally rank two but globally nonfaithful; shared-channel interference restores faithfulness on the global-sign quotient",
    "smallest_exact_falsifier": "same M and partial widths but opposite interference sign",
    "architecture_consistency_tests": ["M^2*c_eff+I=0", "I^2=Gamma_phi*Gamma_psi in the declared normalization"],
    "physical_instrument_gate": "the mediator grammar must independently provide two coherent amplitudes to one resolved final state, calibrated phase convention, finite-width line shape and detector resolution",
}

out = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "wp603_mediator_interference_sign_instrument.json"
)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
