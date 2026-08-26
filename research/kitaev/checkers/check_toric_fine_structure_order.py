import hashlib
import itertools
import json
from pathlib import Path


def lattice_edges(size):
    return [
        (x, y, direction)
        for y in range(size)
        for x in range(size)
        for direction in ("h", "v")
    ]


def endpoints(edge, size):
    x, y, direction = edge
    if direction == "h":
        return (x, y), ((x + 1) % size, y)
    return (x, y), (x, (y + 1) % size)


def is_cycle(selected, size):
    parity = {(x, y): 0 for y in range(size) for x in range(size)}
    for edge in selected:
        left, right = endpoints(edge, size)
        parity[left] ^= 1
        parity[right] ^= 1
    return all(value == 0 for value in parity.values())


def winding(selected, size):
    horizontal = sum(1 for x, y, direction in selected if direction == "h" and x == size - 1) % 2
    vertical = sum(1 for x, y, direction in selected if direction == "v" and y == size - 1) % 2
    return horizontal, vertical


audits = []
for size in (2, 3, 4):
    edges = lattice_edges(size)
    nontrivial_below_distance = []
    checked_subsets = 0
    for weight in range(size):
        for indices in itertools.combinations(range(len(edges)), weight):
            checked_subsets += 1
            selected = [edges[index] for index in indices]
            if is_cycle(selected, size) and winding(selected, size) != (0, 0):
                nontrivial_below_distance.append(indices)
    assert nontrivial_below_distance == []

    horizontal_loop = [(x, 0, "h") for x in range(size)]
    vertical_loop = [(0, y, "v") for y in range(size)]
    assert is_cycle(horizontal_loop, size)
    assert is_cycle(vertical_loop, size)
    assert winding(horizontal_loop, size) == (1, 0)
    assert winding(vertical_loop, size) == (0, 1)

    audits.append(
        {
            "L": size,
            "edge_count": len(edges),
            "subsets_checked_below_L": checked_subsets,
            "nontrivial_cycles_below_L": 0,
            "horizontal_logical_weight": len(horizontal_loop),
            "vertical_logical_weight": len(vertical_loop),
        }
    )

payload = {
    "status": "pass",
    "theorem": "code_distance_is_a_perturbative_fine_structure_selection_rule",
    "audits": audits,
    "single_edge_perturbation_first_allowed_order": "L",
    "distance_proves_nonzero_coefficient": False,
    "logical_readout_implies_splitting": False,
    "uniform_completion_proved": False,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "toric-fine-structure-order.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
