#!/usr/bin/env python3
"""Exact variance audit for identity selections under cyclic deck maps."""

import json
import math
from pathlib import Path


MAX_MODULUS = 20
homomorphism_count = 0
selection_pullback_checks = 0
multiplication_naturality_checks = 0
injective_count = 0
noninjective_count = 0

for source_order in range(2, MAX_MODULUS + 1):
    for target_order in range(2, MAX_MODULUS + 1):
        # A homomorphism C_m -> C_k is determined by phi(1)=a subject to m*a=0 mod k.
        for a in range(target_order):
            if (source_order * a) % target_order:
                continue
            homomorphism_count += 1
            images = [((a * x) % target_order) for x in range(source_order)]
            kernel = [x for x, image in enumerate(images) if image == 0]
            injective = len(kernel) == 1
            if injective:
                injective_count += 1
            else:
                noninjective_count += 1

            # phi^* delta_0,target equals delta_0,source exactly for monomorphisms.
            pullback = [int(image == 0) for image in images]
            source_delta = [int(x == 0) for x in range(source_order)]
            assert (pullback == source_delta) == injective
            selection_pullback_checks += source_order

            # Every group homomorphism commutes with [n].
            for n in range(1, 31):
                for x in range(source_order):
                    lhs = (a * ((n * x) % source_order)) % target_order
                    rhs = (n * ((a * x) % target_order)) % target_order
                    assert lhs == rhs
                    multiplication_naturality_checks += 1

result = {
    "schema": "marici.nima.deck_selection_variance.v1",
    "cyclic_orders": [2, MAX_MODULUS],
    "homomorphism_count": homomorphism_count,
    "injective_count": injective_count,
    "noninjective_count": noninjective_count,
    "selection_pullback_checks": selection_pullback_checks,
    "multiplication_naturality_checks": multiplication_naturality_checks,
    "theorem": "phi^* delta_0,H = delta_0,G iff phi:G->H is injective",
    "multiplication_maps_natural_for_all_homomorphisms": True,
    "noninjective_map_requirement": "pushforward/trace/Gysin data; naive pullback changes physical selection",
    "passed": True,
}
out = Path(__file__).with_name("results") / "deck-selection-variance.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

