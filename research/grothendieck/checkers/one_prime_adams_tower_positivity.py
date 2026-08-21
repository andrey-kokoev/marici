"""Exact rational determinant audit for geometric one-prime Gram towers."""

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


for r in (F(1, 2), F(-2, 3), F(3, 4)):
    for n in range(1, 9):
        gram = [[r ** abs(i - j) for j in range(n + 1)] for i in range(n + 1)]
        assert determinant(gram) == (1 - r * r) ** n

result = {
    "geometric_tower_kernel": "G(i,j)=r^|i-j|",
    "determinant": "(1-r^2)^n for an (n+1)-cell tower",
    "edge_contraction_plus_exact_composition_implies_all_length_positivity": True,
    "tested_exact_sizes_through": 9,
    "first_nongeometric_gate": "successive Schur/Verblunsky defect contractions",
    "mixed_prime_cycles_closed": False,
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "one-prime-adams-tower-positivity.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")

