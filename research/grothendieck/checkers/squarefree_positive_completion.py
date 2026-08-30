"""Exact sparse-versus-completed Walsh positivity comparison."""

from fractions import Fraction as F
from itertools import product


D = F(1)
edges = [F(1, 2), F(-1, 3), F(1, 5)]
characters = list(product((0, 1), repeat=len(edges)))

sparse = {
    eta: D + sum((-1) ** bit * edge for bit, edge in zip(eta, edges))
    for eta in characters
}
# Spell out the product outside the comprehension to retain exact rationals
# and keep the claimed formula directly auditable.
completed = {}
for eta in characters:
    value = D
    for bit, edge in zip(eta, edges):
        value *= 1 + (-1) ** bit * edge / D
    completed[eta] = value

assert min(sparse.values()) == F(-1, 30)
assert all(abs(edge) <= D for edge in edges)
assert min(completed.values()) > 0
assert sum(completed.values()) == (2 ** len(edges)) * D

mixed_pair_coefficients = {
    f"{i},{j}": str(edges[i] * edges[j] / D)
    for i in range(len(edges))
    for j in range(i + 1, len(edges))
}

result = {
    "diagonal": str(D),
    "edges": [str(edge) for edge in edges],
    "sparse_minimum": str(min(sparse.values())),
    "sparse_kernel_positive": False,
    "completion_criterion": "max_j abs(r_j)<=D",
    "completed_minimum": str(min(completed.values())),
    "completed_kernel_positive": True,
    "mixed_pair_coefficients": mixed_pair_coefficients,
    "mixed_terms_are_completion_not_von_Mangoldt_atoms": True,
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "squarefree-positive-completion.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
