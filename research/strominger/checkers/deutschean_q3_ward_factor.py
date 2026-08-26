"""Exact algebraic audit of the universal q^3 curvature factor."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-primitive-cumulant-completion-explanation.md"
RESULT = ROOT / "research/strominger/results/deutschean_q3_ward_factor.json"


def main() -> None:
    q, u, du, ddu = sp.symbols("q u du ddu")
    r = 1 + q * u
    dr = u + q * du
    ddr = 2 * du + q * ddu
    curvature = (
        r
        - 1 / r
        + q * (1 - 3 / r) * dr
        + q**2 * (ddr - 2 * dr**2 / r)
    )
    reduced = ((1 + q * u) * ddu - u * du - 2 * q * du**2) / (1 + q * u)

    c = sp.symbols("c", nonzero=True)
    hostile_r = 1 + c
    hostile_curvature = sp.factor(hostile_r - 1 / hostile_r)

    checks = {
        "memoryless_fixed_section_has_zero_curvature": sp.simplify(
            curvature.subs({u: 0, du: 0, ddu: 0})
        )
        == 0,
        "regular_deformation_has_exact_q_cubed_ward_factor": sp.simplify(
            curvature - q**3 * reduced
        )
        == 0,
        "reduced_curvature_is_regular_when_one_plus_q_u_is_invertible": (
            sp.denom(sp.cancel(reduced)) == q * u + 1
        ),
        "hostile_nonregular_deformation_destroys_q_cubed_factor": (
            hostile_curvature != 0 and hostile_curvature.subs(q, 0) != 0
        ),
    }
    payload = {
        "artifact_sha256": sha256(PACKET.read_bytes()).hexdigest().upper(),
        "checks": checks,
        "observed": {
            "factored_curvature": str(sp.factor(curvature)),
            "reduced_curvature": str(sp.factor(reduced)),
            "hostile_curvature": str(hostile_curvature),
        },
        "passed": all(checks.values()),
        "semantic_boundary": (
            "This proves the algebraic Ward factor whenever r-1 is divisible by q. "
            "Source connected-cumulant regularity supplies that premise. It does not "
            "prove positivity or Borel-Laplace contractivity of the reduced curvature."
        ),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if not payload["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
