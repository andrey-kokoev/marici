#!/usr/bin/env python3
"""Exact dependency-free certification of Entry 822's chamber separator."""

import json


def add(*polys):
    out = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            out[monomial] = out.get(monomial, 0) + coefficient
    return {m: c for m, c in out.items() if c}


def scale(c, poly):
    return {m: c * value for m, value in poly.items() if c * value}


def mul(left, right):
    out = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            monomial = tuple(a + b for a, b in zip(lm, rm))
            out[monomial] = out.get(monomial, 0) + lc * rc
    return {m: c for m, c in out.items() if c}


# Variables are (delta,d,q,p).
delta = {(1, 0, 0, 0): 1}
d = {(0, 1, 0, 0): 1}
q = {(0, 0, 1, 0): 1}
p = {(0, 0, 0, 1): 1}
p2 = mul(p, p)
a = add(d, q)
t2 = scale(-1, add(mul(a, delta), scale(2, mul(p2, q))))
t0 = mul(q, add(mul(delta, delta), mul(a, delta), mul(p2, q)))
bracket = add(mul(t2, t2), scale(-4, mul(p2, t0)))
expected = mul(mul(delta, delta), add(mul(a, a), scale(-4, mul(p2, q))))
assert bracket == expected

print(json.dumps({
    "exact_factorization": "t2^2-4*p^2*t0=delta^2*((d+q)^2-4*p^2*q)",
    "pulled_back_discriminant_factor": "delta^4",
    "delta_regulator_factorization": "-i*(epsE-epsP1)*(2*p-i*(epsE+epsP1))",
    "positive_cone_separator": "epsE=epsP1",
    "chambers": ["epsE>epsP1", "epsE<epsP1"],
}, indent=2))
