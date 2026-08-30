#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

from sympy import diff, simplify, symbols

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/normalization-unit-winding.json"


def logarithmic_residue(power, z):
    unit = z ** power
    return simplify(z * diff(unit, z) / unit)


def main():
    z = symbols("z", nonzero=True)
    winding = {}
    for n in (-3, -1, 0, 1, 2, 4):
        assert logarithmic_residue(n, z) == n
        assert (z ** n).subs(z, 1) == 1
        winding[str(n)] = {
            "vacuum_value": 1,
            "winding": n,
            "sheet_cocycle": n % 2,
            "square_root_exists": n % 2 == 0,
        }

    for m, n in ((1, 2), (-1, 4), (3, 5)):
        assert logarithmic_residue(m + n, z) == (
            logarithmic_residue(m, z) + logarithmic_residue(n, z)
        )
    assert logarithmic_residue(-3, z) == -logarithmic_residue(3, z)
    assert (-3) % 2 == 3 % 2

    payload = {
        "schema": "marici.kitaev.normalization_unit_winding.v1",
        "status": "pass",
        "annular_monomial_fixtures": winding,
        "composition": "nu(uv)=nu(u)+nu(v)",
        "reciprocal": "nu(u^-1)=-nu(u)",
        "sheet_cocycle": "nu mod 2",
        "vacuum_rule": "selects_root_sign_only_after_even_winding",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
