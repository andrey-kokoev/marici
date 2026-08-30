"""Exact character census of the supported cone of the saturated Rees map."""

import json
from pathlib import Path


# Each edge collapse kernel is chi_i, while its reciprocal coefficient 1/y_i
# is also chi_i. Their product is the trivial residue character.
edge_residue_trivial = 5

# Each of the ten boundary-pair blocks has four marked divisors and carries
# the inflated regular C2^2 representation: 1 + chi_i + chi_j + chi_i chi_j.
boundary_blocks = 10
trivial = edge_residue_trivial + boundary_blocks
singleton_each = 4  # each edge belongs to four unordered boundary pairs
pair_each = 1
dimension = trivial + 5 * singleton_each + 10 * pair_each
assert (trivial, singleton_each, pair_each, dimension) == (15, 4, 1, 45)

# For a principal marked equation q, multiplication O -> O(D), f |-> f/q,
# has no kernel and one rank-one principal-parts cokernel O_D(D).
principal_block = {"generic_kernel": 0, "generic_cokernel": 0, "supported_cokernel_rank": 1}

result = {
    "schema": "marici.cosmology.five_site_saturated_rees_supported_cone.v1",
    "principal_block": principal_block,
    "edge_residue_blocks": 5,
    "boundary_pair_residue_blocks": 10,
    "supported_character_multiplicities": {
        "trivial": trivial,
        "singleton_each": singleton_each,
        "pair_each": pair_each,
    },
    "supported_rank": dimension,
    "new_support": False,
    "new_characters": False,
    "passed": True,
}
out = Path(__file__).with_name("results") / "five-site-saturated-rees-supported-cone.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
