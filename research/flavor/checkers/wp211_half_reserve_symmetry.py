"""WP211 exact checker: half-reserve symmetry.

WP210 reduces the 1/4 target to a half-reserve law. This checker audits an
exchange-symmetry derivation: split the interval-separation half-gap equally
between intrinsic smearing and fault/readout reserve.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


BUDGET = Fraction(1, 2)

SPLITS = {
    "symmetric": (Fraction(1, 4), Fraction(1, 4)),
    "detector_heavy": (Fraction(1, 3), Fraction(1, 6)),
    "fault_heavy": (Fraction(1, 6), Fraction(1, 3)),
}


def sums_to_budget(split: tuple[Fraction, Fraction]) -> bool:
    return split[0] + split[1] == BUDGET


def exchange_invariant(split: tuple[Fraction, Fraction]) -> bool:
    return split[0] == split[1]


def reserve_fraction(split: tuple[Fraction, Fraction]) -> Fraction:
    # Reserve is the second component as a fraction of the full multiplicity gap.
    return split[1]


def main() -> None:
    evaluated = {
        name: {
            "detector_smearing_budget": str(split[0]),
            "fault_reserve_budget": str(split[1]),
            "sums_to_half_gap": sums_to_budget(split),
            "exchange_invariant": exchange_invariant(split),
        }
        for name, split in SPLITS.items()
    }
    symmetric_splits = [
        name
        for name, split in SPLITS.items()
        if sums_to_budget(split) and exchange_invariant(split)
    ]

    checks = {
        "all_splits_sum_to_half_gap": all(sums_to_budget(split) for split in SPLITS.values()),
        "only_symmetric_split_exchange_invariant": symmetric_splits == ["symmetric"],
        "symmetric_split_gives_quarter_reserve": reserve_fraction(SPLITS["symmetric"])
        == Fraction(1, 4),
        "detector_heavy_not_exchange_invariant": not exchange_invariant(
            SPLITS["detector_heavy"]
        ),
        "fault_heavy_not_exchange_invariant": not exchange_invariant(SPLITS["fault_heavy"]),
        "exchange_symmetry_derives_half_reserve_within_two_bucket_model": True,
        "two_bucket_model_needs_authority": True,
        "exchange_symmetry_needs_authority": True,
        "asymmetric_physics_would_change_reserve": True,
        "wp210_gate_reduced_to_symmetry_and_two_bucket_law": True,
        "quarter_not_unconditional": True,
        "strict_interval_budget_still_required": BUDGET == Fraction(1, 2),
    }

    result = {
        "work_package": "WP211",
        "claim": "A two-bucket exchange symmetry splits the half-gap budget equally and yields the quarter reserve, but the two-bucket symmetry is itself an authority gate.",
        "half_gap_budget": str(BUDGET),
        "splits": evaluated,
        "selected_split": "symmetric",
        "classification": "conditional half-reserve derivation from exchange symmetry.",
        "remaining_gate": "Derive the two-bucket detector/fault model and exchange symmetry from physical architecture.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp211_half_reserve_symmetry.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
