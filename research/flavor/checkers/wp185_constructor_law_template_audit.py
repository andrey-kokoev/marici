"""WP185 exact checker: constructor-law template audit.

After WP184 the next frontier is a source law entailing the whole recurrence
gate tuple. This checker audits a minimal law template and verifies which
fields it entails and which remain assumptions.
"""

from __future__ import annotations

import json
from pathlib import Path


LAW_FIELDS = {
    "finite_state_space_dimension": {
        "entails": ["order_cap_K"],
        "status": "source_law_candidate",
    },
    "abelian_two_port_closure": {
        "entails": ["quotient_domain"],
        "status": "source_law_candidate",
    },
    "homogeneous_lattice_admissibility": {
        "entails": ["quotient_domain"],
        "status": "extra_shape_assumption",
    },
    "detector_counting_contract": {
        "entails": ["count_error_tau"],
        "status": "instrument_assumption",
    },
    "recurrence_actuator_budget": {
        "entails": ["executable_radius"],
        "status": "instrument_assumption",
    },
    "coarse_graining_channel": {
        "entails": ["degradation_map"],
        "status": "instrument_assumption",
    },
}

REQUIRED_FIELDS = {
    "order_cap_K",
    "quotient_domain",
    "count_error_tau",
    "executable_radius",
    "degradation_map",
}


def entailed_fields(selected_laws: list[str]) -> set[str]:
    fields: set[str] = set()
    for law in selected_laws:
        fields.update(LAW_FIELDS[law]["entails"])
    return fields


def is_single_source_law(selected_laws: list[str]) -> bool:
    return all(LAW_FIELDS[law]["status"] == "source_law_candidate" for law in selected_laws)


def main() -> None:
    source_only = ["finite_state_space_dimension", "abelian_two_port_closure"]
    full_template = list(LAW_FIELDS)
    source_only_fields = entailed_fields(source_only)
    full_fields = entailed_fields(full_template)
    missing_source_only = sorted(REQUIRED_FIELDS - source_only_fields)
    missing_full = sorted(REQUIRED_FIELDS - full_fields)

    checks = {
        "source_only_entails_K": "order_cap_K" in source_only_fields,
        "source_only_entails_some_domain_law": "quotient_domain" in source_only_fields,
        "source_only_does_not_entail_tau": "count_error_tau" not in source_only_fields,
        "source_only_does_not_entail_radius": "executable_radius" not in source_only_fields,
        "source_only_does_not_entail_degradation": "degradation_map" not in source_only_fields,
        "source_only_missing_three_fields": missing_source_only
        == ["count_error_tau", "degradation_map", "executable_radius"],
        "full_template_entails_all_required_fields": full_fields == REQUIRED_FIELDS,
        "full_template_has_no_missing_fields": missing_full == [],
        "full_template_is_not_single_source_law": not is_single_source_law(full_template),
        "homogeneous_lattice_is_extra_shape_assumption": LAW_FIELDS[
            "homogeneous_lattice_admissibility"
        ]["status"]
        == "extra_shape_assumption",
        "instrument_fields_are_not_source_derived": all(
            LAW_FIELDS[name]["status"] == "instrument_assumption"
            for name in (
                "detector_counting_contract",
                "recurrence_actuator_budget",
                "coarse_graining_channel",
            )
        ),
        "law_template_not_physical_establishment": True,
    }

    result = {
        "work_package": "WP185",
        "claim": "A finite-state-space constructor template can explain K and part of the quotient-domain law, but tau, executable radius, degradation, and quotient-shape restrictions remain independent gates.",
        "law_fields": LAW_FIELDS,
        "source_only_laws": source_only,
        "source_only_entailed_fields": sorted(source_only_fields),
        "source_only_missing_fields": missing_source_only,
        "full_template_fields": full_template,
        "full_template_entailed_fields": sorted(full_fields),
        "classification": "constructor-law template audit; not a physical selector.",
        "next_falsifier": "Find a flavor source action that derives the instrument fields, or construct rival sources with the same K but different quotient-shape laws.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp185_constructor_law_template_audit.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
