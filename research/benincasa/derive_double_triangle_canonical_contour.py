#!/usr/bin/env python3
"""Derive the source vertices and complete facet packet for the double triangle."""

import itertools
import json
import math
from fractions import Fraction
from pathlib import Path


VERTICES = tuple(range(1, 7))
EDGES = ((1, 2), (2, 3), (3, 1), (3, 4), (4, 5), (5, 6), (6, 4))
EDGE_NAMES = ("12", "23", "31", "34", "45", "56", "64")


def rank(rows):
    matrix = [[Fraction(value) for value in row] for row in rows if any(row)]
    if not matrix:
        return 0
    row_count, column_count, pivot_row = len(matrix), len(matrix[0]), 0
    for column in range(column_count):
        pivot = next((row for row in range(pivot_row, row_count) if matrix[row][column]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        value = matrix[pivot_row][column]
        matrix[pivot_row] = [entry / value for entry in matrix[pivot_row]]
        for row in range(row_count):
            if row != pivot_row and matrix[row][column]:
                value = matrix[row][column]
                matrix[row] = [left - value * right for left, right in zip(matrix[row], matrix[pivot_row])]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def determinant(square):
    matrix = [[Fraction(value) for value in row] for row in square]
    size = len(matrix)
    result = Fraction(1)
    for column in range(size):
        pivot = next((row for row in range(column, size) if matrix[row][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
            result = -result
        value = matrix[column][column]
        result *= value
        for row in range(column + 1, size):
            ratio = matrix[row][column] / value
            for inner in range(column, size):
                matrix[row][inner] -= ratio * matrix[column][inner]
    return result


def connected(vertex_set, edge_indices):
    if len(vertex_set) == 1:
        return not edge_indices
    adjacency = {vertex: set() for vertex in vertex_set}
    for edge_index in edge_indices:
        left, right = EDGES[edge_index]
        adjacency[left].add(right)
        adjacency[right].add(left)
    reached = {next(iter(vertex_set))}
    stack = list(reached)
    while stack:
        reached.update(adjacency[stack.pop()] - reached)
        stack.extend(adjacency[vertex] - reached for vertex in [])
    # The update above is sufficient only for one layer; use a fixed closure.
    changed = True
    while changed:
        before = len(reached)
        reached |= set().union(*(adjacency[vertex] for vertex in reached))
        changed = len(reached) != before
    return reached == set(vertex_set)


def main() -> None:
    coordinate_order = [*[f"X{vertex}" for vertex in VERTICES], *[f"y{name}" for name in EDGE_NAMES]]
    source_vertices = []
    for edge_index, (left, right) in enumerate(EDGES):
        for vertex_type, (left_value, right_value, edge_value) in enumerate(
            ((1, 1, -1), (1, -1, 1), (-1, 1, 1)), start=1
        ):
            column = [0] * len(coordinate_order)
            column[left - 1] = left_value
            column[right - 1] = right_value
            column[len(VERTICES) + edge_index] = edge_value
            source_vertices.append(
                {
                    "contour_variable": f"c_{EDGE_NAMES[edge_index]}_{vertex_type}",
                    "edge": EDGE_NAMES[edge_index],
                    "vertex_type": vertex_type,
                    "column": column,
                    "regulator": f"epsilon_{EDGE_NAMES[edge_index]}_{vertex_type}",
                }
            )

    facets = []
    # Singleton connected subgraphs.
    for vertex in VERTICES:
        row = [0] * len(coordinate_order)
        row[vertex - 1] = 1
        for edge_index, edge in enumerate(EDGES):
            row[len(VERTICES) + edge_index] = int(vertex in edge)
        facets.append({"label": f"g_{vertex}", "vertices": [vertex], "edges": [], "row": row})

    # Every nonempty connected edge-subgraph. Its vertex set is the set of
    # endpoints. An omitted ambient edge contributes once for each retained
    # endpoint, reproducing the occurrence-resolved partial-energy valuation.
    for edge_count in range(1, len(EDGES) + 1):
        for edge_indices in itertools.combinations(range(len(EDGES)), edge_count):
            vertex_set = set().union(*(set(EDGES[index]) for index in edge_indices))
            if not connected(vertex_set, edge_indices):
                continue
            row = [0] * len(coordinate_order)
            for vertex in vertex_set:
                row[vertex - 1] = 1
            selected = set(edge_indices)
            for edge_index, edge in enumerate(EDGES):
                if edge_index not in selected:
                    row[len(VERTICES) + edge_index] = sum(vertex in vertex_set for vertex in edge)
            label = "g_" + "".join(map(str, sorted(vertex_set))) + "__" + "_".join(EDGE_NAMES[index] for index in edge_indices)
            facets.append(
                {
                    "label": label,
                    "vertices": sorted(vertex_set),
                    "edges": [EDGE_NAMES[index] for index in edge_indices],
                    "row": row,
                }
            )

    columns = [item["column"] for item in source_vertices]
    ambient_rank = rank(columns)
    projective_dimension = ambient_rank - 1
    for facet in facets:
        values = [sum(left * right for left, right in zip(facet["row"], column)) for column in columns]
        zero_columns = [column for column, value in zip(columns, values) if value == 0]
        base = zero_columns[0]
        affine_rank = rank([[left - right for left, right in zip(column, base)] for column in zero_columns[1:]])
        facet["zero_source_vertex_count"] = len(zero_columns)
        facet["zero_affine_rank"] = affine_rank
        facet["nonnegative_on_source_vertices"] = min(values) >= 0

    # Greedy source-column localization basis.
    localization_indices = []
    selected_columns = []
    current_rank = 0
    for index, column in enumerate(columns):
        candidate_rank = rank(selected_columns + [column])
        if candidate_rank > current_rank:
            localization_indices.append(index)
            selected_columns.append(column)
            current_rank = candidate_rank
        if current_rank == ambient_rank:
            break
    localization_matrix = [[selected_columns[column][row] for column in range(ambient_rank)] for row in range(ambient_rank)]
    localization_determinant = determinant(localization_matrix)
    unfixed = [index for index in range(len(columns)) if index not in localization_indices]

    left_facet = next(item for item in facets if item["vertices"] == [1, 2, 3] and set(item["edges"]) == {"12", "23", "31"})
    right_facet = next(item for item in facets if item["vertices"] == [4, 5, 6] and set(item["edges"]) == {"45", "56", "64"})
    checks = {
        "coordinate_count": len(coordinate_order),
        "source_vertex_count": len(source_vertices),
        "ambient_rank": ambient_rank,
        "projective_dimension": projective_dimension,
        "facet_count": len(facets),
        "all_declared_facets_are_nonnegative": all(item["nonnegative_on_source_vertices"] for item in facets),
        "all_declared_facets_have_codimension_one_zero_span": all(item["zero_affine_rank"] == projective_dimension - 1 for item in facets),
        "localization_basis_size": len(localization_indices),
        "localization_determinant": str(localization_determinant),
        "unfixed_contour_dimension": len(unfixed),
        "left_cut_facet_row": left_facet["row"],
        "right_cut_facet_row": right_facet["row"],
        "left_cut_facet_is_X123_plus_y34": left_facet["row"] == [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        "right_cut_facet_is_X456_plus_y34": right_facet["row"] == [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    }
    assert checks["ambient_rank"] == 13
    assert checks["projective_dimension"] == 12
    assert checks["source_vertex_count"] == 21
    assert checks["all_declared_facets_are_nonnegative"]
    assert checks["all_declared_facets_have_codimension_one_zero_span"]
    assert localization_determinant != 0
    assert checks["unfixed_contour_dimension"] == 8
    assert checks["left_cut_facet_is_X123_plus_y34"]
    assert checks["right_cut_facet_is_X456_plus_y34"]

    packet = {
        "schema": "marici.double-triangle-canonical-contour.v1",
        "status": "pass",
        "primary_construction": "general cosmological-polytope source-vertex and connected-subgraph facet formula",
        "ambient_orientation": coordinate_order,
        "contour_orientation": [item["contour_variable"] for item in source_vertices],
        "source_vertices": source_vertices,
        "facets": facets,
        "localization_basis": {
            "indices_zero_based": localization_indices,
            "variables": [source_vertices[index]["contour_variable"] for index in localization_indices],
            "determinant": str(localization_determinant),
            "unfixed_indices_zero_based": unfixed,
            "unfixed_variables": [source_vertices[index]["contour_variable"] for index in unfixed],
        },
        "normalization": f"1/({projective_dimension}!*(2*pi*i)^{len(unfixed)})",
        "bridge_cut_facets": {"left": left_facet["label"], "right": right_facet["label"]},
        "checks": checks,
    }
    out = Path(__file__).with_name("double-triangle-canonical-contour.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": packet["status"], "checks": checks}, indent=2))


if __name__ == "__main__":
    main()
