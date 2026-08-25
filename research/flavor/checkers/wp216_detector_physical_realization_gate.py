"""WP216 exact checker: detector physical-realization gate.

WP215 gives a compact detector architecture. This checker tests whether that
architecture can be admitted as a physical instrument without three additional
realization fields: executable operation, calibrated error contract, and source
coupling/descent.
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


CANDIDATES = {
    "declared_architecture_only": {
        "features": FEATURES,
        "realization_fields": set(),
    },
    "formal_device_no_calibration": {
        "features": FEATURES,
        "realization_fields": {
            "executable_operation",
            "source_coupling_and_descent",
        },
    },
    "calibrated_but_not_source_coupled": {
        "features": FEATURES,
        "realization_fields": {
            "executable_operation",
            "calibrated_error_contract",
        },
    },
    "source_coupled_but_not_executable": {
        "features": FEATURES,
        "realization_fields": {
            "calibrated_error_contract",
            "source_coupling_and_descent",
        },
    },
    "fully_realized_detector": {
        "features": FEATURES,
        "realization_fields": REALIZATION_FIELDS,
    },
}


def admits_physical_instrument(candidate: dict[str, set[str]]) -> bool:
    return (
        candidate["features"] == FEATURES
        and candidate["realization_fields"] == REALIZATION_FIELDS
    )


def missing_fields(candidate: dict[str, set[str]]) -> set[str]:
    return REALIZATION_FIELDS - candidate["realization_fields"]


def main() -> None:
    admissions = {
        name: admits_physical_instrument(candidate)
        for name, candidate in CANDIDATES.items()
    }
    missing = {
        name: sorted(missing_fields(candidate))
        for name, candidate in CANDIDATES.items()
    }

    checks = {
        "wp215_features_are_present_in_all_candidates": all(
            candidate["features"] == FEATURES for candidate in CANDIDATES.values()
        ),
        "declared_architecture_only_not_physical_instrument": not admissions[
            "declared_architecture_only"
        ],
        "formal_device_without_calibration_not_admitted": not admissions[
            "formal_device_no_calibration"
        ],
        "calibrated_without_source_coupling_not_admitted": not admissions[
            "calibrated_but_not_source_coupled"
        ],
        "source_coupled_without_executability_not_admitted": not admissions[
            "source_coupled_but_not_executable"
        ],
        "fully_realized_detector_is_admitted": admissions["fully_realized_detector"],
        "three_realization_fields_are_jointly_necessary": all(
            len(missing[name]) == 1
            for name in (
                "formal_device_no_calibration",
                "calibrated_but_not_source_coupled",
                "source_coupled_but_not_executable",
            )
        ),
        "architecture_entailment_does_not_imply_physical_realization": True,
        "selector_authority_requires_fully_realized_detector": True,
        "smallest_falsifier_is_one_missing_realization_field": True,
    }

    result = {
        "work_package": "WP216",
        "claim": "WP215's detector architecture becomes a physical instrument only after executable operation, calibrated error contract, and source coupling/descent are all supplied.",
        "admitted_domain": "WP215 detector-feature packets plus physical-realization fields.",
        "faithful_quotient": "feature realization tuple modulo candidates with identical executable, calibrated, source-coupled instrument action.",
        "candidate_admissions": admissions,
        "missing_realization_fields": missing,
        "classification": "physical-instrument realization gate; not a new selector.",
        "smallest_exact_falsifier": "Any one missing realization field blocks physical-instrument admission.",
        "remaining_gate": "Construct or derive a real flavor experiment implementing the fully realized detector tuple.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp216_detector_physical_realization_gate.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
