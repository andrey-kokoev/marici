from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path


def admissible_matchings(source_times, detector_times, tolerance):
    matchings = []
    for permutation in itertools.permutations(range(len(detector_times))):
        if all(
            abs(source_times[source_index] - detector_times[detector_index]) <= tolerance
            for source_index, detector_index in enumerate(permutation)
        ):
            matchings.append(permutation)
    return tuple(matchings)


def main() -> None:
    source_times = (Fraction(0), Fraction(1))
    detector_times = (Fraction(2, 5), Fraction(3, 5))
    broad_tolerance = Fraction(3, 5)
    broad_matchings = admissible_matchings(source_times, detector_times, broad_tolerance)
    assert broad_matchings == ((0, 1), (1, 0))

    amplitudes = (Fraction(1, 2), Fraction(1))
    conditions = ("reset", "control")
    conditional_records = tuple(
        {conditions[k]: str(amplitudes[matching[k]]) for k in range(2)}
        for matching in broad_matchings
    )
    assert conditional_records == (
        {"reset": "1/2", "control": "1"},
        {"reset": "1", "control": "1/2"},
    )

    tight_tolerance = Fraction(1, 2)
    tight_matchings = admissible_matchings(source_times, detector_times, tight_tolerance)
    assert tight_matchings == ((0, 1),)

    # Source-carried pilot symbols separate incidence even under broad timing.
    source_pilots = ("alpha", "beta")
    detector_pilots = ("alpha", "beta")
    pilot_matchings = tuple(
        permutation
        for permutation in broad_matchings
        if all(source_pilots[k] == detector_pilots[permutation[k]] for k in range(2))
    )
    assert pilot_matchings == ((0, 1),)

    # Downstream-only row identifiers are unique but provide no crossing
    # relation to source events; they retain both temporal matchings.
    downstream_row_ids = ("row-17", "row-18")
    assert len(set(downstream_row_ids)) == 2
    assert len(broad_matchings) == 2

    result = {
        "schema": "marici.aspect.interval-clock-event-matching.v1",
        "status": "pass",
        "source_times": [str(value) for value in source_times],
        "detector_times": [str(value) for value in detector_times],
        "broad_tolerance": str(broad_tolerance),
        "broad_matching_count": len(broad_matchings),
        "compatible_matchings": [list(value) for value in broad_matchings],
        "compatible_conditional_records": list(conditional_records),
        "tight_tolerance": str(tight_tolerance),
        "tight_matching_count": len(tight_matchings),
        "source_pilot_matching_count": len(pilot_matchings),
        "downstream_unique_ids_repair_crossing": False,
        "verdict": "Distinct timestamps do not guarantee unique event incidence when clock uncertainty makes the bipartite association graph admit multiple perfect matchings. Tightening the timing bound repairs the frozen geometry; a source-carried pilot symbol repairs incidence under the broad bound. Unique identifiers created only downstream do not establish a crossing to source events.",
        "claim_boundary": "two events, exact rational timestamps, symmetric hard tolerance, no missed or extra events, perfect pilot symbols, and one-to-one matching; no probabilistic jitter, clock drift trajectory, pilot corruption, pileup, or unequal event counts",
    }
    output = Path(__file__).parents[1] / "results" / "interval_clock_event_matching.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
