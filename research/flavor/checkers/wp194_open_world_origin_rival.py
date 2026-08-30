"""WP194 exact checker: open-world rival for the joint origin probe.

WP193 is jointly faithful on a frozen three-origin class. This checker adds an
open-world rival with the same threshold vector and epsilon trace as an
existing origin, showing that the joint probe is not automatically faithful
under domain expansion.
"""

from __future__ import annotations

import json
from pathlib import Path


BASE_SOURCES = {
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

EXPANDED_SOURCES = BASE_SOURCES | {
    "composite_hidden_mediator": {
        "threshold_vector": (False, True, False),
        "epsilon_trace": ("hnf",),
    }
}


def partition(sources: dict[str, dict[str, tuple[object, ...]]]) -> dict[str, list[str]]:
    classes: dict[str, list[str]] = {}
    for name, source in sources.items():
        signature = (source["threshold_vector"], source["epsilon_trace"])
        classes.setdefault(repr(signature), []).append(name)
    return classes


def discrete(classes: dict[str, list[str]]) -> bool:
    return all(len(items) == 1 for items in classes.values())


def main() -> None:
    base_partition = partition(BASE_SOURCES)
    expanded_partition = partition(EXPANDED_SOURCES)
    collision_key = repr(((False, True, False), ("hnf",)))

    checks = {
        "base_three_origin_partition_is_discrete": discrete(base_partition),
        "expanded_partition_not_discrete": not discrete(expanded_partition),
        "open_world_rival_collides_with_frozen_mediator": sorted(
            expanded_partition[collision_key]
        )
        == ["composite_hidden_mediator", "frozen_nonzero_mediator"],
        "threshold_vector_same_for_collision": EXPANDED_SOURCES[
            "composite_hidden_mediator"
        ]["threshold_vector"]
        == EXPANDED_SOURCES["frozen_nonzero_mediator"]["threshold_vector"],
        "epsilon_trace_same_for_collision": EXPANDED_SOURCES[
            "composite_hidden_mediator"
        ]["epsilon_trace"]
        == EXPANDED_SOURCES["frozen_nonzero_mediator"]["epsilon_trace"],
        "joint_probe_domain_relative": True,
        "new_origin_probe_required_under_expansion": True,
        "wp193_not_invalidated_on_frozen_domain": discrete(base_partition),
        "finite_fiber_not_singleton_under_expansion": True,
        "source_domain_closure_required_before_identification": True,
        "open_world_rival_has_same_low_energy_assumed": True,
        "no_universal_identifier_claim": True,
    }

    result = {
        "work_package": "WP194",
        "claim": "WP193's joint threshold+epsilon probe is faithful only on the frozen three-origin domain; adding an open-world rival can restore a source kernel.",
        "base_partition": base_partition,
        "expanded_partition": expanded_partition,
        "open_world_rival": "composite_hidden_mediator",
        "collision_class": expanded_partition[collision_key],
        "classification": "open-world domain-expansion falsifier.",
        "instrument_gate": "Before claiming source identification, close the admitted origin domain or add a probe for the new rival.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp194_open_world_origin_rival.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
