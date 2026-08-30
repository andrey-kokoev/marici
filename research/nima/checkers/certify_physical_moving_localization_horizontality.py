"""Certify the cross-prime/cutoff moving-localization result from packets."""

from __future__ import annotations

import json
from pathlib import Path

RESULTS = Path(__file__).resolve().parents[1] / "results"
OUT = RESULTS / "physical_moving_localization_horizontality_certificate.json"

PACKETS = {
    "small_envelope": (32003, 10, 5),
    "stable_base": (32003, 12, 6),
    "stable_second_prime": (32009, 12, 6),
    "stable_higher_cutoff": (32003, 12, 7),
}


def load(spec):
    prime, ambient, cutoff = spec
    path = RESULTS / (
        f"physical_moving_localization_horizontality_p{prime}_a{ambient}_c{cutoff}.json"
    )
    return path, json.loads(path.read_text(encoding="utf-8"))


def signature(packet):
    return {
        "dimensions": [
            [axis["absolute_dimension"], axis["common_dimension"]]
            for axis in packet["axes"]
        ],
        "tangent_relation_ranks": [
            [
                axis["absolute_tangent_relation_rank"],
                axis["common_tangent_relation_rank"],
            ]
            for axis in packet["axes"]
        ],
        "moving_derivative_ranks": [
            axis["moving_derivative_rank"] for axis in packet["axes"]
        ],
        "frozen_commutator_ranks": [
            axis["frozen_commutator_rank"] for axis in packet["axes"]
        ],
        "mixed_curvature_ranks": [
            axis["mixed_curvature_rank"] for axis in packet["axes"]
        ],
    }


def main():
    loaded = {name: load(spec) for name, spec in PACKETS.items()}
    signatures = {name: signature(packet) for name, (_, packet) in loaded.items()}
    expected = {
        "dimensions": [[9, 26], [9, 26]],
        "tangent_relation_ranks": [[0, 0], [0, 0]],
        "moving_derivative_ranks": [3, 3],
        "frozen_commutator_ranks": [3, 3],
        "mixed_curvature_ranks": [1, 1],
    }
    rank_failures = [
        name for name, observed in signatures.items() if observed != expected
    ]

    strong_names = ("stable_second_prime", "stable_higher_cutoff")
    strong_failures = []
    for name in strong_names:
        packet = loaded[name][1]
        if not packet.get("passed"):
            strong_failures.append({"packet": name, "reason": "presentation_not_certified"})
        if packet.get("combined_mixed_curvature_rank") != 2:
            strong_failures.append({"packet": name, "reason": "combined_rank_not_two"})
        for axis in packet["axes"]:
            if not axis.get("dual_value_channel_matches_frozen_map"):
                strong_failures.append({"packet": name, "reason": "value_channel_mismatch"})
            if axis.get("mixed_curvature_parity_ranks") != {
                "(0, 0)": 0,
                "(0, 1)": 0,
                "(1, 0)": 1,
                "(1, 1)": 0,
            }:
                strong_failures.append({"packet": name, "reason": "parity_signature_mismatch"})

    packet = {
        "schema": "marici.physical-moving-localization-horizontality-certificate.v1",
        "sources": {
            name: str(path.relative_to(RESULTS.parent.parent))
            for name, (path, _) in loaded.items()
        },
        "expected_rank_signature": expected,
        "observed_rank_signatures": signatures,
        "rank_failures": rank_failures,
        "strong_stabilized_failures": strong_failures,
        "cross_prime_stability": (
            signatures["stable_base"] == signatures["stable_second_prime"]
        ),
        "cutoff_stability": (
            signatures["stable_base"] == signatures["stable_higher_cutoff"]
        ),
    }
    packet["certified"] = (
        not rank_failures
        and not strong_failures
        and packet["cross_prime_stability"]
        and packet["cutoff_stability"]
    )
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    if not packet["certified"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
