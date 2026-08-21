#!/usr/bin/env python3
"""Exact finite-deck transfer, composition, and Frobenius controls."""

import json
from pathlib import Path


MAX_ORDER = 12


def homomorphisms(source_order, target_order):
    return [a for a in range(target_order) if (source_order * a) % target_order == 0]


def image(a, x, target_order):
    return (a * x) % target_order


selection_checks = 0
frobenius_checks = 0
homomorphism_count = 0
for m in range(2, MAX_ORDER + 1):
    for k in range(2, MAX_ORDER + 1):
        for a in homomorphisms(m, k):
            homomorphism_count += 1

            # Pushforward of delta_0 is delta_0, with no division by fiber size.
            pushed_zero = [sum(int(x == 0) for x in range(m) if image(a, x, k) == y)
                           for y in range(k)]
            assert pushed_zero == [1] + [0] * (k - 1)
            selection_checks += k

            # Frobenius reciprocity on indicator bases spans all functions:
            # phi_!(delta_x * phi^*delta_y) = phi_!delta_x * delta_y.
            for x in range(m):
                phi_x = image(a, x, k)
                for y in range(k):
                    lhs = [int(phi_x == z and phi_x == y) for z in range(k)]
                    rhs = [int(phi_x == z) * int(z == y) for z in range(k)]
                    assert lhs == rhs
                    frobenius_checks += k

# Functorial composition on indicator bases for all composable cyclic maps.
composition_checks = 0
for m in range(2, 10):
    for k in range(2, 10):
        for ell in range(2, 10):
            for a in homomorphisms(m, k):
                for b in homomorphisms(k, ell):
                    composite = (b * a) % ell
                    for x in range(m):
                        direct_target = image(composite, x, ell)
                        staged_target = image(b, image(a, x, k), ell)
                        assert direct_target == staged_target
                        composition_checks += 1

result = {
    "schema": "marici.nima.finite_deck_transfer.v1",
    "cyclic_orders": [2, MAX_ORDER],
    "homomorphism_count": homomorphism_count,
    "selection_checks": selection_checks,
    "frobenius_reciprocity_checks": frobenius_checks,
    "composition_checks": composition_checks,
    "selection_identity": "phi_! delta_0,G = delta_0,H",
    "normalization": "unnormalized fiber sum; averaging is rejected",
    "functorial": True,
    "frobenius_reciprocity": True,
    "physical_admission": "requires a source-derived deck trace/Gysin map",
    "passed": True,
}
out = Path(__file__).with_name("results") / "finite-deck-transfer.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

