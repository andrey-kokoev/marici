import json
from pathlib import Path


def reachable(adjacency, seeds):
    reached = set(seeds)
    frontier = list(seeds)
    while frontier:
        source = frontier.pop()
        for target in adjacency.get(source, ()):
            if target not in reached:
                reached.add(target)
                frontier.append(target)
    return tuple(sorted(reached))


# Three disjoint two-cycles.
proper_graph = {
    0: (1,), 1: (0,),
    2: (3,), 3: (2,),
    4: (5,), 5: (4,),
}
proper = reachable(proper_graph, (0,))
assert proper == (0, 1)

# One strongly connected directed cycle.
full_graph = {index: ((index + 1) % 6,) for index in range(6)}
full_closures = {reachable(full_graph, (seed,)) for seed in range(6)}
assert full_closures == {tuple(range(6))}

# Growing finite chain family forces infinite saturation in the colimit.
chain_sizes = []
for size in range(1, 13):
    chain = {index: ((index + 1,) if index + 1 < size else ()) for index in range(size)}
    saturation = reachable(chain, (0,))
    assert len(saturation) == size
    chain_sizes.append(len(saturation))
assert chain_sizes == list(range(1, 13))

# Typed partial hostile: the same nominal provenance class contains histories
# with different downstream definedness and different authority fibers.
history_a = {
    "endpoint": "same",
    "downstream_defined": True,
    "authority_kind": "execute",
}
history_b = {
    "endpoint": "same",
    "downstream_defined": False,
    "authority_kind": "inspect",
}
assert history_a["endpoint"] == history_b["endpoint"]
definedness_congruent = history_a["downstream_defined"] == history_b["downstream_defined"]
fiber_congruent = history_a["authority_kind"] == history_b["authority_kind"]
assert not definedness_congruent
assert not fiber_congruent

result = {
    "schema": "marici.context-saturation-trichotomy.v1",
    "finite_proper_closure": list(proper),
    "strongly_connected_singleton_closure_size": 6,
    "chain_cutoff_saturation_sizes": chain_sizes,
    "completion_stable_finite_chain_bound": False,
    "partial_definedness_congruence": definedness_congruent,
    "typed_fiber_congruence": fiber_congruent,
    "verdicts": [
        "finite_proper_context_closure",
        "full_or_forced_infinite_context_closure",
        "invalid_partial_or_fibred_quotient",
    ],
    "claim_boundary": "context saturation size and partial congruence classify the provenance frontier",
    "status": "pass",
}

output = Path(__file__).resolve().parents[1] / "results" / "context-saturation-trichotomy.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
