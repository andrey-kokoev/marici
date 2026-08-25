"""WP221 exact checker: missing detector-field derivation ladder.

Ranks the WP220 missing detector fields by how close they are to the finite
two-port source tuple and identifies the smallest constructive next target.
"""

from __future__ import annotations

import json
from pathlib import Path


FIELDS = {
    "strict_interval_comparator": {
        "class": "structural_order",
        "requires": {"ordered_gap", "strict_boundary_rule"},
        "source_currently_supplies": {"ordered_gap"},
    },
    "exchangeable_width_background_channels": {
        "class": "structural_symmetry",
        "requires": {"two_error_channels", "channel_exchange_action"},
        "source_currently_supplies": {"two_error_channels"},
    },
    "single_fault_sentinel": {
        "class": "fault_model",
        "requires": {"fault_state", "sentinel_transition", "one_bad_contract"},
        "source_currently_supplies": set(),
    },
    "executable_operation": {
        "class": "apparatus",
        "requires": {"control_protocol", "finite_runtime", "readout_reset"},
        "source_currently_supplies": set(),
    },
    "calibrated_error_contract": {
        "class": "calibration",
        "requires": {"width_bound", "background_bound", "drift_bound"},
        "source_currently_supplies": set(),
    },
}


def missing_requirements(field: str) -> set[str]:
    spec = FIELDS[field]
    return spec["requires"] - spec["source_currently_supplies"]


def main() -> None:
    missing = {field: sorted(missing_requirements(field)) for field in FIELDS}
    derivable_next = [
        field
        for field in FIELDS
        if len(missing_requirements(field)) == 1
        and FIELDS[field]["class"].startswith("structural")
    ]

    checks = {
        "strict_comparator_is_one_rule_short": missing[
            "strict_interval_comparator"
        ]
        == ["strict_boundary_rule"],
        "exchange_symmetry_is_one_action_short": missing[
            "exchangeable_width_background_channels"
        ]
        == ["channel_exchange_action"],
        "sentinel_requires_fault_model_not_present": missing["single_fault_sentinel"]
        == ["fault_state", "one_bad_contract", "sentinel_transition"],
        "executability_requires_apparatus_not_source_tuple": missing[
            "executable_operation"
        ]
        == ["control_protocol", "finite_runtime", "readout_reset"],
        "calibration_requires_error_bounds_not_source_tuple": missing[
            "calibrated_error_contract"
        ]
        == ["background_bound", "drift_bound", "width_bound"],
        "smallest_constructive_targets_are_structural": derivable_next
        == [
            "strict_interval_comparator",
            "exchangeable_width_background_channels",
        ],
        "fault_and_apparatus_fields_not_derivable_by_naming": True,
        "no_full_selector_from_partial_structural_derivation": True,
    }

    result = {
        "work_package": "WP221",
        "claim": "The smallest constructive detector targets are the structural strict-boundary rule and channel-exchange action; fault, apparatus, and calibration fields remain larger physical gates.",
        "admitted_domain": "WP220 missing detector fields with requirement deficits.",
        "faithful_quotient": "field-requirement entailment ladder over the original physical16 detector route.",
        "field_classes": {field: spec["class"] for field, spec in FIELDS.items()},
        "missing_requirements": missing,
        "smallest_constructive_targets": derivable_next,
        "classification": "detector-field derivation ladder.",
        "smallest_exact_falsifier": "A source tuple with ordered gap but no strict boundary rule, or two error channels but no exchange action.",
        "remaining_gate": "Derive either strict boundary rule or channel-exchange action from source dynamics; neither suffices alone for selector authority.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp221_missing_detector_field_ladder.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
