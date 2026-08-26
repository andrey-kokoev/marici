#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

from sympy import simplify, symbols

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/reciprocal-sheet-winding.json"


def main():
    z = symbols("z", nonzero=True)
    fixtures = []
    for n in (1, 2, 3, 4):
        plus = z ** n
        minus = z ** (-n)
        assert simplify(plus * minus) == 1
        assert plus.subs(z, 1) == minus.subs(z, 1) == 1
        plus_parity = n % 2
        minus_parity = (-n) % 2
        assert plus_parity == minus_parity
        assert (plus_parity + minus_parity) % 2 == 0
        fixtures.append({
            "winding_pair": [n, -n],
            "combined_winding": 0,
            "combined_product": "1",
            "sheet_cocycle_pair": [plus_parity, minus_parity],
            "sheetwise_square_roots_exist": n % 2 == 0,
        })

    assert simplify((z * z ** -1) - (z ** 2 * z ** -2)) == 0

    payload = {
        "schema": "marici.kitaev.reciprocal_sheet_winding.v1",
        "status": "pass",
        "fixtures": fixtures,
        "scalar_indistinguishability": {
            "odd_pair_product": "1", "even_pair_product": "1",
            "vacuum_values_equal": True,
            "sheetwise_root_existence_differs": True,
        },
        "typing": "combined_closure_does_not_imply_sheetwise_trivialization",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
