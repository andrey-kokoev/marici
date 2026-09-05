from __future__ import annotations

import json
from fractions import Fraction
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/nima/results/six-point-nmhv-super-five-bracket.json"
LEFT = [(1,2,3,4,5), (1,2,3,5,6), (1,3,4,5,6)]
RIGHT = [(1,2,3,4,6), (1,2,4,5,6), (2,3,4,5,6)]
T_PROBES = [(1,2,3,4,5,6), (1,2,4,7,11,16), (0,1,3,6,10,15)]


def det(columns):
    a = [[Fraction(x) for x in row] for row in zip(*columns)]
    out = Fraction(1)
    for col in range(len(a)):
        pivot = next((r for r in range(col, len(a)) if a[r][col]), None)
        if pivot is None: return Fraction(0)
        if pivot != col: a[col], a[pivot], out = a[pivot], a[col], -out
        p = a[col][col]; out *= p
        for j in range(col, len(a)): a[col][j] /= p
        for r in range(col + 1, len(a)):
            q = a[r][col]
            for j in range(col, len(a)): a[r][j] -= q * a[col][j]
    return out


def five_bracket(vertices, Z):
    a,b,c,d,e = vertices
    cyclic_facets = [(a,b,c,d),(b,c,d,e),(c,d,e,a),(d,e,a,b),(e,a,b,c)]
    brackets = [det([Z[i] for i in facet]) for facet in cyclic_facets]
    denominator = product_fraction(brackets)
    q = {a: brackets[1], b: brackets[2], c: brackets[3], d: brackets[4], e: brackets[0]}
    out = {}
    for labels in product(vertices, repeat=4):
        coefficient = product_fraction(q[label] for label in labels) / denominator
        if coefficient: out[labels] = coefficient
    return out


def product_fraction(values):
    out = Fraction(1)
    for value in values: out *= value
    return out


def add(target, source, sign=1):
    for monomial, coefficient in source.items():
        target[monomial] = target.get(monomial, Fraction(0)) + sign * coefficient
        if not target[monomial]: del target[monomial]


def evaluate(ts):
    Z = {i + 1: (Fraction(1), Fraction(t), Fraction(t*t), Fraction(t**3)) for i, t in enumerate(ts)}
    total = {}
    for cell in LEFT: add(total, five_bracket(cell, Z), 1)
    for cell in RIGHT: add(total, five_bracket(cell, Z), -1)
    mutated = {}
    add(mutated, five_bracket(LEFT[0], Z), -1)
    for cell in LEFT[1:]: add(mutated, five_bracket(cell, Z), 1)
    for cell in RIGHT: add(mutated, five_bracket(cell, Z), -1)
    ordered_positive = all(det([Z[i] for i in cell]) > 0 for cell in [(1,2,3,4),(1,2,3,5),(1,2,3,6),(1,2,4,5),(1,2,4,6),(1,2,5,6),(1,3,4,5),(1,3,4,6),(1,3,5,6),(1,4,5,6),(2,3,4,5),(2,3,4,6),(2,3,5,6),(2,4,5,6),(3,4,5,6)])
    return {"t": list(ts), "residual_monomials": len(total), "mutation_residual_monomials": len(mutated), "ordered_four_brackets_positive": ordered_positive}


def main():
    probes = [evaluate(ts) for ts in T_PROBES]
    checks = {
        "super_five_bracket_identity_at_all_probes": all(p["residual_monomials"] == 0 for p in probes),
        "orientation_mutation_detected_at_all_probes": all(p["mutation_residual_monomials"] > 0 for p in probes),
        "all_momentum_twistor_probes_positive": all(p["ordered_four_brackets_positive"] for p in probes)
    }
    out = {
        "schema": "marici.nima.six_point_nmhv_super_five_bracket.result.v1",
        "status": "passed" if all(checks.values()) else "failed",
        "checks": checks,
        "probes": probes,
        "grassmann_basis": "monomials chi_{i1}^1 chi_{i2}^2 chi_{i3}^3 chi_{i4}^4 represented by (i1,i2,i3,i4)",
        "claim_boundary": "Exact componentwise Grassmann-polynomial equality at three declared positive rational momentum-twistor probes using the standard authored five-bracket formula. Finite probes can falsify but do not prove the generic superidentity or source normalization."
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    if out["status"] != "passed": raise SystemExit(1)


if __name__ == "__main__": main()
