from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def moments(weights):
    positions = (-1, 0, 1)
    return tuple(
        sum(weight * position**degree for weight, position in zip(weights, positions))
        for degree in range(3)
    )


def determinant_3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def main() -> None:
    # Actual three-bin scatter includes a central channel.
    actual_weights = (Fraction(1, 100), Fraction(2, 100), Fraction(2, 100))
    actual_moments = moments(actual_weights)
    assert actual_moments == (Fraction(1, 20), Fraction(1, 100), Fraction(3, 100))

    # A two-endpoint model fits total and contrast exactly but reallocates the
    # central weight to the endpoints.
    endpoint_fit = (Fraction(2, 100), Fraction(0), Fraction(3, 100))
    endpoint_moments = moments(endpoint_fit)
    assert endpoint_moments[:2] == actual_moments[:2]
    assert endpoint_moments[2] == Fraction(1, 20)
    assert endpoint_moments[2] != actual_moments[2]

    loading = (
        (Fraction(1), Fraction(1), Fraction(1)),
        (Fraction(-1), Fraction(0), Fraction(1)),
        (Fraction(1), Fraction(0), Fraction(1)),
    )
    assert determinant_3(loading) == Fraction(2)

    total, contrast, second_moment = actual_moments
    recovered_center = total - second_moment
    recovered_right = (second_moment + contrast) / 2
    recovered_left = (second_moment - contrast) / 2
    recovered = (recovered_left, recovered_center, recovered_right)
    assert recovered == actual_weights

    # A full-rank chart on the declared grid does not certify that the grid is
    # complete. One off-grid two-atom measure matches all three moments.
    # Positions ±sqrt(3/5) with unequal weights reproduce the frozen moments.
    # We retain this symbolically as squared position and weight difference.
    off_grid_position_squared = second_moment / total
    off_grid_weight_difference_times_position = contrast
    assert off_grid_position_squared == Fraction(3, 5)
    assert off_grid_weight_difference_times_position == Fraction(1, 100)

    result = {
        "schema": "marici.aspect.scatter-model-order-moments.v1",
        "status": "pass",
        "declared_positions": [-1, 0, 1],
        "actual_weights": [str(value) for value in actual_weights],
        "moments": [str(value) for value in actual_moments],
        "two_endpoint_fit": [str(value) for value in endpoint_fit],
        "two_endpoint_moments": [str(value) for value in endpoint_moments],
        "three_moment_loading_determinant": "2",
        "recovered_weights": [str(value) for value in recovered],
        "off_grid_alias": {
            "symmetric_position_squared": str(off_grid_position_squared),
            "weight_difference_times_position": str(off_grid_weight_difference_times_position),
        },
        "verdict": "Total plus angular contrast can exactly fit a two-endpoint model while hiding a central scatter channel. The second angular moment uniquely resolves all three weights on the declared {-1,0,+1} grid. Full rank on that grid does not certify the grid itself; an off-grid atomic measure can reproduce the same finite moments.",
        "claim_boundary": "exact nonnegative weights on a declared three-point angular grid; the off-grid hostile shows that continuous-angle model order remains uncertified without more moments or a source-derived support law",
    }
    output = Path(__file__).parents[1] / "results" / "scatter_model_order_moments.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
