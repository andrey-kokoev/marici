"""Exact rank-two dictionary for double-slit and Gaussian purity relations."""

import json
from fractions import Fraction
from pathlib import Path


def det2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


double_slit = []
for m, n in ((2, 1), (3, 2), (4, 1), (5, 3), (7, 4)):
    den = Fraction(m * m + n * n)
    visibility = Fraction(m * m - n * n, den)
    distinguishability = Fraction(2 * m * n, den)
    gram = ((Fraction(1), visibility), (visibility, Fraction(1)))
    assert det2(gram) == distinguishability**2
    assert visibility**2 + distinguishability**2 == 1
    double_slit.append({"V": str(visibility), "D": str(distinguishability), "det_Gram": str(det2(gram))})

gaussian = []
for lam in (Fraction(0), Fraction(1, 5), Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)):
    den = 1 - lam * lam
    a = (1 + lam * lam) / (2 * den)
    c = lam / den
    A = ((a, Fraction(0)), (Fraction(0), a))
    C = ((c, Fraction(0)), (Fraction(0), -c))
    assert det2(A) + det2(C) == Fraction(1, 4)
    gaussian.append({"det_A": str(det2(A)), "det_C": str(det2(C)), "vacuum_minor": "1/4"})

packet = {
    "schema": "marici.two-occurrence-purity-dictionary.v1",
    "common_engine": "rank-two complementary exterior-square minors constrained by global purity",
    "double_slit": {
        "Gram": "[[1,gamma],[gamma*,1]]",
        "local_port": "V^2=|gamma|^2",
        "cross_port": "D^2=det(Gram)=||d0 wedge d1||^2",
        "relation": "V^2+D^2=1",
        "tests": double_slit,
    },
    "gaussian": {
        "purity_equation": "V Omega V=Omega/4",
        "local_port": "Delta=det(A)-1/4",
        "cross_port": "-det(C)",
        "relation": "det(A)+det(C)=1/4",
        "tests": gaussian,
    },
    "qualification": "shared rank-two exterior-square architecture, not equality of the physical invariants or a universal higher-rank theorem",
}

out = Path(__file__).parent / "results" / "two-occurrence-purity-dictionary.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
