#!/usr/bin/env python3
"""Exact five-point factorization in the universal localized kinematic ring."""
import json
from fractions import Fraction
from pathlib import Path

N = 5
ZERO = (0,) * N
triangulation_pairs = [(0, 1), (0, 4), (1, 2), (2, 3), (3, 4)]


def monomial(*negative_indices):
    exponent = [0] * N
    for index in negative_indices:
        exponent[index] -= 1
    return tuple(exponent)


def evaluate(poly, point):
    total = Fraction(0)
    for exponent, coefficient in poly.items():
        term = coefficient
        for value, power in zip(point, exponent):
            term *= Fraction(value) ** power
        total += term
    return total


def coefficient_residue(poly, channel):
    out = {}
    for exponent, coefficient in poly.items():
        if exponent[channel] == -1:
            residual = list(exponent)
            residual[channel] = 0
            residual = tuple(residual)
            out[residual] = out.get(residual, Fraction(0)) + coefficient
    return out


amplitude = {monomial(i, j): Fraction(1) for i, j in triangulation_pairs}
assert len(amplitude) == 5
factorizations = []
for channel in range(N):
    expected = {
        monomial((channel - 1) % N): Fraction(1),
        monomial((channel + 1) % N): Fraction(1),
    }
    actual = coefficient_residue(amplitude, channel)
    assert actual == expected
    factorizations.append({
        "channel": channel,
        "residual_channels": [(channel - 1) % N, (channel + 1) % N],
        "identity": f"Coeff[a{channel}^-1](m5)=a{(channel - 1) % N}^-1+a{(channel + 1) % N}^-1",
    })

lorentzian_point = [-3, -3, -2, -2, 2]
amplitude_value = evaluate(amplitude, lorentzian_point)
specialized_residues = []
for channel in range(N):
    universal_residue = coefficient_residue(amplitude, channel)
    specialized = evaluate(universal_residue, lorentzian_point)
    expected = Fraction(1, lorentzian_point[(channel - 1) % N]) + Fraction(1, lorentzian_point[(channel + 1) % N])
    assert specialized == expected
    specialized_residues.append(str(specialized))

result = {
    "schema": "marici.fact5-kinematic-factorization.v1",
    "status": "passed",
    "strength": "identity in the universal five-point Laurent coordinate ring plus one Lorentzian specialization; not an analytic residue, normalized amplitude, or pole prescription",
    "coordinate_ring": "Q[a0^±1,...,a4^±1]",
    "universal_weighted_sum_terms": len(amplitude),
    "coefficient_factorizations": factorizations,
    "lorentzian_specialization": {
        "point": lorentzian_point,
        "weighted_sum_value": str(amplitude_value),
        "coefficient_residue_values": specialized_residues,
        "all_specialization_squares_commute": True,
    },
    "boundary": "Coeff[a_i^-1] is formal Laurent coefficient extraction; an analytic residue requires a declared local coordinate and differential normalization",
}
out = Path("research/nima/results/fact5_kinematic_factorization.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
