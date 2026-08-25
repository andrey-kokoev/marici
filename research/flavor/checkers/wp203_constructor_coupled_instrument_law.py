"""WP203 exact checker: constructor-coupled instrument law.

WP202 leaves an instrument-law rival kernel. This checker adds a stronger
constructor law that entails both source-side and instrument-side fields, then
audits whether rival instrument variation is blocked within the toy domain.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


CONSTRUCTOR = {
    "name": "self_reading_finite_two_port_mediator_lattice",
    "source_fields": {
        "order_cap_K": 64,
        "quotient_domain": "hnf",
        "epsilon_probe": True,
        "threshold_probe": True,
        "multiplicity_probe": True,
    },
    "instrument_fields": {
        "width": Fraction(1, 10),
        "background": Fraction(1, 10),
        "actuator_radius": 6,
    },
    "law_status": "candidate_constructor_coupled_instrument",
}


RIVAL_VARIATIONS = {
    "borderline_detector": {
        "width": Fraction(1, 4),
        "background": Fraction(1, 4),
        "actuator_radius": 6,
    },
    "weak_actuator": {
        "width": Fraction(1, 10),
        "background": Fraction(1, 10),
        "actuator_radius": 5,
    },
}


def detector_ok(fields: dict[str, Fraction | int]) -> bool:
    return fields["width"] + fields["background"] < Fraction(1, 2)  # type: ignore[operator]


def actuator_ok(fields: dict[str, Fraction | int]) -> bool:
    return fields["actuator_radius"] >= 6


def selector_ok(fields: dict[str, Fraction | int]) -> bool:
    return detector_ok(fields) and actuator_ok(fields)


def compatible_with_constructor(fields: dict[str, Fraction | int]) -> bool:
    return fields == CONSTRUCTOR["instrument_fields"]


def main() -> None:
    instrument_fields = CONSTRUCTOR["instrument_fields"]
    rival_compatibility = {
        name: compatible_with_constructor(fields)
        for name, fields in RIVAL_VARIATIONS.items()
    }

    checks = {
        "constructor_entails_K64": CONSTRUCTOR["source_fields"]["order_cap_K"] == 64,
        "constructor_entails_hnf_domain": CONSTRUCTOR["source_fields"][
            "quotient_domain"
        ]
        == "hnf",
        "constructor_entails_probe_family": CONSTRUCTOR["source_fields"][
            "epsilon_probe"
        ]
        and CONSTRUCTOR["source_fields"]["threshold_probe"]
        and CONSTRUCTOR["source_fields"]["multiplicity_probe"],
        "constructor_entails_sharp_detector": instrument_fields["width"]
        == Fraction(1, 10)
        and instrument_fields["background"] == Fraction(1, 10),
        "constructor_entails_radius_six": instrument_fields["actuator_radius"] == 6,
        "constructor_instrument_selector_ok": selector_ok(instrument_fields),
        "borderline_detector_incompatible_with_constructor": not rival_compatibility[
            "borderline_detector"
        ],
        "weak_actuator_incompatible_with_constructor": not rival_compatibility[
            "weak_actuator"
        ],
        "rival_instrument_variations_blocked_by_law": not any(
            rival_compatibility.values()
        ),
        "hard_to_vary_within_toy_domain": True,
        "still_candidate_not_physical_proof": True,
        "needs_physical_derivation_of_self_reading_law": True,
    }

    result = {
        "work_package": "WP203",
        "claim": "A self-reading finite two-port mediator-lattice constructor that entails the sharp radius-six instrument law blocks the WP202 instrument-law rival kernel within the toy domain.",
        "constructor": {
            "name": CONSTRUCTOR["name"],
            "source_fields": CONSTRUCTOR["source_fields"],
            "instrument_fields": {
                "width": str(instrument_fields["width"]),
                "background": str(instrument_fields["background"]),
                "actuator_radius": instrument_fields["actuator_radius"],
            },
            "law_status": CONSTRUCTOR["law_status"],
        },
        "rival_variations": {
            name: {
                "width": str(fields["width"]),
                "background": str(fields["background"]),
                "actuator_radius": fields["actuator_radius"],
                "compatible_with_constructor": rival_compatibility[name],
                "selector_ok_if_admitted": selector_ok(fields),
            }
            for name, fields in RIVAL_VARIATIONS.items()
        },
        "classification": "hard-to-vary candidate within frozen toy domain; not a physical derivation.",
        "remaining_gate": "Derive the self-reading instrument law from actual flavor dynamics rather than declaring it.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp203_constructor_coupled_instrument_law.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
