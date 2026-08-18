"""Sparse source-divisor pole census for the Gysin extension class."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from check_gysin_multidivisor_extension import (
    DEFAULT_INPUT,
    ROOT,
    connection,
    factors_and_derivatives,
    inv,
    monomials,
    rank,
)


DEFAULT_OUTPUT = ROOT / "research/nima/gysin-sparse-pole-extension-census.json"
FACTOR_NAMES = [
    "u", "v", "y", "1-y", "1+y", "v-u", "y-u^2", "y+u^2", "P6"
]


def weighted_divisor_data(u: int, v: int, prime: int, weights: tuple[int, ...]):
    data = factors_and_derivatives(u, v, prime)
    if data is None:
        return None
    # Recover individual factors using the same frozen formulas as the
    # authoritative uniform checker.
    half = inv(2, prime)
    quarter = half * half % prime
    y = ((u + v) * half - 1) % prime
    u2 = u * u % prime
    factors = [
        (u, 1, 0),
        (v, 0, 1),
        (y, half, half),
        ((1 - y) % prime, -half, -half),
        ((1 + y) % prime, half, half),
        ((v - u) % prime, -1, 1),
        ((y - u2) % prime, half - 2 * u, half),
        ((y + u2) % prime, half + 2 * u, half),
    ]
    p6 = (
        1 - u - v + v * v * quarter + u * v * half - 7 * u2 * quarter
        + u2 * v + u2 * u - u2 * u * v + u2 * u2
    ) % prime
    p6u = (-1 + v * half - 14 * u * quarter + 2 * u * v + 3 * u2 - 3 * u2 * v + 4 * u * u2) % prime
    p6v = (-1 + 2 * v * quarter + u * half + u2 - u2 * u) % prime
    factors.append((p6, p6u, p6v))
    divisor = 1
    dlog_u = 0
    dlog_v = 0
    for weight, (value, du, dv) in zip(weights, factors):
        if weight:
            divisor = divisor * pow(value, weight, prime) % prime
            reciprocal = inv(value, prime)
            dlog_u = (dlog_u + weight * du * reciprocal) % prime
            dlog_v = (dlog_v + weight * dv * reciprocal) % prime
    return divisor, dlog_u, dlog_v


def census(entries, prime: int, weights: tuple[int, ...], degree: int, seed: int):
    mons = monomials(degree)
    unknowns = 4 * len(mons)
    target_rows = unknowns + 32
    matrix: list[list[int]] = []
    weight_code = sum(weight << (2 * index) for index, weight in enumerate(weights))
    state_u = seed ^ weight_code ^ degree
    state_v = seed ^ 0x9E3779B97F4A7C15 ^ (degree << 23) ^ (weight_code << 1)
    accepted = 0
    while len(matrix) < target_rows:
        state_u = (state_u * 6364136223846793005 + 1447) % prime
        state_v = (state_v * 2862933555777941757 + 1451) % prime
        u, v = state_u, state_v
        divisor_data = weighted_divisor_data(u, v, prime, weights)
        if divisor_data is None:
            continue
        divisor, dlog_u, dlog_v = divisor_data
        au = connection(entries, "u", u, v, prime)
        av = connection(entries, "v", u, v, prime)
        if au is None or av is None:
            continue
        accepted += 1
        for axis, a, dlog in [(0, au, dlog_u), (1, av, dlog_v)]:
            for i in range(2):
                for j in range(2):
                    row = [0] * (unknowns + 1)
                    for q in range(2):
                        for k in range(2):
                            block = (2 * q + k) * len(mons)
                            for index, (du, dv) in enumerate(mons):
                                value = pow(u, du, prime) * pow(v, dv, prime) % prime
                                exponent = du if axis == 0 else dv
                                derivative = 0
                                if exponent:
                                    derivative = exponent * (
                                        pow(u, du - 1, prime) * pow(v, dv, prime)
                                        if axis == 0
                                        else pow(u, du, prime) * pow(v, dv - 1, prime)
                                    ) % prime
                                coefficient = 0
                                if q == i and k == j:
                                    coefficient += derivative - dlog * value
                                if q == i:
                                    coefficient += value * a[k][j]
                                if k == j:
                                    coefficient -= value * a[i + 2][q + 2]
                                row[block + index] = coefficient % prime
                    row[-1] = (-divisor * a[i + 2][j]) % prime
                    matrix.append(row)
    coefficient_rank = rank([row[:-1] for row in matrix], unknowns, prime)
    augmented_rank = rank(matrix, unknowns + 1, prime)
    return {
        "pole_vector": dict(zip(FACTOR_NAMES, weights)),
        "numerator_degree": degree,
        "unknowns": unknowns,
        "sample_points": accepted,
        "equations": len(matrix),
        "coefficient_rank": coefficient_rank,
        "kernel_dimension": unknowns - coefficient_rank,
        "augmented_rank": augmented_rank,
        "augmented_rank_defect": augmented_rank - coefficient_rank,
        "split_found": augmented_rank == coefficient_rank,
    }


def selected_vectors() -> list[tuple[int, ...]]:
    vectors = set()
    # Entry 758's direct serialized-denominator divisibility audit.
    detected = (1, 1, 1, 0, 0, 1, 1, 1, 0)
    active = [index for index, exponent in enumerate(detected) if exponent]
    # Its complete downward localization lattice.
    for mask in range(1 << len(active)):
        vector = [0] * 9
        for bit, index in enumerate(active):
            vector[index] = (mask >> bit) & 1
        vectors.add(tuple(vector))
    # First and second resonant thickenings over the detected ordinary base.
    for e0 in range(3):
        for e1 in range(3):
            for e2 in range(3):
                vector = list(detected)
                vector[5:8] = [e0, e1, e2]
                vectors.add(tuple(vector))
    return sorted(vectors)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--max-degree", type=int, default=6)
    parser.add_argument("--seed", type=lambda value: int(value, 0), default=0x243F6A8885A308D3)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    prime = int(payload["prime"])
    entries = {(item["axis"], item["row"], item["col"]): item["fit"] for item in payload["entries"]}
    results = []
    for weights in selected_vectors():
        for degree in range(args.max_degree + 1):
            result = census(entries, prime, weights, degree, args.seed)
            results.append(result)
            print(json.dumps(result, sort_keys=True))
    output = {
        "schema": "marici.nima.gysin_sparse_pole_extension_census.v1",
        "prime": prime,
        "connection_source": str(args.input.relative_to(ROOT)).replace("\\", "/"),
        "factor_order": FACTOR_NAMES,
        "partial_detected_vector": [1, 1, 1, 0, 0, 1, 1, 1, 0],
        "vector_family": "downward lattice plus resonant order-two thickenings",
        "Q_included": False,
        "sampling_seed": args.seed,
        "vector_count": len(selected_vectors()),
        "results": results,
    }
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
