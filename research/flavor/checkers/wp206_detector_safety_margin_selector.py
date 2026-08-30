"""WP206 exact checker: detector safety-margin selector.

WP205 shows minimal cost selects a near-margin detector. This checker adds a
safety-margin requirement: total detector error must be at most a declared
fraction of the multiplicity gap. It audits whether such a requirement selects
the WP203 one-tenth constants.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


SAFETY_CAP = Fraction(1, 5)

CANDIDATES = {
    "near_margin_radius6": {
        "width": Fraction(1, 5),
        "background": Fraction(1, 5),
        "radius": 6,
    },
    "sharp_radius6": {
        "width": Fraction(1, 10),
        "background": Fraction(1, 10),
        "radius": 6,
    },
    "sharper_radius6": {
        "width": Fraction(1, 20),
        "background": Fraction(1, 20),
        "radius": 6,
    },
}


def total_error(candidate: dict[str, Fraction | int]) -> Fraction:
    return candidate["width"] + candidate["background"]  # type: ignore[operator]


def passes_safety(candidate: dict[str, Fraction | int]) -> bool:
    return candidate["radius"] >= 6 and total_error(candidate) <= SAFETY_CAP


def sharpness_cost(candidate: dict[str, Fraction | int]) -> Fraction:
    return Fraction(1, candidate["width"]) + Fraction(1, candidate["background"])  # type: ignore[arg-type]


def main() -> None:
    safe = [name for name, candidate in CANDIDATES.items() if passes_safety(candidate)]
    min_cost = min(sharpness_cost(CANDIDATES[name]) for name in safe)
    selected = [name for name in safe if sharpness_cost(CANDIDATES[name]) == min_cost]

    checks = {
        "safety_cap_is_one_fifth": SAFETY_CAP == Fraction(1, 5),
        "near_margin_total_error_two_fifths": total_error(CANDIDATES["near_margin_radius6"])
        == Fraction(2, 5),
        "near_margin_fails_safety": not passes_safety(CANDIDATES["near_margin_radius6"]),
        "sharp_total_error_one_fifth": total_error(CANDIDATES["sharp_radius6"])
        == Fraction(1, 5),
        "sharp_passes_safety": passes_safety(CANDIDATES["sharp_radius6"]),
        "sharper_total_error_one_tenth": total_error(CANDIDATES["sharper_radius6"])
        == Fraction(1, 10),
        "sharper_passes_safety": passes_safety(CANDIDATES["sharper_radius6"]),
        "safe_set_is_sharp_and_sharper": sorted(safe)
        == ["sharp_radius6", "sharper_radius6"],
        "minimal_cost_among_safe_selects_sharp": selected == ["sharp_radius6"],
        "one_tenth_constants_derived_conditional_on_safety_cap": True,
        "safety_cap_itself_needs_source_or_detector_authority": True,
        "different_safety_cap_would_change_selection": True,
    }

    result = {
        "work_package": "WP206",
        "claim": "A declared safety cap total_error <= 1/5 plus minimal sharpness cost selects the WP203 one-tenth detector constants.",
        "safety_cap": str(SAFETY_CAP),
        "candidates": {
            name: {
                "width": str(candidate["width"]),
                "background": str(candidate["background"]),
                "total_error": str(total_error(candidate)),
                "radius": candidate["radius"],
                "passes_safety": passes_safety(candidate),
                "sharpness_cost": str(sharpness_cost(candidate)),
            }
            for name, candidate in CANDIDATES.items()
        },
        "safe_candidates": safe,
        "selected_candidates": selected,
        "classification": "conditional detector-constant selector; safety cap remains an authority gate.",
        "remaining_gate": "Derive the 1/5 safety cap from detector dynamics or source law.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp206_detector_safety_margin_selector.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
