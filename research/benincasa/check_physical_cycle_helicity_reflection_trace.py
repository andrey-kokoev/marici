#!/usr/bin/env python3
"""Physical reflection trace of the two CM-compiled tensor helicities."""

import json
from pathlib import Path

import sympy as sp


x, y, z = sp.symbols("x y z", real=True)
p, hx, hy = sp.symbols("p hx hy", real=True)
i = sp.I

# Distances from the loop apex to three vertices of the external plane.
d0sq = x**2 + y**2 + z**2
d1sq = (x - p) ** 2 + y**2 + z**2
d2sq = (x - hx) ** 2 + (y - hy) ** 2 + z**2
distances = [d0sq, d1sq, d2sq]
for distance in distances:
    assert sp.expand(distance.subs(z, -z) - distance) == 0

H_plus = sp.expand((y + i * z) ** 2)
H_minus = sp.expand((y - i * z) ** 2)
assert sp.expand(H_plus.subs(z, -z) - H_minus) == 0
assert sp.expand(H_minus.subs(z, -z) - H_plus) == 0

trace = sp.expand(H_plus + H_minus)
anti_trace = sp.expand(H_plus - H_minus)
assert trace == 2 * (y**2 - z**2)
assert anti_trace == 4 * i * y * z
assert sp.expand(trace.subs(z, -z) - trace) == 0
assert sp.expand(anti_trace.subs(z, -z) + anti_trace) == 0

# Every polynomial distance score remains reflection-even, hence its product
# with the anti-trace remains odd.  This finite basis represents arbitrary
# monomials because the parity statement is multiplicative.
score_basis = [
    sp.Integer(1),
    d0sq,
    d1sq,
    d2sq,
    d0sq * d1sq,
    d1sq * d2sq,
    d2sq * d0sq,
    d0sq * d1sq * d2sq,
]
for score in score_basis:
    assert sp.expand(score.subs(z, -z) - score) == 0
    assert sp.expand((score * anti_trace).subs(z, -z) + score * anti_trace) == 0

# The reflection action on the labelled helicity packet and its invariant
# and anti-invariant ranks.
reflection = sp.Matrix([[0, 1], [1, 0]])
assert reflection**2 == sp.eye(2)
assert (reflection - sp.eye(2)).rank() == 1
assert (reflection + sp.eye(2)).rank() == 1

packet = {
    "schema": "marici.benincasa.physical-cycle-helicity-reflection-trace.v1",
    "status": "passed",
    "primary_cycle": {
        "source": "arXiv:2408.16386, equations (2.3)-(2.4)",
        "description": "positive Cayley-Menger pushforward of the full real loop-momentum cycle",
        "reflection": "z -> -z across the external momentum plane",
        "density_character": 1,
    },
    "helicity_action": {
        "H_plus": "maps to H_minus",
        "H_minus": "maps to H_plus",
        "matrix": [[0, 1], [1, 0]],
        "invariant_rank": 1,
        "anti_invariant_rank": 1,
    },
    "physical_trace": {
        "surviving_numerator": str(trace),
        "annihilated_numerator": str(anti_trace),
        "integrated_relation": "I_plus=I_minus",
        "generic_helicity_image_rank": 1,
    },
    "score_tower": {
        "admitted_scores": "functions of labelled distances, energies, and marked walls",
        "reflection_character": 1,
        "anti_trace_recovery": False,
        "reason": "every admitted scalar score times the anti-trace remains reflection-odd",
    },
    "classification": "source-derived physical descent/selection, not singular rank loss",
    "new_carrier_support": False,
    "scope_warning": (
        "The theorem uses the parity-even full real loop cycle. A separately "
        "derived parity-odd interaction, oriented current, or chiral boundary "
        "condition would define a different physical coefficient problem."
    ),
}

output = Path(__file__).with_name("physical-cycle-helicity-reflection-trace.json")
output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2, sort_keys=True))
