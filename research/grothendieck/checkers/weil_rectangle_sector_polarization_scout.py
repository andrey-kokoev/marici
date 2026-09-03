"""Decompose rectangle parity numerators into explicit-formula sector terms."""

import json
from pathlib import Path

import mpmath as mp

import gaussian_translation_weil_rectangle_scout as source

mp.mp.dps = 80
A = mp.log(2)
B = mp.log(3)
ARGS = [mp.mpf("0"), A, B, A + B, B - A]
TIMES = [mp.mpf("0.03"), mp.mpf("0.05"), mp.mpf("0.08")]


def block(values, parity):
    k0, ka, kb, kab, kd = values
    if parity == "plus":
        return (k0 + kab, ka + kb, k0 + kd)
    return (k0 - kab, ka - kb, k0 - kd)


def determinant(matrix):
    a, b, d = matrix
    return a * d - b * b


def polarization(left, right):
    a, b, d = left
    e, f, g = right
    return a * g + d * e - 2 * b * f


def text(value):
    return mp.nstr(value, 20)


rows = []
for t in TIMES:
    cutoff = source.cutoff_for(t, max(ARGS))
    mangoldt = source.von_mangoldt_table(cutoff)
    sectors = {
        "endpoint": [source.endpoint_term(t, a) for a in ARGS],
        "gamma": [source.gamma_term(t, a) for a in ARGS],
        "prime": [source.prime_term(t, a, mangoldt) for a in ARGS],
    }
    total_values = [sum(sectors[name][j] for name in sectors) for j in range(5)]
    k0_squared = total_values[0] ** 2
    row = {"t": text(t), "prime_cutoff": cutoff, "K0": text(total_values[0]), "channels": {}}
    for parity in ("plus", "minus"):
        blocks = {name: block(values, parity) for name, values in sectors.items()}
        pieces = {f"self_{name}": determinant(value) for name, value in blocks.items()}
        names = list(blocks)
        for i, left in enumerate(names):
            for right in names[i + 1 :]:
                pieces[f"mixed_{left}_{right}"] = polarization(blocks[left], blocks[right])
        total = determinant(block(total_values, parity))
        reconstructed = sum(pieces.values())
        row["channels"][parity] = {
            "normalized_total": text(total / k0_squared),
            "normalized_pieces": {key: text(value / k0_squared) for key, value in pieces.items()},
            "reconstruction_residual": text((total - reconstructed) / k0_squared),
        }
    rows.append(row)

result = {
    "schema": "marici.grothendieck.weil-rectangle-sector-polarization-scout.v1",
    "rows": rows,
    "claim_boundary": "Non-directed numerical decomposition; cancellation anatomy only.",
}
output = Path(__file__).parents[1] / "results" / "weil-rectangle-sector-polarization-scout.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
