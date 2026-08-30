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


def correlation(counts: dict[str, F]) -> F:
    total = sum(counts.values(), F(0))
    return (counts["++"] + counts["--"] - counts["+-"] - counts["-+"]) / total


def subtract(prompt: dict[str, F], side: dict[str, F]) -> dict[str, F]:
    return {label: prompt[label] - side[label] for label in LABELS}


def reconstruct(records: dict[str, F]) -> tuple[F, F]:
    return (records["XX"] - records["YY"]) / 4, -(records["XY"] + records["YX"]) / 4


def main() -> None:
    ideal = {"XX": F(2, 25), "YY": F(-1, 25), "XY": F(-9, 100), "YX": F(-7, 100)}
    true_vector = reconstruct(ideal)
    boundary_product = F(1, 400)
    assert true_vector[0] ** 2 + true_vector[1] ** 2 == boundary_product

    accidental_rate = F(1, 100)
    background_correlations = {"XX": F(1), "YY": F(-1), "XY": F(-1), "YX": F(-1)}

    # Exact repair: the side window transports the complete background
    # distribution with the correct exposure scaling.
    exact_corrected = {}
    for setting, signal_correlation in ideal.items():
        signal = distribution(signal_correlation)
        background = distribution(background_correlations[setting])
        prompt = {
            label: signal[label] + accidental_rate * background[label]
            for label in LABELS
        }
        matched_side = {
            label: accidental_rate * background[label] for label in LABELS
        }
        exact_corrected[setting] = correlation(subtract(prompt, matched_side))
    assert exact_corrected == ideal

    # Hostile: side window has the correct total rate but is assumed uniform,
    # while the prompt background carries setting-dependent correlation.
    uniform = distribution(F(0))
    hostile_corrected = {}
    for setting, signal_correlation in ideal.items():
        signal = distribution(signal_correlation)
        prompt_background = distribution(background_correlations[setting])
        prompt = {
            label: signal[label] + accidental_rate * prompt_background[label]
            for label in LABELS
        }
        wrong_side = {label: accidental_rate * uniform[label] for label in LABELS}
        hostile_corrected[setting] = correlation(subtract(prompt, wrong_side))
        assert hostile_corrected[setting] == signal_correlation + accidental_rate * background_correlations[setting]

    hostile_vector = reconstruct(hostile_corrected)
    false_npt_residual = hostile_vector[0] ** 2 + hostile_vector[1] ** 2 - boundary_product
    assert false_npt_residual == F(3, 4000)
    assert false_npt_residual > 0

    # A bounded exposure mismatch leaves a typed correlation residual. Here
    # the side window underestimates a matched polarized background by 1/1000.
    side_rate = F(9, 1000)
    exposure_residual = accidental_rate - side_rate
    assert exposure_residual == F(1, 1000)
    assert abs(exposure_residual * background_correlations["XX"]) == F(1, 1000)

    result = {
        "schema": "marici.aspect.accidental-coincidence-x-state-determinant.v1",
        "status": "pass",
        "accidental_to_signal_ratio": str(accidental_rate),
        "matched_full_distribution_side_window_exact": True,
        "equal_total_rate_alone_sufficient": False,
        "hostile_prompt_background_correlations": {key: str(value) for key, value in background_correlations.items()},
        "hostile_corrected_correlations": {key: str(value) for key, value in hostile_corrected.items()},
        "hostile_false_npt_residual": str(false_npt_residual),
        "exposure_mismatch": str(exposure_residual),
        "resulting_single_setting_correlation_residual": "1/1000",
        "verdict": "Side-window subtraction is exact only for a transported channel-resolved background law; equal total accidentals can conceal setting-dependent correlation and manufacture NPT.",
        "claim_boundary": "additive background, linear detector response, exact channel efficiencies, no dead time, pileup, afterpulsing, or side-window statistical uncertainty",
    }
    output = Path(__file__).parents[1] / "results" / "accidental_coincidence_x_state_determinant.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
