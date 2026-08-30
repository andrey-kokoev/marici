"""Verify the frozen exponent-adapter quarter-support packet.

The full sparse pencils are source-generated packets.  This checker verifies
their ranks at the generic point and at the two reconstructed quarter points.
For the discovery prime it also removes the previously certified rational
torsion factors from the gcd of adapted maximal minors and checks the residual
factorization.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "research" / "benincasa" / "results"


def add(row: dict[int, int], column: int, value: int, prime: int) -> None:
    value = (row.get(column, 0) + value) % prime
    if value:
        row[column] = value
    else:
        row.pop(column, None)


def rank_at(packet: dict, numerator: int, denominator: int, rows: int) -> int:
    prime = packet["p"]
    gamma = numerator * pow(denominator, prime - 2, prime) % prime
    matrix = [dict() for _ in range(rows)]
    for i, j, value in packet["a"]:
        if i < rows:
            add(matrix[i], j, value, prime)
    for i, j, value in packet["b"]:
        if i < rows:
            add(matrix[i], j, gamma * value, prime)

    pivots: dict[int, dict[int, int]] = {}
    for source in matrix:
        row = dict(source)
        while row:
            pivot = max(row)
            coefficient = row[pivot]
            if pivot not in pivots:
                inverse = pow(coefficient, prime - 2, prime)
                pivots[pivot] = {
                    column: value * inverse % prime for column, value in row.items()
                }
                break
            for column, value in pivots[pivot].items():
                add(row, column, -coefficient * value, prime)
    return len(pivots)


def trim(polynomial: list[int], prime: int) -> list[int]:
    polynomial = [value % prime for value in polynomial]
    while len(polynomial) > 1 and not polynomial[-1]:
        polynomial.pop()
    return polynomial


def divide_linear(polynomial: list[int], root: int, prime: int) -> list[int]:
    polynomial = trim(polynomial, prime)
    quotient = [0] * (len(polynomial) - 1)
    quotient[-1] = polynomial[-1]
    for index in range(len(quotient) - 2, -1, -1):
        quotient[index] = (polynomial[index + 1] + root * quotient[index + 1]) % prime
    remainder = (polynomial[0] + root * quotient[0]) % prime
    assert remainder == 0
    return trim(quotient, prime)


def multiply(left: list[int], right: list[int], prime: int) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            result[i + j] = (result[i + j] + x * y) % prime
    return trim(result, prime)


def monic(polynomial: list[int], prime: int) -> list[int]:
    polynomial = trim(polynomial, prime)
    inverse = pow(polynomial[-1], prime - 2, prime)
    return [value * inverse % prime for value in polynomial]


def main() -> None:
    expected = {
        (17, 1): (479, 505),
        (-5, 4): (479, 500),
        (-7, 4): (479, 498),
    }
    ranks = {}
    for prime in (32003, 32009):
        packet = json.loads(
            (RESULTS / f"exponent_adapter_full_pencil_{prime}.json").read_text()
        )
        for point, target in expected.items():
            observed = (rank_at(packet, *point, 720), rank_at(packet, *point, 756))
            assert observed == target, (prime, point, observed, target)
            ranks[f"{prime}:{point[0]}/{point[1]}"] = list(observed)

    prime = 32003
    gcd = json.loads((RESULTS / "exponent_adapter_adapted_gcd_32003.json").read_text())
    known = [(-2, 2), (-3 * pow(2, prime - 2, prime) % prime, 7), (0, 56),
             (pow(2, prime - 2, prime), 6), (1, 78),
             (3 * pow(2, prime - 2, prime) % prime, 6), (2, 99)]
    residual = gcd
    for root, multiplicity in known:
        for _ in range(multiplicity):
            residual = divide_linear(residual, root, prime)

    predicted = [1]
    for _ in range(5):
        predicted = multiply(predicted, [5, 4], prime)
    for _ in range(7):
        predicted = multiply(predicted, [7, 4], prime)
    assert monic(residual, prime) == monic(predicted, prime)

    output = {
        "status": "pass",
        "rank_convention": "[rank(M), rank([M;L])]",
        "ranks": ranks,
        "discovery_prime_gcd_degree": len(trim(gcd, prime)) - 1,
        "known_factor_degree": sum(multiplicity for _, multiplicity in known),
        "residual_degree": len(trim(residual, prime)) - 1,
        "residual_factorization": "(4*gamma+5)^5*(4*gamma+7)^7",
    }
    (RESULTS / "exponent_adapter_quarter_divisor.json").write_text(
        json.dumps(output, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
