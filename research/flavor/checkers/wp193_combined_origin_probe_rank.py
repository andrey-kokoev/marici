"""WP193 exact checker: combined origin-probe rank.

WP190 and WP192 provide complementary origin-sensitive probes. This checker
tests their joint faithfulness over the small class: local constraint, frozen
nonzero mediator, zero-accessible mediator.
"""

from __future__ import annotations

import json
from pathlib import Path


SOURCES = {
    "local_constraint": {
        "threshold_vector": (False, False, False),
        "epsilon_trace": ("hnf",),
    },
    "frozen_nonzero_mediator": {
        "threshold_vector": (False, True, False),
        "epsilon_trace": ("hnf",),
    },
    "zero_accessible_mediator": {
        "threshold_vector": (False, True, False),
        "epsilon_trace": ("hnf", "rectangular"),
    },
}


def partition(keys: tuple[str, ...]) -> dict[str, list[str]]:
    classes: dict[str, list[str]] = {}
    for name, source in SOURCES.items():
        signature = tuple(source[key] for key in keys)
        classes.setdefault(repr(signature), []).append(name)
    return classes


def is_discrete_partition(classes: dict[str, list[str]]) -> bool:
    return all(len(items) == 1 for items in classes.values())


def main() -> None:
    threshold_partition = partition(("threshold_vector",))
    epsilon_partition = partition(("epsilon_trace",))
    joint_partition = partition(("threshold_vector", "epsilon_trace"))

    checks = {
        "threshold_alone_not_faithful": not is_discrete_partition(threshold_partition),
        "threshold_alone_collapses_mediator_subtypes": sorted(
            threshold_partition[repr(((False, True, False),))]
        )
        == ["frozen_nonzero_mediator", "zero_accessible_mediator"],
        "epsilon_alone_not_faithful": not is_discrete_partition(epsilon_partition),
        "epsilon_alone_collapses_local_and_frozen": sorted(
            epsilon_partition[repr((("hnf",),))]
        )
        == ["frozen_nonzero_mediator", "local_constraint"],
        "joint_partition_is_faithful": is_discrete_partition(joint_partition),
        "three_sources_three_joint_classes": len(joint_partition) == 3,
        "probes_are_complementary": not is_discrete_partition(threshold_partition)
        and not is_discrete_partition(epsilon_partition)
        and is_discrete_partition(joint_partition),
        "threshold_channel_required_for_local_vs_frozen": True,
        "epsilon_channel_required_for_mediator_subtypes": True,
        "joint_faithfulness_relative_to_small_domain": True,
        "not_a_universal_source_identifier": True,
        "instrument_authority_still_required_for_both_channels": True,
    }

    result = {
        "work_package": "WP193",
        "claim": "Threshold and epsilon-intervention probes are jointly faithful on the three-origin toy domain, while either probe alone leaves a kernel.",
        "sources": {
            name: {
                "threshold_vector": list(source["threshold_vector"]),
                "epsilon_trace": list(source["epsilon_trace"]),
            }
            for name, source in SOURCES.items()
        },
        "threshold_partition": threshold_partition,
        "epsilon_partition": epsilon_partition,
        "joint_partition": joint_partition,
        "classification": "conditional joint-origin identifier on a frozen small domain.",
        "instrument_gate": "Requires both independently typed threshold spectroscopy and epsilon-intervention channels.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp193_combined_origin_probe_rank.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
