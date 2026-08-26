"""Typed source versus external-control factorization of the six-port pencil."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp535 = load("wp535_six_port_bilocal_instrument.json")
wp538 = load("wp538_source_six_port_system_pencil.json")
wp539 = load("wp539_common_ensemble_resolvent_contexts.json")
wp541 = load("wp541_twisted_continuum_context_ladder.json")
wp542 = load("wp542_continuum_volume_design_rank.json")
wp543 = load("wp543_existing_source_constraint_kernel.json")

source_tangent = sp.Matrix(
    [sp.sympify(value) for value in wp538["fixed_v_source_fiber"]["pencil_coefficient_tangent_at_t_1"]]
)

scale_controls = ["qcd_scale"]
twist_controls = [f"twist_{index}" for index in range(6)]
renormalization_controls = [
    f"Z_{row}_{column}" for row in range(4) for column in range(4)
]
threshold_controls = [f"threshold_match_{index}" for index in range(6)]
external_controls = (
    scale_controls
    + twist_controls
    + renormalization_controls
    + threshold_controls
)
external_dimension = len(external_controls)

# Tagged bundle: source coefficients and calibration registers are different
# output sorts. The rank is additive, but only the first column and first six
# rows define source-image rank.
tagged_jacobian = sp.diag(source_tangent, sp.eye(external_dimension))
source_projection = tagged_jacobian[:6, :1]
control_projection = tagged_jacobian[6:, 1:]

# If the external QCD scale is not independently calibrated, uniform source
# pole scaling and inverse instrument-unit scaling have the same coefficient
# tangent up to sign. This is a real nuisance degeneracy, not a selector.
untagged_source_scale = sp.Matrix.hstack(source_tangent, -source_tangent)
source_scale_kernel = untagged_source_scale.nullspace()

# Hostile authority smear: declaring every calibration register to be a source
# coordinate inflates the tagged rank from one to thirty.
smeared_source_rank = tagged_jacobian.rank()
true_source_rank = source_projection.rank()

checks = {
    "dependencies_passed": all(
        bool(packet["passed"])
        for packet in (wp535, wp538, wp539, wp541, wp542, wp543)
    ),
    "source_tangent_is_six_by_one": source_tangent.shape == (6, 1),
    "fixed_control_source_image_rank_is_one": true_source_rank == 1,
    "six_port_readout_rank_remains_six": wp538["rank_factorization"]["six_port_state_readout_rank"] == 6,
    "context_operator_rank_remains_twenty_four": wp539["common_ensemble_factorization"]["joint_complex_rank"] == 24,
    "external_control_dimension_is_twenty_nine": external_dimension == 29,
    "renormalization_block_has_sixteen_coordinates": len(renormalization_controls) == 16,
    "threshold_block_has_six_coordinates": len(threshold_controls) == 6,
    "tagged_total_rank_is_thirty": tagged_jacobian.rank() == 30,
    "control_rank_does_not_change_source_rank": control_projection.rank() == 29 and true_source_rank == 1,
    "unfixed_scale_is_exactly_confounding": untagged_source_scale.rank() == 1,
    "source_scale_kernel_is_one_dimensional": len(source_scale_kernel) == 1,
    "common_source_scale_shift_is_in_kernel": untagged_source_scale * sp.Matrix([1, 1]) == sp.zeros(6, 1),
    "authority_smear_would_falsely_inflate_source_rank": smeared_source_rank == 30 and smeared_source_rank > true_source_rank,
    "current_source_selector_kernel_remains_one_dimensional": wp543["authorized_equalities"]["kernel_dimension"] == 1,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP544",
    "domain": "WP538's six-state source pencil composed with WP539-WP542 scale, twist, renormalization, threshold and continuum instrument coordinates.",
    "typed_factorization": {
        "source_coordinate": "t in a=t^2, w=1/t at fixed v",
        "source_pencil_tangent": [str(value) for value in source_tangent],
        "fixed_control_source_image_rank": true_source_rank,
        "six_port_readout_rank": wp538["rank_factorization"]["six_port_state_readout_rank"],
        "context_operator_complex_rank": wp539["common_ensemble_factorization"]["joint_complex_rank"],
        "rule": "Source rank is computed by differentiating the pencil with respect to t while every external control is held fixed. Port and context ranks characterize readout faithfulness, not source selection.",
    },
    "external_control_registry": {
        "scale": scale_controls,
        "twist": twist_controls,
        "renormalization_mixing": renormalization_controls,
        "threshold_matching": threshold_controls,
        "dimension": external_dimension,
        "tagged_control_rank": control_projection.rank(),
        "authority": "Every coordinate is fixed by an instrument calibration, boundary-control protocol, renormalization condition or threshold-matching calculation external to the source selector.",
    },
    "source_scale_confounder": {
        "untagged_jacobian_shape": list(untagged_source_scale.shape),
        "rank": untagged_source_scale.rank(),
        "kernel_vector": ["1", "1"],
        "meaning": "Without external QCD scale calibration, a uniform source pole rescaling is exactly confounded with inverse instrument-unit rescaling in the pencil-coefficient packet.",
    },
    "authority_smear_attack": {
        "true_source_rank": true_source_rank,
        "tagged_total_rank": tagged_jacobian.rank(),
        "false_source_rank_if_all_controls_are_relabelled_as_source": smeared_source_rank,
        "conclusion": "The ranks 6, 24, 29 and 30 belong to state readout, contextual analysis, external controls and the tagged bundle. None may be quoted as source-image rank, which is one.",
    },
    "theorem": "The unified typed pencil has fixed-control source-image rank one. Its six-port and contextual maps have ranks six and 24, while 29 external scale, twist, renormalization and threshold coordinates occupy a separate calibration bundle. An uncalibrated scale is exactly confounded with uniform source pole scaling. Counting external-control rank as source rank would inflate one to thirty and is prohibited.",
    "classification": "Complete source-versus-instrument rank reconciliation. The instrument can separate a one-dimensional moving source family once controls are calibrated; it neither creates additional source directions nor selects t.",
    "selector": False,
    "instrument": "The controls are fully typed at contract level. Physical realization still requires external scale and threshold calibrations, implemented twists, nonperturbative mixing/contact subtraction and the WP542 measured covariance.",
    "smallest_exact_falsifier": "Drop external scale calibration. The source-tangent and inverse-unit tangent are opposite columns of a rank-one 6 x 2 Jacobian, with kernel vector (1,1), so t cannot be identified from dimensionless pole coefficients alone.",
    "remaining_gate": "Realize and calibrate every external control with covariance, then measure the rank-one t response. Numerical selection remains a separate source-dynamics problem governed by WP543.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp544_typed_source_instrument_pencil.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
