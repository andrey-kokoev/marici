#!/usr/bin/env python3
"""Test whether the declared five-site OFPT unit sum is an incidence cycle."""

import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / "research/benincasa/results/five-cycle-ofpt-packet.json"
OUTPUT = ROOT / "research/nima/results/five-site-ofpt-constructor-incidence.json"


def boundary(simplex):
    return [(simplex[:i] + simplex[i+1:], -1 if i & 1 else 1)
            for i in range(len(simplex))]


def modular_rank(rows, prime):
    matrix = [[value % prime for value in row] for row in rows]
    if not matrix:
        return 0
    row_count, column_count = len(matrix), len(matrix[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next((row for row in range(pivot_row, row_count)
                      if matrix[row][column]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        inverse = pow(matrix[pivot_row][column], prime-2, prime)
        matrix[pivot_row] = [value*inverse % prime for value in matrix[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or matrix[row][column] == 0:
                continue
            factor = matrix[row][column]
            matrix[row] = [(a-factor*b) % prime
                           for a, b in zip(matrix[row], matrix[pivot_row])]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def main():
    packet = json.loads(PACKET.read_text())
    cycle = packet["five_cycle"]
    terms = cycle["terms"]
    facets = sorted({label for term in terms for label in term})
    order = {label: index for index, label in enumerate(facets)}
    simplices = [tuple(sorted(term, key=order.__getitem__)) for term in terms]
    faces3 = sorted({face for simplex in simplices for face, _ in boundary(simplex)})
    face3_index = {face: index for index, face in enumerate(faces3)}
    d4 = [[0]*len(simplices) for _ in faces3]
    source_boundary = [0]*len(faces3)
    for column, simplex in enumerate(simplices):
        for face, sign in boundary(simplex):
            row = face3_index[face]
            d4[row][column] = sign
            source_boundary[row] += sign

    faces2 = sorted({face for simplex in faces3 for face, _ in boundary(simplex)})
    face2_index = {face: index for index, face in enumerate(faces2)}
    d3 = [[0]*len(faces3) for _ in faces2]
    for column, simplex in enumerate(faces3):
        for face, sign in boundary(simplex):
            d3[face2_index[face]][column] = sign
    d3d4_nonzero = 0
    for row in range(len(faces2)):
        for column in range(len(simplices)):
            value = sum(d3[row][mid]*d4[mid][column]
                        for mid in range(len(faces3)))
            d3d4_nonzero += value != 0

    ranks = {}
    for prime in (1009, 1013):
        ranks[str(prime)] = {
            "rank_d4": modular_rank(d4, prime),
            "kernel_dimension_d4": len(simplices)-modular_rank(d4, prime),
            "rank_d3": modular_rank(d3, prime),
        }
    support = [
        {"face": list(face), "coefficient": coefficient}
        for face, coefficient in zip(faces3, source_boundary) if coefficient
    ]
    output = {
        "schema": "marici.five_site.ofpt_constructor_incidence.v1",
        "source_packet": str(PACKET.relative_to(ROOT)).replace("\\", "/"),
        "declared_orientation_weight": cycle["source_representation"]["orientation_normalized_common_weight"]
        if "source_representation" in cycle else
        packet["source_representation"]["orientation_normalized_common_weight"],
        "facet_count_in_terms": len(facets),
        "four_face_count": len(simplices),
        "three_face_count": len(faces3),
        "two_face_count": len(faces2),
        "boundary_squared_nonzero_entries": d3d4_nonzero,
        "source_unit_sum_is_cycle": not support,
        "source_unit_sum_boundary_support_count": len(support),
        "source_unit_sum_boundary_l1_norm": sum(abs(item["coefficient"]) for item in support),
        "source_unit_sum_boundary_sample": support[:20],
        "ranks": ranks,
        "interpretation": (
            "If the unit OFPT term sum is not an incidence cycle, the term packet alone "
            "does not supply the proposed constructor/cochain differential."
        ),
        "scope": (
            "Abstract simplicial incidence on the packet's compatible four-facet sets; "
            "does not exclude a separately derived oriented polytope or residue complex."
        ),
        "passed": d3d4_nonzero == 0,
    }
    OUTPUT.write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
