"""Exact symbolic Gram for differently translated Gaussian grades."""

import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path


def odd_double_factorial(k):
    out = 1
    for n in range(1, 2 * k, 2):
        out *= n
    return out


def translated_entry(i, j):
    """Terms after factoring exp(-pi*d^2/2)/sqrt(2), d=a-b."""
    terms = {}
    for r in range(i + 1):
        for s in range(j + 1):
            degree_y = r + s
            if degree_y % 2:
                continue
            k = degree_y // 2
            degree_d = i + j - degree_y
            coefficient = Fraction(comb(i, r) * comb(j, s), 2 ** degree_d)
            if (j - s) % 2:
                coefficient *= -1
            coefficient *= Fraction(odd_double_factorial(k), 2 ** (2 * k))
            key = (degree_d, -k)
            terms[key] = terms.get(key, Fraction(0)) + coefficient
    return {key: value for key, value in terms.items() if value}


def encode(terms):
    return [
        {"coefficient": str(value), "d_power": d_power, "pi_power": pi_power}
        for (d_power, pi_power), value in sorted(terms.items(), reverse=True)
    ]


gram = [[translated_entry(i, j) for j in range(4)] for i in range(4)]

# Hermitian symmetry for real translates: G_ij(d)=G_ji(-d).
for i in range(4):
    for j in range(4):
        reflected = {
            key: value * ((-1) ** key[0]) for key, value in gram[j][i].items()
        }
        assert gram[i][j] == reflected

# At zero displacement, odd total degree vanishes and the old Gram is recovered.
for i in range(4):
    for j in range(4):
        zero_terms = {key: value for key, value in gram[i][j].items() if key[0] == 0}
        assert bool(zero_terms) == ((i + j) % 2 == 0)

# Differently translated rays destroy naive odd-parity cancellation.
assert gram[3][0]  # nonzero polynomial for d != 0
assert gram[3][2]

payload = {
    "schema": "marici.research.check.v1",
    "claim": "the differently translated four-grade Gaussian L2 Gram is exact",
    "translation_convention": "U_a f(x)=f(x+a)",
    "displacement": "d=a-b",
    "common_factor": "exp(-pi*d^2/2)/sqrt(2)",
    "term_encoding": "coefficient*d^d_power*pi^pi_power",
    "gram": [[encode(entry) for entry in row] for row in gram],
    "symmetry_Gij_d_equals_Gji_minus_d": True,
    "zero_displacement_recovers_parity_block": True,
    "different_ray_f3_f0_nonzero": True,
    "different_ray_f3_f2_nonzero": True,
    "relative_green_corrections_included": False,
    "g1_1_closed": False,
    "verdict": "all translated Hilbert-grade pairings are explicit; relative boundary/history corrections remain open",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parents[1] / "results" / "rh-translated-four-grade-gaussian-gram.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
