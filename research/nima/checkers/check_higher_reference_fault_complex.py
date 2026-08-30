#!/usr/bin/env python3
"""Exact GF(2) tetrahedral higher-reference fault complex."""

import itertools
import json
from pathlib import Path


def mat_vec(matrix, vector):
    return tuple(sum(a * b for a, b in zip(row, vector)) % 2 for row in matrix)


def compose(left, right):
    columns = list(zip(*right))
    return tuple(tuple(sum(a * b for a, b in zip(row, col)) % 2 for col in columns) for row in left)


def span(vectors):
    values = set()
    for mask in itertools.product((0, 1), repeat=len(vectors)):
        values.add(tuple(sum(mask[i] * vectors[i][j] for i in range(len(vectors))) % 2 for j in range(len(vectors[0]))))
    return values


def columns(matrix):
    return [tuple(row[j] for row in matrix) for j in range(len(matrix[0]))]


def main():
    # Vertices 0..3; edges 01,02,03,12,13,23; faces 012,013,023,123.
    edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    faces = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]

    # Anchor vertex 0; columns are free vertex values 1,2,3.
    d0 = tuple(tuple(int(v in edge) for v in (1, 2, 3)) for edge in edges)
    d1 = tuple(tuple(int(edge[0] in face and edge[1] in face) for edge in edges) for face in faces)
    d2 = ((1, 1, 1, 1),)

    assert all(value == 0 for row in compose(d1, d0) for value in row)
    assert all(value == 0 for row in compose(d2, d1) for value in row)

    vertex_generators = [tuple(row[j] for row in d0) for j in range(3)]
    gauge_image = span(vertex_generators)
    all_edge_records = set(itertools.product((0, 1), repeat=6))
    edge_kernel = {value for value in all_edge_records if mat_vec(d1, value) == (0, 0, 0, 0)}
    assert edge_kernel == gauge_image

    edge_signatures = columns(d1)
    face_signatures = [tuple(int(i == j) for i in range(4)) for j in range(4)]
    assert all(sum(signature) == 2 for signature in edge_signatures)
    assert all(mat_vec(d2, signature) == (0,) for signature in edge_signatures)
    assert all(sum(signature) == 1 for signature in face_signatures)
    assert all(mat_vec(d2, signature) == (1,) for signature in face_signatures)
    all_single_fault_signatures = edge_signatures + face_signatures
    assert len(set(all_single_fault_signatures)) == 10

    # Without a higher trusted comparison, the top report can itself be flipped.
    coherent_face_record = (0, 0, 0, 0)
    true_top = mat_vec(d2, coherent_face_record)[0]
    corrupted_top = true_top ^ 1
    assert true_top == 0 and corrupted_top == 1

    result = {
        "schema": "marici.higher-reference-fault-complex.v1",
        "status": "pass",
        "d1_d0_zero": True,
        "d2_d1_zero": True,
        "edge_kernel_equals_vertex_gauge_image": edge_kernel == gauge_image,
        "vertex_gauge_image_size": len(gauge_image),
        "single_edge_fault_signatures": len(set(edge_signatures)),
        "single_face_check_fault_signatures": len(set(face_signatures)),
        "joint_single_fault_signatures": len(set(all_single_fault_signatures)),
        "single_faults_located": len(set(all_single_fault_signatures)) == 10,
        "top_checker_can_be_corrupted": corrupted_top != true_top,
        "disposition": "higher finite DPC passes; terminal fault boundary remains necessary",
    }
    out = Path(__file__).parents[1] / "results" / "higher-reference-fault-complex.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
