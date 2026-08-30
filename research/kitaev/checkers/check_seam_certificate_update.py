#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

from sympy import Rational, simplify, symbols

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/seam-certificate-update.json"


def product(R, E, delta, t):
    return simplify((R / (1 + t * R)) * (E + t * delta))


def main():
    t = symbols("t", nonnegative=True)

    harmonic = product(2, Rational(1, 8), Rational(1, 4), t)
    assert harmonic == Rational(1, 4)

    R = Rational(2)
    E = Rational(9, 16)
    delta = Rational(9, 16)
    initial = R * E
    threshold = simplify((initial - 1) / (R * (1 - delta)))
    assert initial == Rational(9, 8)
    assert threshold == Rational(1, 7)
    assert product(R, E, delta, threshold) == 1
    assert product(R, E, delta, Rational(1, 2)) < 1
    assert simplify(product(R, E, delta, t) -
                    (delta + (initial - delta) / (1 + t * R))) == 0

    zero_state = product(2, 1, 1, t)
    assert simplify(zero_state - (1 + 1 / (1 + 2 * t))) == 0
    assert zero_state.subs(t, 100) > 1

    payload = {
        "schema": "marici.kitaev.seam_certificate_update.v1",
        "status": "pass",
        "harmonic_no_improvement": {"certificate_product": "1/4 for all t"},
        "slack_fixture": {"initial_product": str(initial),
                          "actual_endpoint_defect": str(delta),
                          "strict_conductance_threshold": "t > 1/7"},
        "zero_endpoint_hostile": {"actual_defect": 1,
                                  "finite_t_certificate_strictly_above_one": True,
                                  "limit_certificate": 1},
        "exact_update": "delta + (R E - delta)/(1+t R)",
        "typing": "seam_improves_observation_certificate_not_state",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
