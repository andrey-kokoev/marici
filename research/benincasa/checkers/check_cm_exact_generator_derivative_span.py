#!/usr/bin/env python3
"""Audit the span supplied by derivatives of the exact CM generators."""

import json
import os
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CRATE = ROOT / "marici-gm"
EXE = CRATE / "target" / "release" / "cm_normal_tower_rank.exe"
CASES = (("A", 32003), ("A", 65521), ("B", 65521), ("HOMA", 32003))


def run_rank(point: str, prime: int, count: int) -> int:
    env = os.environ.copy()
    env.update(
        NORMAL_TOWER="1",
        CM_FIRST_NORMAL_HORIZONTAL="1",
        CM_FIRST_NORMAL_DERIVATIVE_COUNT="0",
        CM_FIRST_NORMAL_INCLUDE_CYCLIC="1",
        CM_EXACT_GENERATOR_DERIVATIVES="1",
        CM_EXACT_GENERATOR_DERIVATIVE_COUNT=str(count),
        KINEMATIC_POINT=point,
        PRIME=str(prime),
    )
    completed = subprocess.run(
        [str(EXE)], cwd=CRATE, env=env, text=True, capture_output=True, check=True
    )
    match = re.search(r"labelled_class_rank=(\d+)", completed.stdout)
    if match is None:
        raise RuntimeError(f"missing rank summary for {point}, {prime}, {count}")
    return int(match.group(1))


def main() -> None:
    if not EXE.exists():
        raise RuntimeError("release executable is absent; run cargo build --release first")
    runs = []
    for point, prime in CASES:
        sequence = [run_rank(point, prime, count) for count in range(13)]
        runs.append({"point": point, "prime": prime, "rank_sequence": sequence})

    expected = [4, 5, 6, 7] + [7] * 9
    checks = {
        "associated_grade_starts_at_rank_four": all(r["rank_sequence"][0] == 4 for r in runs),
        "first_three_exact_derivatives_supply_three_directions": all(
            r["rank_sequence"][:4] == expected[:4] for r in runs
        ),
        "remaining_exact_derivatives_add_no_fiber_rank": all(
            r["rank_sequence"] == expected for r in runs
        ),
        "replicates_across_points_and_primes": len(
            {tuple(r["rank_sequence"]) for r in runs}
        ) == 1,
    }
    packet = {
        "schema": "marici.cm_exact_generator_derivative_span.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "class_order": [
            "d1_exact_gradient_a",
            "d1_exact_gradient_b",
            "d1_exact_gradient_c",
            "d1_exact_localization",
            "d2_exact_gradient_a",
            "d2_exact_gradient_b",
            "d2_exact_gradient_c",
            "d2_exact_localization",
            "d3_exact_gradient_a",
            "d3_exact_gradient_b",
            "d3_exact_gradient_c",
            "d3_exact_localization",
        ],
        "runs": runs,
        "checks": checks,
        "scope": (
            "This is a fiberwise span theorem for derivatives of source exact generators. "
            "It does not establish mixed flatness or a connection on the rank-seven packet."
        ),
    }
    output = ROOT / "results" / "cm-exact-generator-derivative-span.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
