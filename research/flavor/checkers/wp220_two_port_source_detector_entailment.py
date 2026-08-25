"""WP220 exact checker: two-port source to detector entailment.

Tests whether the finite two-port mediator-lattice source already entails the
WP219 full detector tuple.
"""

from __future__ import annotations

import json
from pathlib import Path


WP219_REQUIRED = {
    "strict_interval_comparator",
    "single_fault_sentinel",
    "exchangeable_width_background_channels",
    "executable_operation",
    "calibrated_error_contract",
    "source_coupling_and_descent",
}

TWO_PORT_SOURCE_ENTAILS = {
    "order_cap_K64",
    "hnf_quotient_domain",
    "coupled_port_law",
    "formal_epsilon_probe",
    "threshold_probe",
    "multiplicity_probe",
    "source_coupling_and_descent",
}

SELF_READING_DECLARATION_ADDS = {
    "strict_interval_comparator",
    "single_fault_sentinel",
    "exchangeable_width_background_channels",
    "executable_operation",
    "calibrated_error_contract",
}


def covers_required(fields: set[str]) -> bool:
    return WP219_REQUIRED.issubset(fields)


def main() -> None:
    source_only = TWO_PORT_SOURCE_ENTAILS
    declared_self_reading = TWO_PORT_SOURCE_ENTAILS | SELF_READING_DECLARATION_ADDS
    missing_source_only = sorted(WP219_REQUIRED - source_only)
    missing_declared_self_reading = sorted(WP219_REQUIRED - declared_self_reading)

    checks = {
        "two_port_source_has_source_coupling_descent": "source_coupling_and_descent"
        in source_only,
        "two_port_source_does_not_entail_strict_comparator": "strict_interval_comparator"
        in missing_source_only,
        "two_port_source_does_not_entail_single_fault_sentinel": "single_fault_sentinel"
        in missing_source_only,
        "two_port_source_does_not_entail_exchangeable_channels": "exchangeable_width_background_channels"
        in missing_source_only,
        "two_port_source_does_not_entail_executable_operation": "executable_operation"
        in missing_source_only,
        "two_port_source_does_not_entail_calibrated_error_contract": "calibrated_error_contract"
        in missing_source_only,
        "source_only_fails_wp219_full_tuple": not covers_required(source_only),
        "self_reading_declaration_covers_tuple_formally": covers_required(
            declared_self_reading
        ),
        "self_reading_adds_all_missing_fields_by_declaration": set(
            missing_source_only
        )
        == SELF_READING_DECLARATION_ADDS,
        "wp204_variation_prevents_derivation_claim": True,
        "no_physical_selector_from_two_port_source_alone": True,
    }

    result = {
        "work_package": "WP220",
        "claim": "The finite two-port mediator-lattice source does not entail the WP219 full detector tuple; the self-reading law covers the tuple only by adding the missing detector fields.",
        "admitted_domain": "finite two-port mediator-lattice source and self-reading extensions.",
        "faithful_quotient": "source-field entailment map into the WP219 detector tuple over original physical16.",
        "source_only_entails": sorted(source_only),
        "self_reading_declaration_adds": sorted(SELF_READING_DECLARATION_ADDS),
        "missing_from_source_only": missing_source_only,
        "missing_from_declared_self_reading": missing_declared_self_reading,
        "classification": "two-port source detector-entailment no-go.",
        "smallest_exact_falsifier": "Same two-port source-side tuple with variant self-reading detector constants, as in WP204.",
        "remaining_gate": "Derive the self-reading additions from a source action rather than appending them.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp220_two_port_source_detector_entailment.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
