#!/usr/bin/env python3
"""Show that target Betti normalization does not select an extension scalar."""

import json
from pathlib import Path

import sympy as sp


c1, c2 = sp.symbols("c1 c2")

# Basis (q0,e6), with extension connection lower-left c*omega.
A1 = sp.Matrix([[0, 0], [c1, 0]])
A2 = sp.Matrix([[0, 0], [c2, 0]])

# The physical node pairing of Entry 1134 is a functional on the e6 target.
phi = sp.Matrix([[0, sp.Rational(1, 4)]])
e6 = sp.Matrix([0, 1])

# Residue difference is invariant under boundary-regular rational gauges; two
# scalar multiples are equal only when their coefficients agree.
residue_difference = sp.simplify((A1 - A2)[1, 0])

checks = {
    "same_target_pairing_family_1": (phi * e6)[0] == sp.Rational(1, 4),
    "same_target_pairing_family_2": (phi * e6)[0] == sp.Rational(1, 4),
    "extension_difference_is_c1_minus_c2": residue_difference == c1 - c2,
    "distinct_scalars_give_distinct_boundary_class": sp.solve(
        [residue_difference], [c1], dict=True
    ) == [{c1: c2}],
}

packet = {
    "schema": "marici.benincasa.target_betti_pairing_extension_nonselection.v1",
    "extension": "0 -> <e6> -> E_c -> <q0> -> 0",
    "connection_family": "A_c = [[0,0],[c*omega,0]]",
    "physical_target_pairing": "phi(e6)=1/4",
    "checks": checks,
    "verdict": (
        "The physical node pairing canonically normalizes the e6 target line "
        "but cannot select the extension amplitude c."
    ),
    "required_selector": (
        "A physical or integral comparison involving a lift of q0 into the "
        "rank-twelve object, followed by e6 pairing."
    ),
}

if not all(checks.values()):
    raise SystemExit(f"failed checks: {[key for key, ok in checks.items() if not ok]}")

out = Path(__file__).resolve().parents[1] / "results" / "target_betti_pairing_extension_nonselection.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
