"""Exact Walsh test for a squarefree cube with only single-prime edges."""

from fractions import Fraction as F
from itertools import product


def dot_mod_two(x, y):
    return sum(a * b for a, b in zip(x, y)) % 2


edges = [F(1, 2), F(-1, 3), F(1, 5)]
vertices = list(product((0, 1), repeat=len(edges)))


def kernel_value(x):
    weight = sum(x)
    if weight == 0:
        return F(1)
    if weight == 1:
        return edges[x.index(1)]
    return F(0)


walsh = {
    eta: sum(kernel_value(x) * (-1) ** dot_mod_two(eta, x) for x in vertices)
    for eta in vertices
}
formula = {
    eta: F(1) + sum((-1) ** bit * edge for bit, edge in zip(eta, edges))
    for eta in vertices
}
assert walsh == formula
assert min(walsh.values()) == 1 - sum(abs(edge) for edge in edges)
assert min(walsh.values()) == F(-1, 30)

safe_edges = [F(1, 4), F(-1, 3), F(1, 5)]
safe_minimum = 1 - sum(abs(edge) for edge in safe_edges)
assert safe_minimum == F(13, 60) > 0

result = {
    "rank": len(edges),
    "support": "identity plus single-prime edges only",
    "walsh_formula": "1+sum_j (-1)^eta_j r_j",
    "minimum_formula": "1-sum_j abs(r_j)",
    "psd_iff": "sum_j abs(r_j)<=1",
    "hostile_edges": [str(edge) for edge in edges],
    "hostile_minimum": str(min(walsh.values())),
    "hostile_negative_character_found": True,
    "safe_minimum": str(safe_minimum),
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "additive-prime-edge-budget.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
