"""Exact rational audit of the mixed-prime rectangle parity splitting."""

from fractions import Fraction as F


def determinant(matrix):
    a = [row[:] for row in matrix]
    out = F(1)
    for j in range(len(a)):
        pivot = next(i for i in range(j, len(a)) if a[i][j])
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            out = -out
        value = a[j][j]
        out *= value
        for i in range(j + 1, len(a)):
            ratio = a[i][j] / value
            for k in range(j, len(a)):
                a[i][k] -= ratio * a[j][k]
    return out


def rectangle(r, s, c, d):
    return [[1, r, s, c], [r, 1, d, s], [s, d, 1, r], [c, s, r, 1]]


r, s = F(1, 2), F(-2, 3)
c = d = r * s
plus = (1 + c) * (1 + d) - (r + s) ** 2
minus = (1 - c) * (1 - d) - (r - s) ** 2
assert plus == minus == (1 - r * r) * (1 - s * s)
assert determinant(rectangle(r, s, c, d)) == plus * minus

# Every individual edge contracts, but route holonomy can still kill a parity block.
r = s = F(1, 2)
c, d = F(9, 10), F(-9, 10)
plus = (1 + c) * (1 + d) - (r + s) ** 2
assert all(abs(x) <= 1 for x in (r, s, c, d))
assert plus < 0

result = {
    "even_parity_gate": "(1+c)(1+d) >= (r+s)^2",
    "odd_parity_gate": "(1-c)(1-d) >= (r-s)^2",
    "exact_tensor_case_recovered": True,
    "individual_edge_contractions_sufficient": False,
    "route_holonomy_detected": "(c-d)/2",
    "next_test": "completed-Weil p,q,pq rectangle on one short-support basis",
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "mixed-prime-rectangle-parity.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")

