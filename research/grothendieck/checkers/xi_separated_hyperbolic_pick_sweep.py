"""Hostile separated-triple sweep in logarithmic hyperbolic-secant coordinates."""

from __future__ import annotations

import itertools
import json
import math

from theta_tilt_third_cumulant import raw_moment


def log_a(y: float) -> float:
    return math.log(raw_moment(y, 1) / raw_moment(y, 0))


def kernel(x: float, z: float, hx: float, hz: float) -> float:
    return math.cosh((hz - hx) / 2.0) / math.cosh((z - x) / 2.0)


def main() -> None:
    xs = [-6.0 + 12.0 * index / 60.0 for index in range(61)]
    ys = [math.exp(x) for x in xs]
    hs = [log_a(y) for y in ys]
    rows = []
    for i, j, k in itertools.combinations(range(len(xs)), 3):
        if xs[j] - xs[i] < 0.2 or xs[k] - xs[j] < 0.2:
            continue
        r12 = kernel(xs[i], xs[j], hs[i], hs[j])
        r13 = kernel(xs[i], xs[k], hs[i], hs[k])
        r23 = kernel(xs[j], xs[k], hs[j], hs[k])
        determinant = 1.0 + 2.0 * r12 * r13 * r23 - r12 * r12 - r13 * r13 - r23 * r23
        angles = tuple(math.acos(min(1.0, max(-1.0, value))) for value in (r12, r13, r23))
        triangle_slack = angles[0] + angles[2] - angles[1]
        rows.append((triangle_slack, determinant, (ys[i], ys[j], ys[k]), (r12, r13, r23), angles))
    rows.sort()
    print(
        json.dumps(
            {
                "arithmetic": "IEEE-754 double; source moments by 12000-panel Simpson",
                "triples": len(rows),
                "negative_determinants_below_1e-10": sum(row[1] < -1e-10 for row in rows),
                "negative_triangle_slacks_below_1e-10": sum(row[0] < -1e-10 for row in rows),
                "smallest": [
                    {
                        "triangle_slack": slack,
                        "determinant": determinant,
                        "heights": heights,
                        "correlations": correlations,
                        "angles": angles,
                    }
                    for slack, determinant, heights, correlations, angles in rows[:10]
                ],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
