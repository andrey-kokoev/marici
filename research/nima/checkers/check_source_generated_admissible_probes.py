"""Exact audit of source-generated admissible probe closure over F_2^2."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/source-generated-admissible-probes.json"

State = tuple[int, int]
Probe = tuple[int, int]


def evaluate(probe: Probe, state: State) -> int:
    return (probe[0] * state[0] + probe[1] * state[1]) % 2


def transport_by_swap(probe: Probe) -> Probe:
    return (probe[1], probe[0])


def closure(seed: Probe, symmetry_declared: bool, additive: bool) -> frozenset[Probe]:
    closure = {seed}
    while True:
        enlarged = set(closure)
        if symmetry_declared:
            enlarged |= {transport_by_swap(probe) for probe in closure}
        if additive:
            enlarged |= {
                ((p[0] + q[0]) % 2, (p[1] + q[1]) % 2)
                for p in closure for q in closure
            }
        if enlarged == closure:
            break
        closure = enlarged
    return frozenset(closure)


def profiles(probes: frozenset[Probe]) -> set[tuple[int, ...]]:
    ordered = sorted(probes)
    return {
        tuple(evaluate(probe, state) for probe in ordered)
        for state in itertools.product((0, 1), repeat=2)
    }


states = tuple(itertools.product((0, 1), repeat=2))
p0 = (1, 0)
p1 = (0, 1)
p_sum = (1, 1)

transport_only_closure = closure(p0, symmetry_declared=True, additive=False)
trivial_closure = closure(p0, symmetry_declared=False, additive=True)
source_closure = closure(p0, symmetry_declared=True, additive=True)

proper_symmetry_closed_supersets = []
all_probes = {(0, 0), p0, p1, p_sum}
for size in range(1, len(all_probes) + 1):
    for family in itertools.combinations(all_probes, size):
        family_set = frozenset(family)
        if p0 not in family_set:
            continue
        if {transport_by_swap(p) for p in family_set} != set(family_set):
            continue
        if family_set < transport_only_closure:
            proper_symmetry_closed_supersets.append(family_set)

gates = {
    "primitive_additive_closure_is_nonfaithful": len(profiles(trivial_closure)) == 2,
    "declared_swap_generates_second_coordinate": transport_only_closure == frozenset({p0, p1}),
    "source_generated_orbit_is_jointly_faithful": len(profiles(source_closure)) == len(states),
    "source_closure_is_swap_stable": {
        transport_by_swap(p) for p in source_closure
    } == set(source_closure),
    "transport_orbit_is_minimal": not proper_symmetry_closed_supersets,
    "coefficient_addition_generates_sum_probe": p_sum in source_closure,
    "typed_linear_closure_is_full_dual": source_closure == frozenset(all_probes),
    "faithfulness_is_not_an_admission_axiom": len(profiles(trivial_closure)) < len(states),
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.source-generated-admissible-probes.v1",
    "state_space": "F_2^2",
    "primitive_probe": list(p0),
    "declared_source_symmetry": "coordinate swap",
    "closure_without_symmetry": [list(p) for p in sorted(trivial_closure)],
    "transport_only_closure": [list(p) for p in sorted(transport_only_closure)],
    "source_generated_typed_closure": [list(p) for p in sorted(source_closure)],
    "profile_counts": {
        "primitive_only": len(profiles(trivial_closure)),
        "source_generated": len(profiles(source_closure)),
    },
    "gates": gates,
    "conclusion": (
        "Admissibility requires closure under every operation supplied by the "
        "typed coefficient object. Transport-only closure is incomplete in an "
        "additive category. Faithfulness is an outcome, not an admission axiom."
    ),
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))
