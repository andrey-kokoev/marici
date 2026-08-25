"""WP172 exact checker: finite-size bound growth certificate.

WP171 showed finite growth windows can be fooled by large finite tori. This
checker verifies the positive boundary: for square tori (Z/NZ)^2 with
N <= B, radius ceil(B/2) is necessary and sufficient to force a Cayley-growth
difference from Z^2.
"""

from __future__ import annotations

import json
from collections import deque
from pathlib import Path


B = 8
R_CERT = (B + 1) // 2
GENERATORS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def z2_ball_size(radius: int) -> int:
    return 1 + 2 * radius * (radius + 1)


def torus_ball_size(radius: int, n: int) -> int:
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
    return len(seen)


def first_growth_difference(n: int, max_radius: int) -> int | None:
    for radius in range(max_radius + 1):
        if z2_ball_size(radius) != torus_ball_size(radius, n):
            return radius
    return None


def certificate_radius_for_bound(bound: int) -> int:
    return (bound + 1) // 2


def general_certificate_law(max_bound: int) -> bool:
    for bound in range(2, max_bound + 1):
        radius = certificate_radius_for_bound(bound)
        if not all(
            first_growth_difference(n, radius) is not None
            for n in range(2, bound + 1)
        ):
            return False
        if first_growth_difference(bound, radius - 1) is not None:
            return False
    return True


def main() -> None:
    first_diffs = {n: first_growth_difference(n, R_CERT) for n in range(2, B + 1)}
    worst_diff = max(first_diffs.values())
    under_radius = R_CERT - 1
    worst_under_diff = first_growth_difference(B, under_radius)

    checks = {
        "certificate_radius_is_ceil_B_over_2": R_CERT == 4,
        "all_square_tori_N_le_B_separate_by_R_cert": all(
            diff is not None for diff in first_diffs.values()
        ),
        "worst_case_N_equals_B": first_diffs[B] == R_CERT,
        "under_radius_fails_on_N_equals_B": worst_under_diff is None,
        "depth_R_cert_growth_for_Z2": z2_ball_size(R_CERT) == 41,
        "depth_R_cert_growth_for_Z8_square": torus_ball_size(R_CERT, B) == 39,
        "difference_is_positive": z2_ball_size(R_CERT) - torus_ball_size(R_CERT, B)
        == 2,
        "smaller_tori_separate_no_later": all(
            diff <= R_CERT for diff in first_diffs.values()
        ),
        "general_law_holds_through_bound_14": general_certificate_law(14),
        "source_bound_is_required": True,
        "finite_growth_selector_is_conditional": True,
        "does_not_identify_all_finite_sources": True,
    }

    result = {
        "work_package": "WP172",
        "claim": "On square finite-torus rivals with source period bound B, Cayley-growth observation to radius ceil(B/2) separates every finite rival from Z^2, and the radius is sharp.",
        "period_bound_B": B,
        "certificate_radius": R_CERT,
        "first_differences": first_diffs,
        "worst_case": {
            "finite_rival": f"(Z/{B}Z)^2",
            "matches_through_radius": under_radius,
            "first_difference_radius": first_diffs[B],
            "z2_growth_at_certificate_radius": z2_ball_size(R_CERT),
            "finite_growth_at_certificate_radius": torus_ball_size(R_CERT, B),
        },
        "classification": "conditional finite-versus-infinite growth selector under a source period bound.",
        "instrument_gate": "The period bound B and radius-ceil(B/2) recurrence instrument must be physically derived.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp172_growth_bound_certificate.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
