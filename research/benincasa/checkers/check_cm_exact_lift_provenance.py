#!/usr/bin/env python3
"""Verify provenance-carrying exact lifts for the rank-four CM packet."""

import json
import os
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CRATE = ROOT / "marici-gm"
CASES = (("A", 32003), ("A", 65521), ("B", 65521), ("HOMA", 32003))


def run_case(point, prime):
    environment = os.environ.copy()
    environment.update(
        NORMAL_TOWER="1",
        CM_FIRST_NORMAL_HORIZONTAL="1",
        CM_FIRST_NORMAL_DERIVATIVE_COUNT="9",
        CM_FIRST_NORMAL_INCLUDE_CYCLIC_DERIVATIVES="1",
        CM_EXACT_LIFT_AUDIT="1",
        KINEMATIC_POINT=point,
        PRIME=str(prime),
    )
    completed = subprocess.run(
        ["cargo", "run", "--quiet", "--bin", "cm_normal_tower_rank"],
        cwd=CRATE,
        env=environment,
        text=True,
        capture_output=True,
        check=True,
    )
    audit = re.search(
        r"EXACT_LIFT_AUDIT seed_count=(\d+) basis_count=(\d+) class_count=(\d+) "
        r"trace_nonzero_components=(\d+) trace_term_count=(\d+)",
        completed.stderr,
    )
    rank = re.search(
        r"cohomology_rank=(\d+) labelled_class_rank=(\d+) label_count=(\d+)",
        completed.stdout,
    )
    if audit is None or rank is None:
        raise RuntimeError("missing exact-lift or rank summary")
    return {
        "point": point,
        "prime": prime,
        "seed_count": int(audit.group(1)),
        "basis_count": int(audit.group(2)),
        "class_count": int(audit.group(3)),
        "trace_nonzero_components": int(audit.group(4)),
        "trace_term_count": int(audit.group(5)),
        "cohomology_rank": int(rank.group(1)),
        "class_rank": int(rank.group(2)),
        "label_count": int(rank.group(3)),
    }


def main():
    runs = [run_case(point, prime) for point, prime in CASES]
    checks = {
        "four_original_exact_generators_are_retained": all(run["seed_count"] == 4 for run in runs),
        "all_sixteen_classes_have_verified_traces": all(
            run["class_count"] == run["label_count"] == 16 for run in runs
        ),
        "fiberwise_rank_remains_four": all(run["class_rank"] == 4 for run in runs),
        "every_class_uses_nonzero_exact_provenance": all(
            run["trace_nonzero_components"] >= run["class_count"] for run in runs
        ),
    }
    packet = {
        "schema": "marici.cm_exact_lift_provenance.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "original_exact_generators": [
            "logarithmic_gradient_a",
            "logarithmic_gradient_b",
            "logarithmic_gradient_c",
            "localization_zK_minus_1",
        ],
        "runs": runs,
        "checks": checks,
        "scope": (
            "This certifies exact-lift provenance for fiber reductions. "
            "Differentiating the primitive packet and repairing mixed flatness remains open."
        ),
    }
    output = ROOT / "results" / "cm-exact-lift-provenance.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
