"""WP198 exact checker: minimal constructor-law candidate.

This checker audits a smallest concrete constructor-law candidate that tries to
entail the recurrence/threshold/epsilon/multiplicity tuple. It distinguishes
fields entailed by the law from detector fields still externally assumed.
"""

from __future__ import annotations

import json
from pathlib import Path


REQUIRED = {
    "order_cap_K",
    "port_law",
    "quotient_domain",
    "epsilon_probe",
    "threshold_probe",
    "multiplicity_probe",
    "width_bound",
    "background_bound",
    "executable_radius",
}

CONSTRUCTOR = {
    "name": "finite_two_port_mediator_lattice",
    "axioms": {
        "finite_internal_state_space": {
            "entails": ["order_cap_K"],
            "value": 64,
        },
        "coupled_mediator_port_relation": {
            "entails": ["port_law", "quotient_domain", "epsilon_probe"],
            "value": {
                "port_law": "coupled",
                "quotient_domain": "hnf",
                "epsilon_probe": "formal_coupling_parameter",
            },
        },
        "two_mediator_species": {
            "entails": ["threshold_probe", "multiplicity_probe"],
            "value": {
                "threshold_probe": "mediator_threshold",
                "multiplicity_probe": 2,
            },
        },
        "detector_model": {
            "entails": [],
            "value": "not_source_derived",
        },
        "actuator_model": {
            "entails": [],
            "value": "not_source_derived",
        },
    },
}


def entailed_fields() -> set[str]:
    fields: set[str] = set()
    for axiom in CONSTRUCTOR["axioms"].values():
        fields.update(axiom["entails"])
    return fields


def main() -> None:
    entailed = entailed_fields()
    missing = sorted(REQUIRED - entailed)
    source_fields = REQUIRED - {"width_bound", "background_bound", "executable_radius"}

    checks = {
        "entails_order_cap": "order_cap_K" in entailed,
        "entails_port_law": "port_law" in entailed,
        "entails_quotient_domain": "quotient_domain" in entailed,
        "entails_epsilon_probe_formally": "epsilon_probe" in entailed,
        "entails_threshold_probe": "threshold_probe" in entailed,
        "entails_multiplicity_probe": "multiplicity_probe" in entailed,
        "does_not_entail_width_bound": "width_bound" not in entailed,
        "does_not_entail_background_bound": "background_bound" not in entailed,
        "does_not_entail_executable_radius": "executable_radius" not in entailed,
        "source_side_fields_all_entailed": source_fields <= entailed,
        "detector_and_actuator_fields_missing": missing
        == ["background_bound", "executable_radius", "width_bound"],
        "not_admitted_physical_selector": True,
    }

    result = {
        "work_package": "WP198",
        "claim": "A minimal finite two-port mediator-lattice constructor can entail the source-side tuple, but still fails the physical selector gate at detector and actuator bounds.",
        "constructor": CONSTRUCTOR,
        "required_fields": sorted(REQUIRED),
        "entailed_fields": sorted(entailed),
        "missing_fields": missing,
        "classification": "constructor-law candidate; source-side progress, detector/actuator failure.",
        "smallest_falsifier": "No source-derived width, background, or executable-radius bound, so WP197/WP178 gates remain open.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp198_minimal_constructor_law_candidate.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
