"""Sample the exact generic normal connection in the primitive rank-26 frame."""

from __future__ import annotations

import json
import os
from pathlib import Path

import check_rank26_total_energy_source_word_rees as source
import derive_rank26_source_word_basis as basis


P = source.P
T_SIGNED = int(os.environ.get("MARICI_E_VALUE", "1"))
T = T_SIGNED % P
AMBIENT = int(os.environ.get("MARICI_AMBIENT", "12"))
BASIS_FILE = Path(os.environ.get("MARICI_BASIS_FILE", source.HERE / "rank26-source-word-basis.json"))


def add_scaled(target, other, scale):
    for key, value in other.items():
        next_value = (target.get(key, 0) + scale * value) % P
        if next_value: target[key] = next_value
        else: target.pop(key, None)


def normalized_basis_solver(rows):
    pivots = {}
    for index, input_row in enumerate(rows):
        row = dict(input_row)
        coordinates = {index: 1}
        while row:
            pivot = max(row)
            coefficient = row[pivot]
            if pivot not in pivots: break
            pivot_row, pivot_coordinates = pivots[pivot]
            add_scaled(row, pivot_row, -coefficient)
            add_scaled(coordinates, pivot_coordinates, -coefficient)
        assert row, f"basis dependency at {index}"
        pivot = max(row)
        inverse = pow(row[pivot], P - 2, P)
        row = {key: value * inverse % P for key, value in row.items()}
        coordinates = {key: value * inverse % P for key, value in coordinates.items()}
        pivots[pivot] = (row, coordinates)
    assert len(pivots) == len(rows)
    return pivots


def solve(row, pivots):
    residual = dict(row)
    coordinates = {}
    while residual:
        pivot = max(residual)
        coefficient = residual[pivot]
        if pivot not in pivots: break
        pivot_row, pivot_coordinates = pivots[pivot]
        add_scaled(residual, pivot_row, -coefficient)
        add_scaled(coordinates, pivot_coordinates, coefficient)
    return coordinates, residual


def coefficient(row, degree):
    return {column: jet[degree] for column, jet in row.items() if jet[degree]}


def main():
    x, y, boundary_z = source.rees.POINT
    point = (x, y, boundary_z + T_SIGNED)
    old_basis_ambient = basis.AMBIENT
    basis.AMBIENT = AMBIENT
    try:
        pres = basis.presentation(point)
    finally:
        basis.AMBIENT = old_basis_ambient
    _, columns = source.rees.column_packet()
    assert columns == pres["columns"]
    ordered = pres["ordered_columns"]

    old_point = source.rees.POINT
    old_descriptors = source.DESCRIPTORS
    source.rees.POINT = point
    source.DESCRIPTORS = json.loads(BASIS_FILE.read_text())["descriptors"]
    try:
        rows = source.source_word_jets(columns)
        z = (point[2], 1, 0)
        derivatives = [source.derivative_jet_data(x, y, z, axis) for axis in range(3)]
    finally:
        source.rees.POINT = old_point
        source.DESCRIPTORS = old_descriptors

    quotient_rows = [source.rees.base.reduce_row(coefficient(row, 0), pres["pivots"]) for row in rows]
    pivots = normalized_basis_solver(quotient_rows)
    matrix = []
    residual_supports = []
    for row in rows:
        covariant = coefficient(row, 1)
        connection = coefficient(source.raw_connection(row, 2, ordered, columns, derivatives), 0)
        add_scaled(covariant, connection, 1)
        quotient = source.rees.base.reduce_row(covariant, pres["pivots"])
        coordinates, residual = solve(quotient, pivots)
        matrix.append([coordinates.get(index, 0) for index in range(len(rows))])
        residual_supports.append(len(residual))
    solved = max(residual_supports) == 0
    result = {
        "schema":"marici.benincasa.rank26-primitive-normal-connection-sample.v1",
        "field":P,"boundary_point":list(old_point),"E_T":T,"point":list(point),
        "ambient_relation_degree":AMBIENT,"basis_size":len(rows),
        "basis_file":str(BASIS_FILE),
        "residual_supports":residual_supports,"all_derivatives_solved":solved,
        "unsolved_derivative_count":sum(value != 0 for value in residual_supports),
        "matrix":matrix if solved else None,
        "convention":"row i gives (d/dE_T+A_z) applied to primitive i in the ordered primitive basis",
    }
    suffix = f"m{-T_SIGNED}" if T_SIGNED < 0 else str(T_SIGNED)
    output = Path(__file__).with_name(f"rank26-primitive-normal-connection-sample-e{suffix}-p{P}.json")
    output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({key:value for key,value in result.items() if key != "matrix"},indent=2,sort_keys=True))


if __name__ == "__main__": main()
