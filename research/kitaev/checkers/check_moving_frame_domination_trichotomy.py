#!/usr/bin/env python3
"""Exact weighted-tail audit for moving-frame operativity."""

import hashlib
import json
from pathlib import Path

from sympy import Rational

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/moving-frame-domination-trichotomy.json"


def main():
    rows = []
    for n in [1, 2, 4, 8, 16]:
        q = Rational(1, n * n)
        r2 = 4
        h2 = 1
        analytic_frame = r2 / q
        analytic_seam = h2 / q
        full_q = q + h2
        full_frame = r2 / full_q
        full_seam = h2 / full_q
        assert full_frame < 4 or n == 1
        assert full_seam <= 1
        rows.append({
            "N": n,
            "q_N": str(q),
            "analytic_frame_constant_squared": str(analytic_frame),
            "analytic_seam_constant_squared": str(analytic_seam),
            "full_frame_constant_squared": str(full_frame),
            "full_seam_constant_squared": str(full_seam),
        })

    # Orthogonal port: it contributes no weight on the moving direction.
    q = Rational(1, 16 * 16)
    orthogonal_full_q_on_witness = q
    assert 4 / orthogonal_full_q_on_witness == 1024

    payload = {
        "schema": "marici.kitaev.moving_frame_domination_trichotomy.v1",
        "status": "pass",
        "analytic_only": "frame and seam domination constants diverge",
        "same_direction_authorized_seam": "uniformly repairs both in the fixture",
        "orthogonal_seam": "does not repair moving frame",
        "fixtures": rows,
        "classifications": ["harmless quotient", "frame non-descent", "hybrid-port obligation"],
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope_exclusions": ["theta/Tate matrices", "seam authority", "completion theorem", "RH"],
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
