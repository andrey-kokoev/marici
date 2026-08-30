"""Exact discrete latent-scale witness for squarefree Walsh positivity."""

from fractions import Fraction as F
from itertools import product


primes = [2, 3, 5]
# A rational two-atom surrogate for a normalized positive log-time measure.
atoms = [(F(1, 3), F(2, 5)), (F(2, 3), F(3, 5))]
D = F(1)
vertices = list(product((0, 1), repeat=len(primes)))


def feature(prime, atom_index):
    # Rational contractions standing in for p^(-u).
    table = [
        [F(1, 2), F(1, 3), F(1, 5)],
        [F(2, 3), F(1, 2), F(1, 4)],
    ]
    return table[atom_index][primes.index(prime)]


def correlation(subset):
    total = F(0)
    for atom_index, (weight, _label) in enumerate(atoms):
        value = F(1)
        for index, bit in enumerate(subset):
            if bit:
                value *= feature(primes[index], atom_index)
        total += weight * value
    return D * total


def dot_mod_two(x, y):
    return sum(a * b for a, b in zip(x, y)) % 2


walsh = {
    eta: sum(correlation(x) * (-1) ** dot_mod_two(eta, x) for x in vertices)
    for eta in vertices
}
factorized = {}
for eta in vertices:
    value = F(0)
    for atom_index, (weight, _label) in enumerate(atoms):
        term = D * weight
        for index, bit in enumerate(eta):
            term *= 1 + (-1) ** bit * feature(primes[index], atom_index)
        value += term
    factorized[eta] = value

assert walsh == factorized
assert min(walsh.values()) > 0

single_2 = correlation((1, 0, 0))
single_3 = correlation((0, 1, 0))
mixed_6 = correlation((1, 1, 0))
assert mixed_6 != single_2 * single_3 / D

result = {
    "prime_count": len(primes),
    "latent_atom_count": len(atoms),
    "walsh_factorization_verified": True,
    "minimum_eigenvalue": str(min(walsh.values())),
    "all_eigenvalues_positive": True,
    "mixed_latent_correlation": str(mixed_6),
    "independent_product_correlation": str(single_2 * single_3 / D),
    "shared_latent_scale_is_not_independent_product": True,
    "mixed_term_is_continuous_sector_not_Lambda_6": True,
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "latent-log-time-squarefree-completion.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
