from __future__ import annotations

import json
from fractions import Fraction
from itertools import permutations


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    n = len(matrix)
    total = Fraction(0)
    for permutation in permutations(range(n)):
        inversions = sum(permutation[i] > permutation[j] for i in range(n) for j in range(i + 1, n))
        term = Fraction(-1 if inversions % 2 else 1)
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        total += term
    return total


def path_product(edges: list[Fraction], i: int, j: int) -> Fraction:
    product = Fraction(1)
    for edge in edges[i:j]:
        product *= edge
    return product


def render(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def main() -> None:
    edges = [Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)]
    size = len(edges) + 1
    gram = [[Fraction(1) if i == j else path_product(edges, min(i, j), max(i, j)) for j in range(size)] for i in range(size)]

    actual_det = determinant(gram)
    predicted_det = Fraction(1)
    for edge in edges:
        predicted_det *= 1 - edge**2
    assert actual_det == predicted_det == Fraction(35, 192)

    left = (edges[0] * edges[1]) * edges[2]
    right = edges[0] * (edges[1] * edges[2])
    assert left == right == Fraction(1, 4)

    result = {
        "schema": "marici.voevodsky.markov-green-amalgamation.v1",
        "status": "restricted_scalar_constructor_verified",
        "edges": [render(edge) for edge in edges],
        "gram": [[render(entry) for entry in row] for row in gram],
        "determinant": render(actual_det),
        "predicted_determinant": render(predicted_det),
        "left_parenthesized_endpoint": render(left),
        "right_parenthesized_endpoint": render(right),
        "associative": left == right,
        "promotion_gate": "source-derived factorization of cross Green returns through intervening sectors",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
