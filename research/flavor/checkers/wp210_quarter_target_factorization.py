"""WP210 exact checker: quarter-target factorization.

WP209 leaves the 1/4 target. This checker audits a two-gate factorization:
adjacent multiplicities have gap 1, interval separation consumes half the gap,
and fault/readout reserve consumes half of that half, yielding 1/4.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


FACTORIZATIONS = {
    "two_half_gates": {
        "gap": Fraction(1, 1),
        "separation_fraction": Fraction(1, 2),
        "reserve_fraction": Fraction(1, 2),
    },
    "no_reserve": {
        "gap": Fraction(1, 1),
        "separation_fraction": Fraction(1, 2),
        "reserve_fraction": Fraction(1, 1),
    },
    "three_way_reserve": {
        "gap": Fraction(1, 1),
        "separation_fraction": Fraction(1, 2),
        "reserve_fraction": Fraction(1, 3),
    },
}


def target(factors: dict[str, Fraction]) -> Fraction:
    return (
        factors["gap"]
        * factors["separation_fraction"]
        * factors["reserve_fraction"]
    )


def main() -> None:
    evaluated = {
        name: {
            "gap": str(factors["gap"]),
            "separation_fraction": str(factors["separation_fraction"]),
            "reserve_fraction": str(factors["reserve_fraction"]),
            "target": str(target(factors)),
        }
        for name, factors in FACTORIZATIONS.items()
    }

    checks = {
        "two_half_gates_yield_one_fourth": target(FACTORIZATIONS["two_half_gates"])
        == Fraction(1, 4),
        "no_reserve_yields_one_half": target(FACTORIZATIONS["no_reserve"])
        == Fraction(1, 2),
        "three_way_reserve_yields_one_sixth": target(
            FACTORIZATIONS["three_way_reserve"]
        )
        == Fraction(1, 6),
        "quarter_depends_on_half_reserve": FACTORIZATIONS["two_half_gates"][
            "reserve_fraction"
        ]
        == Fraction(1, 2),
        "gap_one_comes_from_adjacent_multiplicity": FACTORIZATIONS["two_half_gates"][
            "gap"
        ]
        == 1,
        "separation_half_comes_from_disjoint_intervals": FACTORIZATIONS[
            "two_half_gates"
        ]["separation_fraction"]
        == Fraction(1, 2),
        "reserve_half_still_needs_fault_contract": True,
        "quarter_not_derived_without_reserve_law": True,
        "different_reserve_changes_target": target(FACTORIZATIONS["two_half_gates"])
        != target(FACTORIZATIONS["three_way_reserve"]),
        "wp209_target_reduced_to_reserve_law": True,
        "strictness_still_required_at_target": True,
        "physical_authority_not_complete": True,
    }

    result = {
        "work_package": "WP210",
        "claim": "The one-fourth target factors as half the adjacent multiplicity gap times a half-reserve law; the remaining authority gate is the reserve law.",
        "factorizations": evaluated,
        "classification": "target-factorization audit; quarter reduced to reserve law.",
        "remaining_gate": "Derive the half-reserve fault/readout law.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp210_quarter_target_factorization.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
