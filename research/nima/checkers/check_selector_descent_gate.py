"""Exact finite audit of chart, descending, and faithful quotient selectors."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/selector-descent-gate.json"
State = tuple[int, int]


states: tuple[State, ...] = tuple(itertools.product((0, 1), repeat=2))


def swap(state: State) -> State:
    return state[1], state[0]


def chart_coordinate(state: State) -> int:
    return state[0]


def symmetric_sum(state: State) -> int:
    return (state[0] + state[1]) % 2


def symmetric_product(state: State) -> int:
    return state[0] * state[1]


orbits = {
    frozenset((state, swap(state)))
    for state in states
}
sum_profiles = {
    symmetric_sum(next(iter(orbit)))
    for orbit in orbits
}
faithful_profiles = {
    (
        symmetric_sum(next(iter(orbit))),
        symmetric_product(next(iter(orbit))),
    )
    for orbit in orbits
}

gates = {
    "chart_coordinate_fails_descent": any(
        chart_coordinate(state) != chart_coordinate(swap(state)) for state in states
    ),
    "symmetric_sum_descends": all(
        symmetric_sum(state) == symmetric_sum(swap(state)) for state in states
    ),
    "descending_scalar_need_not_be_faithful": len(sum_profiles) < len(orbits),
    "invariant_pair_is_faithful_on_quotient": len(faithful_profiles) == len(orbits),
    "physical_quotient_has_three_points": len(orbits) == 3,
    "chart_has_four_presentations": len(states) == 4,
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.selector-descent-gate.v1",
    "presentation_count": len(states),
    "physical_orbit_count": len(orbits),
    "descending_scalar_profiles": len(sum_profiles),
    "faithful_quotient_profiles": len(faithful_profiles),
    "gates": gates,
    "conclusion": (
        "A source-generated chart selector is physical only if it descends "
        "through the declared equivalence. Descent alone does not imply "
        "faithful reconstruction; that requires enough invariant coordinates."
    ),
}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))
