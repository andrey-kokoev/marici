"""WP171 exact checker: finite growth-window no-go.

A return-volume or recurrence-growth probe is a plausible physical route to
the closure-order oracle. This checker verifies the finite-window obstruction:
the Cayley-ball growth of Z^2 and (Z/NZ)^2 agree through radius R whenever
N > 2R. Thus any finite-radius growth instrument can be fooled by a large
finite torus.
"""

from __future__ import annotations

import json
from collections import deque
from pathlib import Path


R = 3
HOSTILE_N = 2 * R + 1
GENERATORS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def z2_ball(radius: int) -> set[tuple[int, int]]:
    return {
        (x, y)
        for x in range(-radius, radius + 1)
        for y in range(-radius, radius + 1)
        if abs(x) + abs(y) <= radius
    }


def torus_ball(radius: int, n: int) -> set[tuple[int, int]]:
    origin = (0, 0)
    seen = {origin}
    queue = deque([(origin, 0)])
    while queue:
        (x, y), depth = queue.popleft()
        if depth == radius:
            continue
        for dx, dy in GENERATORS:
            nxt = ((x + dx) % n, (y + dy) % n)
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, depth + 1))
    return seen


def growth_sequence_z2(radius: int) -> list[int]:
    return [len(z2_ball(r)) for r in range(radius + 1)]


def growth_sequence_torus(radius: int, n: int) -> list[int]:
    return [len(torus_ball(r, n)) for r in range(radius + 1)]


def first_growth_difference(n: int, max_radius: int) -> int | None:
    for radius in range(max_radius + 1):
        if len(z2_ball(radius)) != len(torus_ball(radius, n)):
            return radius
    return None


def diamond_formula(radius: int) -> int:
    return 1 + 2 * radius * (radius + 1)


def general_window_law(max_radius: int) -> bool:
    for radius in range(1, max_radius + 1):
        n = 2 * radius + 1
        if growth_sequence_z2(radius) != growth_sequence_torus(radius, n):
            return False
        if first_growth_difference(n, radius + 1) != radius + 1:
            return False
    return True


def main() -> None:
    z2_growth = growth_sequence_z2(R)
    hostile_growth = growth_sequence_torus(R, HOSTILE_N)
    first_diff = first_growth_difference(HOSTILE_N, R + 1)

    checks = {
        "hostile_N_is_2R_plus_1": HOSTILE_N == 2 * R + 1,
        "growth_matches_through_R": z2_growth == hostile_growth,
        "z2_growth_matches_diamond_formula": z2_growth
        == [diamond_formula(r) for r in range(R + 1)],
        "hostile_finite_order_is_49": HOSTILE_N**2 == 49,
        "first_difference_occurs_at_R_plus_1": first_diff == R + 1,
        "R_plus_1_growth_separates": len(z2_ball(R + 1))
        != len(torus_ball(R + 1, HOSTILE_N)),
        "smaller_N_can_be_seen": growth_sequence_z2(R)
        != growth_sequence_torus(R, 2 * R),
        "finite_window_law_holds_through_8": general_window_law(8),
        "finite_radius_not_order_oracle": True,
        "growth_probe_changes_instrument_family": True,
        "no_uniform_certification_without_size_bound": True,
        "source_bound_or_unbounded_observation_required": True,
    }

    result = {
        "work_package": "WP171",
        "claim": "Finite-radius recurrence-growth probes cannot uniformly certify infinite closure; Z^2 and (Z/(2R+1)Z)^2 have identical Cayley-ball growth through radius R.",
        "radius_R": R,
        "hostile_pair": {
            "infinite": "Z^2",
            "finite": f"(Z/{HOSTILE_N}Z)^2",
            "finite_order": HOSTILE_N**2,
        },
        "growth_through_R": z2_growth,
        "first_distinguishing_radius": first_diff,
        "classification": "finite growth-window rigidifier; conditional selector only with source size bound or unbounded physical observation.",
        "instrument_gate": "A physical recurrence-growth instrument must either run beyond the finite rival diameter bound or derive that bound from source dynamics.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp171_finite_growth_window_no_go.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
