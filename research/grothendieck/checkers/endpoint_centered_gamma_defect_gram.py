"""Exact finite-atom audit of the endpoint-centered gamma Gram identity."""

from fractions import Fraction as F


weights = [F(2, 5), F(3, 5)]
features = {
    2: [F(1, 2), F(2, 3)],
    3: [F(1, 3), F(1, 2)],
    5: [F(1, 5), F(1, 4)],
    6: [F(1, 6), F(1, 3)],
}
assert all(features[6][i] == features[2][i] * features[3][i] for i in range(2))


def gram(m, n):
    return sum(
        weight * (1 - features[m][i]) * (1 - features[n][i])
        for i, weight in enumerate(weights)
    )


indices = [2, 3, 5]
matrix = [[gram(m, n) for n in indices] for m in indices]
minor_1 = matrix[0][0]
minor_2 = matrix[0][0] * matrix[1][1] - matrix[0][1] ** 2
determinant = (
    matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] ** 2)
    - matrix[0][1] * (matrix[0][1] * matrix[2][2] - matrix[1][2] * matrix[0][2])
    + matrix[0][2] * (matrix[0][1] * matrix[1][2] - matrix[1][1] * matrix[0][2])
)
assert minor_1 > 0 and minor_2 > 0 and determinant == 0

mixed_expansion = sum(
    weights[i] * (1 - features[2][i] - features[3][i] + features[6][i])
    for i in range(2)
)
assert mixed_expansion == gram(2, 3)

result = {
    "vectors": indices,
    "positive_atom_count": len(weights),
    "first_principal_minor": str(minor_1),
    "second_principal_minor": str(minor_2),
    "determinant": str(determinant),
    "positive_semidefinite": True,
    "mixed_2_3_gram": str(gram(2, 3)),
    "polarized_pq_term_verified": True,
    "rank_equals_atom_count": True,
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "endpoint-centered-gamma-defect-gram.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
