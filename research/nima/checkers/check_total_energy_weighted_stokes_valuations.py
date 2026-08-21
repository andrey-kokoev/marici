#!/usr/bin/env python3
"""Exact E-adic valuations of the three weighted tangency Stokes ratios."""
import hashlib
import json
from pathlib import Path

import sympy as sp

E, x, y, z = sp.symbols("E x y z")

NUMERATORS = {
    "g1": x**3-x**2*y-3*x**2*z-x*y**2-2*x*y*z-x*z**2+y**3+y**2*z-y*z**2-z**3,
    "g2": x**3-x**2*y+x**2*z-x*y**2-2*x*y*z-x*z**2+y**3-3*y**2*z-y*z**2-z**3,
    "g3": (x+y+z)**2,
}
DENOMINATORS = {
    "g1": (y+z)**2*(x-y-z)**4*(x-y+z)**2*(x+y-z)*(x+y+z)**2,
    "g2": (x+z)**2*(x-y-z)**2*(x-y+z)**4*(x+y-z)*(x+y+z)**2,
    "g3": (x+z)**2*(y+z)**2*(x-y-z)**2*(x-y+z)**2*(x+y-z)**2*(x+y+z)**2,
}


def valuation(expression):
    polynomial = sp.Poly(sp.expand(expression), E)
    return min(monomial[0] for monomial, coefficient in polynomial.terms() if coefficient)


def main():
    root = Path(__file__).resolve().parents[3]
    expected = {
        "g1": (0, 2, -2, "1/(32*x**4*y**2)"),
        "g2": (0, 2, -2, "1/(32*x**2*y**4)"),
        "g3": (2, 2, 0, "1/(64*x**4*y**4*(x + y)**2)"),
    }
    rows = {}
    for name in ("g1", "g2", "g3"):
        numerator = sp.factor(NUMERATORS[name].subs(z, E-x-y))
        denominator = sp.factor(DENOMINATORS[name].subs(z, E-x-y))
        numerator_order = valuation(numerator)
        denominator_order = valuation(denominator)
        ratio_order = numerator_order-denominator_order
        leading = sp.factor(sp.limit(E**(-ratio_order)*numerator/denominator, E, 0))
        assert (numerator_order, denominator_order, ratio_order, str(leading)) == expected[name]
        rows[name] = {
            "numerator_order": numerator_order,
            "denominator_order": denominator_order,
            "raw_ratio_order": ratio_order,
            "normalized_leading_coefficient": str(leading),
        }
    leading_values = [sp.sympify(rows[name]["normalized_leading_coefficient"])
                      for name in ("g1", "g2", "g3")]
    assert sp.factor(leading_values[0].subs({x: y, y: x}, simultaneous=True)
                     - leading_values[1]) == 0
    determinant = sp.factor(sp.prod(leading_values))
    assert determinant == 1/(65536*x**10*y**10*(x+y)**2)
    result = {
        "schema": "marici.nima.total_energy_weighted_stokes_valuations.v1",
        "passed": True,
        "specialization": "z=E-x-y, E->0",
        "rows": rows,
        "source_swap_exchanges_side_rows": True,
        "normalized_pairing_determinant": str(determinant),
        "normalized_pairing_rank": 3,
        "interpretation": "the derived E^2 side-wall normalization gives a source-swap-equivariant perfect diagonal pairing on W3; transport to T7 still requires the connecting complex",
        "scope": "valuation of the exact numerator/denominator resultants; not yet a chain-level normalized supported pairing",
    }
    path = root / "research/nima/results/total-energy-weighted-stokes-valuations.json"
    payload = path.read_text(encoding="utf-8")
    assert json.loads(payload) == result
    print(json.dumps({"passed": True, "orders": [-2, -2, 0],
                      "sha256": hashlib.sha256(payload.encode()).hexdigest().upper()}))


if __name__ == "__main__":
    main()
