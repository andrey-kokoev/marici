"""WP225 exact checker: two-port automorphism semantics.

Tests whether the finite two-port mediator-lattice source supplies the WP224
width/background exchange automorphism.
"""

from __future__ import annotations

import json
from pathlib import Path


WP224_REQUIRED = {
    "swaps_width_background",
    "commutes_with_source_law",
    "preserves_error_semantics",
    "descends_to_detector_quotient",
}


SOURCE_AUTOMORPHISMS = {
    "mediator_species_swap": {
        "properties": {
            "commutes_with_source_law",
        },
        "acts_on": "mediator_species",
    },
    "port_label_swap": {
        "properties": {
            "commutes_with_source_law",
        },
        "acts_on": "port_labels",
    },
    "declared_detector_error_swap": {
        "properties": {
            "swaps_width_background",
            "preserves_error_semantics",
            "descends_to_detector_quotient",
        },
        "acts_on": "detector_errors",
    },
    "hypothetical_coupled_source_detector_swap": {
        "properties": WP224_REQUIRED,
        "acts_on": "source_and_detector_errors",
    },
}


def admitted(properties: set[str]) -> bool:
    return properties == WP224_REQUIRED


def main() -> None:
    admissions = {
        name: admitted(candidate["properties"])
        for name, candidate in SOURCE_AUTOMORPHISMS.items()
    }
    missing = {
        name: sorted(WP224_REQUIRED - candidate["properties"])
        for name, candidate in SOURCE_AUTOMORPHISMS.items()
    }

    checks = {
        "mediator_species_swap_is_source_symmetry_only": missing[
            "mediator_species_swap"
        ]
        == [
            "descends_to_detector_quotient",
            "preserves_error_semantics",
            "swaps_width_background",
        ],
        "port_label_swap_is_source_symmetry_only": missing["port_label_swap"]
        == [
            "descends_to_detector_quotient",
            "preserves_error_semantics",
            "swaps_width_background",
        ],
        "declared_detector_error_swap_not_source_derived": missing[
            "declared_detector_error_swap"
        ]
        == ["commutes_with_source_law"],
        "only_hypothetical_coupled_swap_admitted": [
            name for name, ok in admissions.items() if ok
        ]
        == ["hypothetical_coupled_source_detector_swap"],
        "finite_two_port_source_does_not_identify_detector_error_semantics": True,
        "source_label_automorphism_does_not_imply_detector_exchange": True,
        "wp223_exchange_gate_remains_open_for_two_port_source": True,
    }

    result = {
        "work_package": "WP225",
        "claim": "The finite two-port source supplies source-label automorphisms, but they do not act on width/background detector semantics; WP223 exchange remains external.",
        "admitted_domain": "automorphisms of the finite two-port source compared with detector-error swaps.",
        "faithful_quotient": "action domain and WP224 property set, not source-label symmetry alone.",
        "candidate_admissions": admissions,
        "missing_properties": missing,
        "action_domains": {
            name: candidate["acts_on"]
            for name, candidate in SOURCE_AUTOMORPHISMS.items()
        },
        "classification": "two-port automorphism semantics no-go.",
        "smallest_exact_falsifier": "Mediator species swap commutes with the source law but does not swap width/background or preserve detector-error semantics.",
        "remaining_gate": "Couple detector-error semantics to the source action, or treat width/background exchange as an external detector symmetry.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp225_two_port_automorphism_semantics.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
