"""Exact rational Walsh diagonalization for squarefree prime cubes."""

from fractions import Fraction as F
from itertools import product


def dot_mod_two(x, y):
    return sum(a * b for a, b in zip(x, y)) % 2


rank = 3
vertices = list(product((0, 1), repeat=rank))
edges = [F(1, 2), F(-1, 3), F(2, 5)]


def kernel_value(x):
    value = F(1)
    for bit, edge in zip(x, edges):
        if bit:
            value *= edge
    return value


walsh = {
    eta: sum(kernel_value(x) * (-1) ** dot_mod_two(eta, x) for x in vertices)
    for eta in vertices
}
expected = {
    eta: product_value
    for eta in vertices
    for product_value in [
        (1 + (-1) ** eta[0] * edges[0])
        * (1 + (-1) ** eta[1] * edges[1])
        * (1 + (-1) ** eta[2] * edges[2])
    ]
}
assert walsh == expected
assert all(value > 0 for value in walsh.values())

result = {
    "cube_rank": rank,
    "walsh_eigenvalue_formula": "sum_x f(x)(-1)^(eta dot x)",
    "tensor_eigenvalue_formula": "product_j(1+(-1)^eta_j r_j)",
    "all_test_eigenvalues_positive": True,
    "route_independence_required_before_walsh_test": True,
    "negative_character_is_finite_Weil_falsifier": True,
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "squarefree-prime-cube-walsh.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")

