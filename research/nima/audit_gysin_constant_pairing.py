"""Test for constant horizontal bilinear forms on the adapted rank-four connection."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "research/benincasa/marici-gm/gysin-adapted-reconstruction-d12.json"
OUTPUT = ROOT / "research/nima/gysin-constant-pairing-audit.json"


def evaluate(terms, u, v, prime):
    return sum(coefficient * pow(u, du, prime) * pow(v, dv, prime) for du, dv, coefficient in terms) % prime


def rank(matrix, prime):
    work = [row[:] for row in matrix]
    result = 0
    for column in range(len(work[0])):
        pivot = next((i for i in range(result, len(work)) if work[i][column]), None)
        if pivot is None:
            continue
        work[result], work[pivot] = work[pivot], work[result]
        inverse = pow(work[result][column], prime - 2, prime)
        work[result] = [entry * inverse % prime for entry in work[result]]
        for i in range(result + 1, len(work)):
            if work[i][column]:
                scale = work[i][column]
                work[i] = [(x - scale * y) % prime for x, y in zip(work[i], work[result])]
        result += 1
    return result


def main():
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    prime = int(payload["prime"])
    entries = {(item["axis"], item["row"], item["col"]): item for item in payload["entries"]}

    def connection(axis, u, v):
        matrix = []
        for row in range(4):
            values = []
            for column in range(4):
                fit = entries[(axis, row, column)]["fit"]
                numerator = evaluate(fit["numerator"], u, v, prime)
                denominator = evaluate(fit["denominator"], u, v, prime)
                assert denominator
                values.append(numerator * pow(denominator, prime - 2, prime) % prime)
            matrix.append(values)
        return matrix

    samples = [(3, 5), (5, 8), (7, 11)]
    equations = []
    incremental = []
    for u, v in samples:
        for axis in ("u", "v"):
            matrix = connection(axis, u, v)
            # Constant S must satisfy A^T S + S A = 0.
            for i in range(4):
                for j in range(4):
                    equations.append([
                        ((matrix[a][i] if b == j else 0) + (matrix[b][j] if a == i else 0)) % prime
                        for a in range(4) for b in range(4)
                    ])
            current_rank = rank(equations, prime)
            incremental.append({"point": [u, v], "axis": axis, "equation_count": len(equations), "rank": current_rank, "nullity": 16 - current_rank})

    final_rank = rank(equations, prime)
    assert final_rank == 16
    result = {
        "schema": "marici.nima.gysin_constant_pairing_audit.v1",
        "prime": prime,
        "connection_source": str(INPUT.relative_to(ROOT)).replace("\\", "/"),
        "unknown_matrix_dimension": 16,
        "sample_points": [list(point) for point in samples],
        "equation_count": len(equations),
        "final_rank": final_rank,
        "constant_pairing_nullity": 16 - final_rank,
        "nonzero_constant_horizontal_bilinear_form_exists": False,
        "incremental_ranks": incremental,
        "scope": "Rules out constant bilinear forms in the serialized adapted frame; does not rule out rationally varying, twisted, or Betti/integral pairings.",
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in ("equation_count", "final_rank", "constant_pairing_nullity", "nonzero_constant_horizontal_bilinear_form_exists")}, sort_keys=True))


if __name__ == "__main__":
    main()
