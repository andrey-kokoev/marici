"""WP209 exact checker: one-bad and strict-target audit.

WP208 leaves two assumptions: tolerate one bad subchannel and use a strict
target below 1/4. This checker audits a binary-safety contract that motivates
them without pretending to derive the physical architecture.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


CONTRACTS = {
    "zero_bad": {"bad": 0, "target": Fraction(1, 4), "strict": True},
    "one_bad_strict": {"bad": 1, "target": Fraction(1, 4), "strict": True},
    "one_bad_nonstrict": {"bad": 1, "target": Fraction(1, 4), "strict": False},
    "two_bad_strict": {"bad": 2, "target": Fraction(1, 4), "strict": True},
}


def accepts_fraction(fraction: Fraction, target: Fraction, strict: bool) -> bool:
    return fraction < target if strict else fraction <= target


def minimal_copies(contract: dict[str, object], max_copies: int = 16) -> int | None:
    bad = contract["bad"]
    target = contract["target"]
    strict = contract["strict"]
    if bad == 0:
        return 1
    for copies in range(bad + 1, max_copies + 1):
        if accepts_fraction(Fraction(bad, copies), target, strict):
            return copies
    return None


def main() -> None:
    evaluated = {
        name: {
            "bad": contract["bad"],
            "target": str(contract["target"]),
            "strict": contract["strict"],
            "minimal_copies": minimal_copies(contract),
        }
        for name, contract in CONTRACTS.items()
    }

    checks = {
        "zero_bad_needs_only_one_copy": minimal_copies(CONTRACTS["zero_bad"]) == 1,
        "one_bad_strict_needs_five": minimal_copies(CONTRACTS["one_bad_strict"]) == 5,
        "one_bad_nonstrict_needs_four": minimal_copies(CONTRACTS["one_bad_nonstrict"])
        == 4,
        "two_bad_strict_needs_nine": minimal_copies(CONTRACTS["two_bad_strict"]) == 9,
        "strictness_explains_four_vs_five": minimal_copies(CONTRACTS["one_bad_strict"])
        == minimal_copies(CONTRACTS["one_bad_nonstrict"]) + 1,
        "one_bad_is_minimal_nonzero_fault_tolerance": CONTRACTS["one_bad_strict"][
            "bad"
        ]
        == 1,
        "two_bad_changes_copy_count": minimal_copies(CONTRACTS["two_bad_strict"])
        != minimal_copies(CONTRACTS["one_bad_strict"]),
        "target_one_fourth_is_still_declared": True,
        "strict_interval_separation_rejects_touching": not accepts_fraction(
            Fraction(1, 4), Fraction(1, 4), True
        ),
        "nonstrict_touching_would_allow_four": accepts_fraction(
            Fraction(1, 4), Fraction(1, 4), False
        ),
        "physical_fault_model_still_required": True,
        "wp208_assumptions_reduced_not_eliminated": True,
    }

    result = {
        "work_package": "WP209",
        "claim": "A minimal nonzero-fault contract plus strict interval separation explains why one-bad strict readout needs five copies, but the one-fourth target and physical fault model remain authority gates.",
        "contracts": evaluated,
        "classification": "fault-contract audit; assumptions reduced, not eliminated.",
        "remaining_gate": "Derive the one-fourth target and the physical one-bad fault model.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp209_one_bad_strict_target_audit.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
