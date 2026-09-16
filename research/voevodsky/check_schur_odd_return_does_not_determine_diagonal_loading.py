"""Show that a fixed oriented Schur return does not determine diagonal loading.

For C_r=(r, i*h/r)^T and D=1, the positive rank-one return C_r C_r^*
has the same oriented off-diagonal magnitude h for every r>0, while its two
diagonal entries are r^2 and h^2/r^2. Thus the known odd return and Fourier
quarter-turn cannot prove either endpoint survival margin.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = (
    ROOT
    / "research"
    / "voevodsky"
    / "results"
    / "schur_odd_return_diagonal_loading_no_go.json"
)


def sample(r: float, h: float, a: float, b: float) -> dict[str, float | bool]:
    r11 = r * r
    r22 = h * h / (r * r)
    # C=(r, i h/r), so (C C*)_12=-i h and -Im=+h.
    odd = h
    return {
        "r": r,
        "r11": r11,
        "r22": r22,
        "odd_return": odd,
        "rank_one_determinant": r11 * r22 - odd * odd,
        "first_residual": a - r11,
        "second_residual": b - r22,
        "return_positive_semidefinite": r11 >= 0
        and r22 >= 0
        and math.isclose(r11 * r22, odd * odd, abs_tol=1e-12),
    }


def main() -> None:
    h = 0.2
    a = 1.0
    b = 1.0
    r_first_kill = math.sqrt(a)
    r_second_kill = h / math.sqrt(b)
    stages = [
        sample(0.1, h, a, b),
        sample(r_second_kill, h, a, b),
        sample(0.5, h, a, b),
        sample(r_first_kill, h, a, b),
        sample(2.0, h, a, b),
    ]
    checks = {
        "odd_return_fixed": all(
            math.isclose(float(s["odd_return"]), h, abs_tol=1e-12)
            for s in stages
        ),
        "all_returns_positive_semidefinite": all(
            bool(s["return_positive_semidefinite"]) for s in stages
        ),
        "all_returns_rank_one": all(
            math.isclose(float(s["rank_one_determinant"]), 0.0, abs_tol=1e-12)
            for s in stages
        ),
        "first_margin_can_vanish": math.isclose(
            float(stages[3]["first_residual"]), 0.0, abs_tol=1e-12
        ),
        "second_margin_can_vanish": math.isclose(
            float(stages[1]["second_residual"]), 0.0, abs_tol=1e-12
        ),
        "a_margin_can_be_negative": any(
            float(s["first_residual"]) < 0 or float(s["second_residual"]) < 0
            for s in stages
        ),
    }
    result = {
        "schema": "marici.voevodsky.schur-odd-return-diagonal-loading-no-go.v1",
        "parameters": {"h": h, "a": a, "b": b, "D": 1.0},
        "family": "C_r=(r, i*h/r)^T",
        "stages": stages,
        "checks": checks,
        "passed": all(checks.values()),
        "conclusion": (
            "The frozen odd Schur return, positivity, and rank-one quarter-turn "
            "structure leave a reciprocal scaling gauge. Either diagonal endpoint "
            "margin can vanish or become negative. Source-normalized C and D, or "
            "independent diagonal loading bounds, are necessary."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
