from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/nima/results/six-point-nmhv-canonical-form.json"
Z = {i: [Fraction(1), Fraction(i), Fraction(i**2), Fraction(i**3), Fraction(i**4)] for i in range(1, 7)}
LEFT = [(1,2,3,4,5), (1,2,3,5,6), (1,3,4,5,6)]
RIGHT = [(1,2,3,4,6), (1,2,4,5,6), (2,3,4,5,6)]
PROBES = [[Fraction(1), Fraction(a), Fraction(a*a+1), Fraction(a**3+2), Fraction(a**4+3)] for a in range(7, 13)]


def det(columns):
    matrix = [list(row) for row in zip(*columns)]
    out = Fraction(1)
    for col in range(len(matrix)):
        pivot = next((r for r in range(col, len(matrix)) if matrix[r][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
            out = -out
        p = matrix[col][col]
        out *= p
        for j in range(col, len(matrix)):
            matrix[col][j] /= p
        for r in range(col + 1, len(matrix)):
            q = matrix[r][col]
            for j in range(col, len(matrix)):
                matrix[r][j] -= q * matrix[col][j]
    return out


def simplex_form(vertices, y):
    a, b, c, d, e = vertices
    numerator = det([Z[a], Z[b], Z[c], Z[d], Z[e]]) ** 4
    facets = [(a,b,c,d), (b,c,d,e), (c,d,e,a), (d,e,a,b), (e,a,b,c)]
    denominator = Fraction(1)
    for facet in facets:
        denominator *= det([y] + [Z[i] for i in facet])
    if denominator == 0:
        raise ValueError("probe lies on a simplex facet")
    return numerator / denominator


def encode(q):
    return {"numerator": str(q.numerator), "denominator": str(q.denominator)}


def main():
    positivity = {"".join(map(str, v)): det([Z[i] for i in v]) for v in combinations(range(1, 7), 5)}
    probes = []
    for y in PROBES:
        left = sum((simplex_form(v, y) for v in LEFT), Fraction(0))
        right = sum((simplex_form(v, y) for v in RIGHT), Fraction(0))
        mutated = -simplex_form(LEFT[0], y) + sum((simplex_form(v, y) for v in LEFT[1:]), Fraction(0))
        probes.append({"Y": [str(x) for x in y], "residual": encode(left-right), "mutation_residual": encode(mutated-right)})
    equality = all(p["residual"]["numerator"] == "0" for p in probes)
    mutation = all(p["mutation_residual"]["numerator"] != "0" for p in probes)
    positive = all(v > 0 for v in positivity.values())
    result = {
        "schema": "marici.nima.six_point_nmhv_canonical_form.result.v1",
        "status": "passed" if equality and mutation and positive else "failed",
        "moment_curve_Z": {str(i): [str(x) for x in Z[i]] for i in Z},
        "ordered_five_brackets": {k: str(v) for k, v in positivity.items()},
        "all_ordered_five_brackets_positive": positive,
        "probe_count": len(probes),
        "all_exact_probe_residuals_zero": equality,
        "all_orientation_mutation_residuals_nonzero": mutation,
        "probes": probes,
        "claim_boundary": "Exact rational evaluation at six declared Y probes for one explicit positive moment-curve Z. Finite probes can falsify but cannot prove rational-form identity. The supersymmetric numerator, primary-source normalization, and physical boundary dictionary remain unverified."
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    if result["status"] != "passed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
