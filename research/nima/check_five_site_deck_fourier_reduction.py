#!/usr/bin/env python3
"""Exact character bookkeeping for the deck-saturated five-site complex."""

import json
from itertools import combinations
from pathlib import Path


def multiplicities(generic: bool) -> dict[int, int]:
    # The saturated divisor permutation module contains only weights 0, 1, 2.
    if generic:
        return {0: 26, 1: 9, 2: 2, 3: 0, 4: 0, 5: 0}
    return {0: 15, 1: 4, 2: 1, 3: 0, 4: 0, 5: 0}


def dimension(mult: dict[int, int]) -> int:
    return sum(len(list(combinations(range(5), w))) * m for w, m in mult.items())


generic = multiplicities(True)
special = multiplicities(False)
kernel = {w: generic[w] - special[w] for w in range(6)}

assert dimension(generic) == 91
assert dimension(special) == 45
assert dimension(kernel) == 46
assert kernel == {0: 11, 1: 5, 2: 1, 3: 0, 4: 0, 5: 0}

# Removing the total-energy carrier line leaves the rank-45 Rees attachment.
rees = dict(kernel)
rees[0] -= 1
assert dimension(rees) == 45
assert rees == {0: 10, 1: 5, 2: 1, 3: 0, 4: 0, 5: 0}

out = {
    "schema": "marici.five_site.deck_fourier_reduction.v1",
    "deck_group": "C2^5",
    "character_blocks": 32,
    "generic_divisor_character_multiplicity_by_weight": generic,
    "special_divisor_character_multiplicity_by_weight": special,
    "specialization_kernel_character_multiplicity_by_weight": kernel,
    "rees_attachment_after_carrier_removal_by_weight": rees,
    "generic_divisor_rank": dimension(generic),
    "special_divisor_rank": dimension(special),
    "rees_attachment_rank": dimension(rees),
    "higher_weight_divisor_generators": 0,
    "passed": True,
}

target = Path(__file__).with_name("results") / "five-site-deck-fourier-reduction.json"
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out, sort_keys=True))
