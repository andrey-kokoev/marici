from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def map_distribution(distribution, transform):
    merged = {}
    for value, probability in distribution:
        mapped = transform(value)
        merged[mapped] = merged.get(mapped, Fraction(0)) + probability
    return tuple(sorted(merged.items()))


def moment(distribution, degree):
    return sum(probability * value**degree for value, probability in distribution)


def tail(distribution, threshold):
    return sum(probability for value, probability in distribution if abs(value) >= threshold)


def main() -> None:
    moderate = ((-2, Fraction(1, 8)), (0, Fraction(3, 4)), (2, Fraction(1, 8)))
    severe = ((-4, Fraction(1, 8)), (0, Fraction(3, 4)), (4, Fraction(1, 8)))
    clip = lambda value: max(-1, min(1, value))
    clipped_moderate = map_distribution(moderate, clip)
    clipped_severe = map_distribution(severe, clip)
    assert clipped_moderate == clipped_severe == (
        (-1, Fraction(1, 8)),
        (0, Fraction(3, 4)),
        (1, Fraction(1, 8)),
    )

    assert moment(clipped_moderate, 2) == moment(clipped_severe, 2) == Fraction(1, 4)
    assert moment(clipped_moderate, 4) == moment(clipped_severe, 4) == Fraction(1, 4)
    assert moment(moderate, 2) == 1
    assert moment(severe, 2) == 4
    assert moment(moderate, 4) == 4
    assert moment(severe, 4) == 64

    # A one-bit overflow flag records the common burst rate, not severity.
    overflow_moderate = tail(moderate, Fraction(1))
    overflow_severe = tail(severe, Fraction(1))
    assert overflow_moderate == overflow_severe == Fraction(1, 4)

    # A second threshold directly answers a severity question.
    severe_threshold = Fraction(3)
    assert tail(moderate, severe_threshold) == 0
    assert tail(severe, severe_threshold) == Fraction(1, 4)

    # A pre-calibrated quarter-gain channel remains unsaturated for both frozen laws.
    low_gain = Fraction(1, 4)
    low_moderate = map_distribution(moderate, lambda value: low_gain * value)
    low_severe = map_distribution(severe, lambda value: low_gain * value)
    assert low_moderate != low_severe
    assert max(abs(value) for value, _ in low_moderate) == Fraction(1, 2)
    assert max(abs(value) for value, _ in low_severe) == Fraction(1)

    result = {
        "schema": "marici.aspect.clipped-tail-dual-gain.v1",
        "status": "pass",
        "shared_clipped_distribution": [[str(v), str(p)] for v, p in clipped_moderate],
        "shared_overflow_probability": str(overflow_moderate),
        "true_variances": {"moderate": "1", "severe": "4"},
        "true_fourth_moments": {"moderate": "4", "severe": "64"},
        "clipped_variance": "1/4",
        "clipped_fourth_moment": "1/4",
        "threshold_3_probabilities": {"moderate": "0", "severe": "1/4"},
        "low_gain": str(low_gain),
        "low_gain_peak_records": {"moderate": "1/2", "severe": "1"},
        "verdict": "Hard clipping makes moderate and severe burst laws identical, including every moment of the clipped record. A one-bit overflow flag recovers burst rate but not amplitude severity. A second threshold distinguishes the declared severity event; a pre-calibrated unsaturated low-gain channel recovers amplitude on the frozen support. Dual gain requires independent lineage and source-tap auditing.",
        "claim_boundary": "two exact discrete symmetric burst laws with common event probability, instantaneous memoryless clipping, perfect overflow logic, and an exact quarter-gain auxiliary channel; no recovery dead time, pileup, gain uncertainty, or tap back-action",
    }
    output = Path(__file__).parents[1] / "results" / "clipped_tail_dual_gain.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
