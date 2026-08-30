#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

from sympy import Matrix, Rational

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/cross-minor-spin-two.json"


def packet(m):
    a, b, d = m[0, 0], m[0, 1], m[1, 1]
    t = a + d
    determinant = m.det()
    q = a - d
    r = 2 * b
    cross = b ** 2
    assert q ** 2 + r ** 2 == t ** 2 - 4 * determinant
    assert cross == (t ** 2 - 4 * determinant - q ** 2) / 4
    return t, determinant, q, r, cross


def main():
    diagonal = Matrix.diag(2, 1)
    forty_five = Matrix([[Rational(3, 2), Rational(1, 2)],
                         [Rational(1, 2), Rational(3, 2)]])
    p0 = packet(diagonal)
    p45 = packet(forty_five)
    assert p0 == (3, 2, 1, 0, 0)
    assert p45 == (3, 2, 0, 1, Rational(1, 4))

    Q = Matrix([[Rational(3, 5), -Rational(4, 5)],
                [Rational(4, 5), Rational(3, 5)]])
    rotated = Q * diagonal * Q.T
    reflected = Matrix.diag(1, -1) * rotated * Matrix.diag(1, -1)
    pr = packet(rotated)
    pf = packet(reflected)
    assert pr[:3] == pf[:3]
    assert pr[3] == -pf[3]
    assert pr[4] == pf[4] == Rational(144, 625)
    assert abs(pr[2]) == Rational(7, 25)
    assert abs(pr[3]) == Rational(24, 25)

    payload = {
        "schema": "marici.kitaev.cross_minor_spin_two.v1",
        "status": "pass",
        "spectral_circle_identity": "q^2+r^2=t^2-4 Delta",
        "cross_minor_formula": "X=(t^2-4 Delta-q^2)/4=r^2/4",
        "isospectral_frames": {
            "diagonal_cross_minor": "0",
            "forty_five_degree_cross_minor": "1/4",
        },
        "rational_reflection_fixture": {
            "absolute_q": "7/25", "r_pair": [str(pr[3]), str(pf[3])],
            "shared_cross_minor": "144/625",
        },
        "orientation_port": "one C2 bit after nonzero magnitude is known",
        "theta_application_status": "frozen_pending_symmetric_labelled_block_typing",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
