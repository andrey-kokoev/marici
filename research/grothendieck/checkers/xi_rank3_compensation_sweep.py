"""Diagnostic sweep of the compact confluent rank-three propagation margin."""

from __future__ import annotations

import json

from theta_tilt_third_cumulant import raw_moment


def margin_data(y: float) -> dict[str, float]:
    moments = [raw_moment(y, order) for order in range(5)]
    moments = [value / moments[0] for value in moments]
    mean = moments[1]
    variance = moments[2] - mean * mean
    third = moments[3] - 3.0 * mean * moments[2] + 2.0 * mean**3
    fourth = (
        moments[4]
        - 4.0 * mean * moments[3]
        - 3.0 * moments[2] ** 2
        + 12.0 * mean * mean * moments[2]
        - 6.0 * mean**4
    )
    q = mean - y * variance
    positive = 3.0 * q * (variance + y * third)
    negative = -mean * y * y * fourth
    derivative = positive - negative
    return {
        "y": y,
        "compensation_ratio_minus_one": positive / negative - 1.0,
        "margin_derivative": derivative,
        "margin_derivative_over_y5": derivative / y**5,
    }


def main() -> None:
    heights = [0.01 + (7.22 - 0.01) * index / 180.0 for index in range(181)]
    rows = [margin_data(y) for y in heights]
    print(
        json.dumps(
            {
                "arithmetic": "IEEE-754 double; 12000-panel Simpson",
                "points": len(rows),
                "minimum_compensation_reserve": min(
                    rows, key=lambda row: row["compensation_ratio_minus_one"]
                ),
                "minimum_normalized_derivative": min(
                    rows, key=lambda row: row["margin_derivative_over_y5"]
                ),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
