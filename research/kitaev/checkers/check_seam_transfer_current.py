#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

from sympy import Matrix, simplify, symbols

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/seam-transfer-current.json"


def metrics(L, h, b, u):
    inv = L.inv()
    R = (h.T * inv * h)[0]
    rb = (b.T * inv * b)[0]
    tau = (b.T * inv * h)[0]
    E = (u.T * L * u)[0]
    g = (b.T * u)[0]
    return R, rb, tau, E, g


def main():
    t = symbols("t", nonnegative=True)
    L = Matrix([[2, -1], [-1, 1]])
    h = Matrix([0, 1])
    remote = Matrix([1, 0])
    state = Matrix([-1, -1])

    R, rb, tau, E, g = metrics(L, h, remote, state)
    score = R * g ** 2 - E * tau ** 2
    assert (R, rb, tau, E, g, score) == (2, 1, 1, 1, -1, 1)
    Rt = simplify(R - t * tau ** 2 / (1 + t * rb))
    Et = E + t * g ** 2
    assert simplify(Rt - (1 + 1 / (1 + t))) == 0
    assert simplify(Rt * Et - (2 + t)) == 0

    direct = h
    dR, drb, dtau, dE, dg = metrics(L, h, direct, state)
    direct_score = dR * dg ** 2 - dE * dtau ** 2
    assert direct_score == -2

    zero_gradient_state = Matrix([0, -1])
    zR, zrb, ztau, zE, zg = metrics(L, h, remote, zero_gradient_state)
    assert zg == 0
    assert zR * zg ** 2 - zE * ztau ** 2 == -1

    payload = {
        "schema": "marici.kitaev.seam_transfer_current.v1",
        "status": "pass",
        "remote_seam_worsening": {
            "R": str(R), "self_resistance": str(rb), "transfer_current": str(tau),
            "energy": str(E), "state_gradient": str(g), "first_order_score": str(score),
            "exact_certificate": "2+t",
        },
        "direct_seam": {"first_order_score": str(direct_score),
                        "universally_nonincreasing": True},
        "same_remote_seam_zero_gradient_state": {"first_order_score": -1,
                                                  "improves": True},
        "placement_rule": "compare transfer-current leverage with state-gradient cost",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
