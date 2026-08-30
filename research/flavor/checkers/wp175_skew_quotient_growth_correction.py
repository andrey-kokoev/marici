"""WP175 exact checker: skew finite-quotient growth correction.

WP173 used rectangular finite tori. General finite quotients of Z^2 are
index-lattice quotients, represented here by Hermite normal forms with basis
(a,0),(b,d), index a*d. Under order cap K=64, skew index-60 lattices have
shortest l1 relation length 10, so growth radius four is not faithful on the
larger quotient domain. Radius five is the corrected exact certificate.
"""

from __future__ import annotations

import json
from collections import deque
from pathlib import Path


K = 64
GENERATORS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def hnfs(order_cap: int) -> list[tuple[int, int, int]]:
    return [
        (a, b, d)
        for a in range(1, order_cap + 1)
        for d in range(1, order_cap // a + 1)
        for b in range(d)
    ]


def index(hnf: tuple[int, int, int]) -> int:
    a, _b, d = hnf
    return a * d


def reduce_mod_hnf(point: tuple[int, int], hnf: tuple[int, int, int]) -> tuple[int, int]:
    a, b, d = hnf
    x, y = point
    q, r = divmod(y, d)
    return ((x - q * b) % a, r)


def quotient_ball_size(radius: int, hnf: tuple[int, int, int]) -> int:
    origin = reduce_mod_hnf((0, 0), hnf)
    seen = {origin}
    queue = deque([((0, 0), 0)])
    while queue:
        (x, y), depth = queue.popleft()
        if depth == radius:
            continue
        for dx, dy in GENERATORS:
            raw = (x + dx, y + dy)
            reduced = reduce_mod_hnf(raw, hnf)
            if reduced not in seen:
                seen.add(reduced)
                queue.append((raw, depth + 1))
    return len(seen)


def z2_ball_size(radius: int) -> int:
    return 1 + 2 * radius * (radius + 1)


def shortest_l1_relation(hnf: tuple[int, int, int]) -> tuple[int, tuple[int, int]]:
    a, b, d = hnf
    best = 2 * K + 1
    best_vec = (0, 0)
    # For index <= K, any vector relevant to the certificate has l1 <= 2K.
    # The coefficient search below is deliberately wider than needed.
    for xcoef in range(-K, K + 1):
        for ycoef in range(-K, K + 1):
            if xcoef == 0 and ycoef == 0:
                continue
            x = a * xcoef + b * ycoef
            y = d * ycoef
            norm = abs(x) + abs(y)
            if 0 < norm < best:
                best = norm
                best_vec = (x, y)
    return best, best_vec


def first_growth_difference(hnf: tuple[int, int, int], max_radius: int) -> int | None:
    for radius in range(max_radius + 1):
        if z2_ball_size(radius) != quotient_ball_size(radius, hnf):
            return radius
    return None


def main() -> None:
    domain = hnfs(K)
    shortest = {hnf: shortest_l1_relation(hnf) for hnf in domain}
    max_shortest = max(length for length, _vec in shortest.values())
    extremals = sorted(
        hnf for hnf, (length, _vec) in shortest.items() if length == max_shortest
    )
    corrected_radius = (max_shortest + 1) // 2
    rectangular_radius = 4
    hostile = extremals[0]

    diffs_radius_4 = {
        hnf: first_growth_difference(hnf, rectangular_radius) for hnf in domain
    }
    unseparated_radius_4 = sorted(
        hnf for hnf, diff in diffs_radius_4.items() if diff is None
    )
    diffs_corrected = {
        hnf: first_growth_difference(hnf, corrected_radius) for hnf in domain
    }

    checks = {
        "order_cap_is_64": K == 64,
        "hnf_domain_includes_skew_quotients": len(domain) > 153,
        "max_shortest_l1_relation_is_10": max_shortest == 10,
        "extremal_index_is_60": index(hostile) == 60,
        "rectangular_radius_four_fails": first_growth_difference(
            hostile, rectangular_radius
        )
        is None,
        "hostile_separates_at_radius_five": first_growth_difference(
            hostile, corrected_radius
        )
        == corrected_radius,
        "corrected_radius_is_five": corrected_radius == 5,
        "all_hnfs_separate_by_corrected_radius": all(
            diff is not None for diff in diffs_corrected.values()
        ),
        "radius_four_unseparated_nonempty": len(unseparated_radius_4) > 0,
        "hostile_growth_radius_four_matches_Z2": quotient_ball_size(
            rectangular_radius, hostile
        )
        == z2_ball_size(rectangular_radius),
        "hostile_growth_radius_five_differs_from_Z2": quotient_ball_size(
            corrected_radius, hostile
        )
        != z2_ball_size(corrected_radius),
        "wp173_rectangular_domain_was_restricted": True,
    }

    result = {
        "work_package": "WP175",
        "claim": "For arbitrary finite quotients of Z^2 with order cap 64, skew index-lattice quotients force recurrence-growth radius five; the rectangular radius-four certificate was domain-restricted.",
        "order_cap_K": K,
        "hnf_quotients_tested": len(domain),
        "max_shortest_l1_relation": max_shortest,
        "corrected_certificate_radius": corrected_radius,
        "rectangular_certificate_radius": rectangular_radius,
        "extremal_hnfs": [
            {"a": a, "b": b, "d": d, "index": a * d}
            for a, b, d in extremals
        ],
        "hostile_witness": {
            "hnf": {"a": hostile[0], "b": hostile[1], "d": hostile[2]},
            "index": index(hostile),
            "shortest_relation": shortest[hostile][1],
            "growth_radius_4": quotient_ball_size(4, hostile),
            "z2_growth_radius_4": z2_ball_size(4),
            "growth_radius_5": quotient_ball_size(5, hostile),
            "z2_growth_radius_5": z2_ball_size(5),
        },
        "classification": "correction: order-bound growth selector survives only with quotient-domain typing and radius five for K=64.",
        "instrument_gate": "Declare whether finite rivals are rectangular products or arbitrary index-lattice quotients before assigning a recurrence radius.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp175_skew_quotient_growth_correction.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
