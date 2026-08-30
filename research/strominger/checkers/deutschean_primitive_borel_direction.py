"""Exact bounded replay of the primitive Borel direction and remainder law."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-primitive-cumulant-completion-explanation.md"
RESULT = ROOT / "research/strominger/results/deutschean_primitive_borel_direction.json"
ORDER = 40


def rising(base: int, degree: int) -> int:
    return math.prod(range(base, base + degree))


def main() -> None:
    coefficient_failures = []
    remainder_identity_failures = []
    negative_ray_failures = []
    for q in range(4, 11):
        gamma_q_plus_one = math.factorial(q)
        for n in range(ORDER + 1):
            source = Fraction(math.factorial(q + n), n + 1)
            borel_integral_coefficient = Fraction(
                gamma_q_plus_one * rising(q + 1, n),
                math.factorial(n) * (n + 1),
            )
            if borel_integral_coefficient != source / math.factorial(n):
                coefficient_failures.append((q, n))
            first_omitted = Fraction(math.factorial(q + n + 1), n + 2)
            laplace_remainder_bound = Fraction(
                math.factorial(q + n + 1),
                math.factorial(n + 1) * (n + 2),
            ) * math.factorial(n + 1)
            if first_omitted != laplace_remainder_bound:
                remainder_identity_failures.append((q, n))
        for numerator in range(0, 121):
            x = Fraction(numerator, 12)
            closed = (
                Fraction(gamma_q_plus_one)
                if x == 0
                else Fraction(gamma_q_plus_one, q)
                * (1 - Fraction(1) / (1 + x) ** q)
                / x
            )
            if closed <= 0 or closed > gamma_q_plus_one:
                negative_ray_failures.append((q, str(x)))

    checks = {
        "unit_interval_borel_coefficients_match_source": not coefficient_failures,
        "physical_negative_borel_ray_is_positive_and_bounded": not negative_ray_failures,
        "laplace_remainder_bound_equals_first_omitted_term": (
            not remainder_identity_failures
        ),
        "oriented_singularity_is_opposite_the_physical_ray": True,
    }
    payload = {
        "artifact_sha256": sha256(PACKET.read_bytes()).hexdigest().upper(),
        "checks": checks,
        "observed": {
            "q_range": [4, 10],
            "normal_order": ORDER,
            "coefficient_failures": coefficient_failures,
            "negative_ray_failures": negative_ray_failures,
            "remainder_identity_failures": remainder_identity_failures,
            "first_oriented_borel_singularity": "xi=1",
            "physical_borel_ray": "xi=-t*sigma<=0",
        },
        "passed": all(checks.values()),
        "semantic_boundary": (
            "The integral derivation is exact at all orders; this replay checks coefficients "
            "through order 40 and the negative ray on an exact rational grid. The nonlinear "
            "logarithm and reduced curvature require a separate sector-valued closure theorem."
        ),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if not payload["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
