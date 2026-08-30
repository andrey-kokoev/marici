from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def moment(distribution, degree):
    return sum(probability * value**degree for value, probability in distribution)


def tail_probability(distribution, threshold):
    return sum(probability for value, probability in distribution if abs(value) >= threshold)


def main() -> None:
    bounded_noise = ((-1, Fraction(1, 2)), (1, Fraction(1, 2)))
    burst_noise = ((-2, Fraction(1, 8)), (0, Fraction(3, 4)), (2, Fraction(1, 8)))
    for distribution in (bounded_noise, burst_noise):
        assert sum(probability for _, probability in distribution) == 1
        assert moment(distribution, 1) == 0
        assert moment(distribution, 2) == 1

    bounded_fourth = moment(bounded_noise, 4)
    burst_fourth = moment(burst_noise, 4)
    assert (bounded_fourth, burst_fourth) == (1, 4)

    threshold = Fraction(3, 2)
    bounded_tail = tail_probability(bounded_noise, threshold)
    burst_tail = tail_probability(burst_noise, threshold)
    assert (bounded_tail, burst_tail) == (0, Fraction(1, 4))

    # Add the same independent unit-variance orthogonal channel to both laws.
    # Both two-channel covariance matrices are exactly identity.
    covariance_bounded = ((1, 0), (0, 1))
    covariance_burst = ((1, 0), (0, 1))
    assert covariance_bounded == covariance_burst

    # A threshold-event counter is the direct port for the declared tail event.
    tail_event_loading = (bounded_tail, burst_tail)
    assert tail_event_loading[0] != tail_event_loading[1]

    result = {
        "schema": "marici.aspect.equal-covariance-tail-hostile.v1",
        "status": "pass",
        "shared_mean": "0",
        "shared_variance": "1",
        "shared_two_channel_covariance": [[1, 0], [0, 1]],
        "fourth_moments": {"bounded": str(bounded_fourth), "burst": str(burst_fourth)},
        "tail_threshold": str(threshold),
        "tail_probabilities": {"bounded": str(bounded_tail), "burst": str(burst_tail)},
        "verdict": "Two optical noise laws can have identical mean and full covariance while one has zero probability beyond the declared threshold and the other has probability one quarter. Covariance-authorized Mahalanobis geometry does not authorize tail probabilities. A fourth-moment port separates these frozen laws; a threshold-event counter directly measures the declared false-alarm event. Neither finite moment port characterizes arbitrary tails without a source-derived noise family.",
        "claim_boundary": "two exact discrete symmetric witness-noise laws with the same independent orthogonal unit-variance channel; no finite-sample estimation, detector clipping, temporal dependence, or global tail reconstruction from four moments",
    }
    output = Path(__file__).parents[1] / "results" / "equal_covariance_tail_hostile.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
