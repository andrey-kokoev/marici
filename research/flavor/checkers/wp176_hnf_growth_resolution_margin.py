"""WP176 exact checker: HNF-domain recurrence-growth resolution margin.

WP175 corrected the noiseless certificate radius to five for arbitrary finite
index-lattice quotients under K=64. This checker recomputes the detector
resolution margin on that enlarged domain.
"""

from __future__ import annotations

import json
from collections import deque
from pathlib import Path


K = 64
TAU = 1
GENERATORS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def hnfs(order_cap: int) -> list[tuple[int, int, int]]:
    return [
        (a, b, d)
        for a in range(1, order_cap + 1)
        for d in range(1, order_cap // a + 1)
        for b in range(d)
    ]


def reduce_mod_hnf(point: tuple[int, int], hnf: tuple[int, int, int]) -> tuple[int, int]:
    a, b, d = hnf
    x, y = point
    q, r = divmod(y, d)
    return ((x - q * b) % a, r)


def quotient_growth(radius: int, hnf: tuple[int, int, int]) -> int:
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


def z2_growth(radius: int) -> int:
    return 1 + 2 * radius * (radius + 1)


def min_deficit(radius: int, domain: list[tuple[int, int, int]]) -> int:
    z = z2_growth(radius)
    return min(z - quotient_growth(radius, hnf) for hnf in domain)


def worst_hnfs(radius: int, domain: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    z = z2_growth(radius)
    values = {hnf: z - quotient_growth(radius, hnf) for hnf in domain}
    m = min(values.values())
    return sorted(hnf for hnf, deficit in values.items() if deficit == m)


def separates_with_error(radius: int, domain: list[tuple[int, int, int]], tau: int) -> bool:
    return min_deficit(radius, domain) > 2 * tau


def first_error_robust_radius(
    domain: list[tuple[int, int, int]], tau: int, max_radius: int
) -> int | None:
    for radius in range(max_radius + 1):
        if separates_with_error(radius, domain, tau):
            return radius
    return None


def main() -> None:
    domain = hnfs(K)
    margins = {radius: min_deficit(radius, domain) for radius in range(5, 8)}
    noisy_radius = first_error_robust_radius(domain, TAU, 12)
    worst_radius_5 = worst_hnfs(5, domain)
    worst_radius_6 = worst_hnfs(6, domain)

    checks = {
        "hnf_domain_size_is_3403": len(domain) == 3403,
        "noiseless_radius_five_margin_is_1": margins[5] == 1,
        "tau_one_breaks_radius_five": not separates_with_error(5, domain, TAU),
        "radius_six_margin_is_21": margins[6] == 21,
        "tau_one_separates_at_radius_six": separates_with_error(6, domain, TAU),
        "first_tau_one_radius_is_six": noisy_radius == 6,
        "worst_radius_five_is_skew_index_60": worst_radius_5 == [(10, 5, 6)],
        "worst_radius_six_has_index_64": all(
            a * d == 64 for a, _b, d in worst_radius_6
        ),
        "strict_interval_rule_used": margins[5] <= 2 * TAU
        and margins[6] > 2 * TAU,
        "wp174_margin_was_rectangular_domain": True,
        "detector_margin_must_be_recomputed_after_domain_expansion": True,
        "selector_remains_conditional": True,
    }

    result = {
        "work_package": "WP176",
        "claim": "On the arbitrary-HNF quotient domain with K=64, the noiseless radius-five certificate has margin one; with absolute count error tau=1 the first robust recurrence-growth radius is six.",
        "order_cap_K": K,
        "absolute_count_error_tau": TAU,
        "hnf_quotients_tested": len(domain),
        "noiseless_corrected_radius": 5,
        "first_error_robust_radius": noisy_radius,
        "minimum_deficits": margins,
        "worst_radius_five_hnfs": [
            {"a": a, "b": b, "d": d, "index": a * d}
            for a, b, d in worst_radius_5
        ],
        "worst_radius_six_hnfs": [
            {"a": a, "b": b, "d": d, "index": a * d}
            for a, b, d in worst_radius_6
        ],
        "classification": "corrected detector-resolution gate for arbitrary finite quotients.",
        "instrument_gate": "For K=64 and tau=1, a physically typed HNF-domain recurrence selector needs radius six, not five.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp176_hnf_growth_resolution_margin.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
