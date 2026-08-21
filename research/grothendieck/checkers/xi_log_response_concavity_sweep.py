"""Hostile sweep for concavity of h(x)=log a(exp x)."""

from __future__ import annotations

import json

from theta_tilt_third_cumulant import sample


def main() -> None:
    heights = [10.0 ** (-3.0 + 6.0 * index / 180.0) for index in range(181)]
    rows = []
    for y in heights:
        data = sample(y)
        a = data["mean"]
        variance = data["variance"]
        third = data["third_cumulant"]
        q = a - y * variance
        w = y * variance / a
        r = -y * y * third
        margin = r - w * q
        rows.append(
            {
                "y": y,
                "margin": margin,
                "margin_over_y3": margin / y**3,
                "h_prime": w,
            }
        )
    print(
        json.dumps(
            {
                "points": len(rows),
                "negative_below_1e-10": sum(row["margin"] < -1e-10 for row in rows),
                "minimum_raw_margin": min(rows, key=lambda row: row["margin"]),
                "minimum_normalized_margin": min(
                    rows, key=lambda row: row["margin_over_y3"]
                ),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
