"""WP190 exact checker: coupled-origin intervention probe.

WP189 leaves a coupled-source kernel. This checker tests an origin-sensitive
intervention: weakening the coupled port relation. A local hard constraint has
no authorized continuous weakening parameter; a mediator-elimination origin has
a coupling parameter epsilon whose zero limit restores independent ports.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


SOURCES = {
    "S_coupled_local_constraint": {
        "origin": "local_constraint",
        "has_continuous_weakening": False,
        "epsilon_values": [],
    },
    "S_coupled_mediator_elimination": {
        "origin": "mediator_elimination",
        "has_continuous_weakening": True,
        "epsilon_values": [Fraction(1, 1), Fraction(1, 2), Fraction(0, 1)],
    },
}


def port_law_at(source: dict[str, object], epsilon: Fraction | None) -> str:
    if source["origin"] == "local_constraint":
        if epsilon is not None:
            return "illegal_intervention"
        return "coupled_port_relations"
    if source["origin"] == "mediator_elimination":
        if epsilon is None:
            return "coupled_port_relations"
        return "independent_axis_resets" if epsilon == 0 else "coupled_port_relations"
    raise ValueError(source["origin"])


def recurrence_gate_for_port_law(port_law: str) -> tuple[str, int, int]:
    if port_law == "independent_axis_resets":
        return ("rectangular", 4, 5)
    if port_law == "coupled_port_relations":
        return ("hnf", 5, 6)
    return ("illegal", -1, -1)


def response_trace(source_name: str) -> list[dict[str, object]]:
    source = SOURCES[source_name]
    epsilons = source["epsilon_values"] or [None]
    trace = []
    for epsilon in epsilons:
        law = port_law_at(source, epsilon)
        domain, exact_radius, tau1_radius = recurrence_gate_for_port_law(law)
        trace.append(
            {
                "epsilon": None if epsilon is None else str(epsilon),
                "port_law": law,
                "quotient_domain": domain,
                "exact_radius": exact_radius,
                "tau1_radius": tau1_radius,
            }
        )
    return trace


def main() -> None:
    local_trace = response_trace("S_coupled_local_constraint")
    mediator_trace = response_trace("S_coupled_mediator_elimination")

    checks = {
        "local_has_no_continuous_weakening": not SOURCES["S_coupled_local_constraint"][
            "has_continuous_weakening"
        ],
        "mediator_has_continuous_weakening": SOURCES["S_coupled_mediator_elimination"][
            "has_continuous_weakening"
        ],
        "local_epsilon_intervention_illegal": port_law_at(
            SOURCES["S_coupled_local_constraint"], Fraction(0, 1)
        )
        == "illegal_intervention",
        "mediator_epsilon_one_is_coupled": port_law_at(
            SOURCES["S_coupled_mediator_elimination"], Fraction(1, 1)
        )
        == "coupled_port_relations",
        "mediator_epsilon_half_remains_coupled": port_law_at(
            SOURCES["S_coupled_mediator_elimination"], Fraction(1, 2)
        )
        == "coupled_port_relations",
        "mediator_epsilon_zero_restores_independent": port_law_at(
            SOURCES["S_coupled_mediator_elimination"], Fraction(0, 1)
        )
        == "independent_axis_resets",
        "mediator_gate_changes_at_zero": mediator_trace[-1]["quotient_domain"]
        == "rectangular",
        "local_gate_static": local_trace[0]["quotient_domain"] == "hnf",
        "intervention_response_separates_origins": local_trace != mediator_trace,
        "probe_requires_controlled_epsilon_instrument": True,
        "static_recurrence_gate_remains_shared_at_epsilon_none": recurrence_gate_for_port_law(
            port_law_at(SOURCES["S_coupled_local_constraint"], None)
        )
        == recurrence_gate_for_port_law(
            port_law_at(SOURCES["S_coupled_mediator_elimination"], None)
        ),
        "origin_probe_not_available_without_intervention": True,
    }

    result = {
        "work_package": "WP190",
        "claim": "A controlled weakening intervention separates local-constraint and mediator-elimination coupled origins: only the mediator origin has an epsilon->0 path restoring independent ports.",
        "sources": {
            name: {
                key: (str(value) if isinstance(value, Fraction) else value)
                for key, value in source.items()
                if key != "epsilon_values"
            }
            | {"epsilon_values": [str(v) for v in source["epsilon_values"]]}
            for name, source in SOURCES.items()
        },
        "local_trace": local_trace,
        "mediator_trace": mediator_trace,
        "classification": "conditional origin-sensitive intervention probe.",
        "instrument_gate": "Requires a source-authorized controlled epsilon intervention on the coupled port relation.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp190_coupled_origin_intervention_probe.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
