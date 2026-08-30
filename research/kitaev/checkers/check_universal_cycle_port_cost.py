import hashlib
import itertools
import json
from pathlib import Path


VERTICES = tuple(range(4))
EDGES = {frozenset(edge) for edge in itertools.combinations(VERTICES, 2)}


def canonical_cycle(sequence):
    sequence = tuple(sequence)
    rotations = []
    for oriented in (sequence, tuple(reversed(sequence))):
        rotations.extend(oriented[i:] + oriented[:i] for i in range(len(oriented)))
    return min(rotations)


cycles = set()
for length in (3, 4):
    for subset in itertools.combinations(VERTICES, length):
        for ordering in itertools.permutations(subset):
            edge_set = {
                frozenset((ordering[i], ordering[(i + 1) % length]))
                for i in range(length)
            }
            if edge_set <= EDGES:
                cycles.add(canonical_cycle(ordering))

triangles = sorted(cycle for cycle in cycles if len(cycle) == 3)
quadrilaterals = sorted(cycle for cycle in cycles if len(cycle) == 4)
assert len(triangles) == 4
assert len(quadrilaterals) == 3
assert len(cycles) == 7


def cycle_edges(cycle):
    return {
        frozenset((cycle[i], cycle[(i + 1) % len(cycle)]))
        for i in range(len(cycle))
    }


# On support exactly C, every distinct simple-cycle monomial vanishes.
for omitted in cycles:
    support = cycle_edges(omitted)
    survivors = [other for other in cycles if cycle_edges(other) <= support]
    assert survivors == [omitted]

cycle_rank = len(EDGES) - len(VERTICES) + 1
assert cycle_rank == 3

payload = {
    "status": "pass",
    "theorem": "universal_support_robustness_costs_one_port_per_simple_cycle",
    "graph": "K4",
    "edge_count": len(EDGES),
    "cycle_rank": cycle_rank,
    "triangle_count": len(triangles),
    "four_cycle_count": len(quadrilaterals),
    "unoriented_simple_cycle_count": len(cycles),
    "generic_phase_ports": cycle_rank,
    "universal_cycle_monomial_ports": len(cycles),
    "omission_falsifier_verified_for_every_cycle": True,
    "theta_application_frozen": True,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "universal-cycle-port-cost.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
