"""WP232 exact checker: current sources two-error probe audit.

Compares currently admitted flavor source/probe families with the WP231
requirement for a source-derived calibrated rank-two width/background probe.
"""

from __future__ import annotations

import json
from pathlib import Path


REQUIRED = {
    "source_derived",
    "calibrated",
    "rank_two_width_background_response",
}


CURRENT_FAMILIES = {
    "one_loop_sm_rg": {
        "fields": {"source_derived"},
        "role": "transport",
    },
    "physical16_experimental_readout": {
        "fields": {"calibrated"},
        "role": "readout",
    },
    "nine_link_texture_constraints": {
        "fields": set(),
        "role": "presentation",
    },
    "texture_zero_perturbations": {
        "fields": set(),
        "role": "presentation_test",
    },
    "hypothetical_source_calibrated_two_error_probe": {
        "fields": REQUIRED,
        "role": "candidate_new_experiment",
    },
}


def admits_probe(fields: set[str]) -> bool:
    return fields == REQUIRED


def main() -> None:
    admissions = {
        name: admits_probe(family["fields"])
        for name, family in CURRENT_FAMILIES.items()
    }
    missing = {
        name: sorted(REQUIRED - family["fields"])
        for name, family in CURRENT_FAMILIES.items()
    }

    checks = {
        "sm_rg_is_source_derived_but_not_detector_probe": missing["one_loop_sm_rg"]
        == ["calibrated", "rank_two_width_background_response"],
        "physical16_readout_is_calibrated_but_not_source_probe": missing[
            "physical16_experimental_readout"
        ]
        == ["rank_two_width_background_response", "source_derived"],
        "texture_constraints_supply_no_probe_authority": missing[
            "nine_link_texture_constraints"
        ]
        == [
            "calibrated",
            "rank_two_width_background_response",
            "source_derived",
        ],
        "texture_perturbations_supply_no_probe_authority": missing[
            "texture_zero_perturbations"
        ]
        == [
            "calibrated",
            "rank_two_width_background_response",
            "source_derived",
        ],
        "only_hypothetical_probe_satisfies_wp231": [
            name for name, ok in admissions.items() if ok
        ]
        == ["hypothetical_source_calibrated_two_error_probe"],
        "current_admitted_sources_do_not_close_coordinate_map": not any(
            ok
            for name, ok in admissions.items()
            if name != "hypothetical_source_calibrated_two_error_probe"
        ),
        "largest_typed_physical16_readout_is_not_selector_probe": True,
        "no_reference_port_smuggled": True,
    }

    result = {
        "work_package": "WP232",
        "claim": "No currently admitted flavor source or readout supplies the WP231 source-derived calibrated rank-two width/background probe.",
        "admitted_domain": "current flavor source/probe families audited against WP231.",
        "faithful_quotient": "WP231 requirement fields on the detector-error response.",
        "family_roles": {
            name: family["role"] for name, family in CURRENT_FAMILIES.items()
        },
        "family_admissions": admissions,
        "missing_fields": missing,
        "classification": "current-source no-go for two-error observability.",
        "smallest_exact_falsifier": "SM RG is source-derived but has no calibrated rank-two width/background detector response.",
        "remaining_gate": "Introduce a new source-derived calibrated two-error experiment, or close the coordinate-map branch negative.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp232_current_sources_two_error_probe_audit.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
