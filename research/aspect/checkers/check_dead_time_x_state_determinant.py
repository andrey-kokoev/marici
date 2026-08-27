from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


LABELS = ("++", "+-", "-+", "--")


def distribution(correlation: F) -> dict[str, F]:
    return {
        "++": (1 + correlation) / 4,
        "+-": (1 - correlation) / 4,
        "-+": (1 - correlation) / 4,
        "--": (1 + correlation) / 4,
    }


def detect(probabilities: dict[str, F], rate: F, dead_times: dict[str, F]) -> dict[str, F]:
    return {
        label: rate * probabilities[label] / (1 + dead_times[label] * rate * probabilities[label])
        for label in LABELS
    }


def invert(observed: dict[str, F], dead_times: dict[str, F]) -> dict[str, F]:
    true_rates = {
        label: observed[label] / (1 - dead_times[label] * observed[label])
        for label in LABELS
    }
    total = sum(true_rates.values(), F(0))
    return {label: value / total for label, value in true_rates.items()}


def correlation(counts: dict[str, F]) -> F:
    total = sum(counts.values(), F(0))
    return (counts["++"] + counts["--"] - counts["+-"] - counts["-+"]) / total


def reconstruct(records: dict[str, F]) -> tuple[F, F]:
    return (records["XX"] - records["YY"]) / 4, -(records["XY"] + records["YX"]) / 4


def main() -> None:
    ideal = {"XX": F(2, 25), "YY": F(-1, 25), "XY": F(-9, 100), "YX": F(-7, 100)}
    boundary = F(1, 400)
    ideal_vector = reconstruct(ideal)
    assert ideal_vector[0] ** 2 + ideal_vector[1] ** 2 == boundary

    rate = F(1)
    common_dead_time = {label: F(1) for label in LABELS}
    common_observed = {
        setting: correlation(detect(distribution(value), rate, common_dead_time))
        for setting, value in ideal.items()
    }
    assert all(abs(common_observed[key]) < abs(ideal[key]) for key in ideal)
    common_vector = reconstruct(common_observed)
    common_residual = common_vector[0] ** 2 + common_vector[1] ** 2 - boundary
    assert common_residual < 0

    # Channel-dependent saturation can bias each setting in the direction that
    # enlarges the reconstructed coherence norm.
    same_saturated = {"++": F(1), "+-": F(0), "-+": F(0), "--": F(1)}
    different_saturated = {"++": F(0), "+-": F(1), "-+": F(1), "--": F(0)}
    hostile_dead_times = {
        "XX": different_saturated,
        "YY": same_saturated,
        "XY": same_saturated,
        "YX": same_saturated,
    }
    hostile_observed = {
        setting: correlation(detect(distribution(value), rate, hostile_dead_times[setting]))
        for setting, value in ideal.items()
    }
    hostile_vector = reconstruct(hostile_observed)
    false_npt_residual = hostile_vector[0] ** 2 + hostile_vector[1] ** 2 - boundary
    assert false_npt_residual > 0

    corrected = {}
    for setting, value in ideal.items():
        measured = detect(distribution(value), rate, hostile_dead_times[setting])
        corrected[setting] = correlation(invert(measured, hostile_dead_times[setting]))
    assert corrected == ideal

    # A rate sweep is a falsifier for unmodelled saturation. Exact inversion
    # restores rate invariance when the source probabilities and dead times are stable.
    low_rate, high_rate = F(1, 10), F(1)
    xx_low = detect(distribution(ideal["XX"]), low_rate, hostile_dead_times["XX"])
    xx_high = detect(distribution(ideal["XX"]), high_rate, hostile_dead_times["XX"])
    assert correlation(xx_low) != correlation(xx_high)
    assert correlation(invert(xx_low, hostile_dead_times["XX"])) == ideal["XX"]
    assert correlation(invert(xx_high, hostile_dead_times["XX"])) == ideal["XX"]

    result = {
        "schema": "marici.aspect.dead-time-x-state-determinant.v1",
        "status": "pass",
        "detector_model": "nonparalyzable channel rate r=lambda*p/(1+tau*lambda*p)",
        "common_dead_time_correlations": {key: str(value) for key, value in common_observed.items()},
        "common_dead_time_determinant_residual": str(common_residual),
        "common_dead_time_false_npt": False,
        "common_dead_time_can_hide_npt": True,
        "hostile_channel_dependent_correlations": {key: str(value) for key, value in hostile_observed.items()},
        "hostile_false_npt_residual": str(false_npt_residual),
        "known_dead_time_inverse": "true_rate=r/(1-tau*r), followed by normalization",
        "exact_correction_verified": True,
        "rate_sweep_detects_uncorrected_nonlinearity": True,
        "corrected_rate_invariance_verified": True,
        "verdict": "Normalization does not remove channelwise dead time; hardware-calibrated inverse response repairs the frozen model, and a source-rate sweep falsifies unmodelled compression.",
        "claim_boundary": "nonparalyzable independent channel model with stable source state and known dead times; no pileup, shared electronics, afterpulsing, or dead-time uncertainty",
    }
    output = Path(__file__).parents[1] / "results" / "dead_time_x_state_determinant.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
