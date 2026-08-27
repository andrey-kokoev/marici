import json
from pathlib import Path


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def matsub(a, b):
    return [[x - y for x, y in zip(row_a, row_b)]
            for row_a, row_b in zip(a, b)]


def matvec(a, v):
    return [sum(x * y for x, y in zip(row, v)) for row in a]


semantic_swap = [[0, 1], [1, 0]]
operational_projection = [[1, 0], [0, 0]]
os_route = matmul(operational_projection, semantic_swap)
so_route = matmul(semantic_swap, operational_projection)
commutator = matsub(os_route, so_route)

assert os_route != so_route
assert commutator != [[0, 0], [0, 0]]

state = [1, 0]
semantic_then_operational = matvec(os_route, state)
operational_then_semantic = matvec(so_route, state)
assert semantic_then_operational == [0, 0]
assert operational_then_semantic == [0, 1]

result = {
    "status": "pass",
    "claim": "separately admitted semantic and operational actions require cross-axis coherence",
    "semantic_action_admitted": True,
    "operational_action_admitted": True,
    "semantic_then_operational": os_route,
    "operational_then_semantic": so_route,
    "commutator": commutator,
    "hostile_state": state,
    "hostile_outputs": {
        "semantic_then_operational": semantic_then_operational,
        "operational_then_semantic": operational_then_semantic,
    },
    "combined_constructor_admitted": False,
    "typed_residual": "missing_cross_axis_coherence",
    "minimal_repair": "authorized_distributive_law_or_beck_chevalley_cell",
}

out = Path(__file__).parents[1] / "results" / "semantic-operational-interface-coherence.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

