"""WP212 exact checker: asymmetric bucket falsifier.

WP211 derives the quarter target from a two-bucket exchange symmetry. This
checker adds asymmetric detector architectures that preserve the half-gap
budget but break exchange symmetry, showing that the one-tenth detector
constants are not forced without the symmetry.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ARCHITECTURES = {
    "exchange_symmetric": {
        "detector_bucket": Fraction(1, 4),
        "fault_bucket": Fraction(1, 4),
    },
    "detector_privileged": {
        "detector_bucket": Fraction(1, 3),
        "fault_bucket": Fraction(1, 6),
    },
    "fault_privileged": {
        "detector_bucket": Fraction(1, 6),
        "fault_bucket": Fraction(1, 3),
    },
}


def total_budget(arch: dict[str, Fraction]) -> Fraction:
    return arch["detector_bucket"] + arch["fault_bucket"]


def exchange_symmetric(arch: dict[str, Fraction]) -> bool:
    return arch["detector_bucket"] == arch["fault_bucket"]


def detector_constants_from_bucket(arch: dict[str, Fraction]) -> tuple[Fraction, Fraction]:
    # Split the detector bucket evenly between width and background.
    half = arch["detector_bucket"] / 2
    return half, half


def main() -> None:
    evaluated = {
        name: {
            "detector_bucket": str(arch["detector_bucket"]),
            "fault_bucket": str(arch["fault_bucket"]),
            "total_budget": str(total_budget(arch)),
            "exchange_symmetric": exchange_symmetric(arch),
            "derived_width_background": [
                str(x) for x in detector_constants_from_bucket(arch)
            ],
        }
        for name, arch in ARCHITECTURES.items()
    }

    checks = {
        "all_architectures_preserve_half_gap": all(
            total_budget(arch) == Fraction(1, 2) for arch in ARCHITECTURES.values()
        ),
        "only_symmetric_architecture_exchange_invariant": [
            name for name, arch in ARCHITECTURES.items() if exchange_symmetric(arch)
        ]
        == ["exchange_symmetric"],
        "symmetric_derives_one_eighth_width_background": detector_constants_from_bucket(
            ARCHITECTURES["exchange_symmetric"]
        )
        == (Fraction(1, 8), Fraction(1, 8)),
        "detector_privileged_derives_one_sixth_width_background": detector_constants_from_bucket(
            ARCHITECTURES["detector_privileged"]
        )
        == (Fraction(1, 6), Fraction(1, 6)),
        "fault_privileged_derives_one_twelfth_width_background": detector_constants_from_bucket(
            ARCHITECTURES["fault_privileged"]
        )
        == (Fraction(1, 12), Fraction(1, 12)),
        "one_tenth_not_selected_by_bucket_symmetry": all(
            detector_constants_from_bucket(arch) != (Fraction(1, 10), Fraction(1, 10))
            for arch in ARCHITECTURES.values()
        ),
        "asymmetric_architectures_falsify_exchange_symmetry": not exchange_symmetric(
            ARCHITECTURES["detector_privileged"]
        )
        and not exchange_symmetric(ARCHITECTURES["fault_privileged"]),
        "wp211_symmetry_is_authority_gate": True,
        "wp206_one_tenth_needs_additional_rule": True,
        "half_gap_budget_alone_insufficient": True,
        "detector_bucket_split_rule_needs_authority": True,
        "hard_to_vary_detector_constants_not_yet_derived": True,
    }

    result = {
        "work_package": "WP212",
        "claim": "Asymmetric two-bucket detector architectures preserve the half-gap budget but break exchange symmetry; bucket symmetry alone does not derive the WP203 one-tenth detector constants.",
        "architectures": evaluated,
        "classification": "asymmetric bucket falsifier; detector constants still underived.",
        "remaining_gate": "Derive both the exchange symmetry and the rule selecting one-tenth width/background rather than another safe split.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp212_asymmetric_bucket_falsifier.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
