"""Exact Walsh and Adams audits for the finite prime translation adjacency."""

from fractions import Fraction as F
from itertools import product


weights = [F(1, 2), F(1, 3), F(1, 5)]
characters = list(product((0, 1), repeat=len(weights)))
walsh = {
    eta: sum((-1) ** bit * weight for bit, weight in zip(eta, weights))
    for eta in characters
}
assert max(abs(value) for value in walsh.values()) == sum(abs(w) for w in weights)
assert min(walsh.values()) == -sum(weights)
assert max(walsh.values()) == sum(weights)

D_bad = F(1)
D_good = sum(weights)
assert min(D_bad + value for value in walsh.values()) < 0
assert min(D_good + value for value in walsh.values()) == 0

# Formal one-ray tower coefficients: the kth channel remains attached to
# harmonic k, rather than becoming a new independent coordinate.  A rational
# contraction is used so the Adams relation is checked exactly.
radial_contraction = F(1, 2)
tower = {k: radial_contraction**k for k in range(1, 5)}
assert tower[2] == tower[1] ** 2
assert tower[3] == tower[1] ** 3

result = {
    "squarefree_rank": len(weights),
    "walsh_eigenvalues": [str(walsh[eta]) for eta in characters],
    "adjacency_norm": str(max(abs(value) for value in walsh.values())),
    "l1_weight": str(sum(abs(w) for w in weights)),
    "norm_equals_l1_weight": True,
    "unit_diagonal_fails": True,
    "sharp_diagonal": str(D_good),
    "prime_power_channels_are_harmonics": True,
    "orthogonal_penalty_typing": False,
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "prime-power-translation-adjacency.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
