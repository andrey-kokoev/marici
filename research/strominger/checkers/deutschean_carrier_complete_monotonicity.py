"""Exact finite-jet hostile for the fixed-measure carrier.

This checker tests coefficient signs only.  It does not prove complete
monotonicity on the positive half-line or the completed cumulant theorem.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-primitive-cumulant-completion-explanation.md"
RESULT = ROOT / "research/strominger/results/deutschean_carrier_complete_monotonicity.json"
MAX_GRADE = 120


def convolve(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(MAX_GRADE + 1)]
    for n in range(MAX_GRADE + 1):
        out[n] = sum(left[k] * right[n - k] for k in range(n + 1))
    return out


def carrier_coefficients(q: int) -> list[Fraction]:
    log_ratio = [Fraction((-1) ** n, n + 1) for n in range(MAX_GRADE + 1)]
    quarter_power = [Fraction(1)]
    for n in range(1, MAX_GRADE + 1):
        quarter_power.append(
            quarter_power[-1] * (Fraction(1, 4) - (n - 1)) / n
        )

    power = [Fraction(0) for _ in range(MAX_GRADE + 1)]
    power[0] = Fraction(1)
    for _ in range(q):
        power = convolve(power, log_ratio)
    return convolve(quarter_power, power)


def signed_failures(coefficients: list[Fraction]) -> list[int]:
    return [
        n
        for n, coefficient in enumerate(coefficients)
        if ((-1) ** n) * coefficient < 0
    ]


def main() -> None:
    failures = {}
    for q in range(1, 11):
        failures[str(q)] = signed_failures(carrier_coefficients(q))

    checks = {
        "q1_hostile_has_failure": bool(failures["1"]),
        "q1_first_failure_is_grade_19": failures["1"][0] == 19,
        "q2_through_q10_have_no_failure_through_grade_120": all(
            not failures[str(q)] for q in range(2, 11)
        ),
    }
    payload = {
        "artifact_sha256": sha256(PACKET.read_bytes()).hexdigest().upper(),
        "checks": checks,
        "observed": {
            "maximum_grade": MAX_GRADE,
            "first_failure_by_q": {
                q: (grades[0] if grades else None) for q, grades in failures.items()
            },
        },
        "passed": all(checks.values()),
        "semantic_boundary": (
            "Exact Taylor-coefficient evidence at the memoryless divisor only. "
            "Absence of a failure through grade 120 does not prove complete "
            "monotonicity, analytic cone preservation, or reserve domination."
        ),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if not payload["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
