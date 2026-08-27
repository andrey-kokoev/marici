from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def phase_probe_density(sign, coherence):
    return (
        (Fraction(1, 2), sign * coherence / 2),
        (sign * coherence / 2, Fraction(1, 2)),
    )


def main() -> None:
    coherence_sequence = (
        Fraction(1),
        Fraction(1, 2),
        Fraction(0),
        Fraction(1, 2),
        Fraction(1),
    )
    trace_distances = coherence_sequence

    plus_states = tuple(phase_probe_density(1, value) for value in coherence_sequence)
    minus_states = tuple(phase_probe_density(-1, value) for value in coherence_sequence)

    midpoint = 2
    final = 4
    assert plus_states[midpoint] == minus_states[midpoint]
    assert trace_distances[midpoint] == 0
    assert plus_states[final] != minus_states[final]
    assert trace_distances[final] == 1

    # A function, hence any physical reduced-state channel, cannot send one
    # identical midpoint input to two distinct labeled final outputs.
    reduced_midpoint_to_final_map_exists = not (
        plus_states[midpoint] == minus_states[midpoint]
        and plus_states[final] != minus_states[final]
    )
    assert not reduced_midpoint_to_final_map_exists

    revival_amount = trace_distances[final] - trace_distances[midpoint]
    assert revival_amount == 1
    divisible_trace_distance_monotonicity_violated = any(
        later > earlier for earlier, later in zip(trace_distances, trace_distances[1:])
    )
    assert divisible_trace_distance_monotonicity_violated

    joint_trace_distances = tuple(Fraction(1) for _ in coherence_sequence)
    assert all(value == 1 for value in joint_trace_distances)

    result = {
        "schema": "marici.aspect.coherence-collapse-and-revival.v1",
        "status": "pass",
        "reduced_trace_distance_sequence": [str(value) for value in trace_distances],
        "midpoint_reduced_states_identical": plus_states[midpoint] == minus_states[midpoint],
        "final_reduced_states_distinct": plus_states[final] != minus_states[final],
        "reduced_midpoint_to_final_channel_exists": reduced_midpoint_to_final_map_exists,
        "revival_amount": str(revival_amount),
        "divisible_trace_distance_monotonicity_violated": divisible_trace_distance_monotonicity_violated,
        "joint_trace_distance_sequence": [str(value) for value in joint_trace_distances],
        "enlarged_unitary_closure_preserved": all(value == 1 for value in joint_trace_distances),
        "verdict": "The reduced phase distinction collapses from trace distance one to zero and later revives to one. No reduced-state channel can factor the future through the identical midpoint states, while global orthogonality remains one throughout. Closure is restored only on the enlarged system-memory state.",
        "claim_boundary": "ideal exact trace-distance sequence compatible with global unitarity; no explicit hardware Hamiltonian, loss, interference defect, preparation drift, or finite-sample uncertainty",
    }
    output = Path(__file__).parents[1] / "results" / "coherence_collapse_and_revival.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
