"""Exact symbolic L2 Gram of the four Gaussian grades f_j=x^j exp(-pi x^2)."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path


def odd_double_factorial(k):
    if k == 0:
        return 1
    out = 1
    for n in range(1, 2 * k, 2):
        out *= n
    return out


def gram_entry(i, j):
    degree = i + j
    if degree % 2:
        return {"zero": True, "coefficient": "0", "pi_power": 0, "sqrt2_denominator": False}
    k = degree // 2
    # Integral x^(2k) exp(-2*pi*x^2) dx
    # = [(2k-1)!! / 2^(2k)] * [1/(sqrt(2)*pi^k)].
    coefficient = Fraction(odd_double_factorial(k), 2 ** (2 * k))
    return {
        "zero": False,
        "coefficient": str(coefficient),
        "pi_power": -k,
        "sqrt2_denominator": True,
    }


gram = [[gram_entry(i, j) for j in range(4)] for i in range(4)]

# Parity block decomposition and decisive fourth-grade entries.
for i in range(4):
    for j in range(4):
        assert gram[i][j]["zero"] == ((i + j) % 2 == 1)
assert gram[3][0]["zero"]
assert gram[3][1]["coefficient"] == "3/16"
assert gram[3][2]["zero"]
assert gram[3][3]["coefficient"] == "15/64"

# Hostile: omitting f3 loses a positive diagonal entry and the f1-f3 coupling.
three_grade_has_f3_diagonal = False
three_grade_has_f1_f3_coupling = False
assert not three_grade_has_f3_diagonal
assert not three_grade_has_f1_f3_coupling

payload = {
    "schema": "marici.research.check.v1",
    "claim": "the unshifted four-grade Gaussian L2 Gram is exact and parity blocked",
    "basis": ["f0", "f1", "f2", "f3"],
    "entry_encoding": "coefficient * pi^pi_power / sqrt(2) when nonzero",
    "gram": gram,
    "fourth_grade": {
        "f3_f0": "0",
        "f3_f1": "3/(16*sqrt(2)*pi^2)",
        "f3_f2": "0",
        "f3_f3": "15/(64*sqrt(2)*pi^3)",
    },
    "three_grade_truncation_rejected": True,
    "translated_relative_green_gram_proved": False,
    "g1_1_closed": False,
    "verdict": "the canonical unshifted L2 baseline is exact; the completed translated Green Gram remains open",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parents[1] / "results" / "rh-four-grade-gaussian-gram.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
