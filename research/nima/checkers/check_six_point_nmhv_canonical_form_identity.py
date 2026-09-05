from __future__ import annotations

import json
from collections import Counter
from fractions import Fraction
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/nima/results/six-point-nmhv-canonical-form-identity.json"
Z = {i: (1, i, i**2, i**3, i**4) for i in range(1, 7)}
LEFT = [(1,2,3,4,5), (1,2,3,5,6), (1,3,4,5,6)]
RIGHT = [(1,2,3,4,6), (1,2,4,5,6), (2,3,4,5,6)]
ZERO = (0,0,0,0,0)


def det(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    out = Fraction(1)
    for c in range(len(a)):
        p = next((r for r in range(c, len(a)) if a[r][c]), None)
        if p is None: return Fraction(0)
        if p != c: a[c], a[p], out = a[p], a[c], -out
        q = a[c][c]; out *= q
        for j in range(c, len(a)): a[c][j] /= q
        for r in range(c + 1, len(a)):
            q = a[r][c]
            for j in range(c, len(a)): a[r][j] -= q * a[c][j]
    return out


def bracket(columns):
    return det(list(zip(*columns)))


def y_form(facet):
    coeff = []
    for i in range(5):
        basis = tuple(1 if i == j else 0 for j in range(5))
        coeff.append(int(bracket([basis] + [Z[v] for v in facet])))
    return tuple(coeff)


def canonical_factor(coeff):
    g = 0
    for x in coeff: g = gcd(g, abs(x))
    primitive = tuple(x // g for x in coeff)
    first = next(x for x in primitive if x)
    sign = 1 if first > 0 else -1
    return tuple(sign*x for x in primitive), g*sign


def term(vertices):
    a,b,c,d,e = vertices
    facets = [(a,b,c,d),(b,c,d,e),(c,d,e,a),(d,e,a,b),(e,a,b,c)]
    factors = Counter()
    scalar = 1
    for facet in facets:
        factor, scale = canonical_factor(y_form(facet))
        factors[factor] += 1; scalar *= scale
    numerator = int(bracket([Z[v] for v in vertices])) ** 4
    return Fraction(numerator, scalar), factors


def mul_linear(poly, linear):
    out = {}
    for exponent, coefficient in poly.items():
        for i, value in enumerate(linear):
            if not value: continue
            nxt = list(exponent); nxt[i] += 1; nxt = tuple(nxt)
            out[nxt] = out.get(nxt, Fraction(0)) + coefficient * value
    return {k:v for k,v in out.items() if v}


def common_numerator(signed_cells):
    terms = [(sign, *term(cell)) for sign, cell in signed_cells]
    lcm = Counter()
    for _, _, factors in terms:
        for factor, multiplicity in factors.items():
            lcm[factor] = max(lcm[factor], multiplicity)
    total = {}
    for sign, numerator, factors in terms:
        poly = {ZERO: sign * numerator}
        missing = lcm.copy(); missing.subtract(factors)
        for factor, multiplicity in missing.items():
            for _ in range(multiplicity): poly = mul_linear(poly, factor)
        for exponent, coefficient in poly.items():
            total[exponent] = total.get(exponent, Fraction(0)) + coefficient
    return {k:v for k,v in total.items() if v}, lcm


def main():
    signed = [(1,c) for c in LEFT] + [(-1,c) for c in RIGHT]
    residual, denominator = common_numerator(signed)
    mutated = signed[:]
    mutated[0] = (-1, mutated[0][1])
    mutation_residual, _ = common_numerator(mutated)
    result = {
        "schema": "marici.nima.six_point_nmhv_canonical_form_identity.result.v1",
        "status": "passed" if not residual and mutation_residual else "failed",
        "identity_common_numerator_term_count": len(residual),
        "common_denominator_distinct_linear_factors": len(denominator),
        "orientation_mutation_numerator_term_count": len(mutation_residual),
        "identity_proved_for_explicit_Z": not residual,
        "orientation_mutation_detected": bool(mutation_residual),
        "claim_boundary": "Exact polynomial common-numerator proof for the explicit moment-curve Z and declared bosonic simplex-form convention. It is not a proof for generic Z, the supersymmetric six-point NMHV amplitude, or the physical boundary dictionary."
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    if result["status"] != "passed": raise SystemExit(1)


if __name__ == "__main__": main()
