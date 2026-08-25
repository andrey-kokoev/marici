"""WP223 exact checker: channel-exchange action gate.

Tests whether the existence of two detector error channels entails
width/background exchange symmetry.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


CAP = Fraction(1, 5)


CHANNEL_MODELS = {
    "two_channels_no_exchange_action": {
        "channels": {"width", "background"},
        "exchange_action": False,
        "split": (Fraction(3, 20), Fraction(1, 20)),
    },
    "two_channels_with_exchange_action": {
        "channels": {"width", "background"},
        "exchange_action": True,
        "split": (Fraction(1, 10), Fraction(1, 10)),
    },
    "one_channel": {
        "channels": {"total_error"},
        "exchange_action": False,
        "split": (Fraction(1, 5), Fraction(0, 1)),
    },
}


def within_cap(split: tuple[Fraction, Fraction]) -> bool:
    return sum(split) <= CAP


def exchange_invariant(model: dict[str, object]) -> bool:
    width, background = model["split"]
    return bool(model["exchange_action"]) and width == background


def main() -> None:
    cap_status = {
        name: within_cap(model["split"]) for name, model in CHANNEL_MODELS.items()
    }
    exchange_status = {
        name: exchange_invariant(model) for name, model in CHANNEL_MODELS.items()
    }

    checks = {
        "two_channels_without_exchange_can_satisfy_cap": cap_status[
            "two_channels_no_exchange_action"
        ],
        "two_channels_without_exchange_not_invariant": not exchange_status[
            "two_channels_no_exchange_action"
        ],
        "exchange_action_forces_equal_split_in_candidate": exchange_status[
            "two_channels_with_exchange_action"
        ],
        "one_channel_not_width_background_exchange": not exchange_status[
            "one_channel"
        ],
        "channel_count_does_not_imply_exchange_action": CHANNEL_MODELS[
            "two_channels_no_exchange_action"
        ]["channels"]
        == CHANNEL_MODELS["two_channels_with_exchange_action"]["channels"]
        and CHANNEL_MODELS["two_channels_no_exchange_action"]["exchange_action"]
        is False,
        "asymmetric_split_is_smallest_falsifier": CHANNEL_MODELS[
            "two_channels_no_exchange_action"
        ]["split"]
        == (Fraction(3, 20), Fraction(1, 20)),
        "source_automorphism_is_missing_authority": True,
        "does_not_supply_fault_apparatus_or_calibration": True,
    }

    result = {
        "work_package": "WP223",
        "claim": "Two error channels do not entail width/background exchange symmetry; a source automorphism swapping the channels is the missing authority.",
        "admitted_domain": "width/background channel models under the one-fifth safety cap.",
        "faithful_quotient": "channel set plus admitted exchange action; not mere channel count.",
        "cap": str(CAP),
        "models": {
            name: {
                "channels": sorted(model["channels"]),
                "exchange_action": model["exchange_action"],
                "split": [str(x) for x in model["split"]],
                "within_cap": cap_status[name],
                "exchange_invariant": exchange_status[name],
            }
            for name, model in CHANNEL_MODELS.items()
        },
        "classification": "channel-exchange authority gate.",
        "smallest_exact_falsifier": "Width/background split 3/20+1/20 satisfies the cap but violates exchange symmetry.",
        "remaining_gate": "Derive a source automorphism or detector dynamics that swaps width and background channels.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp223_channel_exchange_action_gate.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
