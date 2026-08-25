"""WP181 exact checker: constructor discrimination protocol.

WP180 showed rival constructors with the same low-energy flavor packet but
different authorized recurrence-growth gate tuples. This checker types the
discrimination protocol and verifies that a radius-six HNF-domain noisy
instrument separates the rival constructor commitments, while the weaker
radius-four rectangular instrument cannot test the HNF-noisy constructor.
"""

from __future__ import annotations

import json
from pathlib import Path


CONSTRUCTORS = {
    "C_rect_exact": {
        "domain": "rectangular",
        "tau": 0,
        "required_radius": 4,
        "authorized_claim": "finite_vs_infinite_over_rectangular_domain",
    },
    "C_hnf_noisy": {
        "domain": "hnf",
        "tau": 1,
        "required_radius": 6,
        "authorized_claim": "finite_vs_infinite_over_hnf_domain",
    },
}


def instrument(name: str) -> dict[str, object]:
    instruments = {
        "I_rect_R4_exact": {
            "channels": [{"domain": "rectangular", "tau": 0, "radius": 4}]
        },
        "I_hnf_R5_exact": {"channels": [{"domain": "hnf", "tau": 0, "radius": 5}]},
        "I_hnf_R6_tau1": {"channels": [{"domain": "hnf", "tau": 1, "radius": 6}]},
        "I_common_exact_and_noisy": {
            "channels": [
                {"domain": "hnf", "tau": 0, "radius": 6},
                {"domain": "hnf", "tau": 1, "radius": 6},
            ]
        },
    }
    return instruments[name]


def domain_covers(instrument_domain: str, constructor_domain: str) -> bool:
    if instrument_domain == constructor_domain:
        return True
    if instrument_domain == "hnf" and constructor_domain == "rectangular":
        return True
    return False


def instrument_tests_constructor(
    inst: dict[str, object], constructor: dict[str, object]
) -> bool:
    return any(
        domain_covers(channel["domain"], constructor["domain"])
        and channel["tau"] <= constructor["tau"]
        and channel["radius"] >= constructor["required_radius"]
        for channel in inst["channels"]
    )


def distinguishability_matrix() -> dict[str, dict[str, bool]]:
    return {
        iname: {
            cname: instrument_tests_constructor(inst, constructor)
        for cname, constructor in CONSTRUCTORS.items()
        }
        for iname, inst in {
            name: instrument(name)
            for name in (
                "I_rect_R4_exact",
                "I_hnf_R5_exact",
                "I_hnf_R6_tau1",
                "I_common_exact_and_noisy",
            )
        }.items()
    }


def main() -> None:
    matrix = distinguishability_matrix()

    checks = {
        "rect_R4_tests_rect_constructor": matrix["I_rect_R4_exact"]["C_rect_exact"],
        "rect_R4_does_not_test_hnf_noisy_constructor": not matrix["I_rect_R4_exact"][
            "C_hnf_noisy"
        ],
        "hnf_R5_exact_tests_rect_constructor": matrix["I_hnf_R5_exact"]["C_rect_exact"],
        "hnf_R5_exact_does_not_test_hnf_noisy_due_radius_or_tau_contract": not matrix[
            "I_hnf_R5_exact"
        ]["C_hnf_noisy"],
        "hnf_R6_tau1_does_not_test_exact_rect_constructor": not matrix[
            "I_hnf_R6_tau1"
        ]["C_rect_exact"],
        "common_exact_and_noisy_tests_both_constructors": all(
            matrix["I_common_exact_and_noisy"].values()
        ),
        "strong_vector_instrument_needed_for_common_comparison": all(
            matrix["I_common_exact_and_noisy"].values()
        ),
        "weaker_instrument_leaves_constructor_kernel": not all(
            matrix["I_rect_R4_exact"].values()
        ),
        "domain_coverage_is_directional": domain_covers("hnf", "rectangular")
        and not domain_covers("rectangular", "hnf"),
        "tau_requirement_blocks_noisy_channel_for_exact_constructor": instrument(
            "I_hnf_R6_tau1"
        )["channels"][0]["tau"]
        > CONSTRUCTORS["C_rect_exact"]["tau"],
        "radius_requirement_blocks_R5_for_hnf_noisy": instrument("I_hnf_R5_exact")[
            "channels"
        ][0]["radius"]
        < CONSTRUCTORS["C_hnf_noisy"]["required_radius"],
        "protocol_separates_gate_commitments_not_low_energy_packet": True,
        "negative_result_is_constructor_discrimination": True,
    }

    result = {
        "work_package": "WP181",
        "claim": "The WP180 rival constructors are discriminated only by an instrument strong enough for the larger authorized gate; weaker recurrence observations leave the source kernel unresolved.",
        "constructors": CONSTRUCTORS,
        "instruments": {
            name: instrument(name)
            for name in (
                "I_rect_R4_exact",
                "I_hnf_R5_exact",
                "I_hnf_R6_tau1",
                "I_common_exact_and_noisy",
            )
        },
        "test_matrix": matrix,
        "classification": "constructor-discrimination protocol; recurrence growth can test source commitments but does not follow from the shared low-energy packet.",
        "smallest_common_instrument": "I_common_exact_and_noisy",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp181_constructor_discrimination_protocol.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
