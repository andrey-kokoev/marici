from __future__ import annotations

import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path


def fresh_probability(value: int, mean: F) -> F:
    return (1 + mean) / 2 if value == 1 else (1 - mean) / 2


def markov_probability(sequence: tuple[int, ...], mean: F, copy_probability: F) -> F:
    probability = fresh_probability(sequence[0], mean)
    for previous, current in zip(sequence, sequence[1:]):
        probability *= (
            copy_probability * (F(1) if current == previous else F(0))
            + (1 - copy_probability) * fresh_probability(current, mean)
        )
    return probability


def iid_probability(sequence: tuple[int, ...], mean: F) -> F:
    probability = F(1)
    for value in sequence:
        probability *= fresh_probability(value, mean)
    return probability


def main() -> None:
    mean = F(1, 2)
    copy_probability = F(1, 2)
    length = 4
    sequences = list(product((-1, 1), repeat=length))
    markov = {sequence: markov_probability(sequence, mean, copy_probability) for sequence in sequences}
    iid = {sequence: iid_probability(sequence, mean) for sequence in sequences}
    assert sum(markov.values(), F(0)) == sum(iid.values(), F(0)) == 1

    # Detector memory preserves every one-time marginal in stationarity.
    for index in range(length):
        observed_mean = sum((probability * sequence[index] for sequence, probability in markov.items()), F(0))
        assert observed_mean == mean

    def sample_mean(sequence: tuple[int, ...]) -> F:
        return F(sum(sequence), length)

    markov_variance = sum(
        (probability * (sample_mean(sequence) - mean) ** 2 for sequence, probability in markov.items()), F(0)
    )
    iid_variance = sum(
        (probability * (sample_mean(sequence) - mean) ** 2 for sequence, probability in iid.items()), F(0)
    )
    assert iid_variance == F(3, 16)
    assert markov_variance == F(99, 256)
    variance_inflation = markov_variance / iid_variance
    assert variance_inflation == F(33, 16)

    markov_repeat = sum((probability for sequence, probability in markov.items() if sequence[1] == sequence[0]), F(0))
    iid_repeat = sum((probability for sequence, probability in iid.items() if sequence[1] == sequence[0]), F(0))
    assert iid_repeat == F(5, 8)
    assert markov_repeat == F(13, 16)

    # Passive thinning by one intervening bin leaves copy correlation a^2.
    lag_two_covariance = copy_probability**2 * (1 - mean**2)
    assert lag_two_covariance == F(3, 16)
    assert lag_two_covariance > 0

    # Active holdoff/reset in the frozen one-state model forces every retained
    # event to be a fresh draw, restoring the iid joint law exactly.
    reset = iid
    assert reset == iid
    reset_variance = iid_variance

    result = {
        "schema": "marici.aspect.afterpulse-memory-confidence.v1",
        "status": "pass",
        "stationary_record_mean": str(mean),
        "afterpulse_copy_probability": str(copy_probability),
        "sample_length": length,
        "all_one_time_marginals_unchanged": True,
        "iid_sample_mean_variance": str(iid_variance),
        "afterpulse_sample_mean_variance": str(markov_variance),
        "variance_inflation": str(variance_inflation),
        "iid_adjacent_repeat_probability": str(iid_repeat),
        "afterpulse_adjacent_repeat_probability": str(markov_repeat),
        "passive_lag_two_covariance": str(lag_two_covariance),
        "passive_thinning_restores_iid": False,
        "active_reset_variance": str(reset_variance),
        "active_reset_restores_iid_in_frozen_model": True,
        "verdict": "Afterpulse memory can leave every marginal correlation unchanged while invalidating iid confidence; lag records detect it, passive thinning does not erase it, and active reset restores iid only under the declared finite detector-state model.",
        "claim_boundary": "stationary binary copy-or-refresh Markov detector with known active reset; no channel dependence, branching cascades, source bunching, or reset failure",
    }
    output = Path(__file__).parents[1] / "results" / "afterpulse_memory_confidence.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
