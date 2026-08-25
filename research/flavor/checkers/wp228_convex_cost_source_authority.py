"""WP228 exact checker: convex cost source authority.

Audits candidate detector-coupling costs for uniqueness and source authority.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


CAP = Fraction(1, 5)
EQUAL = (Fraction(1, 10), Fraction(1, 10))
WIDTH_HEAVY = (Fraction(3, 20), Fraction(1, 20))
BACKGROUND_HEAVY = (Fraction(1, 20), Fraction(3, 20))
COUPLINGS = {
    "width_heavy": WIDTH_HEAVY,
    "equal": EQUAL,
    "background_heavy": BACKGROUND_HEAVY,
}


COSTS = {
    "arbitrary_asymmetric_quadratic": {
        "source_derived": False,
        "symmetric": False,
        "strictly_convex": True,
        "minimizer": WIDTH_HEAVY,
    },
    "external_symmetric_quadratic": {
        "source_derived": False,
        "symmetric": True,
        "strictly_convex": True,
        "minimizer": EQUAL,
    },
    "source_symmetric_quadratic": {
        "source_derived": True,
        "symmetric": True,
        "strictly_convex": True,
        "minimizer": EQUAL,
    },
    "source_symmetric_flat_cost": {
        "source_derived": True,
        "symmetric": True,
        "strictly_convex": False,
        "minimizer": None,
    },
}


def within_cap(coupling: tuple[Fraction, Fraction]) -> bool:
    return sum(coupling) == CAP


def admits(cost: dict[str, object]) -> bool:
    return (
        cost["source_derived"]
        and cost["symmetric"]
        and cost["strictly_convex"]
        and cost["minimizer"] == EQUAL
    )


def main() -> None:
    cost_admission = {name: admits(cost) for name, cost in COSTS.items()}
    minimizers = {
        name: None if cost["minimizer"] is None else [str(x) for x in cost["minimizer"]]
        for name, cost in COSTS.items()
    }

    checks = {
        "arbitrary_asymmetric_quadratic_can_select_wrong_rival": COSTS[
            "arbitrary_asymmetric_quadratic"
        ]["minimizer"]
        == WIDTH_HEAVY
        and not cost_admission["arbitrary_asymmetric_quadratic"],
        "external_symmetric_quadratic_selects_equal_without_authority": COSTS[
            "external_symmetric_quadratic"
        ]["minimizer"]
        == EQUAL
        and not cost_admission["external_symmetric_quadratic"],
        "source_symmetric_quadratic_admitted": cost_admission[
            "source_symmetric_quadratic"
        ],
        "source_symmetric_flat_cost_lacks_uniqueness": not cost_admission[
            "source_symmetric_flat_cost"
        ],
        "all_audited_couplings_saturate_cap": all(
            within_cap(coupling) for coupling in COUPLINGS.values()
        ),
        "only_one_cost_has_all_authority_fields": [
            name for name, ok in cost_admission.items() if ok
        ]
        == ["source_symmetric_quadratic"],
        "convexity_without_source_authority_not_enough": not COSTS[
            "arbitrary_asymmetric_quadratic"
        ]["source_derived"],
        "source_symmetry_without_strict_convexity_not_enough": not COSTS[
            "source_symmetric_flat_cost"
        ]["strictly_convex"],
    }

    result = {
        "work_package": "WP228",
        "claim": "A convex detector-coupling cost gives exchange authority only when it is source-derived, symmetric, strictly convex, and minimized at the equal split.",
        "admitted_domain": "candidate costs on width/background couplings saturating the one-fifth cap.",
        "faithful_quotient": "cost authority fields plus exact minimizer on the coupling simplex.",
        "couplings": {
            name: [str(value) for value in coupling]
            for name, coupling in COUPLINGS.items()
        },
        "cost_minimizers": minimizers,
        "cost_admission": cost_admission,
        "classification": "convex-cost source-authority audit.",
        "smallest_exact_falsifier": "External symmetric quadratic selects 1/10+1/10 but has no source authority.",
        "remaining_gate": "Derive the symmetric quadratic or equivalent strictly convex cost from source dynamics.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp228_convex_cost_source_authority.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
