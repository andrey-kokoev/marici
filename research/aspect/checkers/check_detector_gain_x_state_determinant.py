from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


def observed_correlation(true_correlation: F, imbalance_product: F) -> F:
    return (true_correlation + imbalance_product) / (
        1 + imbalance_product * true_correlation
    )


def reconstruct(records: dict[str, F]) -> tuple[F, F]:
    return (records["XX"] - records["YY"]) / 4, -(records["XY"] + records["YX"]) / 4


def main() -> None:
    records = {"XX": F(2, 25), "YY": F(-1, 25), "XY": F(-9, 100), "YX": F(-7, 100)}
    true_vector = reconstruct(records)
    boundary_product = F(1, 400)
    assert true_vector == (F(3, 100), F(1, 25))
    assert true_vector[0] ** 2 + true_vector[1] ** 2 == boundary_product

    # A scalar setting gain multiplies all four outcome counts and cancels in
    # the normalized correlation by construction.
    common_gain = F(7, 13)
    same_probability = (1 + records["XX"]) / 2
    different_probability = (1 - records["XX"]) / 2
    normalized = (
        common_gain * same_probability - common_gain * different_probability
    ) / (common_gain * same_probability + common_gain * different_probability)
    assert normalized == records["XX"]

    # For zero local transverse marginals, one-sided outcome imbalance also
    # cancels. Two-sided imbalance enters only through k=e_A e_B.
    assert observed_correlation(records["XX"], F(0)) == records["XX"]

    # Setting-dependent two-sided imbalance products form a hostile error box.
    imbalance_products = {"XX": F(1, 100), "YY": F(-1, 100), "XY": F(-1, 100), "YX": F(-1, 100)}
    biased = {
        setting: observed_correlation(value, imbalance_products[setting])
        for setting, value in records.items()
    }
    biased_vector = reconstruct(biased)
    false_npt_residual = biased_vector[0] ** 2 + biased_vector[1] ** 2 - boundary_product
    assert false_npt_residual > 0

    # Swapping one detector side flips k. Averaging the two normalized records
    # suppresses the leading k bias but is not exactly unbiased.
    k = F(1, 100)
    c0 = records["XX"]
    swapped_average = (
        observed_correlation(c0, k) + observed_correlation(c0, -k)
    ) / 2
    swap_residual = swapped_average - c0
    assert swap_residual != 0
    assert abs(swap_residual) < abs(observed_correlation(c0, k) - c0)

    # Dividing each outcome count by its independently calibrated channel
    # efficiency and then normalizing recovers the ideal probabilities exactly.
    probabilities = {"++": F(27, 100), "+-": F(23, 100), "-+": F(23, 100), "--": F(27, 100)}
    efficiencies = {"A+": F(9, 10), "A-": F(4, 5), "B+": F(7, 10), "B-": F(3, 5)}
    source_gain = F(11, 13)
    measured = {}
    for label, probability in probabilities.items():
        a_key = "A+" if label[0] == "+" else "A-"
        b_key = "B+" if label[1] == "+" else "B-"
        measured[label] = source_gain * efficiencies[a_key] * efficiencies[b_key] * probability
    corrected = {}
    for label, count in measured.items():
        a_key = "A+" if label[0] == "+" else "A-"
        b_key = "B+" if label[1] == "+" else "B-"
        corrected[label] = count / (efficiencies[a_key] * efficiencies[b_key])
    corrected_total = sum(corrected.values(), F(0))
    corrected_correlation = (
        corrected["++"] + corrected["--"] - corrected["+-"] - corrected["-+"]
    ) / corrected_total
    assert corrected_correlation == F(2, 25)

    result = {
        "schema": "marici.aspect.detector-gain-x-state-determinant.v1",
        "status": "pass",
        "common_setting_gain_cancels": True,
        "one_sided_imbalance_cancels_for_zero_transverse_marginals": True,
        "two_sided_bias_law": "C_observed=(C+e_A*e_B)/(1+e_A*e_B*C)",
        "hostile_imbalance_products": {key: str(value) for key, value in imbalance_products.items()},
        "hostile_false_npt_residual": str(false_npt_residual),
        "one_side_detector_swap_residual": str(swap_residual),
        "detector_swap_exact_repair": False,
        "efficiency_corrected_correlation": str(corrected_correlation),
        "efficiency_calibration_exact_repair": True,
        "verdict": "Local normalization removes common gain but not setting-dependent two-sided outcome imbalance; calibrated per-channel efficiency correction is exact, while detector swapping only suppresses bias.",
        "claim_boundary": "factorized channel efficiencies, zero transverse local marginals, no accidentals, dead time, saturation, or efficiency-calibration uncertainty",
    }
    output = Path(__file__).parents[1] / "results" / "detector_gain_x_state_determinant.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
