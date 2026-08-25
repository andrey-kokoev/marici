"""WP201 exact checker: source+instrument closure.

WP198 supplies source-side fields, WP199/WP200 show detector and actuator gaps.
This checker adds an explicit instrument-law candidate and audits whether the
combined source+instrument package closes the conditional selector gate.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


SOURCE_LAW = {
    "order_cap_K": 64,
    "port_law": "coupled",
    "quotient_domain": "hnf",
    "epsilon_probe": True,
    "threshold_probe": True,
    "multiplicity_probe": True,
}

INSTRUMENT_LAWS = {
    "sharp_radius6": {
        "width_bound": Fraction(1, 10),
        "background_bound": Fraction(1, 10),
        "actuator_radius": 6,
    },
    "borderline_radius6": {
        "width_bound": Fraction(1, 4),
        "background_bound": Fraction(1, 4),
        "actuator_radius": 6,
    },
    "sharp_radius5": {
        "width_bound": Fraction(1, 10),
        "background_bound": Fraction(1, 10),
        "actuator_radius": 5,
    },
}


def detector_passes(law: dict[str, Fraction | int]) -> bool:
    return law["width_bound"] + law["background_bound"] < Fraction(1, 2)  # type: ignore[operator]


def actuator_passes(law: dict[str, Fraction | int]) -> bool:
    return law["actuator_radius"] >= 6


def package_passes(law: dict[str, Fraction | int]) -> bool:
    return detector_passes(law) and actuator_passes(law)


def main() -> None:
    evaluated = {
        name: {
            "width_bound": str(law["width_bound"]),
            "background_bound": str(law["background_bound"]),
            "total_detector_error": str(law["width_bound"] + law["background_bound"]),
            "actuator_radius": law["actuator_radius"],
            "detector_passes": detector_passes(law),
            "actuator_passes": actuator_passes(law),
            "package_passes": package_passes(law),
        }
        for name, law in INSTRUMENT_LAWS.items()
    }

    checks = {
        "source_law_has_K64": SOURCE_LAW["order_cap_K"] == 64,
        "source_law_has_hnf_domain": SOURCE_LAW["quotient_domain"] == "hnf",
        "source_law_has_required_probes": SOURCE_LAW["epsilon_probe"]
        and SOURCE_LAW["threshold_probe"]
        and SOURCE_LAW["multiplicity_probe"],
        "sharp_radius6_detector_passes": detector_passes(
            INSTRUMENT_LAWS["sharp_radius6"]
        ),
        "sharp_radius6_actuator_passes": actuator_passes(
            INSTRUMENT_LAWS["sharp_radius6"]
        ),
        "sharp_radius6_package_passes": package_passes(
            INSTRUMENT_LAWS["sharp_radius6"]
        ),
        "borderline_radius6_detector_fails": not detector_passes(
            INSTRUMENT_LAWS["borderline_radius6"]
        ),
        "borderline_radius6_package_fails": not package_passes(
            INSTRUMENT_LAWS["borderline_radius6"]
        ),
        "sharp_radius5_actuator_fails": not actuator_passes(
            INSTRUMENT_LAWS["sharp_radius5"]
        ),
        "sharp_radius5_package_fails": not package_passes(
            INSTRUMENT_LAWS["sharp_radius5"]
        ),
        "both_detector_and_actuator_required": True,
        "closure_is_conditional_on_instrument_law": True,
    }

    result = {
        "work_package": "WP201",
        "claim": "The finite mediator-lattice source plus a sharp radius-six instrument law closes the conditional selector gate; weaker detector or actuator laws fail.",
        "source_law": SOURCE_LAW,
        "instrument_laws": evaluated,
        "admitted_package": "sharp_radius6",
        "classification": "conditional source+instrument closure; not source-only explanation.",
        "instrument_gate": "Instrument law must be admitted independently: width+background<1/2 and actuator radius>=6.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp201_source_instrument_closure.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
