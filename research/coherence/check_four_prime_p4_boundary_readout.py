#!/usr/bin/env python3
"""Retain the genuine left-boundary, grade-two readout of the P4 pairing."""

import json
from fractions import Fraction
from pathlib import Path
import check_four_prime_cube_bianchi as cube
import check_four_prime_curvature_pairing as p4

BOUNDARY_WIDTH = max(cube.SHIFTS)
GRADE_TWO_MASKS = tuple(m for m in range(16) if m.bit_count() == 2)
BASIS = tuple((m, x) for m in GRADE_TWO_MASKS for x in range(BOUNDARY_WIDTH))
INDEX = {state: i for i, state in enumerate(BASIS)}


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        scale = a[r][c]
        a[r] = [x / scale for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                scale = a[i][c]
                a[i] = [x - scale * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def main():
    matrix = [[0 for _ in BASIS] for _ in BASIS]
    transitions = []
    for col, (mask, x) in enumerate(BASIS):
        source = cube.basis(mask * cube.N + x)
        value = p4.four_pairing(source)
        for target_mask, target_x in BASIS:
            coefficient = value[target_mask * cube.N + target_x]
            if coefficient:
                row = INDEX[(target_mask, target_x)]
                matrix[row][col] = coefficient
                transitions.append({
                    "source_face_mask": mask,
                    "source_x": x,
                    "target_face_mask": target_mask,
                    "target_x": target_x,
                    "coefficient": coefficient,
                    "complementary_faces": target_mask == (15 ^ mask),
                })

    matrix_rank = rank(matrix)
    assert transitions
    assert all(t["complementary_faces"] for t in transitions)
    assert matrix_rank > 0
    result = {
        "schema": "marici.coherence.four-prime-p4-boundary-readout.v1",
        "readout": "rho_L(P4)=Pi_(Lambda2,x<max_shift) P4 Pi_(Lambda2,x<max_shift)",
        "boundary_width": BOUNDARY_WIDTH,
        "face_channels": GRADE_TWO_MASKS,
        "readout_dimension": len(BASIS),
        "nonzero_transitions": len(transitions),
        "rank": matrix_rank,
        "all_transitions_pair_complementary_two_faces": True,
        "trace": sum(matrix[i][i] for i in range(len(BASIS))),
        "transitions": transitions,
        "matrix": matrix,
    }
    target = Path(__file__).with_name("four-prime-p4-boundary-readout.v1.json")
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("boundary_width", "readout_dimension", "nonzero_transitions", "rank", "all_transitions_pair_complementary_two_faces", "trace")}, indent=2))


if __name__ == "__main__":
    main()
