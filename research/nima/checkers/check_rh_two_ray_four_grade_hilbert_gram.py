"""Exact two-ray Hilbert Gram for the four-grade first-prime packet."""

import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path


def add(a, b):
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, Fraction(0)) + value
        if not out[key]:
            del out[key]
    return out


def mul(a, b):
    out = {}
    for (la, pa), va in a.items():
        for (lb, pb), vb in b.items():
            key = (la + lb, pa + pb)
            out[key] = out.get(key, Fraction(0)) + va * vb
    return {key: value for key, value in out.items() if value}


def scale(a, scalar):
    return {key: value * scalar for key, value in a.items() if value * scalar}


def mono(coefficient, l_power, pi_power):
    return {(l_power, pi_power): Fraction(coefficient)}


def odd_double_factorial(k):
    out = 1
    for n in range(1, 2 * k, 2):
        out *= n
    return out


def translated_entry(i, j, displacement_multiple):
    # Polynomial after exp(-pi*d^2/2)/sqrt(2), with d=m*L.
    out = {}
    for r in range(i + 1):
        for s in range(j + 1):
            degree_y = r + s
            if degree_y % 2:
                continue
            k = degree_y // 2
            degree_d = i + j - degree_y
            coefficient = Fraction(comb(i, r) * comb(j, s), 2 ** degree_d)
            coefficient *= (-1) ** (j - s)
            coefficient *= Fraction(odd_double_factorial(k), 2 ** (2 * k))
            coefficient *= displacement_multiple ** degree_d
            out = add(out, mono(coefficient, degree_d, -k))
    return out


def quadratic(coeff_left, coeff_right, displacement_multiple):
    out = {}
    for i in range(4):
        for j in range(4):
            term = mul(mul(coeff_left[i], coeff_right[j]), translated_entry(i, j, displacement_multiple))
            out = add(out, term)
    return out


def encode(poly):
    return [
        {"coefficient": str(value), "L_power": lp, "pi_power": pp}
        for (lp, pp), value in sorted(poly.items(), reverse=True)
    ]


# E+O and E-O coefficient columns.
plus = [mono(-2, 2, 1), mono(8, 1, 1), mono(4, 2, 2), mono(-8, 1, 2)]
minus = [mono(-2, 2, 1), mono(-8, 1, 1), mono(4, 2, 2), mono(8, 1, 2)]

diagonal_plus = quadratic(plus, plus, 0)
diagonal_minus = quadratic(minus, minus, 0)
cross_plus_minus = quadratic(plus, minus, 2)
cross_minus_plus = quadratic(minus, plus, -2)

assert diagonal_plus == diagonal_minus
assert cross_plus_minus == cross_minus_plus
assert cross_plus_minus
# The f3 diagonal and f1-f3 coupling are included because all four indices run.

payload = {
    "schema": "marici.research.check.v1",
    "claim": "the two-ray four-grade packet has an exact ordinary Hilbert Gram",
    "packet_plus": "U_L(E+O)",
    "packet_minus": "U_-L(E-O)",
    "diagonal_common_factor": "1/sqrt(2)",
    "cross_common_factor": "exp(-2*pi*L^2)/sqrt(2)",
    "term_encoding": "coefficient*L^L_power*pi^pi_power",
    "diagonal_polynomial": encode(diagonal_plus),
    "cross_polynomial": encode(cross_plus_minus),
    "equal_ray_norms": True,
    "symmetric_cross_pairing": True,
    "fourth_grade_retained": True,
    "relative_green_gram_proved": False,
    "g1_1_closed": False,
    "verdict": "the complete two-ray Hilbert baseline is exact; relative Green corrections remain open",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parents[1] / "results" / "rh-two-ray-four-grade-hilbert-gram.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
