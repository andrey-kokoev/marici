"""Exact incidence audit for conductor and elliptic signed-energy branches."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "conductor-elliptic-physical-incidence.json"

E, x, y = sp.symbols("E x y")
X3 = E - x - y

delta1 = 4 * x * (x * y**2 + 2 * E * x * y - E**2 * (x + 2 * y - E))
delta2 = 4 * y * (x**2 * y + 2 * E * x * y - E**2 * (2 * x + y - E))

letters = {
    "ell1": 2 * x - E,
    "ell2": E - 2 * y,
    "ell3": 2 * (x + y) - E,
    "ell4": E,
}
branch_E = {
    "ell1": 2 * x,
    "ell2": 2 * y,
    "ell3": 2 * (x + y),
    "ell4": 0,
}

expected = {
    "ell1": (4 * x**2 * (2 * x - y) ** 2, 4 * x**2 * y**2),
    "ell2": (4 * x**2 * y**2, 4 * y**2 * (x - 2 * y) ** 2),
    "ell3": (4 * x**2 * (2 * x + 3 * y) ** 2, 4 * y**2 * (3 * x + 2 * y) ** 2),
    "ell4": (4 * x**2 * y**2, 4 * x**2 * y**2),
}

restrictions = {}
for label, value in branch_E.items():
    d1 = sp.factor(delta1.subs(E, value))
    d2 = sp.factor(delta2.subs(E, value))
    assert sp.expand(d1 - expected[label][0]) == 0
    assert sp.expand(d2 - expected[label][1]) == 0
    restrictions[label] = {
        "E": str(value),
        "Delta1": str(d1),
        "Delta2": str(d2),
        "X3": str(sp.factor(X3.subs(E, value))),
    }

# Elimination checks preserve occurrence labels and independently reproduce
# the product of the two branchwise intersection factors.
A = sp.expand(letters["ell1"] * letters["ell2"])
B = sp.expand(letters["ell3"] * letters["ell4"])
resultants = {
    "Res_E_Delta1_A": sp.factor(sp.resultant(delta1, A, E)),
    "Res_E_Delta2_A": sp.factor(sp.resultant(delta2, A, E)),
    "Res_E_Delta1_B": sp.factor(sp.resultant(delta1, B, E)),
    "Res_E_Delta2_B": sp.factor(sp.resultant(delta2, B, E)),
}
assert resultants["Res_E_Delta1_A"] == -16 * x**4 * y**2 * (2 * x - y) ** 2
assert resultants["Res_E_Delta2_A"] == -16 * x**2 * y**4 * (x - 2 * y) ** 2
assert resultants["Res_E_Delta1_B"] == -16 * x**4 * y**2 * (2 * x + 3 * y) ** 2
assert resultants["Res_E_Delta2_B"] == -16 * x**2 * y**4 * (3 * x + 2 * y) ** 2

# Nonsoft collision roots are incompatible with x>0,y>0,X3>0:
# ell1/Delta1 gives y=2x and hence X3=-x;
# ell2/Delta2 gives x=2y and hence X3=-y;
# ell3 roots force opposite signs.
physical_obstructions = {
    "ell1_Delta1": {
        "root": "y=2*x",
        "X3_on_root": str(sp.factor(X3.subs({E: 2 * x, y: 2 * x}))),
        "violates": "X3>0 for x>0",
    },
    "ell2_Delta2": {
        "root": "x=2*y",
        "X3_on_root": str(sp.factor(X3.subs({E: 2 * y, x: 2 * y}))),
        "violates": "X3>0 for y>0",
    },
    "ell3_Delta1": {
        "root": "2*x+3*y=0",
        "violates": "x>0 and y>0",
    },
    "ell3_Delta2": {
        "root": "3*x+2*y=0",
        "violates": "x>0 and y>0",
    },
}
assert physical_obstructions["ell1_Delta1"]["X3_on_root"] == "-x"
assert physical_obstructions["ell2_Delta2"]["X3_on_root"] == "-y"

# Deliberate-failure witness: the algebraic collision locus is genuinely
# nonempty outside the physical chamber; it is not being erased.
hostile_point = {x: 1, y: 2, E: 2}
assert letters["ell1"].subs(hostile_point) == 0
assert delta1.subs(hostile_point) == 0
assert X3.subs(hostile_point) == -1

result = {
    "schema": "marici.benincasa.conductor-elliptic-physical-incidence.v1",
    "signed_energy_letters": {key: str(value) for key, value in letters.items()},
    "elliptic_factors": {"A": str(A), "B": str(B)},
    "branch_restrictions": restrictions,
    "resultants": {key: str(value) for key, value in resultants.items()},
    "physical_obstructions": physical_obstructions,
    "hostile_nonphysical_collision": {
        "point": {"x": 1, "y": 2, "E": 2, "X3": -1},
        "ell1": 0,
        "Delta1": 0,
    },
    "conclusion": {
        "nonsoft_conductor_elliptic_collisions_in_positive_chamber": 0,
        "physical_intersection_support": ["x=0", "y=0"],
        "physical_intersections_closed_by_entry_2394": True,
        "new_carrier_datum": False,
    },
    "scope": (
        "Exact support/physical-incidence theorem for the homogeneous signed-energy "
        "elliptic branches; it does not classify analytically continued nonphysical "
        "sheets as physical readouts."
    ),
}

OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result["conclusion"], sort_keys=True))
