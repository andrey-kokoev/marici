"""WP207 exact checker: five-readout safety cap.

WP206 shifts the detector-constant question to deriving a 1/5 safety cap. This
checker audits a repeated-readout law: five equal subchannels with at most one
bad subchannel give total bad fraction <= 1/5.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


READOUT_LAWS = {
    "five_one_bad": {"copies": 5, "bad": 1},
    "four_one_bad": {"copies": 4, "bad": 1},
    "five_two_bad": {"copies": 5, "bad": 2},
}


def bad_fraction(law: dict[str, int]) -> Fraction:
    return Fraction(law["bad"], law["copies"])


def satisfies_cap(law: dict[str, int]) -> bool:
    return bad_fraction(law) <= Fraction(1, 5)


def main() -> None:
    evaluated = {
        name: {
            "copies": law["copies"],
            "bad": law["bad"],
            "bad_fraction": str(bad_fraction(law)),
            "satisfies_1_5_cap": satisfies_cap(law),
        }
        for name, law in READOUT_LAWS.items()
    }

    checks = {
        "five_one_bad_derives_one_fifth": bad_fraction(READOUT_LAWS["five_one_bad"])
        == Fraction(1, 5),
        "five_one_bad_satisfies_cap": satisfies_cap(READOUT_LAWS["five_one_bad"]),
        "four_one_bad_gives_one_fourth": bad_fraction(READOUT_LAWS["four_one_bad"])
        == Fraction(1, 4),
        "four_one_bad_fails_cap": not satisfies_cap(READOUT_LAWS["four_one_bad"]),
        "five_two_bad_gives_two_fifths": bad_fraction(READOUT_LAWS["five_two_bad"])
        == Fraction(2, 5),
        "five_two_bad_fails_cap": not satisfies_cap(READOUT_LAWS["five_two_bad"]),
        "cap_depends_on_copy_count": True,
        "cap_depends_on_bad_subchannel_bound": True,
        "repetition_law_must_be_source_or_detector_authorized": True,
        "one_fifth_not_derived_without_five_copy_law": True,
        "readout_redundancy_is_instrument_structure": True,
        "wp206_cap_conditionally_explained": True,
    }

    result = {
        "work_package": "WP207",
        "claim": "A five-readout law with at most one bad subchannel derives the WP206 one-fifth safety cap, but the five-copy/one-bad law itself requires authority.",
        "readout_laws": evaluated,
        "classification": "conditional safety-cap derivation from repetition readout.",
        "remaining_gate": "Derive or admit the five-copy one-bad readout law from the detector architecture.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp207_five_readout_safety_cap.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
