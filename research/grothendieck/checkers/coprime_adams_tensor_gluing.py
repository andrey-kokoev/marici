"""Exact rational audit of the first coprime-prime tensor rectangle."""

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


r = F(1, 2)
s = F(-2, 3)
gp = [[F(1), r], [r, F(1)]]
gq = [[F(1), s], [s, F(1)]]
rectangle = [[gp[i // 2][j // 2] * gq[i % 2][j % 2] for j in range(4)] for i in range(4)]
expected = (1 - r * r) ** 2 * (1 - s * s) ** 2
assert determinant(rectangle) == expected > 0

result = {
    "rectangle_kernel": "G_p tensor G_q",
    "rectangle_determinant": str(expected),
    "exact_coprime_tensor_interchange_implies_positivity": True,
    "Euler_additivity_alone_implies_Weil_tensor_factorization": False,
    "first_mixed_gate": "compare direct pq edge with p-then-q and q-then-p routes",
    "rh_not_proved": True,
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "coprime-adams-tensor-gluing.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")

