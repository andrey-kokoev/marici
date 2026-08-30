"""Dependency-free exact separation of residual carrier loss and sheet interference."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/strominger/results/magnetic_two_level_interference.json"

def clean(p):
    return {k: v for k, v in p.items() if v}

def addp(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, Fraction(0)) + v
    return clean(out)

def scalep(c, a):
    return clean({k: c * v for k, v in a.items()})

def mulp(a, b):
    out = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            key = (i + k, j + l)
            out[key] = out.get(key, Fraction(0)) + x * y
    return clean(out)

def derivp(a, axis):
    out = {}
    for exponents, value in a.items():
        power = exponents[axis]
        if power:
            target = list(exponents)
            target[axis] -= 1
            out[tuple(target)] = value * power
    return clean(out)

def reflectp(a):
    return {(j, i): v for (i, j), v in a.items()}

ONE = {(0, 0): Fraction(1)}
DEN = {(0, 0): Fraction(1), (1, 1): Fraction(1)}

class Rat:
    def __init__(self, num, den=ONE):
        self.num = clean(num)
        self.den = clean(den)
    def __add__(self, other):
        return Rat(addp(mulp(self.num, other.den), mulp(other.num, self.den)),
                   mulp(self.den, other.den))
    def __neg__(self):
        return Rat(scalep(-1, self.num), self.den)
    def __sub__(self, other):
        return self + (-other)
    def __mul__(self, other):
        return Rat(mulp(self.num, other.num), mulp(self.den, other.den))
    def deriv(self, axis):
        return Rat(
            addp(mulp(derivp(self.num, axis), self.den),
                 scalep(-1, mulp(self.num, derivp(self.den, axis)))),
            mulp(self.den, self.den),
        )
    def reflect(self):
        return Rat(reflectp(self.num), reflectp(self.den))
    def is_zero(self):
        return not self.num
    def equals(self, other):
        return mulp(self.num, other.den) == mulp(other.num, self.den)
    def support_size(self):
        return len(self.num)

def monomial(i, j, coefficient=1):
    return Rat({(i, j): Fraction(coefficient)})

gamma = Rat({(0, 1): Fraction(-2)}, DEN)

def chain(grade, datum, barred=False):
    value = datum
    axis = 1 if barred else 0
    connection = gamma.reflect() if barred else gamma
    for weight in range(2, grade + 2):
        value = value.deriv(axis) - Rat({(0, 0): Fraction(weight)}) * connection * value
    return value

def sheet_packet(grade, datum):
    unbarred = chain(grade, datum)
    barred = chain(grade, datum.reflect(), barred=True)
    return unbarred.deriv(1), barred.deriv(0)

E1 = monomial(0, 0) - monomial(0, -2)
E2 = monomial(0, -8) - Rat({(-4, 2): Fraction(3)}) + Rat({(-6, 0): Fraction(2)})
packets = {"E1": sheet_packet(2, E1), "E2": sheet_packet(2, E2)}

checks = []
def record(cid, statement, condition, detail):
    checks.append({"id": cid, "statement": statement,
                   "status": "pass" if condition else "FAIL", "detail": detail})

for name, (left, right) in packets.items():
    record(f"{name}.nonzero", f"{name} has two nonzero sheet outputs",
           not left.is_zero() and not right.is_zero(),
           {"left_numerator_terms": left.support_size(),
            "right_numerator_terms": right.support_size()})
    record(f"{name}.magnetic", f"{name} is magnetic-zero by equal-sheet coherence",
           left.equals(right), "A=B")
    record(f"{name}.electric", f"{name} remains visible to the complementary sum",
           not (left + right).is_zero() and (left + right).equals(Rat({(0, 0): Fraction(2)}) * left),
           "A+B=2A!=0")

E1_expected = Rat({(1, 0): Fraction(40), (0, 1): Fraction(40)},
                  mulp(mulp(DEN, DEN), DEN))
record("E1.closed", "the first exceptional sheet has the closed formula",
       packets["E1"][0].equals(E1_expected),
       "40(z+zb)/(1+z*zb)^3")

failed = [check for check in checks if check["status"] != "pass"]
payload = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_two_level_interference_checks.py",
    "author": "marici.Strominger",
    "dependency_posture": "Python standard library exact Laurent-rational arithmetic",
    "scope": {"strength": "exact full-fold mechanism distinction",
              "grade": 2, "classes": ["E1", "E2"]},
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": "E1 and E2 have A=B nonzero. They are pure electric-ideal states: magnetic projection vanishes while the complementary electric readout equals 2A and remains nonzero."
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(1 if failed else 0)
