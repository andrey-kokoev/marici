"""Exact audit of an SO(5) vector orbifold zero-mode projector."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
I5 = sp.eye(5)
P = sp.diag(1, 1, 1, 1, -1)
Pi_plus = (I5 + P) / 2
Pi_minus = (I5 - P) / 2

# The physical diagonal SO(3) acts on the first three coordinates. Its
# quadratic Casimir distinguishes the triplet from the two singlets.
J1 = sp.zeros(5)
J2 = sp.zeros(5)
J3 = sp.zeros(5)
J1[1, 2], J1[2, 1] = -1, 1
J2[2, 0], J2[0, 2] = -1, 1
J3[0, 1], J3[1, 0] = -1, 1
casimir = sp.simplify(-(J1**2 + J2**2 + J3**2))
triplet_projector = sp.diag(1, 1, 1, 0, 0)
selected_singlet_projector = sp.diag(0, 0, 0, 1, 0)
removed_singlet_projector = sp.diag(0, 0, 0, 0, 1)

# Conditional inheritance of WP736's representation-fixed normalized portal
# ray, followed by the most general independent boundary-localized shifts.
k, delta_parent, delta_a, delta_b = sp.symbols("k Delta_parent delta_A delta_B", real=True)
kappa_a = k / sp.sqrt(2)
kappa_b = sp.sqrt(2) * k
clebsch_ratio = sp.simplify(kappa_b**2 / kappa_a**2)
threshold_contrast = sp.expand(delta_parent + delta_b - delta_a)

g5, ell = sp.symbols("g5 ell", positive=True)
g4 = g5 / sp.sqrt(ell)
log_sensitivities = (
    sp.simplify(g5 * sp.diff(g4, g5) / g4),
    sp.simplify(ell * sp.diff(g4, ell) / g4),
)

checks = {
    "parity_is_involutive": P**2 == I5,
    "plus_zero_mode_projector_is_exact": Pi_plus**2 == Pi_plus,
    "minus_zero_mode_projector_is_exact": Pi_minus**2 == Pi_minus,
    "plus_intrinsic_parity_keeps_four_modes": sp.trace(Pi_plus) == 4,
    "minus_intrinsic_parity_keeps_one_mode": sp.trace(Pi_minus) == 1,
    "casimir_identifies_triplet": casimir == 2*triplet_projector,
    "kept_four_decompose_as_triplet_plus_one_singlet": Pi_plus == triplet_projector + selected_singlet_projector,
    "unwanted_second_singlet_is_removed": Pi_plus*removed_singlet_projector == sp.zeros(5),
    "intrinsic_parity_choice_changes_the_zero_mode_domain": Pi_plus != Pi_minus,
    "conditional_clebsch_ratio_is_four": clebsch_ratio == 4,
    "triplet_boundary_shift_changes_the_ordered_contrast": sp.diff(threshold_contrast, delta_b) == 1,
    "singlet_boundary_shift_changes_the_ordered_contrast": sp.diff(threshold_contrast, delta_a) == -1,
    "four_dimensional_magnitude_retains_bulk_coupling": log_sensitivities[0] == 1,
    "four_dimensional_magnitude_retains_compactification_length": log_sensitivities[1] == -sp.Rational(1, 2),
    "deliberate_failure_residual_is_nonzero": (Pi_plus-Pi_minus).norm() == sp.sqrt(5),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP742",
    "status": "PASS",
    "checks": checks,
    "source_domain": "five-dimensional SO(5) vector on an S1/Z2 interval with equal endpoint parity P=diag(1,1,1,1,-1) and an independently chosen intrinsic field parity",
    "changed_groupoid": "the orbifold experiment reduces SO(5) to the stabilizer of P; its connected zero-mode group is SO(4), followed by the declared diagonal SO(3)",
    "zero_mode_partition": {
        "intrinsic_parity_plus": "4 = 3 + 1 under diagonal SO(3)",
        "intrinsic_parity_minus": "1 only",
    },
    "classification": "conditional presentation rigidifier and labelled-projector selector, but not a source selector because the boundary and intrinsic parity class are input data",
    "conditional_portal_result": "the surviving 4 inherits the WP736 normalized Clebsch ratio kappa_B^2/kappa_A^2=4",
    "magnitude_fiber": "g4=g5/sqrt(ell), with logarithmic sensitivities (1,-1/2)",
    "threshold_falsifier": "independent residual-symmetry boundary shifts give Delta_low=Delta_parent+delta_B-delta_A",
    "smallest_exact_falsifier": "switching intrinsic parity replaces the rank-four zero-mode projector by its rank-one complement; their difference has Frobenius norm sqrt(5)",
    "instrument": "none supplied by the compactification; representation labels are not a calibrated detector channel",
    "remaining_source_gate": "derive the boundary-condition equivalence class, intrinsic parity, compactification clock, and absence or fixed values of boundary-localized operators from one admitted source dynamics",
    "remaining_physical_gate": "construct two calibrated representation-labelled detector responses on physical16 and show threshold corrections preserve their rank and ordered contrast",
}
(ROOT / "results" / "wp742_orbifold_projector_conditional_rigidifier.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
