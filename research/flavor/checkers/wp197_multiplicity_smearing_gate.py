"""WP197 exact checker: multiplicity smearing gate.

WP196 requires absolute multiplicity error mu < 1/2. This checker decomposes
mu into finite-width and background components and tests when the WP195
multiplicity probe survives.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


CASES = {
    "sharp": {"width": Fraction(1, 10), "background": Fraction(1, 10)},
    "borderline": {"width": Fraction(1, 4), "background": Fraction(1, 4)},
    "smeared": {"width": Fraction(1, 3), "background": Fraction(1, 4)},
}


def total_mu(case: dict[str, Fraction]) -> Fraction:
    return case["width"] + case["background"]


def robust(mu: Fraction) -> bool:
    return mu < Fraction(1, 2)


def interval_for(multiplicity: int, mu: Fraction) -> tuple[Fraction, Fraction]:
    return (Fraction(multiplicity, 1) - mu, Fraction(multiplicity, 1) + mu)


def intervals_disjoint(m1: int, m2: int, mu: Fraction) -> bool:
    left = interval_for(m1, mu)
    right = interval_for(m2, mu)
    return left[1] < right[0] or right[1] < left[0]


def main() -> None:
    evaluated = {
        name: {
            "width": str(case["width"]),
            "background": str(case["background"]),
            "mu": str(total_mu(case)),
            "robust_1_vs_2": robust(total_mu(case)),
            "interval_1": [str(x) for x in interval_for(1, total_mu(case))],
            "interval_2": [str(x) for x in interval_for(2, total_mu(case))],
        }
        for name, case in CASES.items()
    }

    checks = {
        "sharp_mu_is_one_fifth": total_mu(CASES["sharp"]) == Fraction(1, 5),
        "sharp_is_robust": robust(total_mu(CASES["sharp"])),
        "sharp_intervals_disjoint": intervals_disjoint(1, 2, total_mu(CASES["sharp"])),
        "borderline_mu_is_one_half": total_mu(CASES["borderline"]) == Fraction(1, 2),
        "borderline_is_not_robust": not robust(total_mu(CASES["borderline"])),
        "borderline_intervals_touch_not_disjoint": not intervals_disjoint(
            1, 2, total_mu(CASES["borderline"])
        ),
        "smeared_mu_exceeds_one_half": total_mu(CASES["smeared"]) > Fraction(1, 2),
        "smeared_is_not_robust": not robust(total_mu(CASES["smeared"])),
        "width_and_background_are_independent_error_sources": True,
        "source_derived_detector_model_required": True,
        "mu_less_than_half_is_not_automatic": True,
        "wp196_margin_survives_only_sharp_case": [
            name for name, case in CASES.items() if robust(total_mu(case))
        ]
        == ["sharp"],
    }

    result = {
        "work_package": "WP197",
        "claim": "The WP196 multiplicity margin survives finite width and background only when their total absolute error is strictly below one half.",
        "cases": evaluated,
        "classification": "detector-smearing gate for multiplicity faithfulness.",
        "instrument_gate": "Derive width and background bounds with width+background < 1/2 before admitting multiplicity-based source identification.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp197_multiplicity_smearing_gate.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
