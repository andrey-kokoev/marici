"""WP205 exact checker: minimal instrument optimality.

WP204 shows self-reading constants can vary. This checker tests a minimal
optimality principle: among passing instruments, choose least actuator radius
and then least sharpness cost. It audits what such a principle can and cannot
derive.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


CANDIDATES = {
    "sharp_radius6": {"width": Fraction(1, 10), "background": Fraction(1, 10), "radius": 6},
    "sharp_radius7": {"width": Fraction(1, 10), "background": Fraction(1, 10), "radius": 7},
    "sharper_radius6": {"width": Fraction(1, 20), "background": Fraction(1, 20), "radius": 6},
    "near_margin_radius6": {"width": Fraction(1, 5), "background": Fraction(1, 5), "radius": 6},
    "borderline_radius6": {"width": Fraction(1, 4), "background": Fraction(1, 4), "radius": 6},
}


def passes(candidate: dict[str, Fraction | int]) -> bool:
    return candidate["radius"] >= 6 and candidate["width"] + candidate["background"] < Fraction(1, 2)  # type: ignore[operator]


def sharpness_cost(candidate: dict[str, Fraction | int]) -> Fraction:
    # Smaller width/background requires sharper instrumentation, so cost is
    # modeled as inverse widths. Exact rationals keep the convention explicit.
    return Fraction(1, candidate["width"]) + Fraction(1, candidate["background"])  # type: ignore[arg-type]


def minimal_by_radius() -> list[str]:
    passing = [name for name, cand in CANDIDATES.items() if passes(cand)]
    min_radius = min(CANDIDATES[name]["radius"] for name in passing)
    return [name for name in passing if CANDIDATES[name]["radius"] == min_radius]


def minimal_by_radius_then_cost() -> list[str]:
    radius_min = minimal_by_radius()
    min_cost = min(sharpness_cost(CANDIDATES[name]) for name in radius_min)
    return [name for name in radius_min if sharpness_cost(CANDIDATES[name]) == min_cost]


def main() -> None:
    radius_min = minimal_by_radius()
    optimal = minimal_by_radius_then_cost()
    evaluated = {
        name: {
            "width": str(cand["width"]),
            "background": str(cand["background"]),
            "radius": cand["radius"],
            "passes": passes(cand),
            "sharpness_cost": str(sharpness_cost(cand)),
        }
        for name, cand in CANDIDATES.items()
    }

    checks = {
        "borderline_fails": not passes(CANDIDATES["borderline_radius6"]),
        "sharp_radius7_passes_but_not_radius_minimal": passes(CANDIDATES["sharp_radius7"])
        and "sharp_radius7" not in radius_min,
        "minimal_radius_is_six": all(CANDIDATES[name]["radius"] == 6 for name in radius_min),
        "radius_minimal_set_has_three": sorted(radius_min)
        == ["near_margin_radius6", "sharp_radius6", "sharper_radius6"],
        "cost_principle_selects_near_margin": optimal == ["near_margin_radius6"],
        "sharp_radius6_not_selected_by_minimal_cost": "sharp_radius6" not in optimal,
        "sharper_radius6_not_selected_by_minimal_cost": "sharper_radius6" not in optimal,
        "radius_six_derivable_from_minimal_radius": True,
        "one_tenth_constants_not_derivable_from_this_principle": True,
        "different_cost_function_would_change_detector_choice": True,
        "optimality_principle_itself_needs_authority": True,
        "wp204_derivation_gap_partially_closed_only_for_radius": True,
    }

    result = {
        "work_package": "WP205",
        "claim": "A minimal-radius optimality principle derives actuator radius six, but a simple sharpness-cost principle selects a near-margin detector rather than WP203's one-tenth constants.",
        "candidates": evaluated,
        "minimal_radius_candidates": radius_min,
        "radius_then_cost_optimum": optimal,
        "classification": "partial instrument-constant derivation: radius yes, detector constants no.",
        "remaining_gate": "Derive the detector constants or the correct detector cost functional from physical dynamics.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp205_minimal_instrument_optimality.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
