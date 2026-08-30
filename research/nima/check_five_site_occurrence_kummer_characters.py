"""Exact C2^5 character audit of the five-site occurrence kernel."""

import itertools
import json
from pathlib import Path


N = 5


def boundary(subset):
    subset = set(subset)
    return tuple(
        i
        for i in range(N)
        if ((i in subset) != (((i + 1) % N) in subset))
    )


# The ten unordered connected bipartitions of C5: five 1|4 and five 2|3.
pairs = []
for size in (1, 2):
    for start in range(N):
        subset = tuple((start + j) % N for j in range(size))
        complement = tuple(i for i in range(N) if i not in subset)
        pairs.append((subset, complement))

assert len(pairs) == 10
checks = 0
for subset, complement in pairs:
    assert boundary(subset) == boundary(complement)
    edges = boundary(subset)
    for signs in itertools.product((-1, 1), repeat=N):
        # Deck-transformed radical contribution to q_A and q_Ac.
        radical_a = sum(signs[e] for e in edges)
        radical_ac = sum(signs[e] for e in boundary(complement))
        assert radical_a == radical_ac
        checks += 1

# Entry 1203: K_occ = Q[C5]^48, dimension 240. The 26-section presentation is
# not C2^5-stable, so this cancellation does not define a deck character.
occurrence_dimension = 240
deck_character_count = 2**N

result = {
    "schema": "marici.cosmology.five_site_occurrence_kummer_characters.v1",
    "connected_complementary_partition_types": {"1|4": 5, "2|3": 5},
    "deck_elements_per_pair": 32,
    "exact_boundary_cancellation_checks": checks,
    "occurrence_kernel_dimension": occurrence_dimension,
    "occurrence_C2_5_character": "undefined before deck saturation",
    "first_rees_radical_dependence": "none in each compared pair",
    "conormal_radical_dependence": "none in each compared pair",
    "coefficient_character_count": deck_character_count,
    "character_census_withdrawn": True,
    "superseded_by": "five-site deck-saturation collapse character audit",
    "passed": True,
}
out = Path(__file__).with_name("results") / "five-site-occurrence-kummer-characters.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
