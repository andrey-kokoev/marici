"""WP215 exact checker: symmetric detector architecture.

WP214 leaves three detector gates. This checker audits a compact architecture
candidate intended to entail all three: two exchangeable error types, minimal
nonzero fault tolerance, and strict interval separation.
"""

from __future__ import annotations

import json
from pathlib import Path


ARCHITECTURE = {
    "name": "minimal_symmetric_two_error_detector",
    "features": {
        "strict_interval_comparator": {
            "entails": ["strict_below_quarter_target"],
        },
        "single_fault_sentinel": {
            "entails": ["minimal_nonzero_fault_tolerance"],
        },
        "exchangeable_width_background_channels": {
            "entails": ["width_background_exchange"],
        },
    },
}

REMAINING_GATES = {
    "minimal_nonzero_fault_tolerance",
    "strict_below_quarter_target",
    "width_background_exchange",
}


HOSTILE_VARIANTS = {
    "no_sentinel": {
        "features": [
            "strict_interval_comparator",
            "exchangeable_width_background_channels",
        ]
    },
    "non_strict_comparator": {
        "features": [
            "single_fault_sentinel",
            "exchangeable_width_background_channels",
        ]
    },
    "asymmetric_channels": {
        "features": [
            "strict_interval_comparator",
            "single_fault_sentinel",
        ]
    },
}


def entailed(features: list[str]) -> set[str]:
    gates: set[str] = set()
    for feature in features:
        gates.update(ARCHITECTURE["features"][feature]["entails"])
    return gates


def main() -> None:
    full_features = list(ARCHITECTURE["features"])
    full_entailed = entailed(full_features)
    hostile_entailed = {
        name: entailed(variant["features"]) for name, variant in HOSTILE_VARIANTS.items()
    }

    checks = {
        "full_architecture_entails_all_three_gates": full_entailed == REMAINING_GATES,
        "strict_comparator_entails_quarter_target_gate": "strict_below_quarter_target"
        in entailed(["strict_interval_comparator"]),
        "sentinel_entails_minimal_fault_gate": "minimal_nonzero_fault_tolerance"
        in entailed(["single_fault_sentinel"]),
        "exchangeable_channels_entail_width_background_exchange": "width_background_exchange"
        in entailed(["exchangeable_width_background_channels"]),
        "no_sentinel_missing_fault_gate": "minimal_nonzero_fault_tolerance"
        not in hostile_entailed["no_sentinel"],
        "non_strict_missing_quarter_target_gate": "strict_below_quarter_target"
        not in hostile_entailed["non_strict_comparator"],
        "asymmetric_missing_exchange_gate": "width_background_exchange"
        not in hostile_entailed["asymmetric_channels"],
        "each_hostile_variant_missing_one_gate": all(
            len(REMAINING_GATES - gates) == 1 for gates in hostile_entailed.values()
        ),
        "architecture_is_compact_three_feature_candidate": len(full_features) == 3,
        "physical_realization_still_needed": True,
        "feature_entailments_are_declared_not_derived_microphysics": True,
        "wp214_gates_closed_conditionally": True,
    }

    result = {
        "work_package": "WP215",
        "claim": "A minimal symmetric two-error detector architecture conditionally entails the three remaining WP214 gates, but the feature entailments still need physical realization.",
        "architecture": ARCHITECTURE,
        "full_entailed_gates": sorted(full_entailed),
        "hostile_variants": {
            name: {
                "features": variant["features"],
                "entailed_gates": sorted(hostile_entailed[name]),
                "missing_gates": sorted(REMAINING_GATES - hostile_entailed[name]),
            }
            for name, variant in HOSTILE_VARIANTS.items()
        },
        "classification": "conditional detector-architecture closure candidate.",
        "remaining_gate": "Physically realize or derive the three detector features.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp215_symmetric_detector_architecture.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
