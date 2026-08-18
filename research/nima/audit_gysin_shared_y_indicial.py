"""Audit both fixed-chart representatives of the shared y/(v-u) support."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "research/benincasa"))
from check_gysin_occurrence_covariance import poly_from_terms, valuation  # noqa: E402

INPUT = ROOT / "research/benincasa/marici-gm/gysin-adapted-reconstruction-d12.json"
OUTPUT = ROOT / "research/nima/gysin-shared-y-indicial-audit.json"


def evaluate(poly, u, v, prime):
    return sum(c * pow(u, i, prime) * pow(v, j, prime) for (i, j), c in poly.items()) % prime


def rank(matrix, prime):
    work = [row[:] for row in matrix]
    result = 0
    for column in range(len(work[0])):
        pivot = next((i for i in range(result, len(work)) if work[i][column]), None)
        if pivot is None:
            continue
        work[result], work[pivot] = work[pivot], work[result]
        inverse = pow(work[result][column], prime - 2, prime)
        work[result] = [x * inverse % prime for x in work[result]]
        for i in range(len(work)):
            if i != result and work[i][column]:
                scale = work[i][column]
                work[i] = [(x - scale * y) % prime for x, y in zip(work[i], work[result])]
        result += 1
    return result


def main():
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    prime = int(payload["prime"])
    half = pow(2, prime - 2, prime)
    entries = {(item["axis"], item["row"], item["col"]): item for item in payload["entries"]}
    representatives = [
        ("y", {(1, 0): half, (0, 1): half, (0, 0): prime - 1}, lambda u: (2 - u) % prime, 2),
        ("v-u", {(0, 1): 1, (1, 0): prime - 1}, lambda u: u, 1),
    ]
    results = []
    for name, factor, v_on_divisor, normal_multiplier in representatives:
        samples = []
        for u in (3, 5, 7, 11):
            v = v_on_divisor(u)

            def residue(row, column):
                fit = entries[("v", row, column)]["fit"]
                numerator = poly_from_terms(fit["numerator"], prime)
                denominator = poly_from_terms(fit["denominator"], prime)
                numerator_order, numerator = valuation(numerator, factor, prime)
                denominator_order, denominator = valuation(denominator, factor, prime)
                if denominator_order - numerator_order != 1:
                    return 0
                return normal_multiplier * evaluate(numerator, u, v, prime) * pow(evaluate(denominator, u, v, prime), prime - 2, prime) % prime

            target = [[residue(i, j) for j in range(2)] for i in range(2)]
            exceptional = [[residue(i + 2, j + 2) for j in range(2)] for i in range(2)]
            hom = []
            for out_i in range(2):
                for out_j in range(2):
                    hom.append([((exceptional[out_i][i] if j == out_j else 0) - (target[j][out_j] if i == out_i else 0)) % prime for i in range(2) for j in range(2)])
            nullities = {}
            for order in range(1, 17):
                shifted = [row[:] for row in hom]
                for i in range(4):
                    shifted[i][i] = (shifted[i][i] - order) % prime
                nullities[str(order)] = 4 - rank(shifted, prime)
            samples.append({"u": u, "v": v, "target_residue": target, "exceptional_residue": exceptional, "positive_order_nullities": nullities})
        assert all(not any(sample["positive_order_nullities"].values()) for sample in samples)
        results.append({"representative": name, "samples": samples, "positive_indicial_kernel_found": False})
    result = {
        "schema": "marici.nima.gysin_shared_y_indicial_audit.v1",
        "prime": prime,
        "support_class": "y ~ v-u modulo chart units",
        "representatives": results,
        "positive_orders_tested": [1, 16],
        "positive_indicial_kernel_found": False,
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"representatives": [item["representative"] for item in results], "positive_orders_tested": [1, 16], "positive_indicial_kernel_found": False}, sort_keys=True))


if __name__ == "__main__":
    main()
