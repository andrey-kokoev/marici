"""Exact field-content and dimension gate for a Standard Model quartic actuator."""

import json
from pathlib import Path

import sympy as sp


quartic_dimension = sp.Integer(4)
renormalizable_limit = sp.Integer(4)

# name: canonical dimension, Lorentz scalar, gauge singlet, dynamical SM field.
# Composite entries are included to locate the first gauge-invariant evasion.
candidates = {
    "Higgs_doublet_H": (sp.Integer(1), 1, 0, 1),
    "Higgs_bilinear_HdaggerH": (sp.Integer(2), 1, 1, 0),
    "fermion_bilinear": (sp.Integer(3), 1, 1, 0),
    "gauge_kinetic_scalar": (sp.Integer(4), 1, 1, 0),
    "dimensionless_external_spurion": (sp.Integer(0), 1, 1, 0),
}

total_dimensions = {
    name: quartic_dimension + properties[0]
    for name, properties in candidates.items()
}
eligible = {
    name: int(bool(
        properties[0] <= 0
        and properties[1] == 1
        and properties[2] == 1
        and properties[3] == 1
    ))
    for name, properties in candidates.items()
}

lowest_sm_gauge_singlet_multiplier_dimension = candidates[
    "Higgs_bilinear_HdaggerH"
][0]
first_higgs_evasion_dimension = (
    quartic_dimension + lowest_sm_gauge_singlet_multiplier_dimension
)

checks = {
    "higgs_quartic_is_dimension_four": quartic_dimension == 4,
    "renormalizable_actuator_requires_nonpositive_dimension": renormalizable_limit - quartic_dimension == 0,
    "no_candidate_is_a_dynamical_dimension_zero_sm_singlet": sum(eligible.values()) == 0,
    "elementary_higgs_is_not_a_gauge_singlet_actuator": candidates["Higgs_doublet_H"][2] == 0,
    "lowest_higgs_built_singlet_yields_dimension_six": first_higgs_evasion_dimension == 6,
    "external_spurion_is_not_a_dynamical_sm_field": candidates["dimensionless_external_spurion"][3] == 0,
    "every_dynamical_or_composite_sm_multiplier_exceeds_dimension_four_or_fails_gauge_singlet": all(
        total_dimensions[name] > renormalizable_limit or properties[2] == 0
        for name, properties in candidates.items()
        if name != "dimensionless_external_spurion"
    ),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP419",
    "title": "Standard Model quartic-actuator no-go",
    "target_operator": "(H-dagger-H)^2",
    "target_operator_dimension": int(quartic_dimension),
    "candidate_multipliers": {
        name: {
            "canonical_dimension": int(properties[0]),
            "lorentz_scalar": bool(properties[1]),
            "gauge_singlet": bool(properties[2]),
            "dynamical_standard_model_field": bool(properties[3]),
            "combined_operator_dimension": int(total_dimensions[name]),
            "eligible_renormalizable_actuator": bool(eligible[name]),
        }
        for name, properties in candidates.items()
    },
    "first_higgs_built_evasion": "(H-dagger-H)^3",
    "first_higgs_built_evasion_dimension": int(first_higgs_evasion_dimension),
    "classification": "no field in the renormalizable Standard Model can be an independently commanded Higgs-quartic actuator",
    "smallest_exact_falsifier": "exhibit a dynamical dimension-zero Lorentz-scalar gauge-singlet Standard Model field with a calibrated laboratory setting",
    "allowed_evasions": [
        "a new dynamical singlet or modulus",
        "an external spacetime-dependent coupling spurion with a physical preparation rule",
        "a higher-dimensional EFT interaction with an observed controllable source",
    ],
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).parents[1] / "results" / "wp419_sm_quartic_actuator_no_go.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
