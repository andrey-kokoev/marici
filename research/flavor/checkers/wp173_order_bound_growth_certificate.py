"""WP173 exact checker: order-bound growth certificate.

WP172 used a source period bound. This checker weakens the source datum to a
finite-order cap K on rectangular tori (Z/n1Z)x(Z/n2Z). A radius R growth
window separates every finite rival of order <= K from Z^2 exactly when no
pair n1,n2 with n1*n2 <= K has both n1,n2 > 2R.
"""

from __future__ import annotations

import json
from collections import deque
from pathlib import Path


K = 64
GENERATORS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def z2_ball_size(radius: int) -> int:
    return 1 + 2 * radius * (radius + 1)


def torus_ball_size(radius: int, n1: int, n2: int) -> int:
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


def first_growth_difference(n1: int, n2: int, max_radius: int) -> int | None:
    for radius in range(max_radius + 1):
        if z2_ball_size(radius) != torus_ball_size(radius, n1, n2):
            return radius
    return None


def certificate_radius_for_order_cap(order_cap: int) -> int:
    radius = 0
    while (2 * radius + 1) ** 2 <= order_cap:
        radius += 1
    return radius


def general_order_cap_law(max_order_cap: int) -> bool:
    for order_cap in range(4, max_order_cap + 1):
        radius = certificate_radius_for_order_cap(order_cap)
        rivals = rivals_under_order_cap(order_cap)
        if not all(
            first_growth_difference(n1, n2, radius) is not None
            for n1, n2 in rivals
        ):
            return False
        if radius > 0 and (2 * (radius - 1) + 1) ** 2 <= order_cap:
            n = 2 * (radius - 1) + 1
            if n >= 2 and first_growth_difference(n, n, radius - 1) is not None:
                return False
    return True


def main() -> None:
    radius = certificate_radius_for_order_cap(K)
    rivals = rivals_under_order_cap(K)
    first_diffs = {
        f"({n1},{n2})": first_growth_difference(n1, n2, radius)
        for n1, n2 in rivals
    }
    under_radius = radius - 1
    hostile_under_n = 2 * under_radius + 1

    checks = {
        "order_cap_is_64": K == 64,
        "certificate_radius_is_4": radius == 4,
        "all_order_bounded_rivals_separate_by_radius": all(
            diff is not None for diff in first_diffs.values()
        ),
        "under_radius_has_hostile_square_torus": hostile_under_n == 7
        and hostile_under_n**2 <= K,
        "hostile_square_matches_through_under_radius": first_growth_difference(
            hostile_under_n, hostile_under_n, under_radius
        )
        is None,
        "radius_four_separates_hostile_square": first_growth_difference(
            hostile_under_n, hostile_under_n, radius
        )
        == radius,
        "z2_growth_radius_four_is_41": z2_ball_size(radius) == 41,
        "hostile_growth_radius_four_is_37": torus_ball_size(
            radius, hostile_under_n, hostile_under_n
        )
        == 37,
        "square_torus_is_extremal_for_under_radius": (2 * under_radius + 1) ** 2
        <= K
        and (2 * radius + 1) ** 2 > K,
        "general_order_cap_law_holds_through_100": general_order_cap_law(100),
        "source_order_cap_required": True,
        "not_complete_finite_source_identifier": True,
    }

    result = {
        "work_package": "WP173",
        "claim": "A source finite-order cap K gives a finite recurrence-growth certificate at the least radius R with (2R+1)^2 > K.",
        "order_cap_K": K,
        "certificate_radius": radius,
        "rivals_tested": len(rivals),
        "hostile_under_radius_pair": {
            "finite_rival": f"(Z/{hostile_under_n}Z)^2",
            "order": hostile_under_n**2,
            "matches_Z2_through_radius": under_radius,
            "separates_at_radius": radius,
            "z2_growth_at_radius": z2_ball_size(radius),
            "finite_growth_at_radius": torus_ball_size(
                radius, hostile_under_n, hostile_under_n
            ),
        },
        "classification": "conditional finite-versus-infinite growth selector under a source order cap.",
        "instrument_gate": "The finite-order cap K and recurrence radius R must be derived before the readout has selector authority.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp173_order_bound_growth_certificate.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
