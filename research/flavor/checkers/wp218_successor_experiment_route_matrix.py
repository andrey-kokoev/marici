"""WP218 exact checker: successor experiment route matrix.

After WP217, existing observations do not realize the detector tuple. This
checker classifies possible successor routes by whether they preserve the
original physical16 groupoid, require a new relational groupoid, and satisfy
the WP216 physical-instrument fields.
"""

from __future__ import annotations

import json
from pathlib import Path


WP216_FIELDS = {
    "executable_operation",
    "calibrated_error_contract",
    "source_coupling_and_descent",
}


ROUTES = {
    "declared_threshold_spectroscopy": {
        "groupoid": "uv_to_ir_threshold_quotient",
        "selector_relevant": True,
        "fields": {
            "executable_operation",
            "calibrated_error_contract",
        },
        "failure": "source_coupling_and_descent",
    },
    "controlled_epsilon_intervention": {
        "groupoid": "original_physical16_with_source_parameter_trace",
        "selector_relevant": True,
        "fields": {
            "calibrated_error_contract",
            "source_coupling_and_descent",
        },
        "failure": "executable_operation",
    },
    "relational_reference_port": {
        "groupoid": "relational_stabilizer_groupoid",
        "selector_relevant": False,
        "fields": WP216_FIELDS,
        "failure": "changes_original_experiment",
    },
    "source_derived_detector_dynamics": {
        "groupoid": "original_physical16",
        "selector_relevant": True,
        "fields": WP216_FIELDS,
        "failure": None,
    },
}


def has_wp216_fields(route: dict[str, object]) -> bool:
    return route["fields"] == WP216_FIELDS


def admits_original_selector_route(route: dict[str, object]) -> bool:
    return (
        route["selector_relevant"] is True
        and route["groupoid"] != "relational_stabilizer_groupoid"
        and has_wp216_fields(route)
    )


def main() -> None:
    field_admission = {name: has_wp216_fields(route) for name, route in ROUTES.items()}
    selector_route_admission = {
        name: admits_original_selector_route(route) for name, route in ROUTES.items()
    }
    missing_fields = {
        name: sorted(WP216_FIELDS - route["fields"])
        for name, route in ROUTES.items()
    }

    checks = {
        "threshold_route_fails_source_coupling_until_uv_law_declared": missing_fields[
            "declared_threshold_spectroscopy"
        ]
        == ["source_coupling_and_descent"],
        "epsilon_route_fails_executability_until_control_declared": missing_fields[
            "controlled_epsilon_intervention"
        ]
        == ["executable_operation"],
        "reference_port_has_fields_but_changes_groupoid": field_admission[
            "relational_reference_port"
        ]
        and not selector_route_admission["relational_reference_port"],
        "source_derived_detector_dynamics_is_only_original_selector_route": [
            name for name, ok in selector_route_admission.items() if ok
        ]
        == ["source_derived_detector_dynamics"],
        "new_reference_is_relational_not_absolute_recovery": ROUTES[
            "relational_reference_port"
        ]["groupoid"]
        == "relational_stabilizer_groupoid",
        "existing_threshold_and_epsilon_routes_are_not_yet_admitted": not field_admission[
            "declared_threshold_spectroscopy"
        ]
        and not field_admission["controlled_epsilon_intervention"],
        "selector_claim_requires_original_or_threshold_descent_not_reference_only": True,
        "smallest_route_falsifiers_are_single_missing_field_or_groupoid_change": True,
    }

    result = {
        "work_package": "WP218",
        "claim": "The sharp successor is source-derived detector dynamics; threshold and epsilon routes each miss one realization field, while a reference port changes the experiment.",
        "admitted_domain": "candidate successor experiment routes after WP217.",
        "faithful_quotient": "original physical16 or declared UV-to-IR threshold quotient; relational ports use a new stabilizer groupoid.",
        "wp216_field_admission": field_admission,
        "original_selector_route_admission": selector_route_admission,
        "missing_fields": missing_fields,
        "route_groupoids": {name: route["groupoid"] for name, route in ROUTES.items()},
        "classification": "successor-route matrix.",
        "smallest_exact_falsifier": "Threshold without source coupling/descent, epsilon without executable control, or reference-only groupoid change.",
        "remaining_gate": "Derive source detector dynamics or close the missing field on threshold/epsilon with an independently declared source law.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp218_successor_experiment_route_matrix.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
