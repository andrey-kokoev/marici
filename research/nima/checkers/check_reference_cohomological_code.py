#!/usr/bin/env python3
"""Exact GF(2) checks for the cohomological reference-code DPC."""

import itertools
import json
from pathlib import Path


def dot(row, vector):
    return sum(a * b for a, b in zip(row, vector)) % 2


def syndrome(matrix, vector):
    return tuple(dot(row, vector) for row in matrix)


def span(vectors):
    if not vectors:
        return {()}
    result = set()
    for mask in itertools.product((0, 1), repeat=len(vectors)):
        value = tuple(
            sum(mask[i] * vectors[i][j] for i in range(len(vectors))) % 2
            for j in range(len(vectors[0]))
        )
        result.add(value)
    return result


def columns(matrix):
    return [tuple(row[j] for row in matrix) for j in range(len(matrix[0]))]


def main():
    # A triangle has one cycle equation. Every edge has the same syndrome.
    triangle_h = [(1, 1, 1)]
    triangle_columns = columns(triangle_h)
    assert len(set(triangle_columns)) == 1
    assert triangle_columns[0] == (1,)

    # K4 edges: 01, 02, 03, 12, 13, 23. Fundamental cycles use a star tree.
    k4_h = [
        (1, 1, 0, 1, 0, 0),  # 01-02-12
        (1, 0, 1, 0, 1, 0),  # 01-03-13
        (0, 1, 1, 0, 0, 1),  # 02-03-23
    ]
    k4_columns = columns(k4_h)
    assert len(set(k4_columns)) == 6
    assert all(column != (0, 0, 0) for column in k4_columns)

    # Coboundaries from vertex assignments with vertex 0 fixed.
    edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    coboundary_generators = []
    for vertex in (1, 2, 3):
        coboundary_generators.append(
            tuple(int(vertex in edge) for edge in edges)
        )
    coboundaries = span(coboundary_generators)
    assert len(coboundaries) == 8
    assert all(syndrome(k4_h, value) == (0, 0, 0) for value in coboundaries)

    all_edges = set(itertools.product((0, 1), repeat=6))
    kernel = {value for value in all_edges if syndrome(k4_h, value) == (0, 0, 0)}
    assert kernel == coboundaries

    nonzero_kernel_weights = [sum(value) for value in kernel if any(value)]
    distance = min(nonzero_kernel_weights)
    assert distance == 3

    single_fault_syndromes = {
        syndrome(k4_h, tuple(int(i == j) for i in range(6))): j
        for j in range(6)
    }
    assert len(single_fault_syndromes) == 6

    result = {
        "schema": "marici.reference-cohomological-code.v1",
        "status": "pass",
        "triangle_single_edge_syndrome_classes": len(set(triangle_columns)),
        "k4_independent_cycle_checks": len(k4_h),
        "k4_distinct_single_edge_syndromes": len(set(k4_columns)),
        "k4_coboundary_count": len(coboundaries),
        "k4_syndrome_kernel_count": len(kernel),
        "kernel_equals_coboundary_image": kernel == coboundaries,
        "reference_code_distance": distance,
        "correctable_edge_faults": (distance - 1) // 2,
        "disposition": "finite binary cohomological reference-code DPC passes",
    }
    out = Path(__file__).parents[1] / "results" / "reference-cohomological-code.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

