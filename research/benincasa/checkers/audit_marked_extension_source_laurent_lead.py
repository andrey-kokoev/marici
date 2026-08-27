"""Compute the top-to-e6 Laurent lead from the cleared source system itself."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from fractions import Fraction
from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa" / ".tmp_sympy"))

from sympy.polys.domains import GF
from sympy.polys.matrices import DomainMatrix


EXE = ROOT / "research" / "benincasa" / "marici-gm" / "target" / "release" / "marked_relative_reduction_engine.exe"
RESULT = ROOT / "research" / "benincasa" / "results" / "marked_extension_source_laurent_lead.json"
V = int(os.environ.get("MARICI_LAURENT_V", "5"))
DEGREE = int(os.environ.get("MARICI_LAURENT_DEGREE", "16"))
MAX_ORDER = int(os.environ.get("MARICI_LAURENT_MAX_ORDER", "3"))
MIN_ORDER = -2


def export(u: int) -> dict:
    env = os.environ.copy()
    env.update(
        MARICI_EXACT_POINT_SOURCE_MODE="1",
        MARICI_EXACT_U=str(u),
        MARICI_EXACT_V=str(V),
        MARICI_EXACT_AXIS="u",
        MARICI_EXACT_MASTER="0",
        MARICI_EXACT_RAW_RESIDUES="1",
    )
    return json.loads(subprocess.run([str(EXE)], env=env, check=True, capture_output=True, text=True).stdout)


def inverse(matrix: list[list[int]], prime: int) -> list[list[int]]:
    n = len(matrix)
    augmented = [row[:] + [int(i == j) for j in range(n)] for i, row in enumerate(matrix)]
    for column in range(n):
        pivot = next(row for row in range(column, n) if augmented[row][column] % prime)
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = pow(augmented[column][column], -1, prime)
        augmented[column] = [(value * scale) % prime for value in augmented[column]]
        for row in range(n):
            if row != column and augmented[row][column] % prime:
                scale = augmented[row][column]
                augmented[row] = [
                    (left - scale * right) % prime
                    for left, right in zip(augmented[row], augmented[column])
                ]
    return [row[n:] for row in augmented]


def rational_reconstruct(value: int, modulus: int) -> Fraction:
    bound = isqrt(modulus // 2)
    old_remainder, remainder = modulus, value
    old_denominator, denominator = 0, 1
    while abs(remainder) > bound:
        quotient = old_remainder // remainder
        old_remainder, remainder = remainder, old_remainder - quotient * remainder
        old_denominator, denominator = denominator, old_denominator - quotient * denominator
    if denominator < 0:
        remainder, denominator = -remainder, -denominator
    assert denominator and abs(denominator) <= bound
    assert (remainder - value * denominator) % modulus == 0
    return Fraction(remainder, denominator)


def main() -> None:
    packets = [export(value) for value in range(DEGREE + 2)]
    prime = packets[0]["prime"]
    unknowns = packets[0]["unknowns"]
    row_labels = sorted({tuple(row["monomial"]) for packet in packets for row in packet["rows"]})
    assert len(row_labels) == 132
    row_index = {label: index for index, label in enumerate(row_labels)}

    values: dict[tuple[int, int], list[int]] = {}
    rhs_values: dict[int, list[int]] = {}
    for sample, packet in enumerate(packets):
        rows = {tuple(row["monomial"]): row for row in packet["rows"]}
        for label, index in row_index.items():
            row = rows.get(label, {"entries": [], "rhs": "0"})
            entries = dict((int(column), int(value) % prime) for column, value in row["entries"])
            for column in range(unknowns):
                values.setdefault((index, column), [0] * len(packets))[sample] = entries.get(column, 0)
            rhs_values.setdefault(index, [0] * len(packets))[sample] = int(row["rhs"]) % prime

    size = DEGREE + 1
    vandermonde = [[pow(point, degree, prime) for degree in range(size)] for point in range(size)]
    transform = inverse(vandermonde, prime)

    def coefficients(samples: list[int]) -> list[int]:
        return [sum(transform[degree][point] * samples[point] for point in range(size)) % prime for degree in range(size)]

    matrix_coefficients = {key: coefficients(sample_values) for key, sample_values in values.items()}
    rhs_coefficients = {key: coefficients(sample_values) for key, sample_values in rhs_values.items()}

    # The held-out point certifies the chosen polynomial degree for every source coefficient.
    held_out = DEGREE + 1
    assert all(
        sum(coefficient * pow(held_out, degree, prime) for degree, coefficient in enumerate(coeffs)) % prime
        == sample_values[held_out]
        for key, sample_values in values.items()
        for coeffs in [matrix_coefficients[key]]
    )
    assert all(
        sum(coefficient * pow(held_out, degree, prime) for degree, coefficient in enumerate(coeffs)) % prime
        == sample_values[held_out]
        for key, sample_values in rhs_values.items()
        for coeffs in [rhs_coefficients[key]]
    )

    orders = list(range(MIN_ORDER, MAX_ORDER + 1))
    order_index = {order: index for index, order in enumerate(orders)}
    columns = unknowns * len(orders)
    augmented_column = columns
    dod: dict[int, dict[int, object]] = {}
    field = GF(prime)
    for equation_order in orders:
        for source_row in range(len(row_labels)):
            row: dict[int, object] = {}
            for unknown_order in orders:
                degree = equation_order - unknown_order
                if not 0 <= degree <= DEGREE:
                    continue
                block = order_index[unknown_order] * unknowns
                for source_column in range(unknowns):
                    value = matrix_coefficients[(source_row, source_column)][degree]
                    if value:
                        row[block + source_column] = field(value)
            rhs = rhs_coefficients[source_row][equation_order] if equation_order >= 0 else 0
            if rhs:
                row[augmented_column] = field(rhs)
            if row:
                dod[len(dod)] = row

    matrix = DomainMatrix.from_dod(dod, (len(dod), columns + 1), field)
    reduced, pivots = matrix.rref()
    reduced_dod = reduced.to_dod()
    target = order_index[-2] * unknowns + 8
    assert target in pivots
    pivot_row = pivots.index(target)
    row = reduced_dod.get(pivot_row, {})
    free = set(range(columns)) - set(pivots)
    fixed = all(row.get(column, field.zero) == field.zero for column in free)
    value = int(row.get(augmented_column, field.zero)) % prime if fixed else None
    rational = rational_reconstruct(value, prime) if value is not None else None

    output = {
        "schema": "marici.benincasa.marked_extension_source_laurent_lead.v1",
        "status": "pass" if fixed else "unfixed",
        "prime": prime,
        "v": V,
        "source_polynomial_degree_bound": DEGREE,
        "held_out_polynomial_identity": True,
        "laurent_orders": orders,
        "equations": len(dod),
        "unknowns": columns,
        "rank": len(pivots),
        "target": "u^-2 e6 coordinate in derivative of q0",
        "target_fixed": fixed,
        "target_residue_mod_prime": value,
        "target_rational_reconstruction": str(rational) if rational is not None else None,
    }
    RESULT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
