"""Exact filtered splitting census for the rank-four Gysin extension.

Consumes the committed reconstructed connection over GF(p).  A candidate
primitive is X=N/D^m, where D is the product of the nine source factors and
Q is deliberately omitted.  The script tests the two connection directions
simultaneously by modular linear algebra.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = ROOT / "research/benincasa/marici-gm/gysin-adapted-reconstruction-d12.json"
DEFAULT_OUTPUT = ROOT / "research/nima/gysin-multidivisor-extension-census.json"


def inv(value: int, prime: int) -> int:
    return pow(value % prime, prime - 2, prime)


def monomials(degree: int) -> list[tuple[int, int]]:
    return [(i, j) for total in range(degree + 1) for i in range(total + 1) for j in [total - i]]


def eval_sparse(terms: list[list[int]], u: int, v: int, prime: int) -> int:
    return sum(coefficient * pow(u, du, prime) * pow(v, dv, prime) for du, dv, coefficient in terms) % prime


def eval_fit(fit: dict, u: int, v: int, prime: int) -> int | None:
    numerator = eval_sparse(fit["numerator"], u, v, prime)
    denominator = eval_sparse(fit["denominator"], u, v, prime)
    if denominator == 0:
        return None
    return numerator * inv(denominator, prime) % prime


def connection(entries: dict[tuple[str, int, int], dict], axis: str, u: int, v: int, prime: int):
    matrix = [[0] * 4 for _ in range(4)]
    for row in range(4):
        for column in range(4):
            value = eval_fit(entries[(axis, row, column)], u, v, prime)
            if value is None:
                return None
            matrix[row][column] = value
    return matrix


def factors_and_derivatives(u: int, v: int, prime: int):
    half = inv(2, prime)
    quarter = half * half % prime
    y = ((u + v) * half - 1) % prime
    yu = half
    yv = half
    u2 = u * u % prime
    factors = [
        (u, 1, 0),
        (v, 0, 1),
        (y, yu, yv),
        ((1 - y) % prime, -yu, -yv),
        ((1 + y) % prime, yu, yv),
        ((v - u) % prime, -1, 1),
        ((y - u2) % prime, yu - 2 * u, yv),
        ((y + u2) % prime, yu + 2 * u, yv),
    ]
    p6 = (
        1 - u - v + v * v * quarter + u * v * half - 7 * u2 * quarter
        + u2 * v + u2 * u - u2 * u * v + u2 * u2
    ) % prime
    p6u = (-1 + v * half - 14 * u * quarter + 2 * u * v + 3 * u2 - 3 * u2 * v + 4 * u * u2) % prime
    p6v = (-1 + 2 * v * quarter + u * half + u2 - u2 * u) % prime
    factors.append((p6, p6u, p6v))
    if any(value % prime == 0 for value, _, _ in factors):
        return None
    product = 1
    dlog_u = 0
    dlog_v = 0
    for value, du, dv in factors:
        product = product * value % prime
        reciprocal = inv(value, prime)
        dlog_u = (dlog_u + du * reciprocal) % prime
        dlog_v = (dlog_v + dv * reciprocal) % prime
    return product, dlog_u, dlog_v


def rank(matrix: list[list[int]], columns: int, prime: int) -> int:
    rows = [row[:] for row in matrix]
    pivot_row = 0
    for column in range(columns):
        pivot = next((r for r in range(pivot_row, len(rows)) if rows[r][column] % prime), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = inv(rows[pivot_row][column], prime)
        rows[pivot_row] = [value * scale % prime for value in rows[pivot_row]]
        for r in range(len(rows)):
            if r == pivot_row or rows[r][column] % prime == 0:
                continue
            coefficient = rows[r][column]
            rows[r] = [(left - coefficient * right) % prime for left, right in zip(rows[r], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def census(entries, prime: int, pole: int, degree: int, seed: int):
    mons = monomials(degree)
    unknowns = 4 * len(mons)
    target_rows = unknowns + 32
    matrix: list[list[int]] = []
    state_u = seed ^ (pole << 17) ^ degree
    state_v = seed ^ 0x9E3779B97F4A7C15 ^ (degree << 23)
    accepted = 0
    while len(matrix) < target_rows:
        state_u = (state_u * 6364136223846793005 + 1447) % prime
        state_v = (state_v * 2862933555777941757 + 1451) % prime
        u, v = state_u, state_v
        factor_data = factors_and_derivatives(u, v, prime)
        if factor_data is None:
            continue
        divisor, dlog_u, dlog_v = factor_data
        au = connection(entries, "u", u, v, prime)
        av = connection(entries, "v", u, v, prime)
        if au is None or av is None:
            continue
        accepted += 1
        for axis, a, dlog in [(0, au, dlog_u), (1, av, dlog_v)]:
            divisor_power = pow(divisor, pole, prime)
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
                                    coefficient += derivative - pole * dlog * value
                                if q == i:
                                    coefficient += value * a[k][j]
                                if k == j:
                                    coefficient -= value * a[i + 2][q + 2]
                                row[block + index] = coefficient % prime
                    row[-1] = (-divisor_power * a[i + 2][j]) % prime
                    matrix.append(row)
    coefficient_rank = rank([row[:-1] for row in matrix], unknowns, prime)
    augmented_rank = rank(matrix, unknowns + 1, prime)
    return {
        "pole_bound": pole,
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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--max-degree", type=int, default=6)
    parser.add_argument("--max-pole", type=int, default=2)
    parser.add_argument("--seed", type=lambda value: int(value, 0), default=0x243F6A8885A308D3)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    prime = int(payload["prime"])
    entries = {(item["axis"], item["row"], item["col"]): item["fit"] for item in payload["entries"]}
    results = []
    for pole in range(args.max_pole + 1):
        for degree in range(args.max_degree + 1):
            result = census(entries, prime, pole, degree, args.seed)
            results.append(result)
            print(json.dumps(result, sort_keys=True))
    output = {
        "schema": "marici.nima.gysin_multidivisor_extension_census.v1",
        "prime": prime,
        "connection_source": str(args.input.relative_to(ROOT)).replace("\\", "/"),
        "denominator": "u*v*y*(1-y)*(1+y)*(v-u)*(y-u^2)*(y+u^2)*P6",
        "Q_included": False,
        "sampling_seed": args.seed,
        "results": results,
    }
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
