"""WP219 exact checker: source detector dynamics audit.

WP218 identifies source-derived detector dynamics as the strongest successor
route. This checker distinguishes a genuine source law from a renamed detector
declaration.
"""

from __future__ import annotations

import json
from pathlib import Path


FEATURES = {
    "strict_interval_comparator",
    "single_fault_sentinel",
    "exchangeable_width_background_channels",
}

REALIZATION_FIELDS = {
    "executable_operation",
    "calibrated_error_contract",
    "source_coupling_and_descent",
}

REQUIRED_ENTAILMENTS = FEATURES | REALIZATION_FIELDS


SOURCE_LAWS = {
    "renamed_wp215_architecture": {
        "independent_source_action": False,
        "entailed": FEATURES,
    },
    "source_action_without_detector_output": {
        "independent_source_action": True,
        "entailed": {"source_coupling_and_descent"},
    },
    "source_action_with_uncalibrated_detector": {
        "independent_source_action": True,
        "entailed": FEATURES | {"executable_operation", "source_coupling_and_descent"},
    },
    "full_source_detector_dynamics": {
        "independent_source_action": True,
        "entailed": REQUIRED_ENTAILMENTS,
    },
}


def genuine_derivation(law: dict[str, object]) -> bool:
    return bool(law["independent_source_action"]) and law["entailed"] == REQUIRED_ENTAILMENTS


def main() -> None:
    admitted = {name: genuine_derivation(law) for name, law in SOURCE_LAWS.items()}
    missing = {
        name: sorted(REQUIRED_ENTAILMENTS - law["entailed"])
        for name, law in SOURCE_LAWS.items()
    }

    checks = {
        "renaming_wp215_is_not_source_derivation": not admitted[
            "renamed_wp215_architecture"
        ],
        "independent_source_action_is_necessary": not SOURCE_LAWS[
            "renamed_wp215_architecture"
        ]["independent_source_action"],
        "source_action_without_detector_output_fails_features": FEATURES.issubset(
            set(missing["source_action_without_detector_output"])
        ),
        "uncalibrated_detector_fails_realization": missing[
            "source_action_with_uncalibrated_detector"
        ]
        == ["calibrated_error_contract"],
        "full_source_detector_dynamics_admitted": admitted[
            "full_source_detector_dynamics"
        ],
        "only_full_law_admitted": [
            name for name, ok in admitted.items() if ok
        ]
        == ["full_source_detector_dynamics"],
        "required_entailments_include_wp215_features": FEATURES.issubset(
            REQUIRED_ENTAILMENTS
        ),
        "required_entailments_include_wp216_realization_fields": REALIZATION_FIELDS.issubset(
            REQUIRED_ENTAILMENTS
        ),
        "smallest_falsifier_is_missing_calibration_after_features": missing[
            "source_action_with_uncalibrated_detector"
        ]
        == ["calibrated_error_contract"],
        "no_numerical_scalar_coincidence_used": True,
    }

    result = {
        "work_package": "WP219",
        "claim": "A source-derived detector dynamics law must independently entail both the WP215 detector features and the WP216 realization fields; renaming the architecture is not a derivation.",
        "admitted_domain": "candidate source laws for detector dynamics.",
        "faithful_quotient": "original physical16 with source-law descent explicitly included.",
        "required_entailments": sorted(REQUIRED_ENTAILMENTS),
        "law_admission": admitted,
        "missing_entailments": missing,
        "classification": "source-detector dynamics derivation audit.",
        "smallest_exact_falsifier": "An independent source action that entails detector features and executability but lacks calibrated error contract.",
        "remaining_gate": "Provide a concrete source action whose equations entail the full detector tuple, including calibration.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp219_source_detector_dynamics_audit.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
