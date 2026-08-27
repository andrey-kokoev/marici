from __future__ import annotations

import json
from collections import Counter
from fractions import Fraction
from pathlib import Path


def main() -> None:
    source = (
        {"time": Fraction(0), "pilot": "alpha"},
        {"time": Fraction(1), "pilot": "beta"},
        {"time": Fraction(2), "pilot": "gamma"},
    )
    detector = (
        {"time": Fraction(0), "pilot": "alpha", "amplitude": Fraction(1)},
        {"time": Fraction(2), "pilot": "gamma", "amplitude": Fraction(4)},
        {"time": Fraction(21, 10), "pilot": "gamma", "amplitude": Fraction(1)},
    )
    assert len(source) == len(detector) == 3

    # Forced order matching fabricates a beta record from a gamma detection.
    forced = tuple((source[k]["pilot"], detector[k]["pilot"]) for k in range(3))
    assert forced == (("alpha", "alpha"), ("beta", "gamma"), ("gamma", "gamma"))

    source_counts = Counter(event["pilot"] for event in source)
    detector_counts = Counter(event["pilot"] for event in detector)
    missing = source_counts - detector_counts
    extra = detector_counts - source_counts
    assert missing == Counter({"beta": 1})
    assert extra == Counter({"gamma": 1})

    # Pilot-aware partial matching still cannot tell which gamma record is the
    # source response and which is a copied afterpulse.
    gamma_candidates = tuple(
        (event["time"], event["amplitude"])
        for event in detector
        if event["pilot"] == "gamma"
    )
    assert gamma_candidates == (
        (Fraction(2), Fraction(4)),
        (Fraction(21, 10), Fraction(1)),
    )
    assert len(gamma_candidates) == 2

    # A detector-memory reset suppresses the frozen afterpulse while preserving
    # the source-tagged gamma event. Its causal authority requires a source tap.
    reset_detector = detector[:2]
    reset_counts = Counter(event["pilot"] for event in reset_detector)
    assert reset_counts == Counter({"alpha": 1, "gamma": 1})
    reset_gamma_candidates = tuple(
        (event["time"], event["amplitude"])
        for event in reset_detector
        if event["pilot"] == "gamma"
    )
    assert reset_gamma_candidates == ((Fraction(2), Fraction(4)),)

    result = {
        "schema": "marici.aspect.partial-event-matching-afterpulse.v1",
        "status": "pass",
        "equal_source_detector_counts": True,
        "forced_complete_matching": [list(pair) for pair in forced],
        "missing_source_pilots": dict(missing),
        "extra_detector_pilots": dict(extra),
        "gamma_candidates_before_reset": [
            [str(time), str(amplitude)] for time, amplitude in gamma_candidates
        ],
        "gamma_candidate_count_before_reset": 2,
        "gamma_candidates_after_reset": [
            [str(time), str(amplitude)] for time, amplitude in reset_gamma_candidates
        ],
        "gamma_candidate_count_after_reset": 1,
        "verdict": "Equal source and detector counts can conceal one missed source event plus one extra detector event. Forced complete matching fabricates beta incidence. Source pilots expose missing beta and excess gamma, but a copied gamma pilot leaves parent-versus-afterpulse provenance ambiguous. A detector-memory reset separates the frozen pair only when a source tap verifies source invariance under reset.",
        "claim_boundary": "three exact source triggers, one missed beta record, one gamma-tagged afterpulse, perfect pilot reading, and a reset that suppresses only the afterpulse; no pilot corruption, multiple afterpulse generations, reset-induced source change, or probabilistic matching",
    }
    output = Path(__file__).parents[1] / "results" / "partial_event_matching_afterpulse.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
