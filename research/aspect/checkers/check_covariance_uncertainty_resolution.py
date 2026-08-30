from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def sum_score(correlation):
    return Fraction(2, 1) / (1 + correlation)


def difference_score(correlation):
    return Fraction(2, 1) / (1 - correlation)


def main() -> None:
    nominal_correlation = Fraction(-3, 4)
    admitted_interval = (Fraction(-3, 4), Fraction(3, 4))
    nominal_sum_score = sum_score(nominal_correlation)
    worst_sum_score = sum_score(admitted_interval[1])
    assert nominal_sum_score == 8
    assert worst_sum_score == Fraction(8, 7)
    assert nominal_sum_score / worst_sum_score == 7

    # A tighter independently calibrated negative-correlation interval retains
    # most of the nominal advantage.
    validated_interval = (Fraction(-4, 5), Fraction(-7, 10))
    validated_worst_sum_score = sum_score(validated_interval[1])
    assert validated_worst_sum_score == Fraction(20, 3)

    # Calibration-to-science drift can reverse the correlation sign while
    # preserving both marginal variances.
    science_correlation = Fraction(3, 4)
    science_score = sum_score(science_correlation)
    assert science_score == worst_sum_score

    # Noise correlation optimized for one witness harms the orthogonal witness.
    negative_sum = sum_score(Fraction(-3, 4))
    negative_difference = difference_score(Fraction(-3, 4))
    positive_sum = sum_score(Fraction(3, 4))
    positive_difference = difference_score(Fraction(3, 4))
    assert (negative_sum, negative_difference) == (8, Fraction(8, 7))
    assert (positive_sum, positive_difference) == (Fraction(8, 7), 8)

    result = {
        "schema": "marici.aspect.covariance-uncertainty-resolution.v1",
        "status": "pass",
        "nominal_correlation": str(nominal_correlation),
        "nominal_sum_witness_score": str(nominal_sum_score),
        "admitted_correlation_interval": [str(value) for value in admitted_interval],
        "worst_case_sum_witness_score": str(worst_sum_score),
        "nominal_to_robust_overstatement_factor": "7",
        "validated_negative_interval": [str(value) for value in validated_interval],
        "validated_worst_sum_score": str(validated_worst_sum_score),
        "science_drift_correlation": str(science_correlation),
        "orthogonal_witness_scores": {
            "negative_correlation": {"sum": str(negative_sum), "difference": str(negative_difference)},
            "positive_correlation": {"sum": str(positive_sum), "difference": str(positive_difference)},
        },
        "verdict": "A nominal negative correlation can overstate robust squared separation by a factor of seven when the admitted covariance interval includes the opposite sign. Independently bounding the science-epoch correlation restores a useful lower score. Correlation engineered to improve the sum witness degrades the orthogonal difference witness by the same factor, so noise shaping is question-relative rather than universally informative.",
        "claim_boundary": "two normalized channels with unit marginals and an interval uncertainty only in their correlation; no marginal drift, covariance-estimation sampling law, non-Gaussian contamination, or more than two witness directions",
    }
    output = Path(__file__).parents[1] / "results" / "covariance_uncertainty_resolution.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
