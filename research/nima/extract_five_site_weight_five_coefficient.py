#!/usr/bin/env python3
"""Independently extract the chi_12345 coefficient from the canonical sum."""

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "research/benincasa/results/five-site-asymmetric-canonical-sum.json"
TARGET = ROOT / "research/nima/results/five-site-weight-five-coefficient.json"

# Sparse polynomials in (t,u1,u2,u3).
Poly = dict[tuple[int, int, int, int], int]


def add(a: Poly, b: Poly) -> Poly:
    out = dict(a)
    for monomial, coefficient in b.items():
        out[monomial] = out.get(monomial, 0) + coefficient
        if out[monomial] == 0:
            del out[monomial]
    return out


def mul(a: Poly, b: Poly) -> Poly:
    out: Poly = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            exponent = tuple(x + y for x, y in zip(ea, eb))
            out[exponent] = out.get(exponent, 0) + ca * cb
    return {e: c for e, c in out.items() if c}


def power(a: Poly, n: int) -> Poly:
    out: Poly = {(0, 0, 0, 0): 1}
    base = a
    while n:
        if n & 1:
            out = mul(out, base)
        base = mul(base, base)
        n >>= 1
    return out


def p(terms: list[tuple[int, tuple[int, int, int, int]]]) -> Poly:
    return {exponents: coefficient for coefficient, exponents in terms}


F1 = p([(2, (0, 2, 0, 0)), (2, (0, 0, 2, 0)), (1, (0, 0, 0, 2)),
        (-2, (0, 1, 1, 0)), (-2, (0, 0, 1, 1))])
F = [
    F1,
    add(F1, p([(-2, (0, 1, 0, 0)), (1, (0, 0, 0, 0))])),
    add(F1, p([(-2, (0, 0, 1, 0)), (2, (0, 0, 0, 0))])),
    add(F1, p([(-2, (0, 0, 0, 1)), (3, (0, 0, 0, 0))])),
    add(F1, p([(2, (0, 1, 0, 0)), (2, (0, 0, 1, 0)),
                (-8, (0, 0, 0, 1)), (29, (0, 0, 0, 0))])),
]


def parse_term(term: str) -> tuple[int, int, list[int]]:
    sign = -1 if term.startswith("-") else 1
    term = term.lstrip("+-")
    factors = term.split("*")
    coefficient = sign
    t_power = 0
    y_power = [0] * 5
    for factor in factors:
        if factor.isdigit():
            coefficient *= int(factor)
            continue
        match = re.fullmatch(r"([ty]\d?)(?:\^(\d+))?", factor)
        if not match:
            raise ValueError(f"unparsed factor: {factor}")
        variable, exponent_text = match.groups()
        exponent = int(exponent_text or 1)
        if variable == "t":
            t_power = exponent
        else:
            y_power[int(variable[1:]) - 1] = exponent
    return coefficient, t_power, y_power


packet = json.loads(SOURCE.read_text(encoding="utf-8"))
numerator = packet["combined_numerator"]
terms = re.split(r"(?=[+-])", numerator)
coefficient_poly: Poly = {}
selected_source_terms = 0
for term in terms:
    if not term:
        continue
    coefficient, t_power, y_power = parse_term(term)
    if not all(exponent % 2 == 1 for exponent in y_power):
        continue
    selected_source_terms += 1
    contribution: Poly = {(t_power, 0, 0, 0): coefficient}
    for relation, exponent in zip(F, y_power):
        contribution = mul(contribution, power(relation, (exponent - 1) // 2))
    coefficient_poly = add(coefficient_poly, contribution)

rows = [
    {"coefficient": coefficient, "exponents_t_u1_u2_u3": list(exponents)}
    for exponents, coefficient in sorted(coefficient_poly.items())
]
canonical = json.dumps(rows, separators=(",", ":"), sort_keys=True)
maximum_degree = max(sum(exponents) for exponents in coefficient_poly)
assert len(coefficient_poly) == 526
assert maximum_degree == 11

out = {
    "schema": "marici.five_site.weight_five_coefficient.v1",
    "source": str(SOURCE.relative_to(ROOT)).replace("\\", "/"),
    "source_numerator_terms": len(terms),
    "selected_all_odd_source_terms": selected_source_terms,
    "reduced_term_count": len(rows),
    "maximum_total_degree": maximum_degree,
    "sha256": hashlib.sha256(canonical.encode()).hexdigest(),
    "monomials": rows,
    "passed": True,
}
TARGET.parent.mkdir(parents=True, exist_ok=True)
TARGET.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps({key: value for key, value in out.items() if key != "monomials"}, sort_keys=True))
