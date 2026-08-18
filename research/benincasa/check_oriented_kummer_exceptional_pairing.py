"""Pair the total-energy Kummer sheets with the source Leray boundary."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
x, y, lam = sp.symbols("x y lambda", nonzero=True)


def main() -> None:
    nearby = json.loads((HERE / "et-cut-nearby-normal-form.json").read_text())
    boundary = nearby["canonical_boundary_vector"]
    functional = nearby["exceptional_period_functional_e1_to_e9"]

    assert boundary == [-1, 1]
    assert functional == [0, 0, "y", 0, "x", 1, 0, 0, 0]
    assert nearby["exceptional_functional_gysin_image"] == 0

    coefficient = 1 / (16 * lam * x**2 * y**2)
    sheet_values = [-coefficient, coefficient]
    oriented_value = sp.factor(sum(a * b for a, b in zip(boundary, sheet_values)))
    symmetric_value = sp.factor(sum(sheet_values))

    assert sp.factor(oriented_value - 1 / (8 * lam * x**2 * y**2)) == 0
    assert symmetric_value == 0

    print(json.dumps({
        "schema": "marici.oriented-kummer-exceptional-pairing.v1",
        "boundary_vector": boundary,
        "regularized_sheet_values": ["-c", "+c"],
        "c": "1/(16*lambda*x^2*y^2)",
        "oriented_pairing": "1/(8*lambda*x^2*y^2)",
        "symmetric_pairing": "0",
        "exceptional_functional": functional,
        "infinity_gysin_image": 0,
        "target_sector": "dual algebraic Tate/Kummer kernel",
        "elliptic_nearby_grade_coupling": 0,
        "quartic_support": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
