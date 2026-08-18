"""Exact denominator-level q_G12 residue of the two physical source summands."""

from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    c, a, b, x, y, z = sp.symbols("c a b x y z")
    energy = x + y + z
    denominators = {
        "q_g1": c + b + x,
        "q_g2": c + a + y,
        "q_g3": a + b + z,
        "q_G12": c + energy,
        "q_g23": c + b + y + z,
        "q_g31": c + a + z + x,
    }
    residue_substitution = {c: -energy}
    restricted = {
        name: sp.expand(polynomial.subs(residue_substitution))
        for name, polynomial in denominators.items()
        if name != "q_G12"
    }
    expected = {
        "q_g1": b - y - z,
        "q_g2": a - x - z,
        "q_g3": a + b + z,
        "q_g23": b - x,
        "q_g31": a - y,
    }
    checks = {name: sp.expand(restricted[name] - value) == 0 for name, value in expected.items()}
    result = {
        "schema": "marici.benincasa.physical-five-pole-g12-residue.v1",
        "fiber_orientation": "dc wedge da wedge db",
        "residue_coordinate": "q_G12=c+x+y+z",
        "residue_jacobian_dc": 1,
        "residue_orientation": "da wedge db",
        "restricted_denominators": {name: str(value) for name, value in restricted.items()},
        "summand_g23": ["q_g1", "q_g2", "q_g3", "q_g23"],
        "summand_g31": ["q_g1", "q_g2", "q_g3", "q_g31"],
        "source_combination": "summand_g23 + summand_g31",
        "all_symbolic_checks_pass": all(checks.values()),
        "scope": "denominator-level Poincare residue; no master-space or Gysin projection is inferred",
    }
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
