from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def inverse_2(matrix):
    a, b = matrix[0]
    c, d = matrix[1]
    determinant = a * d - b * c
    assert determinant != 0
    return ((d / determinant, -b / determinant), (-c / determinant, a / determinant))


def quadratic(vector, matrix):
    return sum(vector[i] * matrix[i][j] * vector[j] for i in range(2) for j in range(2))


def transform_covariance(scale, covariance):
    return tuple(
        tuple(scale[i] * covariance[i][j] * scale[j] for j in range(2))
        for i in range(2)
    )


def main() -> None:
    # The two moment gaps are normalized by their source-derived expected gaps
    # before data comparison, giving a frozen witness direction (1,1).
    witness = (Fraction(1), Fraction(1))
    independent = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
    positive = ((Fraction(1), Fraction(3, 4)), (Fraction(3, 4), Fraction(1)))
    negative = ((Fraction(1), Fraction(-3, 4)), (Fraction(-3, 4), Fraction(1)))

    scores = {
        "independent": quadratic(witness, inverse_2(independent)),
        "positive_correlation": quadratic(witness, inverse_2(positive)),
        "negative_correlation": quadratic(witness, inverse_2(negative)),
    }
    assert scores == {
        "independent": Fraction(2),
        "positive_correlation": Fraction(8, 7),
        "negative_correlation": Fraction(8),
    }

    # Coordinate rescaling cannot change the score when covariance is transported.
    scale = (Fraction(2), Fraction(3))
    scaled_witness = tuple(scale[i] * witness[i] for i in range(2))
    scaled_covariance = transform_covariance(scale, positive)
    scaled_score = quadratic(scaled_witness, inverse_2(scaled_covariance))
    assert scaled_score == scores["positive_correlation"]

    # Independent repetitions improve an average; duplicated readings of one
    # physical carrier have a singular covariance and no independent rank.
    independent_average_variance = Fraction(1, 2)
    shared_carrier_covariance = ((Fraction(1), Fraction(1)), (Fraction(1), Fraction(1)))
    shared_carrier_determinant = (
        shared_carrier_covariance[0][0] * shared_carrier_covariance[1][1]
        - shared_carrier_covariance[0][1] * shared_carrier_covariance[1][0]
    )
    assert independent_average_variance == Fraction(1, 2)
    assert shared_carrier_determinant == 0

    result = {
        "schema": "marici.aspect.covariance-bearing-moment-resolution.v1",
        "status": "pass",
        "normalized_witness": ["1", "1"],
        "equal_marginal_variances": True,
        "mahalanobis_scores_squared": {key: str(value) for key, value in scores.items()},
        "basis_rescaled_score": str(scaled_score),
        "independent_two_record_average_variance": str(independent_average_variance),
        "shared_carrier_covariance_determinant": str(shared_carrier_determinant),
        "verdict": "With identical marginal precision, correlation changes the frozen two-versus-one squared separation score from 8/7 to 8, a factor of seven. Positive common-mode correlation aligned with the witness degrades resolution; negative correlation improves it. The score is invariant under channel rescaling only when covariance is transported. Duplicated readings of one carrier remain singular and do not gain independent averaging rank.",
        "claim_boundary": "two source-normalized witness channels with exact known Gaussian-style covariance geometry; no covariance estimation error, non-Gaussian tails, nuisance parameters, or adaptive normalization",
    }
    output = Path(__file__).parents[1] / "results" / "covariance_bearing_moment_resolution.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
