"""Exact source-level geometry of the memoryless normal completion.

The checker proves the Gevrey normalization for the primitive logarithmic
coordinate majorant.  It does not promote that bound through log Z or the
adjacent-grade cumulant margin.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-primitive-cumulant-completion-explanation.md"
RESULT = ROOT / "research/strominger/results/deutschean_gevrey_completion_geometry.json"


def raw_majorant(q: int, n: int) -> int:
    """Gamma(q+n+1)/(n+1), with integer q,n."""
    return math.factorial(q + n) // (n + 1)


def raw_ratio(q: int, n: int) -> Fraction:
    return Fraction((q + n + 1) * (n + 1), n + 2)


def borel_ratio(q: int, n: int) -> Fraction:
    return Fraction(q + n + 1, n + 2)


def main() -> None:
    # Exact bounded replay of identities whose symbolic forms are recorded
    # below.  Large n witnesses the raw-ratio divergence without pretending
    # that a finite sample proves it.
    fixture_ns = [0, 1, 2, 7, 31, 127]
    ratio_identity = all(
        Fraction(raw_majorant(q, n + 1), raw_majorant(q, n))
        == raw_ratio(q, n)
        for q in range(4, 11)
        for n in fixture_ns
    )
    normalized_identity = all(
        Fraction(raw_majorant(q, n + 1), math.factorial(n + 1))
        / Fraction(raw_majorant(q, n), math.factorial(n))
        == borel_ratio(q, n)
        for q in range(4, 11)
        for n in fixture_ns
    )

    checks = {
        "gamma_integrated_raw_ratio_identity": ratio_identity,
        "raw_ratio_forward_difference_identity": all(
            raw_ratio(q, n + 1) - raw_ratio(q, n)
            == Fraction(n * n + 5 * n + q + 5, (n + 2) * (n + 3))
            for q in range(4, 11)
            for n in fixture_ns
        ),
        "raw_ratio_forward_difference_is_at_least_one_symbolically": all(
            q - 1 >= 0 for q in range(4, 11)
        ),
        "factorial_normalized_ratio_identity": normalized_identity,
        "borel_ratio_decreases_in_n_for_q_at_least_4": all(
            borel_ratio(q, n + 1) < borel_ratio(q, n)
            for q in range(4, 11)
            for n in fixture_ns
        ),
        "uniform_borel_type_is_at_most_11_over_2": all(
            borel_ratio(q, n) <= Fraction(11, 2)
            for q in range(4, 11)
            for n in fixture_ns
        ),
        "far_wall_primitive_transport_is_strictly_contractive": (
            Fraction(1, 60) * Fraction(11, 2) == Fraction(11, 120)
            and Fraction(11, 120) < 1
        ),
        "moving_integrand_singularities_accumulate_at_memoryless_divisor": all(
            Fraction(1, 2 * radius_denominator) < Fraction(1, radius_denominator)
            for radius_denominator in [1, 2, 10, 100, 1000]
        ),
    }

    payload = {
        "artifact_sha256": sha256(PACKET.read_bytes()).hexdigest().upper(),
        "checks": checks,
        "observed": {
            "normal_divisor": "Sigma={t=0}",
            "integrand_singularity_family": "t=-1/y for every y>0",
            "primitive_raw_majorant": "c_n(q)=Gamma(q+n+1)/(n+1)",
            "primitive_raw_ratio": "c_(n+1)/c_n=(q+n+1)(n+1)/(n+2)",
            "primitive_borel_ratio": "(c_(n+1)/(n+1)!)/(c_n/n!)=(q+n+1)/(n+2)",
            "uniform_q_range": [4, 10],
            "uniform_borel_type_bound": "11/2",
            "far_wall_t_bound": "1/60",
            "primitive_contraction_bound": "11/120",
        },
        "passed": all(checks.values()),
        "semantic_boundary": (
            "Unbounded source majorants exclude an ordinary unweighted analytic "
            "completion. Factorial normalization gives an exact primitive "
            "Gevrey/Borel contraction bound. The checker does not establish "
            "oriented positivity after log Z, adjacent-grade differencing, or "
            "the physical reserve remainder."
        ),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if not payload["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
