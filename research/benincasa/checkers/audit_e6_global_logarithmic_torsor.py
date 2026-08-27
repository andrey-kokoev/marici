#!/usr/bin/env python3
"""Audit the global rational gauge class of the candidate e6 lift."""

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa" / ".tmp_sympy"))

import sympy as sp


u, v = sp.symbols("u v")
OUT = ROOT / "research" / "benincasa" / "results" / "e6_global_logarithmic_torsor.json"


def main() -> None:
    absolute = json.loads(
        (ROOT / "research" / "benincasa" / "bivariate_soft_gram_connection.json").read_text(encoding="utf-8")
    )
    quotient = json.loads(
        (ROOT / "research" / "benincasa" / "marked-wall-quotient-connection.json").read_text(encoding="utf-8")
    )

    a_e6_v = sp.sympify(absolute["connection_v"][5][5])
    a_q0_v = sp.sympify(quotient["v"]["alpha"])
    a_e6_corner = sp.factor(a_e6_v.subs(u, 0))
    a_q0_corner = sp.factor(a_q0_v)
    assert sp.cancel(a_e6_corner - a_q0_corner) == 0

    c2 = -sp.Rational(1, 8)
    candidate = 1 / (4 * v * (v - 2))
    primitive_log = sp.diff(sp.log(v / (v - 2)), v)
    assert sp.cancel(candidate - c2 * primitive_log) == 0

    residue0 = sp.residue(candidate, v, 0)
    residue2 = sp.residue(candidate, v, 2)
    normalized0 = sp.factor(residue0 / c2)
    normalized2 = sp.factor(residue2 / c2)
    assert (residue0, residue2) == (-sp.Rational(1, 8), sp.Rational(1, 8))
    assert (normalized0, normalized2) == (1, -1)

    # A derivative of a rational function has zero residue at every finite pole.
    # Nonzero residues therefore obstruct removal by a rational triangular gauge.
    rationally_exact = residue0 == 0 and residue2 == 0
    assert not rationally_exact

    output = {
        "schema": "marici.benincasa.e6_global_logarithmic_torsor.v1",
        "status": "pass",
        "e6_v_connection_at_u0": str(a_e6_corner),
        "qtop_v_connection_at_u0": str(a_q0_corner),
        "hom_connection_difference": "0",
        "canonical_double_pole_scale": str(c2),
        "candidate_principal_lift": str(sp.factor(candidate)),
        "factorization": "candidate=C2*dlog(v/(v-2))",
        "residues": {"v=0": str(residue0), "v=2": str(residue2)},
        "residues_normalized_by_C2": {"v=0": str(normalized0), "v=2": str(normalized2)},
        "rational_triangular_gauge_exact": False,
        "global_class": "primitive logarithmic generator on P1 minus {0,2,infinity}, scaled by C2",
        "scope": "exact candidate-class theorem; source selection of this global class remains unproved",
    }
    OUT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
