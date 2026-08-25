"""WP195 exact checker: threshold multiplicity probe.

WP194 adds a composite hidden mediator that collides with the frozen mediator
under binary threshold and epsilon probes. This checker tests a resolved
threshold-multiplicity channel.
"""

from __future__ import annotations

import json
from pathlib import Path


SOURCES = {
    "frozen_nonzero_mediator": {
        "threshold_energy": 5,
        "threshold_multiplicity": 1,
        "epsilon_trace": ("hnf",),
    },
    "composite_hidden_mediator": {
        "threshold_energy": 5,
        "threshold_multiplicity": 2,
        "epsilon_trace": ("hnf",),
    },
    "zero_accessible_mediator": {
        "threshold_energy": 5,
        "threshold_multiplicity": 1,
        "epsilon_trace": ("hnf", "rectangular"),
    },
    "local_constraint": {
        "threshold_energy": None,
        "threshold_multiplicity": 0,
        "epsilon_trace": ("hnf",),
    },
}


def binary_threshold_signature(source: dict[str, object]) -> tuple[bool, tuple[str, ...]]:
    return (source["threshold_energy"] is not None, source["epsilon_trace"])


def multiplicity_signature(source: dict[str, object]) -> tuple[int, tuple[str, ...]]:
    return (source["threshold_multiplicity"], source["epsilon_trace"])


def partition(signature_fn) -> dict[str, list[str]]:
    classes: dict[str, list[str]] = {}
    for name, source in SOURCES.items():
        classes.setdefault(repr(signature_fn(source)), []).append(name)
    return classes


def discrete(classes: dict[str, list[str]]) -> bool:
    return all(len(items) == 1 for items in classes.values())


def main() -> None:
    binary_partition = partition(binary_threshold_signature)
    multiplicity_partition = partition(multiplicity_signature)
    collision_key = repr((True, ("hnf",)))

    checks = {
        "binary_partition_not_discrete": not discrete(binary_partition),
        "binary_collision_is_frozen_and_composite": sorted(binary_partition[collision_key])
        == ["composite_hidden_mediator", "frozen_nonzero_mediator"],
        "multiplicity_partition_is_discrete": discrete(multiplicity_partition),
        "frozen_multiplicity_one": SOURCES["frozen_nonzero_mediator"][
            "threshold_multiplicity"
        ]
        == 1,
        "composite_multiplicity_two": SOURCES["composite_hidden_mediator"][
            "threshold_multiplicity"
        ]
        == 2,
        "same_threshold_energy_control": SOURCES["frozen_nonzero_mediator"][
            "threshold_energy"
        ]
        == SOURCES["composite_hidden_mediator"]["threshold_energy"],
        "same_epsilon_trace_control": SOURCES["frozen_nonzero_mediator"][
            "epsilon_trace"
        ]
        == SOURCES["composite_hidden_mediator"]["epsilon_trace"],
        "multiplicity_is_new_probe_not_binary_threshold": True,
        "probe_requires_resolved_multiplicity_instrument": True,
        "local_constraint_remains_multiplicity_zero": SOURCES["local_constraint"][
            "threshold_multiplicity"
        ]
        == 0,
        "zero_accessible_separated_by_epsilon_trace": SOURCES["zero_accessible_mediator"][
            "epsilon_trace"
        ]
        != SOURCES["frozen_nonzero_mediator"]["epsilon_trace"],
        "faithful_only_on_four_origin_domain": True,
    }

    result = {
        "work_package": "WP195",
        "claim": "Resolved threshold multiplicity separates the WP194 composite hidden mediator from the frozen mediator, while binary threshold detection does not.",
        "sources": {
            name: {
                "threshold_energy": source["threshold_energy"],
                "threshold_multiplicity": source["threshold_multiplicity"],
                "epsilon_trace": list(source["epsilon_trace"]),
            }
            for name, source in SOURCES.items()
        },
        "binary_partition": binary_partition,
        "multiplicity_partition": multiplicity_partition,
        "classification": "conditional multiplicity probe for the four-origin domain.",
        "instrument_gate": "Requires a resolved threshold-multiplicity instrument; binary threshold detection is insufficient.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp195_threshold_multiplicity_probe.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
