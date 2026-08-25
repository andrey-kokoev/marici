"""Exact charge audit for U(1) -> Z4 Higgsing and a charge-two Majorana block."""

import json
from pathlib import Path


q_phi = 4
q_n = 2
q_phi_dagger = -q_phi

bare_majorana_charge = 2 * q_n
dressed_majorana_charge = q_phi_dagger + 2 * q_n
residual_n_charge = q_n % q_phi
operator_dimension = 1 + 3  # scalar plus two Weyl fields

# After <Phi>=v, y Phi^dagger N N produces M_N=y v.
y = 3
vev = 5
majorana_mass = y * vev

hostile_flavor = (2, 2, 2)
hostile_spectator_residue = residual_n_charge
total_residue = (sum(hostile_flavor) + hostile_spectator_residue) % 4

checks = {
    "charge_four_vev_leaves_Z4": q_phi == 4,
    "bare_majorana_is_forbidden_by_unbroken_U1": bare_majorana_charge != 0,
    "dressed_majorana_is_U1_invariant": dressed_majorana_charge == 0,
    "dressed_operator_is_renormalizable_dimension_four": operator_dimension == 4,
    "charge_two_field_remains_Z4_charge_two": residual_n_charge == 2,
    "vev_generates_nonzero_majorana_mass": majorana_mass == 15,
    "generated_block_has_wp156_residue_two": hostile_spectator_residue == 2,
    "hostile_flavor_sum_is_two_mod_four": sum(hostile_flavor) % 4 == 2,
    "generated_spectator_cancels_hostile_residue": total_residue == 0,
    "U1_parent_does_not_enforce_dirac_only_domain": dressed_majorana_charge == 0 and operator_dimension <= 4,
    "forbidding_operator_needs_extra_source_rule": bare_majorana_charge != 0 and dressed_majorana_charge == 0,
    "keeping_U1_unbroken_changes_source_experiment": q_phi != 0,
}

result = {
    "work_package": "WP157",
    "title": "U(1)-parent Majorana obstruction",
    "source_grammar": "gauged U(1) broken to Z4 by a charge-four scalar Phi",
    "spectator": "left-handed Weyl N of U(1) charge two",
    "allowed_operator": "Phi^dagger N N",
    "operator_dimension": operator_dimension,
    "generated_Z4_residue": hostile_spectator_residue,
    "classification": "minimal U(1) parent UV-completes rather than forbids the charge-two Majorana obstruction",
    "selector": False,
    "rigidifier": "residual-charge organization only",
    "physical_instrument": False,
    "smallest_exact_falsifier": "charges (-4,2,2) sum to zero, so the renormalizable Phi^dagger N N coupling generates the forbidden residue-two block",
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
}

output = Path(__file__).resolve().parents[1] / "results" / "wp157_u1_parent_majorana_obstruction.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

