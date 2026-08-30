"""Exact rational example: all two-cell contractions pass, triangle fails."""

from fractions import Fraction as F


r = F(-3, 4)
pair_minor = 1 - r * r
triangle_determinant = (1 - r) ** 2 * (1 + 2 * r)
eigenvalues = [1 - r, 1 - r, 1 + 2 * r]

assert pair_minor == F(7, 16) > 0
assert eigenvalues == [F(7, 4), F(7, 4), F(-1, 2)]
assert triangle_determinant == F(-49, 32) < 0

result = {
    "edge_magnitude": "3/4",
    "every_two_by_two_minor": "7/16 > 0",
    "triangle_eigenvalues": ["7/4", "7/4", "-1/2"],
    "triangle_determinant": "-49/32",
    "pairwise_contractions_sufficient": False,
    "next_coherence_gate": "0, log(p), 2log(p) Adams/Mackey triangle",
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "edgewise-contraction-triangle-no-go.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")

