#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

from sympy import Rational, simplify, symbols

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/small-norm-unit-compiler.json"


def main():
    z = symbols("z")
    safe = 1 + z / 2
    assert safe.subs(z, 0) == 1
    assert safe.subs(z, -2) == 0
    safe_q = Rational(1, 2)
    assert 1 / (1 - safe_q) == 2

    collapse = []
    for n in (2, 4, 8, 16):
        u = 1 - (1 - Rational(1, n)) * z
        assert u.subs(z, 0) == 1
        q = 1 - Rational(1, n)
        boundary_value = simplify(u.subs(z, 1))
        assert boundary_value == Rational(1, n)
        assert 1 / boundary_value == n
        collapse.append({"cutoff": n, "vacuum_value": 1,
                         "distance_to_unit": str(q),
                         "inverse_norm": n,
                         "boundary_value": str(boundary_value)})

    limit = 1 - z
    assert limit.subs(z, 0) == 1
    assert limit.subs(z, 1) == 0

    payload = {
        "schema": "marici.kitaev.small_norm_unit_compiler.v1",
        "status": "pass",
        "safe_fixture": {
            "unit": "1+z/2", "domain": "closed unit disk",
            "distance_to_vacuum_unit": "1/2",
            "inverse_norm_bound": 2, "zero_outside_domain": "-2",
        },
        "nonuniform_completion_hostile": collapse,
        "limit": {"unit": "1-z", "vacuum_value": 1,
                  "boundary_zero": "z=1", "invertible_in_disk_algebra": False},
        "compiler_outputs": ["holomorphic_inverse", "canonical_logarithm",
                             "zero_winding", "all_finite_root_frames"],
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
