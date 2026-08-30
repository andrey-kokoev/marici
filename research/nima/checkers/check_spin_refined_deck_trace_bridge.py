#!/usr/bin/env python3
"""Unique deck-character trace from scaffold polarity to helicity parity."""

import json
from fractions import Fraction
from pathlib import Path


signs = (-1, 1)
roads = (0, 1, 2)
amplitudes = (2, -5, 3)

# Carrier-polarity-odd input f(c,k)=c*a_k.
carrier = {(c, k): c * amplitudes[k] for c in signs for k in roads}


def bridge(alpha, beta):
    # Normalized pushforward over scaffold deck c; p labels spin branch.
    return {
        (p, k): sum(Fraction((c**alpha) * (p**beta) * carrier[(c, k)], 2) for c in signs)
        for p in signs for k in roads
    }


def parity_character(output):
    if all(output[(-p, k)] == output[(p, k)] for p in signs for k in roads):
        return +1
    if all(output[(-p, k)] == -output[(p, k)] for p in signs for k in roads):
        return -1
    return None


audits = {}
working = []
for alpha in (0, 1):
    for beta in (0, 1):
        output = bridge(alpha, beta)
        nonzero = any(value != 0 for value in output.values())
        pchar = parity_character(output)
        key = f"chi_c^{alpha}_chi_p^{beta}"
        audits[key] = {"nonzero": nonzero, "parity_character": pchar}
        if nonzero and pchar == -1:
            working.append(key)

assert working == ["chi_c^1_chi_p^1"]
selected = bridge(1, 1)
assert all(selected[(p, k)] == p * amplitudes[k] for p in signs for k in roads)

result = {
    "status": "PASS",
    "input_character": "scaffold deck odd",
    "audits": audits,
    "unique_nonzero_parity_odd_trace": working[0],
    "formula": "B(f)(p,k) = (1/2) sum_c c*p*f(c,k)",
    "output": {f"{p}:{k}": int(selected[(p, k)]) for p in signs for k in roads},
    "conclusion": "the product deck character chi_scaffold*chi_spin uniquely couples Carrier polarity to helicity parity",
}

out = Path(__file__).resolve().parents[1] / "results" / "spin_refined_deck_trace_bridge.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
