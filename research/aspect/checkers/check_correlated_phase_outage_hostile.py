from __future__ import annotations

import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path


def iid_probability(sequence: tuple[int, ...], good_probability: F) -> F:
    probability = F(1)
    for state in sequence:
        probability *= good_probability if state else F(1) - good_probability
    return probability


def markov_probability(
    sequence: tuple[int, ...],
    stationary_good: F,
    good_to_bad: F,
    bad_to_good: F,
) -> F:
    probability = stationary_good if sequence[0] else F(1) - stationary_good
    for previous, current in zip(sequence, sequence[1:]):
        if previous:
            probability *= F(1) - good_to_bad if current else good_to_bad
        else:
            probability *= bad_to_good if current else F(1) - bad_to_good
    return probability


def main() -> None:
    good_probability = F(9, 10)
    good_to_bad = F(1, 100)
    bad_to_good = F(9, 100)
    observed_full_gap = F(8019, 12500)
    systematic_error = F(1, 100)
    assert bad_to_good / (good_to_bad + bad_to_good) == good_probability

    sequences = list(product((0, 1), repeat=4))
    iid_total = sum((iid_probability(sequence, good_probability) for sequence in sequences), F(0))
    markov_total = sum(
        (markov_probability(sequence, good_probability, good_to_bad, bad_to_good) for sequence in sequences),
        F(0),
    )
    assert iid_total == markov_total == 1

    def contrast(sequence: tuple[int, ...]) -> F:
        return observed_full_gap * F(sum(sequence), 4)

    failing = [sequence for sequence in sequences if contrast(sequence) <= 2 * systematic_error]
    assert failing == [(0, 0, 0, 0)]

    iid_failure = sum((iid_probability(sequence, good_probability) for sequence in failing), F(0))
    markov_failure = sum(
        (markov_probability(sequence, good_probability, good_to_bad, bad_to_good) for sequence in failing),
        F(0),
    )
    assert iid_failure == F(1, 10000)
    assert markov_failure == F(753571, 10000000)
    inflation = markov_failure / iid_failure
    assert inflation == F(753571, 1000)

    one_good_margin = observed_full_gap / 4 - 2 * systematic_error
    assert one_good_margin == F(7019, 50000)
    assert one_good_margin > 0

    result = {
        "schema": "marici.aspect.correlated-phase-outage-hostile.v1",
        "status": "pass",
        "blocks": 4,
        "marginal_coherent_probability_both_models": str(good_probability),
        "iid_all_outage_failure_probability": str(iid_failure),
        "persistent_markov_all_outage_failure_probability": str(markov_failure),
        "failure_probability_inflation": str(inflation),
        "one_coherent_block_worst_case_margin": str(one_good_margin),
        "failing_sequences": [list(sequence) for sequence in failing],
        "static_visibility_sufficient_for_run_failure_certificate": False,
        "required_additional_contract": "mixing-time bound, independent block reset, or phase-monitor record",
        "verdict": "Equal marginal visibility does not control finite-run failure under temporally correlated phase outages.",
        "claim_boundary": "four-block binary outage model; no continuous phase diffusion or feedback dynamics",
    }
    output = Path(__file__).parents[1] / "results" / "correlated_phase_outage_hostile.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
