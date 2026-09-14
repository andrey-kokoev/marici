#!/usr/bin/env python3
"""Exact Cayley--Dickson octonion check for one framed quaternionic mode.

This is a coefficient-algebra test only. It does not construct a canonical
multiplication on the semilocal boundary Hilbert space.
"""
from fractions import Fraction as Q
import json
from pathlib import Path


def qadd(a, b): return tuple(x + y for x, y in zip(a, b))
def qneg(a): return tuple(-x for x in a)
def qconj(a): return (a[0], -a[1], -a[2], -a[3])
def qmul(a, b):
    w, x, y, z = a
    W, X, Y, Z = b
    return (
        w*W-x*X-y*Y-z*Z,
        w*X+x*W+y*Z-z*Y,
        w*Y-x*Z+y*W+z*X,
        w*Z+x*Y-y*X+z*W,
    )

def oadd(x, y): return (qadd(x[0], y[0]), qadd(x[1], y[1]))
def oneg(x): return (qneg(x[0]), qneg(x[1]))
def oconj(x): return (qconj(x[0]), qneg(x[1]))
def omul(x, y):
    # (a,b)(c,d)=(ac-conj(d)b, da+b conj(c))
    a, b = x; c, d = y
    return (
        qadd(qmul(a, c), qneg(qmul(qconj(d), b))),
        qadd(qmul(d, a), qmul(b, qconj(c))),
    )
def oscale(c, x): return (tuple(c*t for t in x[0]), tuple(c*t for t in x[1]))
def onorm2(x):
    p = omul(oconj(x), x)
    assert p[1] == ZQ and p[0][1:] == (0, 0, 0)
    return p[0][0]

ZQ = (Q(0),)*4
ONEQ = (Q(1), Q(0), Q(0), Q(0))
ZERO = (ZQ, ZQ)
ONE = (ONEQ, ZQ)
# e1,e2,e3 are quaternion units; e4 is doubling unit; e5..e7 products.
units = [
    ((Q(0),Q(1),Q(0),Q(0)), ZQ),
    ((Q(0),Q(0),Q(1),Q(0)), ZQ),
    ((Q(0),Q(0),Q(0),Q(1)), ZQ),
    (ZQ, ONEQ),
]
units += [omul(units[i], units[3]) for i in range(3)]


def main():
    minus_one = oneg(ONE)
    square_checks = [omul(e, e) == minus_one for e in units]
    anti_checks = []
    for i in range(7):
        for j in range(i+1, 7):
            anti_checks.append(oadd(omul(units[i], units[j]), omul(units[j], units[i])) == ZERO)

    x = oadd(oscale(Q(2), ONE), oadd(units[0], oscale(Q(3), units[4])))
    y = oadd(units[1], oscale(Q(-2), units[6]))
    z = oadd(oscale(Q(3), units[2]), units[3])
    norm_multiplicative = onorm2(omul(x, y)) == onorm2(x)*onorm2(y)
    # Left Moufang: x(y(xz))=((xy)x)z.
    moufang = omul(x, omul(y, omul(x, z))) == omul(omul(omul(x, y), x), z)
    # Exhibit nonassociativity.
    nonassoc = omul(omul(units[0], units[1]), units[3]) != omul(units[0], omul(units[1], units[3]))

    result = {
        "schema": "marici.voevodsky.cayley-dickson-boundary-mode.v1",
        "imaginary_units": 7,
        "all_unit_squares_minus_one": all(square_checks),
        "all_distinct_units_anticommute": all(anti_checks),
        "pair_anticommutation_checks": len(anti_checks),
        "norm_multiplicative_sample": norm_multiplicative,
        "left_moufang_sample": moufang,
        "nonassociative_sample": nonassoc,
        "algebra": "one framed coefficient fiber H+H*l = O",
        "claim_boundary": (
            "Exact rational coefficient-algebra check only; no canonical frame, "
            "vector-vector product, or octonionic semilocal boundary map is supplied."
        ),
        "next_gate": (
            "Construct a source-derived quaternionic rank-one boundary line or "
            "a measurable framed field of such lines before transporting this product."
        ),
    }
    assert all(square_checks) and all(anti_checks)
    assert norm_multiplicative and moufang and nonassoc
    out = Path(__file__).parents[1] / "results" / "cayley_dickson_boundary_mode.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))

if __name__ == "__main__": main()
