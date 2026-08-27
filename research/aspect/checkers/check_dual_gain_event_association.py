from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def nonparalyzable_accept(times, recovery):
    accepted = []
    last = None
    for time in times:
        if last is None or time - last >= recovery:
            accepted.append(time)
            last = time
    return tuple(accepted)


def main() -> None:
    events = (
        {"event_id": "pulse-A", "condition": "reset", "amplitude": 2},
        {"event_id": "pulse-B", "condition": "control", "amplitude": 4},
    )
    high_gain = tuple((event["event_id"], 1, True) for event in events)
    low_gain_unlabelled = (Fraction(1, 2), Fraction(1))
    assert high_gain[0][1:] == high_gain[1][1:]

    assignments = (
        {"reset": low_gain_unlabelled[0], "control": low_gain_unlabelled[1]},
        {"reset": low_gain_unlabelled[1], "control": low_gain_unlabelled[0]},
    )
    assert assignments[0] != assignments[1]
    assert sorted(assignments[0].values()) == sorted(assignments[1].values())

    keyed_low_gain = {
        event["event_id"]: Fraction(event["amplitude"], 4) for event in events
    }
    condition_by_id = {event["event_id"]: event["condition"] for event in events}
    joined = {condition_by_id[event_id]: value for event_id, value in keyed_low_gain.items()}
    assert joined == {"reset": Fraction(1, 2), "control": Fraction(1)}

    # Two digitizers downstream of one recovering front end duplicate the same
    # censored event set. An independent low-gain front end remains live.
    pulse_times = (0, 1, 3)
    recovery = 2
    shared_front_end_events = nonparalyzable_accept(pulse_times, recovery)
    digitizer_a = shared_front_end_events
    digitizer_b = shared_front_end_events
    independent_low_gain_front_end = pulse_times
    assert shared_front_end_events == (0, 3)
    assert digitizer_a == digitizer_b
    assert independent_low_gain_front_end == (0, 1, 3)

    result = {
        "schema": "marici.aspect.dual-gain-event-association.v1",
        "status": "pass",
        "high_gain_records": [list(record) for record in high_gain],
        "unlabelled_low_gain_multiset": [str(value) for value in low_gain_unlabelled],
        "compatible_condition_assignments": [
            {key: str(value) for key, value in assignment.items()} for assignment in assignments
        ],
        "event_key_join": {key: str(value) for key, value in joined.items()},
        "pulse_times": list(pulse_times),
        "recovery_time": recovery,
        "shared_front_end_detected_times": list(shared_front_end_events),
        "duplicated_digitizers_equal": True,
        "independent_low_gain_detected_times": list(independent_low_gain_front_end),
        "verdict": "Unlabelled dual-gain records recover the marginal amplitude multiset but not which condition produced which burst. Immutable event keys restore the incidence relation. Two digitizers after one dead-time-limited front end duplicate its censored event set; only an independently live front end recovers the missed pulse in the frozen model.",
        "claim_boundary": "two keyed condition records, exact quarter gain, perfect event identifiers, and deterministic nonparalyzable recovery; no clock-key collision, pileup waveform, paralyzable dead time, tap back-action, or event-key loss",
    }
    output = Path(__file__).parents[1] / "results" / "dual_gain_event_association.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
