"""WP208 exact checker: minimal five-copy readout.

WP207 derives a 1/5 cap from five copies with at most one bad subchannel. This
checker audits a minimality principle: require one-bad tolerance and strict
margin below 1/4. The least copy count satisfying bad/copies <= 1/5 is five.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


BAD_SUBCHANNELS = 1
STRICT_TARGET = Fraction(1, 4)
DECLARED_CAP = Fraction(1, 5)


def bad_fraction(copies: int) -> Fraction:
    return Fraction(BAD_SUBCHANNELS, copies)


def passes_strict_target(copies: int) -> bool:
    return bad_fraction(copies) < STRICT_TARGET


def passes_declared_cap(copies: int) -> bool:
    return bad_fraction(copies) <= DECLARED_CAP


def main() -> None:
    evaluated = {
        copies: {
            "bad_fraction": str(bad_fraction(copies)),
            "passes_strict_1_4": passes_strict_target(copies),
            "passes_declared_1_5": passes_declared_cap(copies),
        }
        for copies in range(2, 8)
    }
    minimal_strict = min(c for c in evaluated if evaluated[c]["passes_strict_1_4"])
    minimal_declared = min(c for c in evaluated if evaluated[c]["passes_declared_1_5"])

    checks = {
        "four_copies_bad_fraction_one_fourth": bad_fraction(4) == Fraction(1, 4),
        "four_fails_strict_target": not passes_strict_target(4),
        "five_copies_bad_fraction_one_fifth": bad_fraction(5) == Fraction(1, 5),
        "five_passes_strict_target": passes_strict_target(5),
        "five_passes_declared_cap": passes_declared_cap(5),
        "minimal_copies_for_strict_below_one_fourth_is_five": minimal_strict == 5,
        "minimal_copies_for_declared_one_fifth_cap_is_five": minimal_declared == 5,
        "six_copies_also_pass_but_not_minimal": passes_declared_cap(6)
        and minimal_declared < 6,
        "one_bad_tolerance_is_assumed": BAD_SUBCHANNELS == 1,
        "strict_target_needs_authority": True,
        "five_minimal_conditional_on_one_bad_and_target": True,
        "does_not_explain_why_one_bad_or_one_fourth_target": True,
    }

    result = {
        "work_package": "WP208",
        "claim": "Five readout copies are minimal if the detector architecture must tolerate one bad subchannel with strict margin below one fourth, equivalently satisfy the declared one-fifth cap.",
        "bad_subchannels": BAD_SUBCHANNELS,
        "strict_target": str(STRICT_TARGET),
        "declared_cap": str(DECLARED_CAP),
        "copy_counts": evaluated,
        "minimal_strict_target_copies": minimal_strict,
        "minimal_declared_cap_copies": minimal_declared,
        "classification": "conditional minimality of five-copy readout.",
        "remaining_gate": "Derive the one-bad tolerance and strict one-fourth target from detector/source dynamics.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp208_minimal_five_copy_readout.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
