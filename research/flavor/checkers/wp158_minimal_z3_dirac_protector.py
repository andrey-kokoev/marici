"""Exact charge audit for the minimal auxiliary Z3 Dirac protector."""

import json
from pathlib import Path


z4_phi_dagger = 0  # charge-four parent Higgs is neutral in the residual Z4.
z4_n = 2
z4_nbar = 2
z3_phi_dagger = 0
z3_n = 1
z3_nbar = 2


def charge_sum(modulus: int, *charges: int) -> int:
    return sum(charges) % modulus


nn_z4 = charge_sum(4, z4_phi_dagger, z4_n, z4_n)
nn_z3 = charge_sum(3, z3_phi_dagger, z3_n, z3_n)
nbar_nbar_z4 = charge_sum(4, z4_phi_dagger, z4_nbar, z4_nbar)
nbar_nbar_z3 = charge_sum(3, z3_phi_dagger, z3_nbar, z3_nbar)
dirac_z4 = charge_sum(4, z4_phi_dagger, z4_n, z4_nbar)
dirac_z3 = charge_sum(3, z3_phi_dagger, z3_n, z3_nbar)


def has_non_self_inverse_charge(modulus: int) -> bool:
    return any(q % modulus != 0 and 2 * q % modulus != 0 for q in range(modulus))


checks = {
    "Z2_has_no_nonselfinverse_charge": not has_non_self_inverse_charge(2),
    "Z3_has_nonselfinverse_charge": has_non_self_inverse_charge(3),
    "Z3_is_minimal_nontrivial_cyclic_protector": [m for m in range(2, 8) if has_non_self_inverse_charge(m)][0] == 3,
    "N_majorana_is_Z4_invariant": nn_z4 == 0,
    "N_majorana_is_Z3_forbidden": nn_z3 == 2,
    "Nbar_majorana_is_Z4_invariant": nbar_nbar_z4 == 0,
    "Nbar_majorana_is_Z3_forbidden": nbar_nbar_z3 == 1,
    "Dirac_operator_is_Z4_invariant": dirac_z4 == 0,
    "Dirac_operator_is_Z3_invariant": dirac_z3 == 0,
    "Dirac_pair_has_zero_linear_Z4_residue": (z4_n + z4_nbar) % 4 == 0,
    "Dirac_pair_has_zero_linear_Z3_residue": (z3_n + z3_nbar) % 3 == 0,
    "protector_removes_residue_two_mass_block": nn_z3 != 0 and nbar_nbar_z3 != 0 and dirac_z3 == 0,
}

result = {
    "work_package": "WP158",
    "title": "Minimal Z3 Dirac-protector audit",
    "source_group": "Z4 anomaly character times auxiliary exact Z3",
    "spectator_pair": {
        "N": {"Z4": 2, "Z3": 1},
        "Nbar": {"Z4": 2, "Z3": 2},
    },
    "allowed_mass": "Phi^dagger N Nbar",
    "forbidden_masses": ["Phi^dagger N N", "Phi^dagger Nbar Nbar"],
    "classification": "minimal conditional representation protector restores the Dirac-only spectator grammar",
    "selector": "conditional combined with WP154",
    "rigidifier": False,
    "physical_instrument": False,
    "smallest_exact_falsifier": "breaking or omitting Z3 makes Phi^dagger N N legal again under residual Z4",
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
}

output = Path(__file__).resolve().parents[1] / "results" / "wp158_minimal_z3_dirac_protector.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

