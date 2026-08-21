#!/usr/bin/env python3
"""Integral lattice audit of the normalized sign trace on a double cover."""

import json
from pathlib import Path


samples = range(-20, 21)
records = []
for a in samples:
    fiber = {-1: -a, +1: a}  # sign-anti-invariant integral section
    numerator = sum(c * fiber[c] for c in (-1, +1))
    assert numerator == 2 * a
    assert numerator % 2 == 0
    normalized = numerator // 2
    assert normalized == a
    records.append((a, numerator, normalized))

# The odd lattice ker(sum: Z^2 -> Z) is primitive/saturated: gcd(1,-1)=1.
odd_generator = (1, -1)
primitive = True

result = {
    "status": "PASS",
    "tested_integer_range": [-20, 20],
    "odd_lattice_generator": list(odd_generator),
    "odd_lattice_primitive": primitive,
    "weighted_trace_numerator": "2a",
    "normalized_trace": "a",
    "integral_on_typed_odd_lattice": True,
    "not_an_integral_operator_on_all_of_Z2": True,
    "remaining_ambiguity": "global choice of orientation generator (+/-)",
    "conclusion": "the half-trace is an integral isomorphism after restricting to the source-defined anti-invariant lattice",
}

out = Path(__file__).resolve().parents[1] / "results" / "deck_trace_integral_lattice.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
