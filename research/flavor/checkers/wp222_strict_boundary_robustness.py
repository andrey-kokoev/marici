"""WP222 exact checker: strict boundary from robustness.

Tests whether the strict-boundary rule can be derived from a robustness
requirement rather than declared as a detector convention.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


TARGET = Fraction(1, 4)


CASES = {
    "below": Fraction(1, 5),
    "touching": Fraction(1, 4),
    "above": Fraction(1, 3),
}


def nonstrict_accepts(error: Fraction, target: Fraction = TARGET) -> bool:
    return error <= target


def robust_accepts(error: Fraction, target: Fraction = TARGET) -> bool:
    """Accept only if some positive perturbation can be tolerated."""

    return error < target


def has_positive_margin(error: Fraction, target: Fraction = TARGET) -> bool:
    return target - error > 0


def main() -> None:
    nonstrict = {name: nonstrict_accepts(value) for name, value in CASES.items()}
    robust = {name: robust_accepts(value) for name, value in CASES.items()}
    margins = {name: str(TARGET - value) for name, value in CASES.items()}

    checks = {
        "below_has_positive_margin": has_positive_margin(CASES["below"]),
        "touching_has_zero_margin": TARGET - CASES["touching"] == 0,
        "above_has_negative_margin": TARGET - CASES["above"] < 0,
        "nonstrict_accepts_touching": nonstrict["touching"],
        "robust_rejects_touching": not robust["touching"],
        "robust_accepts_below": robust["below"],
        "robust_rejects_above": not robust["above"],
        "strict_rule_equivalent_to_positive_margin": all(
            robust[name] == has_positive_margin(value) for name, value in CASES.items()
        ),
        "derivation_requires_robustness_axiom": True,
        "does_not_supply_fault_model_apparatus_or_calibration": True,
    }

    result = {
        "work_package": "WP222",
        "claim": "The strict-boundary rule follows from robust discrimination: touching at the target has zero margin and must be rejected.",
        "admitted_domain": "detector comparisons with target 1/4 and robustness under positive perturbation.",
        "faithful_quotient": "comparison outcome plus margin sign; not a new physical16 selector.",
        "target": str(TARGET),
        "cases": {name: str(value) for name, value in CASES.items()},
        "margins": margins,
        "nonstrict_acceptance": nonstrict,
        "robust_acceptance": robust,
        "classification": "conditional structural detector-rule derivation.",
        "smallest_exact_falsifier": "The touching case error=1/4 is accepted by non-strict comparison but has zero robust margin.",
        "remaining_gate": "Admit robustness as a source/detector requirement and separately derive channel exchange, sentinel, executability, and calibration.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp222_strict_boundary_robustness.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
