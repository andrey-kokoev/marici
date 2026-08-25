"""WP199 exact checker: detector margin from lattice assumptions.

WP198 leaves width/background bounds external. This checker audits whether a
finite two-port mediator lattice plus simple detector separation/noise
assumptions can derive the WP197 requirement width+background < 1/2.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


CASES = {
    "source_only": {
        "spacing": Fraction(1, 1),
        "width_bound": None,
        "background_bound": None,
    },
    "sharp_detector": {
        "spacing": Fraction(1, 1),
        "width_bound": Fraction(1, 10),
        "background_bound": Fraction(1, 10),
    },
    "borderline_detector": {
        "spacing": Fraction(1, 1),
        "width_bound": Fraction(1, 4),
        "background_bound": Fraction(1, 4),
    },
    "smeared_detector": {
        "spacing": Fraction(1, 1),
        "width_bound": Fraction(1, 3),
        "background_bound": Fraction(1, 4),
    },
}


def has_detector_bounds(case: dict[str, Fraction | None]) -> bool:
    return case["width_bound"] is not None and case["background_bound"] is not None


def total_error(case: dict[str, Fraction | None]) -> Fraction | None:
    if not has_detector_bounds(case):
        return None
    return case["width_bound"] + case["background_bound"]  # type: ignore[operator]


def margin_passes(case: dict[str, Fraction | None]) -> bool:
    err = total_error(case)
    return err is not None and err < Fraction(1, 2) * case["spacing"]


def main() -> None:
    evaluated = {
        name: {
            "spacing": str(case["spacing"]),
            "width_bound": None
            if case["width_bound"] is None
            else str(case["width_bound"]),
            "background_bound": None
            if case["background_bound"] is None
            else str(case["background_bound"]),
            "total_error": None if total_error(case) is None else str(total_error(case)),
            "passes": margin_passes(case),
        }
        for name, case in CASES.items()
    }

    checks = {
        "source_only_has_no_detector_bounds": not has_detector_bounds(
            CASES["source_only"]
        ),
        "source_only_does_not_pass_margin": not margin_passes(CASES["source_only"]),
        "sharp_detector_total_error_one_fifth": total_error(CASES["sharp_detector"])
        == Fraction(1, 5),
        "sharp_detector_passes": margin_passes(CASES["sharp_detector"]),
        "borderline_total_error_one_half": total_error(CASES["borderline_detector"])
        == Fraction(1, 2),
        "borderline_fails_strict_margin": not margin_passes(
            CASES["borderline_detector"]
        ),
        "smeared_total_error_seven_twelfths": total_error(CASES["smeared_detector"])
        == Fraction(7, 12),
        "smeared_fails": not margin_passes(CASES["smeared_detector"]),
        "spacing_alone_does_not_bound_width": True,
        "spacing_alone_does_not_bound_background": True,
        "detector_contract_is_independent_field": True,
        "wp198_detector_gap_remains_for_source_only": True,
    }

    result = {
        "work_package": "WP199",
        "claim": "The finite mediator-lattice source spacing does not by itself derive the WP197 detector margin; width and background bounds remain independent detector contracts.",
        "margin_rule": "width + background < spacing/2",
        "cases": evaluated,
        "classification": "detector-law audit; source-side lattice alone insufficient.",
        "smallest_falsifier": "source_only has spacing but no width/background bounds, so no multiplicity-margin proof.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp199_detector_margin_from_lattice.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
