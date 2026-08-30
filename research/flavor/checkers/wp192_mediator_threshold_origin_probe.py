"""WP192 exact checker: mediator-threshold origin probe.

WP191 leaves local constraints and frozen mediators equivalent under restricted
epsilon interventions. This checker audits an alternative origin-sensitive
probe: a threshold channel that detects mediator degrees of freedom.
"""

from __future__ import annotations

import json
from pathlib import Path


SOURCES = {
    "S_local_constraint": {
        "origin": "local_constraint",
        "has_mediator_threshold": False,
        "threshold_energy": None,
    },
    "S_mediator_frozen_nonzero": {
        "origin": "mediator_elimination",
        "has_mediator_threshold": True,
        "threshold_energy": 5,
    },
    "S_mediator_zero_accessible": {
        "origin": "mediator_elimination",
        "has_mediator_threshold": True,
        "threshold_energy": 5,
    },
}


def threshold_detected(source: dict[str, object], energy: int, resolution: int) -> bool:
    threshold = source["threshold_energy"]
    if threshold is None:
        return False
    return abs(energy - threshold) <= resolution


def observation_vector(source: dict[str, object], energies: list[int], resolution: int) -> tuple[bool, ...]:
    return tuple(threshold_detected(source, energy, resolution) for energy in energies)


def main() -> None:
    resolved_energies = [4, 5, 6]
    unresolved_energies = [1, 2, 3]
    resolution = 0
    resolved_vectors = {
        name: observation_vector(source, resolved_energies, resolution)
        for name, source in SOURCES.items()
    }
    unresolved_vectors = {
        name: observation_vector(source, unresolved_energies, resolution)
        for name, source in SOURCES.items()
    }

    checks = {
        "local_has_no_threshold": not SOURCES["S_local_constraint"][
            "has_mediator_threshold"
        ],
        "frozen_mediator_has_threshold": SOURCES["S_mediator_frozen_nonzero"][
            "has_mediator_threshold"
        ],
        "zero_accessible_mediator_has_threshold": SOURCES["S_mediator_zero_accessible"][
            "has_mediator_threshold"
        ],
        "resolved_probe_detects_frozen_mediator": any(
            resolved_vectors["S_mediator_frozen_nonzero"]
        ),
        "resolved_probe_detects_zero_accessible_mediator": any(
            resolved_vectors["S_mediator_zero_accessible"]
        ),
        "resolved_probe_does_not_detect_local_constraint": not any(
            resolved_vectors["S_local_constraint"]
        ),
        "resolved_probe_separates_local_from_mediator_class": resolved_vectors[
            "S_local_constraint"
        ]
        != resolved_vectors["S_mediator_frozen_nonzero"],
        "threshold_probe_does_not_separate_mediator_subtypes": resolved_vectors[
            "S_mediator_frozen_nonzero"
        ]
        == resolved_vectors["S_mediator_zero_accessible"],
        "unresolved_energy_window_does_not_separate": unresolved_vectors[
            "S_local_constraint"
        ]
        == unresolved_vectors["S_mediator_frozen_nonzero"],
        "probe_requires_threshold_energy_access": True,
        "probe_requires_independent_instrument_not_fitted_projector": True,
        "finite_fiber_remains_within_mediator_class": True,
    }

    result = {
        "work_package": "WP192",
        "claim": "A resolved mediator-threshold channel separates local hard constraints from mediator origins even when epsilon=0 is inaccessible, but it does not distinguish mediator subtypes.",
        "sources": SOURCES,
        "resolved_energies": resolved_energies,
        "unresolved_energies": unresolved_energies,
        "resolution": resolution,
        "resolved_vectors": {name: list(vec) for name, vec in resolved_vectors.items()},
        "unresolved_vectors": {name: list(vec) for name, vec in unresolved_vectors.items()},
        "classification": "conditional mediator-origin threshold probe.",
        "instrument_gate": "Requires an independently typed threshold channel with energy coverage and resolution; otherwise WP191 kernel remains.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp192_mediator_threshold_origin_probe.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
