#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

from sympy import Rational, exp, simplify, symbols

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/holomorphic-normalization-unit.json"


def main():
    s = symbols("s")
    determinant = 1 - s

    unit = exp(s)
    reciprocal = exp(-s)
    assert simplify(unit * reciprocal) == 1

    base_only = 1 + s
    assert base_only.subs(s, 0) == 1
    assert base_only.subs(s, -1) == 0

    symmetric_hostile = 16 * (s - Rational(1, 4)) * (Rational(3, 4) - s)
    assert simplify(symmetric_hostile.subs(s, 1 - s) - symmetric_hostile) == 0
    assert symmetric_hostile.subs(s, Rational(1, 2)) == 1
    assert symmetric_hostile.subs(s, Rational(1, 4)) == 0
    assert symmetric_hostile.subs(s, Rational(3, 4)) == 0
    contaminated = simplify(symmetric_hostile * determinant)
    assert contaminated.subs(s, Rational(1, 4)) == 0
    assert determinant.subs(s, Rational(1, 4)) != 0

    payload = {
        "schema": "marici.kitaev.holomorphic_normalization_unit.v1",
        "status": "pass",
        "valid_unit_fixture": {
            "unit": "exp(s)", "holomorphic_reciprocal": "exp(-s)",
            "product": "1",
        },
        "base_point_hostile": {
            "factor": "1+s", "value_at_0": 1, "inserted_zero": "-1",
        },
        "symmetric_hostile": {
            "factor": "16(s-1/4)(3/4-s)",
            "reflection_invariant": True, "value_at_half": 1,
            "inserted_zeros": ["1/4", "3/4"],
        },
        "typing": "same_zero_divisor_requires_a_holomorphic_unit",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
