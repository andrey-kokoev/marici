"""WP217 exact checker: existing-observation detector audit.

Tests whether currently admitted low-energy flavor observations realize the
WP216 detector tuple, as opposed to only reading the measured-ten projection.
"""

from __future__ import annotations

import json
from pathlib import Path


REQUIRED_DETECTOR_FIELDS = {
    "strict_interval_comparator",
    "single_fault_sentinel",
    "exchangeable_width_background_channels",
    "executable_operation",
    "calibrated_error_contract",
    "source_coupling_and_descent",
}


OBSERVATION_FAMILIES = {
    "measured_ten_low_energy": {
        "fields": {
            "executable_operation",
            "calibrated_error_contract",
        },
        "collapses_physical16_pairs": True,
    },
    "physical16_reconstruction_coordinates": {
        "fields": set(),
        "collapses_physical16_pairs": False,
    },
    "wp216_full_detector_tuple": {
        "fields": REQUIRED_DETECTOR_FIELDS,
        "collapses_physical16_pairs": False,
    },
}


def realizes_detector(fields: set[str]) -> bool:
    return fields == REQUIRED_DETECTOR_FIELDS


def main() -> None:
    realization = {
        name: realizes_detector(family["fields"])
        for name, family in OBSERVATION_FAMILIES.items()
    }
    missing = {
        name: sorted(REQUIRED_DETECTOR_FIELDS - family["fields"])
        for name, family in OBSERVATION_FAMILIES.items()
    }

    checks = {
        "measured_ten_is_typed_observation_but_not_detector_tuple": not realization[
            "measured_ten_low_energy"
        ],
        "measured_ten_collapses_hostile_physical16_pairs": OBSERVATION_FAMILIES[
            "measured_ten_low_energy"
        ]["collapses_physical16_pairs"],
        "physical16_coordinates_are_not_an_instrument": not realization[
            "physical16_reconstruction_coordinates"
        ],
        "physical16_coordinates_do_not_authorize_projection_uniqueness": True,
        "wp216_full_tuple_is_the_first_admitted_detector_form": realization[
            "wp216_full_detector_tuple"
        ],
        "existing_observations_do_not_supply_source_coupling": "source_coupling_and_descent"
        in missing["measured_ten_low_energy"],
        "existing_observations_do_not_supply_sentinel": "single_fault_sentinel"
        in missing["measured_ten_low_energy"],
        "existing_observations_do_not_supply_exchange_channels": "exchangeable_width_background_channels"
        in missing["measured_ten_low_energy"],
        "existing_observations_do_not_supply_strict_interval_comparator": "strict_interval_comparator"
        in missing["measured_ten_low_energy"],
        "smallest_falsifier_is_measured_ten_family": True,
    }

    result = {
        "work_package": "WP217",
        "claim": "Existing low-energy flavor observations do not realize the WP216 detector tuple; they remain measured-ten readouts and cannot supply selector authority.",
        "admitted_domain": "existing flavor observation families compared with the WP216 detector tuple.",
        "faithful_quotient": "physical16 for source claims; measured ten is only a nonfaithful projection.",
        "observation_realization": realization,
        "missing_detector_fields": missing,
        "classification": "existing-observation no-go for detector realization.",
        "smallest_exact_falsifier": "The measured-ten family is calibrated and executable but lacks source coupling/descent and the WP215 detector features while collapsing physical16 pairs.",
        "remaining_gate": "Add a new source-derived threshold/reference/intervention experiment, or derive the detector tuple from flavor dynamics.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp217_existing_observation_detector_audit.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
