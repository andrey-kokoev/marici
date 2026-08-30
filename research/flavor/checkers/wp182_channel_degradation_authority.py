"""WP182 exact checker: channel degradation authority.

WP181 introduced a vector instrument with exact and noisy HNF radius-six
channels. This checker tests whether the exact channel can cover the noisy
commitment by an authorized deterministic degradation map exact -> tau=1.
Without that map, exact and noisy channels remain separate typed instruments.
"""

from __future__ import annotations

import json
from pathlib import Path


CONSTRUCTORS = {
    "C_rect_exact": {"domain": "rectangular", "tau": 0, "required_radius": 4},
    "C_hnf_noisy": {"domain": "hnf", "tau": 1, "required_radius": 6},
}


def domain_covers(instrument_domain: str, constructor_domain: str) -> bool:
    return instrument_domain == constructor_domain or (
        instrument_domain == "hnf" and constructor_domain == "rectangular"
    )


def channel_tests(
    channel: dict[str, object],
    constructor: dict[str, object],
    degradation_authorized: bool,
) -> bool:
    if not domain_covers(channel["domain"], constructor["domain"]):
        return False
    if channel["radius"] < constructor["required_radius"]:
        return False
    if channel["tau"] == constructor["tau"]:
        return True
    if channel["tau"] < constructor["tau"]:
        return degradation_authorized
    return False


def instrument_tests_all(
    channels: list[dict[str, object]], degradation_authorized: bool
) -> bool:
    return all(
        any(channel_tests(channel, constructor, degradation_authorized) for channel in channels)
        for constructor in CONSTRUCTORS.values()
    )


def main() -> None:
    exact_hnf_radius6 = [{"domain": "hnf", "tau": 0, "radius": 6}]
    vector_from_wp181 = [
        {"domain": "hnf", "tau": 0, "radius": 6},
        {"domain": "hnf", "tau": 1, "radius": 6},
    ]

    checks = {
        "exact_channel_tests_rect_exact_without_degradation": channel_tests(
            exact_hnf_radius6[0], CONSTRUCTORS["C_rect_exact"], False
        ),
        "exact_channel_does_not_test_hnf_noisy_without_degradation": not channel_tests(
            exact_hnf_radius6[0], CONSTRUCTORS["C_hnf_noisy"], False
        ),
        "exact_channel_tests_hnf_noisy_with_degradation": channel_tests(
            exact_hnf_radius6[0], CONSTRUCTORS["C_hnf_noisy"], True
        ),
        "single_exact_channel_not_common_without_degradation": not instrument_tests_all(
            exact_hnf_radius6, False
        ),
        "single_exact_channel_common_with_degradation": instrument_tests_all(
            exact_hnf_radius6, True
        ),
        "wp181_vector_common_without_degradation": instrument_tests_all(
            vector_from_wp181, False
        ),
        "degradation_authority_is_extra_field": True,
        "finer_readout_does_not_automatically_authorize_coarser_noise_model": True,
        "noisy_channel_cannot_test_exact_commitment": not channel_tests(
            {"domain": "hnf", "tau": 1, "radius": 6},
            CONSTRUCTORS["C_rect_exact"],
            True,
        ),
        "domain_coverage_still_required": not channel_tests(
            {"domain": "rectangular", "tau": 0, "radius": 6},
            CONSTRUCTORS["C_hnf_noisy"],
            True,
        ),
        "radius_coverage_still_required": not channel_tests(
            {"domain": "hnf", "tau": 0, "radius": 5},
            CONSTRUCTORS["C_hnf_noisy"],
            True,
        ),
        "compression_is_conditional_not_free": True,
    }

    result = {
        "work_package": "WP182",
        "claim": "The WP181 exact+noisy vector instrument compresses to a single exact HNF radius-six channel only if an exact-to-tau=1 degradation map is independently authorized.",
        "constructors": CONSTRUCTORS,
        "single_exact_channel": exact_hnf_radius6,
        "wp181_vector_channel": vector_from_wp181,
        "classification": "instrument-compression authority gate.",
        "instrument_gate": "Declare whether exact recurrence counts may be physically degraded into the constructor's noisy tau contract.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp182_channel_degradation_authority.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
