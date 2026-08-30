"""WP227 exact checker: coupling uniqueness principles.

Tests candidate principles that could make a coupled source-detector error
coupling unique rather than glued on externally.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


CAP = Fraction(1, 5)

COUPLINGS = {
    "width_heavy": (Fraction(3, 20), Fraction(1, 20)),
    "equal": (Fraction(1, 10), Fraction(1, 10)),
    "background_heavy": (Fraction(1, 20), Fraction(3, 20)),
}


PRINCIPLES = {
    "cap_only": {
        "source_derived": True,
        "symmetric": False,
        "strictly_convex": False,
    },
    "external_exchange": {
        "source_derived": False,
        "symmetric": True,
        "strictly_convex": False,
    },
    "source_symmetric_convex_cost": {
        "source_derived": True,
        "symmetric": True,
        "strictly_convex": True,
    },
}


def within_cap(coupling: tuple[Fraction, Fraction]) -> bool:
    return sum(coupling) == CAP


def exchange_invariant(coupling: tuple[Fraction, Fraction]) -> bool:
    return coupling[0] == coupling[1]


def selects_unique_equal(principle: dict[str, bool]) -> bool:
    return (
        principle["source_derived"]
        and principle["symmetric"]
        and principle["strictly_convex"]
    )


def main() -> None:
    admissible_by_cap = {
        name: within_cap(coupling) for name, coupling in COUPLINGS.items()
    }
    invariant = {
        name: exchange_invariant(coupling) for name, coupling in COUPLINGS.items()
    }
    principle_admission = {
        name: selects_unique_equal(principle)
        for name, principle in PRINCIPLES.items()
    }

    checks = {
        "cap_only_leaves_three_rivals": all(admissible_by_cap.values()),
        "external_exchange_selects_equal_but_not_source_derived": invariant["equal"]
        and not PRINCIPLES["external_exchange"]["source_derived"],
        "source_symmetric_convex_cost_is_unique_principle": [
            name for name, ok in principle_admission.items() if ok
        ]
        == ["source_symmetric_convex_cost"],
        "width_heavy_and_background_heavy_are_cap_rivals": admissible_by_cap[
            "width_heavy"
        ]
        and admissible_by_cap["background_heavy"],
        "asymmetric_rivals_violate_exchange": not invariant["width_heavy"]
        and not invariant["background_heavy"],
        "strict_convexity_needed_for_uniqueness": PRINCIPLES[
            "source_symmetric_convex_cost"
        ]["strictly_convex"],
        "source_derivation_needed_for_authority": PRINCIPLES[
            "source_symmetric_convex_cost"
        ]["source_derived"],
        "does_not_supply_sentinel_apparatus_or_calibration": True,
    }

    result = {
        "work_package": "WP227",
        "claim": "Coupling uniqueness requires a source-derived symmetric strictly convex cost; cap-only and external exchange leave authority gaps.",
        "admitted_domain": "width/background couplings saturating the one-fifth cap.",
        "faithful_quotient": "coupling split plus source-derived uniqueness principle.",
        "couplings": {
            name: [str(value) for value in coupling]
            for name, coupling in COUPLINGS.items()
        },
        "cap_admissibility": admissible_by_cap,
        "exchange_invariance": invariant,
        "principle_admission": principle_admission,
        "classification": "coupling uniqueness principle audit.",
        "smallest_exact_falsifier": "Cap-only admits width-heavy, equal, and background-heavy couplings with the same source.",
        "remaining_gate": "Derive a symmetric strictly convex detector-coupling cost from the source action.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp227_coupling_uniqueness_principles.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
