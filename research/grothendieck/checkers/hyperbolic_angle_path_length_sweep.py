"""Hostile test of the proposed source-angle/path-length comparison."""

from __future__ import annotations

import math
import random


def angle(x_length: float, h_length: float) -> float:
    alpha = (x_length + h_length) / 2.0
    beta = (x_length - h_length) / 2.0
    return 2.0 * math.atan(math.sqrt(math.tanh(alpha / 2.0) * math.tanh(beta / 2.0)))


def main() -> None:
    random.seed(20260820)
    worst = None
    trials = 200_000
    for _ in range(trials):
        pieces = random.randint(1, 20)
        u = random.uniform(0.0, 12.0)
        total_x = 0.0
        total_h = 0.0
        path = 0.0
        for _ in range(pieces):
            length = 10.0 ** random.uniform(-4.0, 0.3)
            slope = -random.random()
            # Shorten at u=0 so that u remains nonnegative.
            if slope < 0.0:
                length = min(length, u / -slope)
            end = u + slope * length
            midpoint = (u + end) / 2.0
            # Fine midpoint quadrature is diagnostic, not a certificate.
            panels = 20
            step = length / panels if panels else 0.0
            h_piece = 0.0
            path_piece = 0.0
            for panel in range(panels):
                value = u + slope * (panel + 0.5) * step
                h_piece += math.tanh(value) * step
                path_piece += 0.5 / math.cosh(value) * step
            total_x += length
            total_h += h_piece
            path += path_piece
            u = max(0.0, end)
        theta = angle(total_x, total_h) if total_x else 0.0
        margin = path - theta
        if worst is None or margin < worst[0]:
            worst = (margin, total_x, total_h, path, theta, u, midpoint)
    print(f"trials={trials}")
    print(f"worst={worst}")
    print(f"failures_below_minus_1e_10={int(worst is not None and worst[0] < -1e-10)}")


if __name__ == "__main__":
    main()
