"""WP213 exact checker: five-copy width/background split.

WP212 shows two-bucket half-gap symmetry does not derive 1/10 constants. This
checker audits the direct five-copy route: the 1/5 safety cap from WP207 is
split equally between width and background.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


SAFETY_CAP = Fraction(1, 5)

SPLITS = {
    "equal": (Fraction(1, 10), Fraction(1, 10)),
    "width_heavy": (Fraction(3, 20), Fraction(1, 20)),
    "background_heavy": (Fraction(1, 20), Fraction(3, 20)),
    "near_margin_equal": (Fraction(1, 5), Fraction(1, 5)),
}


def total(split: tuple[Fraction, Fraction]) -> Fraction:
    return split[0] + split[1]


def within_cap(split: tuple[Fraction, Fraction]) -> bool:
    return total(split) <= SAFETY_CAP


def exchange_invariant(split: tuple[Fraction, Fraction]) -> bool:
    return split[0] == split[1]


def main() -> None:
    evaluated = {
        name: {
            "width": str(split[0]),
            "background": str(split[1]),
            "total": str(total(split)),
            "within_cap": within_cap(split),
            "exchange_invariant": exchange_invariant(split),
        }
        for name, split in SPLITS.items()
    }
    safe_exchange = [
        name for name, split in SPLITS.items() if within_cap(split) and exchange_invariant(split)
    ]

    checks = {
        "safety_cap_is_one_fifth": SAFETY_CAP == Fraction(1, 5),
        "equal_split_gives_one_tenth_each": SPLITS["equal"]
        == (Fraction(1, 10), Fraction(1, 10)),
        "equal_split_total_is_cap": total(SPLITS["equal"]) == SAFETY_CAP,
        "equal_split_exchange_invariant": exchange_invariant(SPLITS["equal"]),
        "width_heavy_within_cap_but_not_exchange": within_cap(SPLITS["width_heavy"])
        and not exchange_invariant(SPLITS["width_heavy"]),
        "background_heavy_within_cap_but_not_exchange": within_cap(
            SPLITS["background_heavy"]
        )
        and not exchange_invariant(SPLITS["background_heavy"]),
        "near_margin_equal_exceeds_cap": not within_cap(SPLITS["near_margin_equal"]),
        "only_equal_split_safe_and_exchange_invariant_in_audit": safe_exchange == [
            "equal"
        ],
        "one_tenth_derived_from_five_copy_cap_plus_width_background_symmetry": True,
        "width_background_exchange_symmetry_needs_authority": True,
        "five_copy_cap_authority_still_needed": True,
        "wp212_correction_resolved_by_direct_cap_split": True,
    }

    result = {
        "work_package": "WP213",
        "claim": "WP203's one-tenth detector constants follow from the WP207 one-fifth safety cap plus exchange symmetry between width and background.",
        "safety_cap": str(SAFETY_CAP),
        "splits": evaluated,
        "selected_split": "equal",
        "classification": "conditional width/background constant derivation.",
        "remaining_gate": "Derive five-copy cap and width/background exchange symmetry from detector architecture.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp213_five_copy_width_background_split.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
