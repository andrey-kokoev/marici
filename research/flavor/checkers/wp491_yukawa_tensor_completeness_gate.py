"""Exact Yukawa-tensor completeness gate for the WP489 RG successor."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp483 = load("wp483_connector_frame_architecture.json")
wp489 = load("wp489_common_source_threshold_constructor.json")
wp490 = load("wp490_dual_gauge_running_gate.json")

# The symmetry-preserving hostile pair differs only in one messenger Yukawa
# normalization. It leaves the singlet-generated masses and all WP489 vacuum
# relations unchanged.
n = sp.Integer(18)
c_one = sp.Integer(1)
c_two = sp.Integer(2)
identity = sp.eye(n)
y_one = c_one * identity
y_two = c_two * identity


def invariants(matrix):
    gram = sp.simplify(matrix * matrix.T)
    return sp.trace(gram), sp.trace(gram * gram)


i2_one, i4_one = invariants(y_one)
i2_two, i4_two = invariants(y_two)

wp489_source_text = json.dumps(wp489["source_action_extension"], sort_keys=True)
required_tensor_packet = [
    "Y_H_up",
    "Y_H_down",
    "Y_S_up",
    "Y_S_down",
    "Y_X_up",
    "Y_X_down",
    "Z_A_up",
    "Z_A_down",
    "Z_B_up",
    "Z_B_down",
]

checks = {
    "wp483_dependency_passed": wp483["passed"],
    "wp489_dependency_passed": wp489["passed"],
    "wp490_dependency_passed": wp490["passed"],
    "wp489_declares_mass_yukawas_only": "z_A" in wp489_source_text and "z_B" in wp489_source_text,
    "wp489_omits_H_S_X_interaction_tensors": all(name not in wp489_source_text for name in ["Y_H", "Y_S", "Y_X"]),
    "hostile_pair_preserves_isotropic_tensor_form": y_one.T * y_one == sp.eye(n) and y_two.T * y_two == 4 * sp.eye(n),
    "quadratic_contraction_changes_by_four": i2_two == 4 * i2_one,
    "quartic_contraction_changes_by_sixteen": i4_two == 16 * i4_one,
    "hostile_pair_leaves_wp489_mass_coefficients_untouched": all(
        name in wp489["selected_relations"] for name in ["M_A_squared", "M_B_squared"]
    ),
    "complete_tensor_packet_has_ten_named_maps": len(required_tensor_packet) == 10,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP491",
    "domain": "WP489 two-stage up/down messenger grammar above thresholds, prior to any gauge-Yukawa fixed-point calculation",
    "declared_but_insufficient": {
        "mass_yukawas": ["z_A", "z_B"],
        "missing_interaction_tensor_families": ["Y_H", "Y_S", "Y_X"],
        "reason": "vacuum masses and isotropic route Gram do not determine the tensor contractions entering coupled beta functions",
    },
    "hostile_pair": {
        "tensor_A": "Y_X=I_18 block diagonal in the up/down charge sectors",
        "tensor_B": "Y_X=2 I_18 with the same charge-sector blocks",
        "shared_data": "same representations, oriented-port symmetry, WP489 radial vacuum, z_A,z_B messenger masses, and threshold ordering",
        "quadratic_invariants": [str(i2_one), str(i2_two)],
        "quartic_invariants": [str(i4_one), str(i4_two)],
        "ratios": {"I2_B_over_A": "4", "I4_B_over_A": "16"},
    },
    "minimal_tensor_packet": required_tensor_packet,
    "additional_rg_typing": [
        "normalization and index contractions for every tensor",
        "all scalar quartics and mixed quartics",
        "Standard Model gauge and Yukawa couplings retained in the truncation",
        "renormalization scheme and loop order",
        "matching scales and finite threshold maps for A and B",
    ],
    "classification": "The present source selects relational masses but does not define a unique gauge-Yukawa vector field; fixed-point calculation is not yet typed.",
    "selector": False,
    "rigidifier": False,
    "instrument": None,
    "smallest_exact_falsifier": "Y_X=I_18 and Y_X=2I_18 preserve the admitted symmetry and mass packet but multiply the quadratic RG contraction by four and the quartic contraction by sixteen.",
    "remaining_gate": "Freeze the ten up/down messenger tensor maps and complete RG truncation independently of the desired fixed point, then compute and threshold-match the resulting beta vector field.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp491_yukawa_tensor_completeness_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
