#!/usr/bin/env python3
"""Exact angular-average audit of the two T7 residual UV directions."""
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    r = 0
    for c in range(len(a[0])):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [a[i][j] - q * a[r][j] for j in range(len(a[0]))]
        r += 1
    return r


def main():
    root = Path(__file__).resolve().parents[3]
    x, y = Fraction(2), Fraction(3)
    delta = x * x - y * y

    # In three dimensions, <|r n+p|> = r + |p|^2/(3r)+O(r^-3).
    # At E=0, q_G12=r.  Hence e2-e4 has a Lambda coefficient delta/3.
    linear_coefficient = delta / 3

    # At E=0 the v_alg coefficients are
    # A=delta*x^2*y^2, B=2*x^2*y^2, C=-2*x^2*y^2.
    # Since <|rn+p|^2>=r^2+|p|^2 exactly, B+C=0 and the averaged
    # v_alg numerator is 3*delta*x^2*y^2, producing Lambda^2 but no Lambda.
    a = delta * x * x * y * y
    b = 2 * x * x * y * y
    c = -2 * x * x * y * y
    assert b + c == 0
    averaged_valg_constant = a + b * x * x + c * y * y
    assert averaged_valg_constant == 3 * delta * x * x * y * y
    valg_linear_coefficient = Fraction(0)

    # Residual coordinates are (e1-dual, e2-e4+180*v_alg).
    # The quartic grade has nonzero e1 coordinate.  Its second coordinate is
    # deliberately denoted kappa: its value is irrelevant to independence.
    kappa = Fraction(1)
    quartic = [Fraction(1), kappa]
    linear = [Fraction(0), linear_coefficient + 180 * valg_linear_coefficient]
    assert linear[1] != 0
    assert rank([quartic, linear]) == 2

    result = {
        "schema": "marici.nima.t7_complete_uv_counterterm_image.v1",
        "passed": True,
        "fiber": {"E": 0, "x": 2, "y": 3},
        "angular_average_identity": "<|r*n+p|>=r+|p|^2/(3*r)+O(r^-3)",
        "linear_counterterm_coefficient_e2_minus_e4": str(linear_coefficient),
        "v_alg_linear_counterterm_coefficient": "0",
        "residual_counterterm_vectors": [["1", "kappa"], ["0", str(linear[1])]],
        "counterterm_image_rank": 2,
        "residual_rank_after_full_uv_subtraction": 0,
        "interpretation": "on the frozen E=0 generic fiber, the quartic mixed subtraction and the linear e2-e4 subtraction span the full two-dimensional supported-cospan residual",
        "scope": "sharp UV asymptotic statement for the frozen source-normalized T7 frame; locality and symmetry admissibility of both subtraction directions remain to be proved before calling this a physical renormalization quotient",
    }
    output = root / "research/nima/results/t7_complete_uv_counterterm_image.json"
    payload = output.read_text(encoding="utf-8")
    assert json.loads(payload) == result
    print(json.dumps({"passed": True, "counterterm_image_rank": 2,
                      "sha256": hashlib.sha256(payload.encode()).hexdigest().upper()}))


if __name__ == "__main__":
    main()
