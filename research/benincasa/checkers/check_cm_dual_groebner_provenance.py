#!/usr/bin/env python3
"""Replicate the dual-number tracked Gröbner and reduction audit."""

import json
import os
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CRATE = ROOT / "marici-gm"
EXE = CRATE / "target" / "release" / "cm_normal_tower_rank.exe"
CASES = (("A", 32003), ("A", 65521), ("B", 65521), ("HOMA", 32003))
PATTERN = re.compile(
    r"DUAL_GROEBNER_AUDIT seed_count=(\d+) basis_count=(\d+) "
    r"tangent_term_count=(\d+) target_count=(\d+) target_tangent_term_count=(\d+)"
)


def run(point, prime, direction):
    env = os.environ.copy()
    env.update(
        NORMAL_TOWER="1",
        CM_DUAL_GROEBNER_AUDIT="1",
        CM_DUAL_DIRECTION=str(direction),
        KINEMATIC_POINT=point,
        PRIME=str(prime),
    )
    completed = subprocess.run(
        [str(EXE)], cwd=CRATE, env=env, text=True, capture_output=True, check=True
    )
    match = PATTERN.search(completed.stderr)
    if match is None:
        raise RuntimeError("missing dual Gröbner audit summary")
    return {
        "point": point,
        "prime": prime,
        "direction": direction,
        "seed_count": int(match.group(1)),
        "basis_count": int(match.group(2)),
        "tangent_term_count": int(match.group(3)),
        "target_count": int(match.group(4)),
        "target_tangent_term_count": int(match.group(5)),
    }


def main():
    runs = [run(point, prime, direction) for point, prime in CASES for direction in range(3)]
    checks = {
        "all_four_source_generators_retained": all(item["seed_count"] == 4 for item in runs),
        "dual_basis_has_expected_thirty_six_elements": all(item["basis_count"] == 36 for item in runs),
        "all_seven_probe_reductions_reconstruct": all(item["target_count"] == 7 for item in runs),
        "every_base_direction_has_nonzero_tangent_data": all(
            item["tangent_term_count"] > 0 and item["target_tangent_term_count"] > 0
            for item in runs
        ),
    }
    packet = {
        "schema": "marici.cm_dual_groebner_provenance.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "runs": runs,
        "checks": checks,
        "scope": (
            "This validates dual-number Buchberger provenance and dual normal-form reconstruction. "
            "Rank-seven matrix curvature extraction remains the next integration gate."
        ),
    }
    output = ROOT / "results" / "cm-dual-groebner-provenance.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": packet["status"], "checks": checks, "runs": runs}, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
