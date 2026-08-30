"""Hostile sweep for increasing differences of the Xi source angle."""

from __future__ import annotations

import itertools
import json
import math

from theta_tilt_third_cumulant import raw_moment


def source_data(y: float) -> tuple[float, float]:
    moments = [raw_moment(y, order) for order in range(3)]
    mean = moments[1] / moments[0]
    variance = moments[2] / moments[0] - mean * mean
    return math.log(mean), y * variance / mean


def angular_velocity(x: float, z: float, hx: float, hz: float, h_prime_z: float) -> float:
    delta_x = z - x
    delta_h = hz - hx
    correlation = math.cosh(delta_h / 2.0) / math.cosh(delta_x / 2.0)
    sine = math.sqrt(max(0.0, 1.0 - correlation * correlation))
    return correlation / (2.0 * sine) * (
        math.tanh(delta_x / 2.0) - h_prime_z * math.tanh(delta_h / 2.0)
    )


def main() -> None:
    xs = [-6.0 + 12.0 * index / 60.0 for index in range(61)]
    ys = [math.exp(x) for x in xs]
    data = [source_data(y) for y in ys]
    rows = []
    for i, j, k in itertools.combinations(range(len(xs)), 3):
        left_velocity = angular_velocity(xs[i], xs[k], data[i][0], data[k][0], data[k][1])
        moved_velocity = angular_velocity(xs[j], xs[k], data[j][0], data[k][0], data[k][1])
        rows.append((moved_velocity - left_velocity, (ys[i], ys[j], ys[k])))
    rows.sort()
    print(
        json.dumps(
            {
                "triples": len(rows),
                "negative_below_1e-10": sum(row[0] < -1e-10 for row in rows),
                "smallest": [
                    {"velocity_difference": difference, "heights": heights}
                    for difference, heights in rows[:10]
                ],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
