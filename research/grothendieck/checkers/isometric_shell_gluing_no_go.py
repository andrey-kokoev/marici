"""Exact finite audit of the isometric shell-gluing degeneracy."""

from fractions import Fraction as F


# Two normalized shell vectors embedded into four resolved prime rays.
W = [
    [F(3, 5), F(0)],
    [F(4, 5), F(0)],
    [F(0), F(5, 13)],
    [F(0), F(12, 13)],
]


def gram(matrix):
    columns = list(zip(*matrix))
    return [[sum(x * y for x, y in zip(a, b)) for b in columns] for a in columns]


assert gram(W) == [[F(1), F(0)], [F(0), F(1)]]

# Exact signed permutations model finite unitary/orthogonal height transport;
# left/right orthogonal dressing preserves the Gram matrix.
left_dressed = [W[1], [-x for x in W[0]], W[3], [-x for x in W[2]]]
assert gram(left_dressed) == [[F(1), F(0)], [F(0), F(1)]]

result = {
    "weighted_shell_embedding_isometric": True,
    "orthogonal_height_dressing_preserves_isometry": True,
    "gluing_gram": "I",
    "det_I_minus_gluing_gram": "0 identically",
    "spectral_defect_required": True,
    "required_location": "two-channel continuation or supported boundary defect before normalization",
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "isometric-shell-gluing-no-go.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")

