from __future__ import annotations

import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path


def markov_probability(sequence: tuple[int, ...]) -> F:
    stationary_good = F(9, 10)
    good_to_bad = F(1, 100)
    bad_to_good = F(9, 100)
    probability = stationary_good if sequence[0] else F(1) - stationary_good
    for previous, current in zip(sequence, sequence[1:]):
        if previous:
            probability *= F(1) - good_to_bad if current else good_to_bad
        else:
            probability *= bad_to_good if current else F(1) - bad_to_good
    return probability


def monitor_pass_probability(
    sequence: tuple[int, ...], false_negative: F, false_positive: F
) -> F:
    probability = F(1)
    for coherent in sequence:
        probability *= F(1) - false_positive if coherent else false_negative
    return probability


def main() -> None:
    false_negative = F(1, 20)
    false_positive = F(1, 100)
    sequences = list(product((0, 1), repeat=4))
    failure = (0, 0, 0, 0)

    accepted_by_sequence = {
        sequence: markov_probability(sequence)
        * monitor_pass_probability(sequence, false_negative, false_positive)
        for sequence in sequences
    }
    acceptance = sum(accepted_by_sequence.values(), F(0))
    accepted_failure = accepted_by_sequence[failure]
    conditional_failure = accepted_failure / acceptance
    prior_failure = markov_probability(failure)

    assert prior_failure == F(753571, 10000000)
    assert accepted_failure == prior_failure * false_negative**4
    assert accepted_failure < prior_failure
    assert conditional_failure < prior_failure

    perfect_detection_failure = prior_failure * F(0) ** 4
    missed_detection_failure = prior_failure * F(1) ** 4
    assert perfect_detection_failure == 0
    assert missed_detection_failure == prior_failure

    result = {
        "schema": "marici.aspect.imperfect-phase-monitor-repair.v1",
        "status": "pass",
        "blocks": 4,
        "false_negative_per_outage_block": str(false_negative),
        "false_positive_per_coherent_block": str(false_positive),
        "prior_failure_probability": str(prior_failure),
        "run_acceptance_probability": str(acceptance),
        "accepted_failure_probability": str(accepted_failure),
        "failure_probability_conditioned_on_acceptance": str(conditional_failure),
        "failed_run_acceptance_suppression_factor": str(false_negative**4),
        "perfect_monitor_accepted_failure_probability": str(perfect_detection_failure),
        "blind_monitor_accepted_failure_probability": str(missed_detection_failure),
        "interpretation": "The monitor identifies and rejects likely outage records; it does not restore lost coherence.",
        "claim_boundary": "four-block binary Markov outage model with conditionally independent monitor errors",
    }
    output = Path(__file__).parents[1] / "results" / "imperfect_phase_monitor_repair.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
