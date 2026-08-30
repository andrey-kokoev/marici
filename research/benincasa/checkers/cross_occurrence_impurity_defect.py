"""Exact audit of the cross-occurrence correction to local Gaussian impurity."""

import json
from fractions import Fraction
from pathlib import Path


def det2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


tests = []
for lam in (Fraction(0), Fraction(1, 7), Fraction(1, 3), Fraction(1, 2), Fraction(3, 4)):
    den = 1 - lam * lam
    a = (1 + lam * lam) / (2 * den)
    c = lam / den
    A = ((a, Fraction(0)), (Fraction(0), a))
    C = ((c, Fraction(0)), (Fraction(0), -c))
    local_delta = det2(A) - Fraction(1, 4)
    cross_det = det2(C)
    assert local_delta == -cross_det

    # For V=[[aI,cZ],[cZ,aI]], determinant factors as (a^2-c^2)^2.
    global_det = (a * a - c * c) ** 2
    assert a * a - c * c == Fraction(1, 4)
    assert global_det == Fraction(1, 16)
    tests.append({
        "lambda": str(lam),
        "det_A_minus_vacuum": str(local_delta),
        "det_C": str(cross_det),
        "det_V_global": str(global_det),
    })

packet = {
    "schema": "marici.cross-occurrence-impurity-defect.v1",
    "covariance_blocks": "V=[[A,C],[C,A]], A=a I2, C=c diag(1,-1)",
    "identity": "Delta_local=det(A)-1/4=-det(C)",
    "global_purity": "det(V)=1/16",
    "interpretation": "the local impurity is exactly the determinant of the discarded cross-occurrence covariance, with sign reversed",
    "qualification": "this is a nonlinear covariance identity, not yet a chain-level Beck-Chevalley theorem",
    "exact_tests": tests,
}

out = Path(__file__).parent / "results" / "cross-occurrence-impurity-defect.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
