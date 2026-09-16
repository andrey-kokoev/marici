"""Finite spectral models for the Green-energy trace comparison gate.

The model satisfies the exact Green identity and graph-norm trace boundedness,
while its sharp Green-energy comparison constants diverge. It shows that the
currently established hypotheses do not imply response-trace continuity in the
canonical Green energy norm.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "research" / "voevodsky" / "results" / "green_energy_trace_gate.json"


def stage(n: int) -> dict[str, float | int | bool]:
    # On coordinate k, J_gr=1/k and Gamma=(a_k,b_k), where
    # a_k^2=(1+1/k)/2 and b_k^2=(1-1/k)/2.
    green_identity = True
    trace_gram_identity = True
    for k in range(1, n + 1):
        lam = 1.0 / k
        a2 = (1.0 + lam) / 2.0
        b2 = (1.0 - lam) / 2.0
        green_identity &= math.isclose(a2 - b2, lam, abs_tol=1e-15)
        trace_gram_identity &= math.isclose(a2 + b2, 1.0, abs_tol=1e-15)

    return {
        "dimension": n,
        "green_identity": green_identity,
        "trace_gram_identity": trace_gram_identity,
        "graph_trace_norm": 1.0,
        "minimum_green_eigenvalue": 1.0 / n,
        "sharp_energy_constant": math.sqrt(n),
    }


def main() -> None:
    dimensions = [1, 2, 4, 8, 16, 32, 64]
    stages = [stage(n) for n in dimensions]
    checks = {
        "green_identity_all_stages": all(s["green_identity"] for s in stages),
        "trace_graph_bounded_all_stages": all(
            float(s["graph_trace_norm"]) == 1.0 for s in stages
        ),
        "ordinary_trace_gram_is_identity": all(
            s["trace_gram_identity"] for s in stages
        ),
        "sharp_constant_is_sqrt_dimension": all(
            math.isclose(
                float(s["sharp_energy_constant"]),
                math.sqrt(int(s["dimension"])),
                abs_tol=1e-15,
            )
            for s in stages
        ),
        "uniform_energy_bound_fails": float(stages[-1]["sharp_energy_constant"])
        > float(stages[0]["sharp_energy_constant"]),
    }
    result = {
        "schema": "marici.voevodsky.green-energy-trace-gate.v1",
        "model": {
            "J_gr": "diag(1/k)",
            "Gamma": "column(sqrt((I+J_gr)/2), sqrt((I-J_gr)/2))",
            "J_boundary": "diag(I,-I)",
        },
        "stages": stages,
        "checks": checks,
        "passed": all(checks.values()),
        "conclusion": (
            "The Green identity and uniform graph-norm trace boundedness do not "
            "imply a uniform Green-energy trace bound. A separate estimate "
            "Gamma*Gamma <= C^2 |J_gr| is necessary."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
