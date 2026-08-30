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
AXIS = os.environ.get("MARICI_LAURENT_AXIS", "u")
RESULT_NAME = os.environ.get(
    "MARICI_LAURENT_RESULT",
    "marked_extension_source_laurent_lead.json" if AXIS == "u"
    else f"marked_extension_source_laurent_{AXIS}_axis.json",
)
RESULT = ROOT / "research" / "benincasa" / "results" / RESULT_NAME
V = int(os.environ.get("MARICI_LAURENT_V", "5"))
U_FIXED = int(os.environ.get("MARICI_LAURENT_U", "0"))
SERIES_AXIS = os.environ.get("MARICI_LAURENT_SERIES_AXIS", "u")
SERIES_CENTER = int(os.environ.get("MARICI_LAURENT_SERIES_CENTER", "0"))
DEGREE = int(os.environ.get("MARICI_LAURENT_DEGREE", "16"))
MAX_ORDER = int(os.environ.get("MARICI_LAURENT_MAX_ORDER", "3"))
MIN_ORDER = -2
TARGET_ORDER = int(os.environ.get("MARICI_LAURENT_TARGET_ORDER", "-2"))


def export(series_offset: int, master: int) -> dict:
    if SERIES_AXIS == "u":
        u_value = series_offset
        v_value = V
    elif SERIES_AXIS == "v":
        u_value = U_FIXED
        v_value = SERIES_CENTER + series_offset
    else:
        raise ValueError(f"unsupported series axis: {SERIES_AXIS}")
    env = os.environ.copy()
    env.update(
        MARICI_EXACT_POINT_SOURCE_MODE="1",
        MARICI_EXACT_U=str(u_value),
        MARICI_EXACT_V=str(v_value),
        MARICI_EXACT_AXIS=AXIS,
        MARICI_EXACT_MASTER=str(master),
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
    sample_offsets = (
        list(range(DEGREE + 2))
        if SERIES_AXIS == "u"
        else list(range(1, DEGREE + 3))
    )
    packets_by_master = [
        [export(value, master) for value in sample_offsets]
        for master in range(3)
    ]
    packets = packets_by_master[0]
    prime = packets[0]["prime"]
    unknowns = packets[0]["unknowns"]
    row_labels = sorted({tuple(row["monomial"]) for packet in packets for row in packet["rows"]})
    assert len(row_labels) == 132
    row_index = {label: index for index, label in enumerate(row_labels)}

    values: dict[tuple[int, int], list[int]] = {}
    rhs_values: list[dict[int, list[int]]] = [{} for _ in range(3)]
    for sample, packet in enumerate(packets):
        rows = {tuple(row["monomial"]): row for row in packet["rows"]}
        for label, index in row_index.items():
            row = rows.get(label, {"entries": [], "rhs": "0"})
            entries = dict((int(column), int(value) % prime) for column, value in row["entries"])
            for column in range(unknowns):
                values.setdefault((index, column), [0] * len(packets))[sample] = entries.get(column, 0)
            for master, master_packets in enumerate(packets_by_master):
                master_rows = {tuple(item["monomial"]): item for item in master_packets[sample]["rows"]}
                rhs_values[master].setdefault(index, [0] * len(packets))[sample] = int(
                    master_rows.get(label, {"rhs": "0"})["rhs"]
                ) % prime

    size = DEGREE + 1
    interpolation_points = sample_offsets[:size]
    vandermonde = [
        [pow(point, degree, prime) for degree in range(size)]
        for point in interpolation_points
    ]
    transform = inverse(vandermonde, prime)

    def coefficients(samples: list[int]) -> list[int]:
        return [sum(transform[degree][point] * samples[point] for point in range(size)) % prime for degree in range(size)]

    matrix_coefficients = {key: coefficients(sample_values) for key, sample_values in values.items()}
    rhs_coefficients = [
        {key: coefficients(sample_values) for key, sample_values in master_values.items()}
        for master_values in rhs_values
    ]

    # The held-out point certifies the chosen polynomial degree for every source coefficient.
    held_out = sample_offsets[-1]
    assert all(
        sum(coefficient * pow(held_out, degree, prime) for degree, coefficient in enumerate(coeffs)) % prime
        == sample_values[-1]
        for key, sample_values in values.items()
        for coeffs in [matrix_coefficients[key]]
    )
    assert all(
        sum(coefficient * pow(held_out, degree, prime) for degree, coefficient in enumerate(coeffs)) % prime
        == sample_values[-1]
        for master in range(3)
        for key, sample_values in rhs_values[master].items()
        for coeffs in [rhs_coefficients[master][key]]
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
            for master in range(3):
                rhs = rhs_coefficients[master][source_row][equation_order] if equation_order >= 0 else 0
                if rhs:
                    row[augmented_column + master] = field(rhs)
            if row:
                dod[len(dod)] = row

    matrix = DomainMatrix.from_dod(dod, (len(dod), columns + 3), field)
    reduced, pivots = matrix.rref()
    reduced_dod = reduced.to_dod()
    target = order_index[TARGET_ORDER] * unknowns + 8
    free = set(range(columns)) - set(pivots)
    target_is_pivot = target in pivots
    row = reduced_dod.get(pivots.index(target), {}) if target_is_pivot else {}
    fixed = target_is_pivot and all(
        row.get(column, field.zero) == field.zero for column in free
    )
    value = int(row.get(augmented_column, field.zero)) % prime if fixed else None
    rational = rational_reconstruct(value, prime) if value is not None else None

    def fixed_coordinate(order: int, coordinate: int, master: int):
        target_column = order_index[order] * unknowns + coordinate
        if target_column not in pivots:
            return None
        target_row = pivots.index(target_column)
        target_data = reduced_dod.get(target_row, {})
        if not all(target_data.get(column, field.zero) == field.zero for column in free):
            return None
        residue = int(target_data.get(augmented_column + master, field.zero)) % prime
        return str(rational_reconstruct(residue, prime))

    final_double = [
        [fixed_coordinate(-2, coordinate, master) for master in range(3)]
        for coordinate in range(8, 12)
    ]
    final_simple = [
        [fixed_coordinate(-1, coordinate, master) for master in range(3)]
        for coordinate in range(8, 12)
    ]

    output = {
        "schema": "marici.benincasa.marked_extension_source_laurent_lead.v1",
        "status": "pass" if fixed else "unfixed",
        "prime": prime,
        "v": V,
        "u_fixed": U_FIXED if SERIES_AXIS == "v" else None,
        "series_axis": SERIES_AXIS,
        "series_center": SERIES_CENTER,
        "source_polynomial_degree_bound": DEGREE,
        "held_out_polynomial_identity": True,
        "laurent_orders": orders,
        "equations": len(dod),
        "unknowns": columns,
        "rank": len(pivots),
        "derivative_axis": AXIS,
        "target": f"({SERIES_AXIS}-{SERIES_CENTER})^{TARGET_ORDER} e6 coordinate in {AXIS}-derivative of q0",
        "target_is_pivot": target_is_pivot,
        "target_fixed": fixed,
        "target_residue_mod_prime": value,
        "target_rational_reconstruction": str(rational) if rational is not None else None,
        "final_basis": ["e6", "e7", "e8", "e9"],
        "source_basis": ["q0", "q1", "q2"],
        "fixed_u_minus_2_matrix": final_double,
        "fixed_u_minus_1_matrix": final_simple,
    }
    RESULT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
