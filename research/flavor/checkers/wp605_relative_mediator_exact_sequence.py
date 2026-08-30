"""Exact WP605 relative mediator sequence and completion gates."""

import json
from pathlib import Path

import sympy as sp


g_phi, g_psi, mass, portal_scale = sp.symbols(
    "g_phi g_psi M kappa", nonzero=True, real=True
)
visibility = sp.symbols("nu", positive=True, real=True)

gamma_phi = g_phi**2
gamma_psi = g_psi**2
relative_arc = g_phi * g_psi
effective_cross = -relative_arc / mass**2
physical16_boundary = portal_scale * effective_cross

sign_group = ((1, 1), (1, -1), (-1, 1), (-1, -1))
global_sign_kernel = {(1, 1), (-1, -1)}
relative_positive = {(1, 1), (-1, -1)}
relative_negative = {(1, -1), (-1, 1)}

norm_fibers = {}
relative_fibers = {}
for first, second in sign_group:
    norm_fibers.setdefault((first**2, second**2), set()).add((first, second))
    relative_fibers.setdefault(
        (first**2, second**2, first * second), set()
    ).add((first, second))

reachable_residual = sp.simplify(relative_arc**2 - gamma_phi * gamma_psi)
matching_residual = sp.simplify(mass**2 * effective_cross + relative_arc)
boundary_residual = sp.simplify(
    physical16_boundary - portal_scale * effective_cross
)

unreachable_tuple = {"Gamma_phi": 4, "Gamma_psi": 9, "I": 5}
unreachable_residual = (
    unreachable_tuple["I"] ** 2
    - unreachable_tuple["Gamma_phi"] * unreachable_tuple["Gamma_psi"]
)

positive_boundary_pair = sp.simplify(
    physical16_boundary.subs({g_phi: 2, g_psi: 3, mass: 5})
)
negative_boundary_pair = sp.simplify(
    physical16_boundary.subs({g_phi: 2, g_psi: -3, mass: 5})
)

completed_positive = visibility * 6
completed_negative = -visibility * 6
completion_separation = sp.simplify(completed_positive - completed_negative)
zero_visibility_separation = completion_separation.subs(visibility, 0)

robust_pass = {
    "visibility": sp.Rational(1, 2),
    "absolute_interference": 6,
    "uncertainty_radius": 2,
}
robust_fail = {
    "visibility": sp.Rational(1, 2),
    "absolute_interference": 6,
    "uncertainty_radius": 3,
}

checks = {
    "sign_group_has_four_elements": len(sign_group) == 4,
    "global_sign_kernel_has_two_elements": len(global_sign_kernel) == 2,
    "relative_quotient_has_two_classes": relative_positive != relative_negative
    and relative_positive | relative_negative == set(sign_group),
    "norm_channel_has_one_four_element_fiber": list(norm_fibers.values())
    == [set(sign_group)],
    "relative_arc_refines_to_global_sign_orbits": set(
        frozenset(fiber) for fiber in relative_fibers.values()
    )
    == {frozenset(relative_positive), frozenset(relative_negative)},
    "source_composition_reachability_is_exact": reachable_residual == 0,
    "hostile_formal_tuple_is_not_reachable": unreachable_residual == -11,
    "tree_matching_commutes": matching_residual == 0,
    "boundary_portal_commutes": boundary_residual == 0,
    "nonzero_calibrated_boundary_separates_relative_sign": sp.simplify(
        positive_boundary_pair - negative_boundary_pair
    )
    == -12 * portal_scale / 25,
    "zero_boundary_scale_would_restore_kernel": sp.simplify(
        (positive_boundary_pair - negative_boundary_pair).subs(portal_scale, 0)
    )
    == 0,
    "positive_visibility_preserves_relative_sign": completion_separation
    == 12 * visibility,
    "zero_visibility_restores_relative_kernel": zero_visibility_separation == 0,
    "robust_completion_passes_strict_margin": (
        robust_pass["visibility"] * robust_pass["absolute_interference"]
        > robust_pass["uncertainty_radius"]
    ),
    "boundary_margin_is_not_robust": not (
        robust_fail["visibility"] * robust_fail["absolute_interference"]
        > robust_fail["uncertainty_radius"]
    ),
}

if not all(checks.values()):
    raise SystemExit(f"WP605 check failed: {checks}")

result = {
    "work_package": "WP605",
    "status": "PASS",
    "checks": {key: bool(value) for key, value in checks.items()},
    "source_domain": "nonzero real coupling pairs modulo simultaneous global sign, restricted to tuples reachable from one common mediator",
    "relative_exact_sequence": "global sign C2 -> coupling-sign group C2xC2 -> relative-sign C2",
    "sector_norm_channels": ["Gamma_phi=g_phi^2", "Gamma_psi=g_psi^2"],
    "relative_arc_channel": "I=g_phi*g_psi",
    "boundary_channel": "J_physical16=-kappa*I/M^2 with independently calibrated nonzero kappa",
    "source_composition_laws": ["I^2=Gamma_phi*Gamma_psi", "M^2*c_eff+I=0"],
    "ordinary_fiber": [["++", "+-", "-+", "--"]],
    "relative_fibers": [["++", "--"], ["+-", "-+"]],
    "reachable_hostile": "the formal tuple (Gamma_phi,Gamma_psi,I)=(4,9,5) fails I^2=Gamma_phi*Gamma_psi by -11",
    "completion_rule": "detector record I_det=nu*I remains sign-faithful for calibrated nu>0; nu=0 restores the relative kernel",
    "robustness_rule": "with uncertainty radius delta, sign classes are separated only when delta<nu*abs(I)",
    "classification": "relative exact-sequence packet; algebraically jointly faithful on the reachable quotient, conditionally continuous under nonzero visibility, not yet a physical instrument",
    "smallest_exact_falsifier": "zero visibility, zero portal scale, an unreachable channel tuple, or a measured matching residual",
    "physical_instrument_gate": "derive common-channel coherence, calibration constants, finite-width completion, detector visibility and a nonzero weak-basis-invariant physical16 portal from one mediator grammar",
}

out = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "wp605_relative_mediator_exact_sequence.json"
)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
