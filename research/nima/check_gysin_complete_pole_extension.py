"""Splitting census on the complete Hom-operator pole lattice."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from audit_gysin_hom_pole_lattice import source_factors
from check_gysin_multidivisor_extension import (
    DEFAULT_INPUT,
    ROOT,
    connection,
    inv,
    monomials,
    rank,
)


DEFAULT_OUTPUT = ROOT / "research/nima/gysin-complete-pole-extension-census.json"
COMPLETE_VECTOR = (1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 2)


def evaluate(polynomial, u: int, v: int, prime: int):
    value = du = dv = 0
    for (eu, ev), coefficient in polynomial.items():
        up = pow(u, eu, prime)
        vp = pow(v, ev, prime)
        value = (value + coefficient * up * vp) % prime
        if eu:
            du = (du + coefficient * eu * pow(u, eu - 1, prime) * vp) % prime
        if ev:
            dv = (dv + coefficient * ev * up * pow(v, ev - 1, prime)) % prime
    return value, du, dv


def divisor_data(factors, weights, u: int, v: int, prime: int):
    divisor = 1
    dlog_u = dlog_v = 0
    for weight, (_, polynomial) in zip(weights, factors):
        value, du, dv = evaluate(polynomial, u, v, prime)
        if value == 0:
            return None
        if weight:
            divisor = divisor * pow(value, weight, prime) % prime
            reciprocal = inv(value, prime)
            dlog_u = (dlog_u + weight * du * reciprocal) % prime
            dlog_v = (dlog_v + weight * dv * reciprocal) % prime
    return divisor, dlog_u, dlog_v


def census(entries, factors, prime: int, weights, degree: int, seed: int):
    mons = monomials(degree)
    unknowns = 4 * len(mons)
    target_rows = unknowns + 32
    matrix = []
    weight_code = sum(weight << (3 * index) for index, weight in enumerate(weights))
    state_u = seed ^ weight_code ^ degree
    state_v = seed ^ 0x9E3779B97F4A7C15 ^ (degree << 23) ^ (weight_code << 1)
    accepted = 0
    while len(matrix) < target_rows:
        state_u = (state_u * 6364136223846793005 + 1447) % prime
        state_v = (state_v * 2862933555777941757 + 1451) % prime
        u, v = state_u, state_v
        data = divisor_data(factors, weights, u, v, prime)
        if data is None:
            continue
        divisor, dlog_u, dlog_v = data
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
                            for index, (eu, ev) in enumerate(mons):
                                value = pow(u, eu, prime) * pow(v, ev, prime) % prime
                                exponent = eu if axis == 0 else ev
                                derivative = 0
                                if exponent:
                                    derivative = exponent * (
                                        pow(u, eu - 1, prime) * pow(v, ev, prime)
                                        if axis == 0
                                        else pow(u, eu, prime) * pow(v, ev - 1, prime)
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
        "pole_vector": list(weights),
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


def selected_vectors():
    vectors = {tuple(0 for _ in COMPLETE_VECTOR), COMPLETE_VECTOR}
    active = [index for index, value in enumerate(COMPLETE_VECTOR) if value]
    for index in active:
        face = list(COMPLETE_VECTOR)
        face[index] -= 1
        vectors.add(tuple(face))
    for multiplier in (2, 3):
        vectors.add(tuple(multiplier * value for value in COMPLETE_VECTOR))
    for order in range(5):
        vector = list(COMPLETE_VECTOR)
        vector[-1] = order
        vectors.add(tuple(vector))
    return sorted(vectors)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--max-degree", type=int, default=10)
    parser.add_argument("--seed", type=lambda value: int(value, 0), default=0x243F6A8885A308D3)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    prime = int(payload["prime"])
    entries = {(item["axis"], item["row"], item["col"]): item["fit"] for item in payload["entries"]}
    declared, additional = source_factors(prime)
    factors = declared + additional
    results = []
    for weights in selected_vectors():
        for degree in range(args.max_degree + 1):
            result = census(entries, factors, prime, weights, degree, args.seed)
            results.append(result)
            print(json.dumps(result, sort_keys=True))
    output = {
        "schema": "marici.nima.gysin_complete_pole_extension_census.v1",
        "prime": prime,
        "connection_source": str(args.input.relative_to(ROOT)).replace("\\", "/"),
        "factor_order": [name for name, _ in factors],
        "complete_vector": list(COMPLETE_VECTOR),
        "vector_family": "complete vector, codimension-one faces, u2+1 orders 0..4, and full multiples 2 and 3",
        "Q_included": False,
        "sampling_seed": args.seed,
        "vector_count": len(selected_vectors()),
        "results": results,
    }
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
