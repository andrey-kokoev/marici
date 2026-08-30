from itertools import combinations
import json
from pathlib import Path


def subsets(n):
    out = []
    universe = tuple(range(n))
    for k in range(n + 1):
        out.extend(combinations(universe, k))
    return out


def complement(subset, n):
    chosen = set(subset)
    return tuple(i for i in range(n) if i not in chosen)


def parity(subset):
    return len(subset) % 2


rank_three = subsets(3)
even_three = [s for s in rank_three if parity(s) == 0]
odd_three = [s for s in rank_three if parity(s) == 1]
assert len(even_three) == 4
assert len(odd_three) == 4
assert all(parity(complement(s, 3)) == 1 - parity(s) for s in rank_three)

epsilon_degree = 1
hodge_epsilon_degree = 3 - epsilon_degree
assert epsilon_degree % 2 == 1
assert hodge_epsilon_degree == 2
assert hodge_epsilon_degree % 2 == 0

rank_two = subsets(2)
assert all(parity(complement(s, 2)) == parity(s) for s in rank_two)

result = {
    "source_rank": 3,
    "hyperbolic_rank": 6,
    "even_half_spinor_dimension": len(even_three),
    "odd_half_spinor_dimension": len(odd_three),
    "charge_spinor_degree": epsilon_degree,
    "reciprocal_hodge_degree": hodge_epsilon_degree,
    "rank_three_hodge_flips_parity": True,
    "rank_two_hodge_flips_parity": False,
    "discrete_sheet_type": "C2 half-spinor parity",
    "maslov_transversality_implied": False,
    "verdict": "the two sectors have a source-derived parity distinction, but parity alone does not orient the scalar pairing",
}

out = Path(__file__).parents[1] / "results" / "rh-half-spinor-parity.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
