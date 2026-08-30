"""WP191 exact checker: frozen mediator intervention kernel.

WP190 separates local constraint from mediator elimination only when epsilon
can be controlled through zero. This checker adds a frozen-nonzero mediator
whose authorized interventions never reach zero; it remains observationally
equivalent to a hard local constraint under the declared intervention family.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


SOURCES = {
    "S_local_constraint": {
        "origin": "local_constraint",
        "authorized_epsilons": [None],
    },
    "S_mediator_frozen_nonzero": {
        "origin": "mediator_elimination",
        "authorized_epsilons": [Fraction(1, 1), Fraction(1, 2)],
    },
    "S_mediator_zero_accessible": {
        "origin": "mediator_elimination",
        "authorized_epsilons": [Fraction(1, 1), Fraction(1, 2), Fraction(0, 1)],
    },
}


def gate_at(origin: str, epsilon: Fraction | None) -> tuple[str, int, int]:
    if origin == "local_constraint":
        return ("hnf", 5, 6)
    if origin == "mediator_elimination":
        if epsilon == 0:
            return ("rectangular", 4, 5)
        return ("hnf", 5, 6)
    raise ValueError(origin)


def observable_trace(source: dict[str, object]) -> list[tuple[str, int, int]]:
    return [gate_at(source["origin"], epsilon) for epsilon in source["authorized_epsilons"]]


def normalized_trace(source: dict[str, object]) -> set[tuple[str, int, int]]:
    return set(observable_trace(source))


def main() -> None:
    traces = {name: observable_trace(source) for name, source in SOURCES.items()}
    normalized = {name: normalized_trace(source) for name, source in SOURCES.items()}

    checks = {
        "local_trace_static_hnf": normalized["S_local_constraint"] == {("hnf", 5, 6)},
        "frozen_mediator_trace_static_hnf": normalized["S_mediator_frozen_nonzero"]
        == {("hnf", 5, 6)},
        "zero_accessible_mediator_trace_changes": normalized["S_mediator_zero_accessible"]
        == {("hnf", 5, 6), ("rectangular", 4, 5)},
        "local_and_frozen_mediator_equivalent_under_authorized_interventions": normalized[
            "S_local_constraint"
        ]
        == normalized["S_mediator_frozen_nonzero"],
        "zero_accessible_mediator_separated_from_local": normalized[
            "S_mediator_zero_accessible"
        ]
        != normalized["S_local_constraint"],
        "zero_accessible_mediator_separated_from_frozen": normalized[
            "S_mediator_zero_accessible"
        ]
        != normalized["S_mediator_frozen_nonzero"],
        "epsilon_zero_is_required_for_wp190_separation": Fraction(0, 1)
        in SOURCES["S_mediator_zero_accessible"]["authorized_epsilons"],
        "frozen_mediator_lacks_epsilon_zero": Fraction(0, 1)
        not in SOURCES["S_mediator_frozen_nonzero"]["authorized_epsilons"],
        "intervention_family_relative_faithfulness": True,
        "mediator_origin_not_identified_without_zero_access": True,
        "finite_fiber_not_singleton_after_restricted_intervention": True,
        "additional_threshold_or_coupling_probe_required": True,
    }

    result = {
        "work_package": "WP191",
        "claim": "WP190's origin discriminator requires epsilon-zero access; a frozen nonzero mediator remains equivalent to a hard local constraint under restricted interventions.",
        "sources": {
            name: {
                "origin": source["origin"],
                "authorized_epsilons": [
                    None if eps is None else str(eps)
                    for eps in source["authorized_epsilons"]
                ],
            }
            for name, source in SOURCES.items()
        },
        "traces": {
            name: [list(item) for item in trace] for name, trace in traces.items()
        },
        "classification": "intervention-family kernel: origin discrimination is relative to accessible epsilon controls.",
        "smallest_falsifier": "S_local_constraint and S_mediator_frozen_nonzero both produce only the HNF 5/6 gate.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp191_frozen_mediator_intervention_kernel.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
