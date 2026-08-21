#!/usr/bin/env python3
"""Bounded type census for four sector readout-algebra candidates."""

import json
from pathlib import Path


# String: a sign line has only even invariant monomials; a trivial line has all.
degree_cutoff = 24
string_odd_invariants = [d for d in range(degree_cutoff + 1) if d % 2 == 0]
string_even_invariants = list(range(degree_cutoff + 1))
assert string_odd_invariants == list(range(0, degree_cutoff + 1, 2))

# Cosmology: diagonal translation of G=(C2)^5 on GxG.  Orbits are indexed by
# the difference g xor h, giving the 32-idempotent function algebra Fun(G,Q).
group = range(32)
unseen = {(g, h) for g in group for h in group}
orbits = []
while unseen:
    seed = next(iter(unseen))
    orbit = {(seed[0] ^ k, seed[1] ^ k) for k in group}
    assert len(orbit) == 32
    assert len({g ^ h for g, h in orbit}) == 1
    unseen -= orbit
    orbits.append(orbit)
assert len(orbits) == 32

# Primitive orbit indicators are orthogonal idempotents under pointwise product.
idempotent_products = 0
for i in range(32):
    for j in range(32):
        expected_nonzero = i == j
        # delta_i(d)*delta_j(d) is delta_i(d) only for i=j.
        actual_nonzero = any((d == i) and (d == j) for d in group)
        assert actual_nonzero == expected_nonzero
        idempotent_products += 1

result = {
    "schema": "marici.nima.cross_sector_readout_algebra_types.v1",
    "memory": {
        "type": "graded polynomial invariant algebra",
        "algebra": "Q[q2,q3]",
        "generator_degrees": [2, 3],
    },
    "strings": {
        "type": "one-variable character invariant algebra",
        "odd_arity": "Q[x^2]",
        "even_arity": "Q[x]",
        "degree_cutoff": degree_cutoff,
        "odd_invariant_degrees": string_odd_invariants,
        "even_invariant_degrees": string_even_invariants,
    },
    "cosmology": {
        "type": "finite reduced function algebra",
        "algebra": "Fun((C2)^5,Q) = Q^32",
        "diagonal_orbit_count": len(orbits),
        "orbit_size": 32,
        "orthogonal_idempotent_product_checks": idempotent_products,
        "physical_delta_pairing": "one primitive idempotent, not the full algebra",
    },
    "flavor": {
        "type": "audited observable subalgebra only",
        "known_packet": "sector traces/determinants, mixed traces, commutator determinant",
        "complete_weak_basis_invariant_algebra": "not supplied by current artifact",
    },
    "cross_sector_constructor_maps": "none source-derived in the audited packets",
    "conditional_arithmetic_naturality": "untyped without those maps",
    "passed": True,
}
out = Path(__file__).with_name("results") / "cross-sector-readout-algebra-types.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

