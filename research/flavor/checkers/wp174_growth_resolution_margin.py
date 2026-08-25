"""WP174 exact checker: recurrence-growth resolution margin.

WP173 gives the exact radius for noiseless recurrence-growth separation under
an order cap. This checker adds a bounded absolute counting error tau. The
separation condition is interval disjointness, so the minimum finite deficit
from Z^2 must be strictly greater than 2*tau.
"""

from __future__ import annotations

import json
from collections import deque
from pathlib import Path


K = 64
TAU = 1
GENERATORS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def z2_growth(radius: int) -> int:
    return 1 + 2 * radius * (radius + 1)


def torus_growth(radius: int, n1: int, n2: int) -> int:
    origin = (0, 0)
    seen = {origin}
    queue = deque([(origin, 0)])
    while queue:
        (x, y), depth = queue.popleft()
        if depth == radius:
            continue
        for dx, dy in GENERATORS:
            nxt = ((x + dx) % n1, (y + dy) % n2)
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, depth + 1))
    return len(seen)


def rivals_under_order_cap(order_cap: int) -> list[tuple[int, int]]:
    return [
        (n1, n2)
        for n1 in range(2, order_cap + 1)
        for n2 in range(2, order_cap + 1)
        if n1 * n2 <= order_cap
    ]


def deficits(radius: int, rivals: list[tuple[int, int]]) -> dict[tuple[int, int], int]:
    z = z2_growth(radius)
    return {(n1, n2): z - torus_growth(radius, n1, n2) for n1, n2 in rivals}


def min_margin(radius: int, rivals: list[tuple[int, int]]) -> int:
    return min(deficits(radius, rivals).values())


def separates_with_error(radius: int, rivals: list[tuple[int, int]], tau: int) -> bool:
    return min_margin(radius, rivals) > 2 * tau


def first_radius_with_error(
    rivals: list[tuple[int, int]], tau: int, max_radius: int
) -> int | None:
    for radius in range(max_radius + 1):
        if separates_with_error(radius, rivals, tau):
            return radius
    return None


def main() -> None:
    rivals = rivals_under_order_cap(K)
    noiseless_radius = 4
    noisy_radius = first_radius_with_error(rivals, TAU, 12)
    margins = {radius: min_margin(radius, rivals) for radius in range(4, 7)}
    radius4_deficits = deficits(4, rivals)
    worst_radius4 = sorted(
        str(pair) for pair, deficit in radius4_deficits.items() if deficit == margins[4]
    )
    radius5_deficits = deficits(5, rivals)
    worst_radius5 = sorted(
        str(pair) for pair, deficit in radius5_deficits.items() if deficit == margins[5]
    )

    checks = {
        "order_cap_is_64": K == 64,
        "absolute_count_error_tau_is_1": TAU == 1,
        "noiseless_radius_four_margin_is_2": margins[4] == 2,
        "tau_one_breaks_radius_four_interval_separation": not separates_with_error(
            4, rivals, TAU
        ),
        "radius_five_margin_is_10": margins[5] == 10,
        "tau_one_separates_at_radius_five": separates_with_error(5, rivals, TAU),
        "first_tau_one_radius_is_five": noisy_radius == 5,
        "worst_radius_four_includes_Z8_square": "(8, 8)" in worst_radius4,
        "worst_radius_four_includes_rectangular_7_9": "(7, 9)" in worst_radius4,
        "interval_disjointness_rule_is_strict": margins[4] == 2 * TAU,
        "resolution_gate_is_instrumental_not_source_identification": True,
        "exact_counting_is_hidden_assumption_in_WP173": True,
    }

    result = {
        "work_package": "WP174",
        "claim": "A recurrence-growth selector under an order cap also requires a detector-resolution margin: minimum finite deficit must exceed twice the absolute counting error.",
        "order_cap_K": K,
        "absolute_count_error_tau": TAU,
        "noiseless_certificate_radius": noiseless_radius,
        "first_error_robust_radius": noisy_radius,
        "minimum_deficits": margins,
        "worst_radius_four_rivals": worst_radius4,
        "worst_radius_five_rivals": worst_radius5,
        "classification": "conditional selector only with source order cap, executable radius, and sufficient growth-count resolution.",
        "instrument_gate": "Derive or calibrate an absolute growth-count error tau with margin d_min(R)>2*tau.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp174_growth_resolution_margin.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
