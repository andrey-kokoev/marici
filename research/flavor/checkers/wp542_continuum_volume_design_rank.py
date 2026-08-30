"""Exact continuum and finite-volume design rank for the 48-real instrument."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp535 = load("wp535_six_port_bilocal_instrument.json")
wp539 = load("wp539_common_ensemble_resolvent_contexts.json")
wp541 = load("wp541_twisted_continuum_context_ladder.json")

# Normalize the L=24 leading finite-volume shape to one and write the L=30
# value as r=exp(-6 m_gap), independently calibrated by the QCD spectrum.
r = sp.symbols("r", positive=True)
ensemble_rows = (
    (sp.Integer(1), sp.Integer(24), sp.Integer(1)),
    (sp.Rational(1, 2), sp.Integer(24), sp.Integer(1)),
    (sp.Rational(1, 3), sp.Integer(24), sp.Integer(1)),
    (sp.Rational(1, 2), sp.Integer(30), r),
    (sp.Rational(1, 3), sp.Integer(30), r),
)
design = sp.Matrix(
    [[1, spacing**2, spacing**4, finite_volume] for spacing, _, finite_volume in ensemble_rows]
)

four_row_minors = [
    sp.factor(design[[row for row in range(5) if row != omitted], :].det())
    for omitted in range(5)
]
rank_witness = design.subs(r, sp.Rational(1, 2))

real_estimator_count = wp539["common_ensemble_factorization"]["real_estimator_count"]
full_design = sp.kronecker_product(rank_witness, sp.eye(real_estimator_count))

# Hostile designs: no volume contrast, and only two distinct spacings.
no_volume_contrast = design.subs(r, 1)
two_spacing_design = sp.Matrix(
    [
        [1, 1, 1, 1],
        [1, sp.Rational(1, 4), sp.Rational(1, 16), 1],
        [1, 1, 1, r],
        [1, sp.Rational(1, 4), sp.Rational(1, 16), r],
        [1, sp.Rational(1, 4), sp.Rational(1, 16), r],
    ]
)

continuum_parameter_count_per_estimator = design.cols
total_parameter_count = continuum_parameter_count_per_estimator * real_estimator_count
total_observation_count = design.rows * real_estimator_count
residual_dimension = total_observation_count - total_parameter_count

checks = {
    "dependencies_passed": all(bool(packet["passed"]) for packet in (wp535, wp539, wp541)),
    "five_ensemble_rows_are_declared": design.rows == 5,
    "three_distinct_lattice_spacings_are_present": len({row[0] for row in ensemble_rows}) == 3,
    "two_distinct_physical_extents_are_present": len({row[1] for row in ensemble_rows}) == 2,
    "generic_design_has_rank_four": rank_witness.rank() == 4,
    "at_least_one_symbolic_minor_is_nonzero_for_r_not_one": any(
        minor != 0 and sp.factor(minor).subs(r, 1) == 0 for minor in four_row_minors
    ),
    "full_forty_eight_estimator_design_has_rank_192": full_design.rank() == total_parameter_count == 192,
    "five_ensemble_design_is_overdetermined": residual_dimension == 48,
    "no_volume_contrast_loses_finite_volume_direction": no_volume_contrast.rank() == 3,
    "two_spacing_hostile_design_cannot_separate_a2_and_a4": two_spacing_design.subs(r, sp.Rational(1, 2)).rank() == 3,
    "required_data_covariance_dimension_is_240": total_observation_count == 240,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP542",
    "domain": "WP541's three-spacing twisted context ladder, augmented by a second physical volume and applied jointly to WP539's 48 real estimators.",
    "ensemble_design": {
        "rows": [
            {
                "a_GeV_inverse": str(spacing),
                "L_GeV_inverse": str(extent),
                "leading_finite_volume_shape": str(finite_volume),
            }
            for spacing, extent, finite_volume in ensemble_rows
        ],
        "per_estimator_model": "y(a,L)=y_cont+c_2 a^2+c_4 a^4+d_L F(L)",
        "finite_volume_ratio": "r=F(30)/F(24)=exp(-6 m_gap), supplied by an independently calibrated QCD mass gap",
        "design_matrix": [[str(value) for value in row] for row in design.tolist()],
        "four_row_minors": [str(value) for value in four_row_minors],
        "generic_rank_condition": "rank four for the declared spacing set whenever r is not one",
    },
    "joint_instrument_fit": {
        "real_estimators_per_ensemble": real_estimator_count,
        "ensemble_count": design.rows,
        "real_observation_count": total_observation_count,
        "parameters_per_estimator": continuum_parameter_count_per_estimator,
        "total_parameter_count": total_parameter_count,
        "joint_design_rank": full_design.rank(),
        "residual_dimension": residual_dimension,
        "required_data_covariance_shape": [total_observation_count, total_observation_count],
        "required_scale_covariance": "The external QCD scale-setting and mass-gap covariance must be propagated as nuisance covariance, not refit from flavor pole data.",
    },
    "renormalization_contract": {
        "common_scheme": "one nonperturbative intermediate scheme for V_LL, S_RR, S_LL and S_RL on every ensemble",
        "common_scale": "one declared physical renormalization scale above the simulated infrared support with step scaling across lattice cutoffs",
        "mixing": "retain the complete four-channel mixing and contact-subtraction matrix before continuum extrapolation",
        "thresholds": "match the continuum bilocal packet across each frozen mediator threshold only after the common scheme limit",
    },
    "hostile_tests": {
        "no_volume_contrast_rank": no_volume_contrast.rank(),
        "two_spacing_rank": two_spacing_design.subs(r, sp.Rational(1, 2)).rank(),
        "conclusion": "Three spacings are necessary to separate a^2 from a^4, and a second physical volume is necessary to separate the leading finite-volume column from the continuum intercept.",
    },
    "theorem": "Five ensembles at three lattice spacings and two physical volumes give an overdetermined exact rank-192 joint design for all 48 real estimators under a continuum plus leading finite-volume model. Removing volume contrast or reducing to two distinct spacings lowers the per-estimator rank from four to three.",
    "classification": "Identifiable continuum-volume analysis contract, not measured calibration. Scale setting and the QCD mass gap are external instrument inputs and cannot be inferred from the flavor answer.",
    "selector": False,
    "instrument": "The ensemble geometry, fit model, renormalization interface and 240 x 240 data-covariance requirement are now preregistered. Gauge ensembles and bilocal measurements remain ungenerated.",
    "smallest_exact_falsifier": "Set r=1 so both volumes have the same finite-volume column. The per-estimator design rank falls from four to three and the continuum intercept cannot be separated from finite-volume contamination.",
    "remaining_gate": "Supply external QCD scale and mass-gap calibrations, generate the five common four-channel ensembles, perform nonperturbative mixing/contact subtraction and threshold matching, and publish the full 240 x 240 observation covariance plus scale-systematic covariance.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp542_continuum_volume_design_rank.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
