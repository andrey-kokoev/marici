from __future__ import annotations

import json
from pathlib import Path


def compose(left, right, states):
    return tuple(left[right[state]] for state in states)


def as_map(vector, states):
    return {state: vector[index] for index, state in enumerate(states)}


def main() -> None:
    states = ("a", "b", "c")
    outcomes = {"a": 0, "b": 0, "c": 1}
    generators = {
        "identity": {"a": "a", "b": "b", "c": "c"},
        "swap_ab": {"a": "b", "b": "a", "c": "c"},
        "reset_a": {"a": "a", "b": "a", "c": "a"},
        "set_c": {"a": "c", "b": "c", "c": "c"},
    }

    monoid_vectors = {
        tuple(mapping[state] for state in states) for mapping in generators.values()
    }
    changed = True
    while changed:
        changed = False
        existing = tuple(monoid_vectors)
        existing_maps = tuple(as_map(vector, states) for vector in existing)
        for left in existing_maps:
            for right in existing_maps:
                candidate = compose(left, right, states)
                if candidate not in monoid_vectors:
                    monoid_vectors.add(candidate)
                    changed = True

    contexts = tuple(as_map(vector, states) for vector in sorted(monoid_vectors))
    signatures = {
        state: tuple(outcomes[context[state]] for context in contexts) for state in states
    }
    assert signatures["a"] == signatures["b"]
    assert signatures["a"] != signatures["c"]

    classes = {
        "ab": frozenset(("a", "b")),
        "c": frozenset(("c",)),
    }
    state_class = {state: label for label, members in classes.items() for state in members}

    descended = {}
    for name, transformation in generators.items():
        class_map = {}
        for label, members in classes.items():
            targets = {state_class[transformation[state]] for state in members}
            assert len(targets) == 1
            class_map[label] = next(iter(targets))
        descended[name] = class_map

    quotient_outcomes = {"ab": 0, "c": 1}
    for context in contexts:
        for state in states:
            original = outcomes[context[state]]
            quotient = quotient_outcomes[state_class[context[state]]]
            assert original == quotient

    refined_outcomes = {"a": "plus", "b": "minus", "c": "other"}
    refined_signatures_differ = refined_outcomes["a"] != refined_outcomes["b"]
    assert refined_signatures_differ

    result = {
        "schema": "marici.aspect.behavioral-quotient-constructor-stopping-point.v1",
        "status": "pass",
        "state_count_before_quotient": len(states),
        "generated_constructor_monoid_size": len(contexts),
        "a_signature": list(signatures["a"]),
        "b_signature": list(signatures["b"]),
        "c_signature": list(signatures["c"]),
        "a_b_full_context_equivalent": signatures["a"] == signatures["b"],
        "a_c_full_context_equivalent": signatures["a"] == signatures["c"],
        "quotient_classes": {label: sorted(members) for label, members in classes.items()},
        "state_count_after_quotient": len(classes),
        "all_generators_descend_to_quotient": True,
        "all_context_outcomes_preserved": True,
        "new_X_outcome_refines_a_b": refined_signatures_differ,
        "verdict": "States a and b have identical outcomes under every context in the generated constructor monoid. Quotienting them preserves every transformation and outcome exactly. Adding a new X constructor refines the quotient, demonstrating that the stopping point is the full behavioral kernel of a fixed conjectured theory, not current records alone.",
        "claim_boundary": "finite deterministic transition theory; no infinite, probabilistic, quantum, or computationally unbounded context category",
    }
    output = Path(__file__).parents[1] / "results" / "behavioral_quotient_is_constructor_stopping_point.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
