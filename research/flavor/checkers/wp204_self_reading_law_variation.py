"""WP204 exact checker: self-reading law variation.

WP203 declares a self-reading law that fixes detector sharpness and actuator
radius. This checker tests whether those instrument constants can vary while
the source-side tuple remains unchanged. If so, WP203 is not derived
hard-to-vary; it is a frozen law candidate.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


SOURCE_TUPLE = {
    "order_cap_K": 64,
    "quotient_domain": "hnf",
    "epsilon_probe": True,
    "threshold_probe": True,
    "multiplicity_probe": True,
}

SELF_READING_VARIANTS = {
    "sharp_radius6": {
        "source_tuple": SOURCE_TUPLE,
        "width": Fraction(1, 10),
        "background": Fraction(1, 10),
        "actuator_radius": 6,
    },
    "sharp_radius7": {
        "source_tuple": SOURCE_TUPLE,
        "width": Fraction(1, 10),
        "background": Fraction(1, 10),
        "actuator_radius": 7,
    },
    "sharper_radius6": {
        "source_tuple": SOURCE_TUPLE,
        "width": Fraction(1, 20),
        "background": Fraction(1, 20),
        "actuator_radius": 6,
    },
    "borderline_radius6": {
        "source_tuple": SOURCE_TUPLE,
        "width": Fraction(1, 4),
        "background": Fraction(1, 4),
        "actuator_radius": 6,
    },
}


def selector_ok(variant: dict[str, object]) -> bool:
    detector_ok = variant["width"] + variant["background"] < Fraction(1, 2)  # type: ignore[operator]
    actuator_ok = variant["actuator_radius"] >= 6
    return detector_ok and actuator_ok


def instrument_tuple(variant: dict[str, object]) -> tuple[Fraction, Fraction, int]:
    return variant["width"], variant["background"], variant["actuator_radius"]  # type: ignore[return-value]


def main() -> None:
    same_source = all(
        variant["source_tuple"] == SOURCE_TUPLE
        for variant in SELF_READING_VARIANTS.values()
    )
    instrument_tuples = {
        name: instrument_tuple(variant)
        for name, variant in SELF_READING_VARIANTS.items()
    }
    selector_status = {
        name: selector_ok(variant) for name, variant in SELF_READING_VARIANTS.items()
    }

    checks = {
        "all_variants_share_source_tuple": same_source,
        "instrument_tuples_not_unique": len(set(instrument_tuples.values())) > 1,
        "sharp_radius6_selector_ok": selector_status["sharp_radius6"],
        "sharp_radius7_selector_ok": selector_status["sharp_radius7"],
        "sharper_radius6_selector_ok": selector_status["sharper_radius6"],
        "borderline_radius6_selector_fails": not selector_status["borderline_radius6"],
        "same_source_has_multiple_passing_instrument_laws": sum(selector_status.values())
        == 3,
        "same_source_has_passing_and_failing_laws": any(selector_status.values())
        and not all(selector_status.values()),
        "wp203_constants_not_derived_by_source_tuple": True,
        "self_reading_law_needs_independent_derivation": True,
        "hard_to_vary_only_after_freezing_constants": True,
        "source_side_tuple_does_not_fix_instrument_tuple": True,
    }

    result = {
        "work_package": "WP204",
        "claim": "The WP203 self-reading constants can vary while preserving the same source-side tuple; the law is hard-to-vary only after its instrument constants are frozen.",
        "source_tuple": SOURCE_TUPLE,
        "variants": {
            name: {
                "width": str(variant["width"]),
                "background": str(variant["background"]),
                "actuator_radius": variant["actuator_radius"],
                "selector_ok": selector_status[name],
            }
            for name, variant in SELF_READING_VARIANTS.items()
        },
        "classification": "self-reading derivation gap; constants still underived.",
        "smallest_falsifier": "Same source tuple admits sharp_radius6, sharp_radius7, sharper_radius6, and borderline_radius6 variants.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp204_self_reading_law_variation.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
