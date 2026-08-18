"""Audit the homogeneous Hom indicial operator on the shared u=0 support."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "research/benincasa"))
from check_gysin_occurrence_covariance import poly_from_terms, valuation  # noqa: E402

INPUT = ROOT / "research/benincasa/marici-gm/gysin-adapted-reconstruction-d12.json"
OUTPUT = ROOT / "research/nima/gysin-u-indicial-audit.json"


def evaluate(poly, u, v, prime):
    return sum(c * pow(u, i, prime) * pow(v, j, prime) for (i, j), c in poly.items()) % prime


def matrix_rank(matrix, prime):
    work = [row[:] for row in matrix]
    rank = 0
    for column in range(len(work[0])):
        pivot = next((i for i in range(rank, len(work)) if work[i][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], prime - 2, prime)
        work[rank] = [x * inverse % prime for x in work[rank]]
        for i in range(len(work)):
            if i != rank and work[i][column]:
                scale = work[i][column]
                work[i] = [(x - scale * y) % prime for x, y in zip(work[i], work[rank])]
        rank += 1
    return rank


def main():
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    prime = int(payload["prime"])
    factor = {(1, 0): 1}
    entries = {(item["axis"], item["row"], item["col"]): item for item in payload["entries"]}

    def residue(row, column, v):
        fit = entries[("u", row, column)]["fit"]
        numerator = poly_from_terms(fit["numerator"], prime)
        denominator = poly_from_terms(fit["denominator"], prime)
        numerator_order, numerator = valuation(numerator, factor, prime)
        denominator_order, denominator = valuation(denominator, factor, prime)
        if denominator_order - numerator_order != 1:
            return 0
        return evaluate(numerator, 0, v, prime) * pow(evaluate(denominator, 0, v, prime), prime - 2, prime) % prime

    samples = []
    for v in (3, 5, 7, 11):
        target = [[residue(i, j, v) for j in range(2)] for i in range(2)]
        exceptional = [[residue(i + 2, j + 2, v) for j in range(2)] for i in range(2)]
        hom = []
        for out_i in range(2):
            for out_j in range(2):
                row = []
                for i in range(2):
                    for j in range(2):
                        row.append(((exceptional[out_i][i] if j == out_j else 0) - (target[j][out_j] if i == out_i else 0)) % prime)
                hom.append(row)
        nullities = {}
        for order in range(1, 17):
            shifted = [row[:] for row in hom]
            for i in range(4):
                shifted[i][i] = (shifted[i][i] - order) % prime
            nullities[str(order)] = 4 - matrix_rank(shifted, prime)
        samples.append({
            "v": v,
            "target_residue": target,
            "exceptional_residue": exceptional,
            "exceptional_trace": (exceptional[0][0] + exceptional[1][1]) % prime,
            "exceptional_determinant": (exceptional[0][0] * exceptional[1][1] - exceptional[0][1] * exceptional[1][0]) % prime,
            "positive_order_nullities": nullities,
        })

    assert all(sample["target_residue"] == [[0, 0], [0, 0]] for sample in samples)
    assert all(sample["exceptional_trace"] == 0 and sample["exceptional_determinant"] == 0 for sample in samples)
    assert all(not any(sample["positive_order_nullities"].values()) for sample in samples)
    result = {
        "schema": "marici.nima.gysin_u_indicial_audit.v1",
        "prime": prime,
        "support": "u=0",
        "sample_count": len(samples),
        "positive_orders_tested": [1, 16],
        "target_residue_zero": True,
        "exceptional_residue_characteristic_polynomial": "lambda^2",
        "positive_indicial_kernel_found": False,
        "samples": samples,
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in ("support", "sample_count", "positive_orders_tested", "positive_indicial_kernel_found")}, sort_keys=True))


if __name__ == "__main__":
    main()
