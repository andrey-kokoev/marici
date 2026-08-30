"""Exact soft-normal compatibility of the RS-3 unequal-energy path."""

import json
from pathlib import Path

import sympy as sp

eta, B, zeta = sp.symbols("eta B zeta")

# Source-normalized path from the equal-energy point eta=1 to the X2-soft
# conductor eta=0, with X1 and X3 frozen.
X1, X2, X3 = sp.Integer(1), eta, sp.Integer(1)
u = sp.cancel((X1 + X2 + X3) / X1)
v = sp.cancel((X1 + X2 - X3) / X1)
assert u == eta + 2
assert v == eta
assert (u.subs(eta, 1), v.subs(eta, 1)) == (3, 1)
assert (u.subs(eta, 0), v.subs(eta, 0)) == (2, 0)

asymmetry = sp.expand(X2 - X3)
asymmetry_jet = sp.diff(asymmetry, eta)
assert asymmetry_jet == 1

# The normalized node equation from the resolved soft center, up to its
# already frozen nonzero source unit.
node = sp.expand(eta * (B - 1))
gysin_normal = sp.diff(node, eta).subs(eta, 0)
assert gysin_normal == B - 1

# Dividing only by the declared generic-conductor unit gives multiplicity one.
gysin_multiplicity = sp.cancel(gysin_normal / (B - 1))
assert gysin_multiplicity == 1

# Negative control: a path tangent to X2=0 changes X1 but has no X2-normal
# component and therefore cannot activate the soft Gysin class.
X1_tan, X2_tan, X3_tan = 1 + zeta, sp.Integer(0), sp.Integer(1)
soft_normal_tangent = sp.diff(X2_tan, zeta)
assert soft_normal_tangent == 0

result = {
    "schema": "marici.rs3.unequal-energy-soft-normal-compatibility.v1",
    "status": "passed",
    "source_path": {"X1": "1", "X2": "eta", "X3": "1"},
    "base_path": {"u": str(u), "v": str(v)},
    "equal_energy_endpoint": {"eta": 1, "u": 3, "v": 1},
    "soft_endpoint": {"eta": 0, "u": 2, "v": 0},
    "unequal_energy_cotangent": "d(X2-X3)=deta",
    "node_smoothing": str(node),
    "gysin_normal_derivative": str(gysin_normal),
    "generic_conductor_locus": "B-1 != 0",
    "gysin_multiplicity": int(gysin_multiplicity),
    "coefficient_transport_status": "not computed",
    "negative_control": {
        "path": {"X1": "1+zeta", "X2": "0", "X3": "1"},
        "soft_normal_component": int(soft_normal_tangent),
    },
    "verdict": (
        "The source-normalized unequal-energy path reaches the known soft center "
        "in its unit Gysin normal direction. Transport of the Tate coefficient "
        "class along the path remains a separate Gauss-Manin gate."
    ),
}

out = Path(__file__).parents[1] / "results" / "rs3-unequal-energy-soft-normal-compatibility.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
