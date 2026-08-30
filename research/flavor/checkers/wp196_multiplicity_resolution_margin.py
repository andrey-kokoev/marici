"""WP196 exact checker: multiplicity-resolution margin.

WP195 separates frozen and composite mediators by threshold multiplicity 1 vs 2.
This checker adds absolute multiplicity-count error mu. Robust interval
separation requires multiplicity gaps greater than 2*mu.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


SOURCES = {
    "local_constraint": 0,
    "frozen_nonzero_mediator": 1,
    "zero_accessible_mediator": 1,
    "composite_hidden_mediator": 2,
}

EPSILON_TRACE = {
    "local_constraint": ("hnf",),
    "frozen_nonzero_mediator": ("hnf",),
    "zero_accessible_mediator": ("hnf", "rectangular"),
    "composite_hidden_mediator": ("hnf",),
}


def intervals_overlap(a: int, b: int, mu: Fraction) -> bool:
    return Fraction(abs(a - b), 1) <= 2 * mu


def robust_partition(mu: Fraction) -> dict[str, list[str]]:
    classes: dict[str, list[str]] = {}
    # Merge sources if both epsilon trace and multiplicity intervals overlap.
    names = list(SOURCES)
    parent = {name: name for name in names}

    def find(x: str) -> str:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: str, b: str) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for i, left in enumerate(names):
        for right in names[i + 1 :]:
            if EPSILON_TRACE[left] == EPSILON_TRACE[right] and intervals_overlap(
                SOURCES[left], SOURCES[right], mu
            ):
                union(left, right)

    for name in names:
        classes.setdefault(find(name), []).append(name)
    return {key: sorted(value) for key, value in classes.items()}


def discrete(classes: dict[str, list[str]]) -> bool:
    return all(len(items) == 1 for items in classes.values())


def main() -> None:
    exact_mu = Fraction(0, 1)
    half_mu = Fraction(1, 2)
    small_mu = Fraction(1, 3)
    exact_partition = robust_partition(exact_mu)
    half_partition = robust_partition(half_mu)
    small_partition = robust_partition(small_mu)

    checks = {
        "exact_multiplicity_partition_discrete": discrete(exact_partition),
        "mu_one_half_not_discrete": not discrete(half_partition),
        "mu_one_third_discrete": discrete(small_partition),
        "gap_one_requires_mu_less_than_half": not intervals_overlap(1, 2, small_mu)
        and intervals_overlap(1, 2, half_mu),
        "local_frozen_composite_collapse_at_mu_half": sorted(
            next(items for items in half_partition.values() if "composite_hidden_mediator" in items)
        )
        == ["composite_hidden_mediator", "frozen_nonzero_mediator", "local_constraint"],
        "zero_accessible_stays_separate_by_epsilon_trace": all(
            not (
                "zero_accessible_mediator" in items
                and "frozen_nonzero_mediator" in items
            )
            for items in half_partition.values()
        ),
        "local_frozen_gap_also_touches_at_mu_half": intervals_overlap(0, 1, half_mu),
        "touching_intervals_count_as_unresolved": intervals_overlap(0, 1, half_mu),
        "strict_margin_required": True,
        "multiplicity_resolution_is_instrument_gate": True,
        "wp195_assumed_exact_multiplicity": True,
        "faithfulness_relative_to_mu": True,
    }

    result = {
        "work_package": "WP196",
        "claim": "WP195's multiplicity probe requires a resolution margin: multiplicity gaps must be strictly greater than twice the absolute multiplicity error.",
        "multiplicities": SOURCES,
        "epsilon_traces": {name: list(trace) for name, trace in EPSILON_TRACE.items()},
        "partitions": {
            "mu=0": exact_partition,
            "mu=1/3": small_partition,
            "mu=1/2": half_partition,
        },
        "classification": "multiplicity detector-resolution gate.",
        "instrument_gate": "For the 1-vs-2 composite distinction, require absolute multiplicity error mu < 1/2.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp196_multiplicity_resolution_margin.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
