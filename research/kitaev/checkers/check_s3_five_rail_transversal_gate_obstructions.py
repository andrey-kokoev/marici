#!/usr/bin/env python3
"""Test candidate transversal gates against the frozen five-rail codes."""

from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from check_s3_five_rail_code_freeze import QUBIT, QUTRIT, span  # noqa: E402


def rank(rows, q):
    matrix = [list(row) for row in rows]
    pivot_row = 0
    width = len(matrix[0]) if matrix else 0
    for column in range(width):
        pivot = next((i for i in range(pivot_row, len(matrix)) if matrix[i][column] % q), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = pow(matrix[pivot_row][column], -1, q)
        matrix[pivot_row] = [(x * scale) % q for x in matrix[pivot_row]]
        for i in range(len(matrix)):
            if i != pivot_row and matrix[i][column] % q:
                scale = matrix[i][column] % q
                matrix[i] = [
                    (matrix[i][j] - scale * matrix[pivot_row][j]) % q for j in range(width)
                ]
        pivot_row += 1
    return pivot_row


def fourier(vector, q):
    x, z = vector[:5], vector[5:]
    return tuple((-z[i]) % q for i in range(5)) + tuple(x[i] % q for i in range(5))


def inversion(vector, q):
    return tuple((-entry) % q for entry in vector)


def product_rows(stabilizers):
    zero = (0,) * 10
    return [row + zero for row in stabilizers] + [zero + row for row in stabilizers]


def transversal_sum(vector, q):
    # Ordering: Xc,Zc,Xt,Zt.  SUM |a,b> = |a,a+b|.
    xc, zc = vector[:5], vector[5:10]
    xt, zt = vector[10:15], vector[15:20]
    return (
        tuple(xc)
        + tuple((zc[i] - zt[i]) % q for i in range(5))
        + tuple((xt[i] + xc[i]) % q for i in range(5))
        + tuple(zt)
    )


def in_span(vector, rows, q):
    return rank(rows + [vector], q) == rank(rows, q)


def single_block_audit(name, stabilizers, q):
    stabilizer_span = span(stabilizers, q)
    fourier_images = [fourier(row, q) for row in stabilizers]
    inversion_images = [inversion(row, q) for row in stabilizers]
    return {
        "code": name,
        "fourier_stabilizer_images_inside": sum(v in stabilizer_span for v in fourier_images),
        "fourier_stabilizer_generator_count": 4,
        "fourier_preserves_code": all(v in stabilizer_span for v in fourier_images),
        "inversion_stabilizer_images_inside": sum(v in stabilizer_span for v in inversion_images),
        "inversion_preserves_code": all(v in stabilizer_span for v in inversion_images),
    }


def sum_audit(name, stabilizers, q):
    rows = product_rows(stabilizers)
    images = [transversal_sum(row, q) for row in rows]
    inside = [in_span(image, rows, q) for image in images]
    return {
        "code": name,
        "product_stabilizer_rank": rank(rows, q),
        "stabilizer_generator_images_inside": sum(inside),
        "stabilizer_generator_count": len(rows),
        "transversal_sum_preserves_two_block_code": all(inside),
        "failed_generator_indices": [i for i, ok in enumerate(inside) if not ok],
    }


def main():
    qubit_single = single_block_audit("[[5,1,3]]_2", QUBIT, 2)
    qutrit_single = single_block_audit("[[5,1,3]]_3", QUTRIT, 3)
    qubit_sum = sum_audit("[[5,1,3]]_2", QUBIT, 2)
    qutrit_sum = sum_audit("[[5,1,3]]_3", QUTRIT, 3)

    assert not qubit_sum["transversal_sum_preserves_two_block_code"]
    assert not qutrit_sum["transversal_sum_preserves_two_block_code"]
    assert not qubit_single["fourier_preserves_code"]
    assert not qutrit_single["fourier_preserves_code"]
    assert qubit_single["inversion_preserves_code"]
    assert qutrit_single["inversion_preserves_code"]

    result = {
        "schema": "marici.kitaev.s3-five-rail-transversal-obstructions.v1",
        "single_block": {"qubit": qubit_single, "qutrit": qutrit_single},
        "two_block_sum": {"qubit": qubit_sum, "qutrit": qutrit_sum},
        "s3_multiplication_consequence": {
            "parity_update_requires_logical_qubit_sum": True,
            "rotation_update_requires_logical_qutrit_sum": True,
            "railwise_s3_multiplication_preserves_code": False,
            "reason": "both necessary component SUM gates send frozen product-code stabilizers outside their stabilizer spans",
        },
        "proved_transversal_survivor": "componentwise inversion on the qutrit rotation coordinate",
        "required_next_resource": "error-corrected logical gate teleportation, verified encoded ancillas, or code switching for SUM and Fourier gates",
        "verdict": "The explicit five-rail codes falsify the assumed railwise multiplication and Fourier contracts. Inversion survives, but executable S3 multiplication and F3/H require a nontransversal fault-tolerant gadget.",
    }
    output = Path(__file__).parents[1] / "results" / "s3-five-rail-transversal-gate-obstructions.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
