#!/usr/bin/env python3
"""Exact five-point census of coherence and observational kernel pairs."""
import importlib.util
import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

helper_path = Path(__file__).with_name("check_generic_polygon_face_product.py")
spec = importlib.util.spec_from_file_location("polygon_faces", helper_path)
poly = importlib.util.module_from_spec(spec)
spec.loader.exec_module(poly)


def diagonal_key(d):
    return tuple(d)


def presentation_routes():
    triangulations = sorted(
        (tuple(sorted(t, key=diagonal_key)) for t in poly.dissections_on(poly.diagonals(5)) if len(t) == 2),
        key=repr,
    )
    routes = []
    for triangulation_index, triangulation in enumerate(triangulations):
        denotation = tuple(diagonal_key(d) for d in triangulation)
        routes.append((f"T{triangulation_index}:global", denotation))
        for diagonal in triangulation:
            routes.append((f"T{triangulation_index}:regional:{diagonal_key(diagonal)}", denotation))
        for order in itertools.permutations(triangulation):
            routes.append((f"T{triangulation_index}:nested:{tuple(map(diagonal_key, order))}", denotation))
    return triangulations, routes


def kernel_pair_count(values):
    multiplicities = Counter(values)
    return sum(size * size for size in multiplicities.values())


triangulations, routes = presentation_routes()
assert len(triangulations) == 5
assert len(routes) == 25

denotations = [denotation for _, denotation in routes]
coherence_pairs = kernel_pair_count(denotations)
assert coherence_pairs == 125

constant_values = [Fraction(1) for _ in routes]
constant_pairs = kernel_pair_count(constant_values)
constant_residual = constant_pairs - coherence_pairs
assert constant_pairs == 625
assert constant_residual == 500  # deliberate nonfaithful-probe witness

all_diagonals = sorted(poly.diagonals(5), key=diagonal_key)
primes = [2, 3, 5, 7, 11]
assert len(all_diagonals) == len(primes)
prime_for = dict(zip(map(diagonal_key, all_diagonals), primes))
prime_values = [
    Fraction(1, prime_for[a] * prime_for[b])
    for a, b in denotations
]
prime_pairs = kernel_pair_count(prime_values)
assert prime_pairs == coherence_pairs

# Source-typing witness for the weak EvenMomentumReadout interface. Work in Z^4
# with four basis momenta and the fifth fixed by conservation.
basis = [tuple(1 if i == j else 0 for i in range(4)) for j in range(4)]
momenta = basis + [tuple(-1 for _ in range(4))]
assert tuple(sum(v[i] for v in momenta) for i in range(4)) == (0, 0, 0, 0)

def add_vectors(vectors):
    return tuple(sum(v[i] for v in vectors) for i in range(4))

channel_vectors = {
    diagonal_key(d): add_vectors(momenta[d[0]:d[1]])
    for d in all_diagonals
}
for a, b in itertools.combinations(channel_vectors.values(), 2):
    assert a != b and a != tuple(-x for x in b)

even_readout = {}
for diagonal, prime in prime_for.items():
    vector = channel_vectors[diagonal]
    even_readout[vector] = prime
    even_readout[tuple(-x for x in vector)] = prime
assert all(value != 0 for value in even_readout.values())
assert [even_readout[channel_vectors[d]] for d in map(diagonal_key, all_diagonals)] == primes

result = {
    "schema": "marici.fact5-presentation-kernel-pairs.v1",
    "status": "passed",
    "strength": "finite five-point route census; not global joint faithfulness or physical realization",
    "presentation_routes": len(routes),
    "laurent_denotations": len(set(denotations)),
    "routes_per_denotation": dict(sorted(Counter(map(repr, denotations)).items())),
    "kernel_pairs": {
        "coherence_q0": coherence_pairs,
        "constant_one_probe": constant_pairs,
        "constant_one_residual": constant_residual,
        "distinct_prime_probe": prime_pairs,
        "distinct_prime_residual": prime_pairs - coherence_pairs,
    },
    "probe_boundary": {
        "constant_one": "admissible algebraic evaluation and deliberate failure of finite detection",
        "distinct_prime": "exact separating assignment on this finite image",
    },
    "source_realization": {
        "momentum_group": "Z^4",
        "momenta": momenta,
        "conservation_checked": True,
        "channel_vectors_distinct_modulo_sign": True,
        "even_readout_values": {repr(k): v for k, v in sorted(even_readout.items())},
        "all_channel_values_units_in_Q": True,
        "scope": "inhabits the current unconstrained EvenMomentumReadout interface; no quadratic, additive, normalization, or physical provenance law",
    },
}
out = Path("research/nima/results/fact5_presentation_kernel_pairs.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
