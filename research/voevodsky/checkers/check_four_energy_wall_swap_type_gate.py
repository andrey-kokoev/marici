#!/usr/bin/env python3
"""Gate identification of energy branch vertices with conductor wall swaps."""
import json
from pathlib import Path
import sympy as sp

R = Path(__file__).resolve().parents[3]
d = json.loads((R / "research/benincasa/conductor-elliptic-physical-incidence.json").read_text())
x, y = sp.symbols("x y", positive=True)
expected = {
    "ell1": (4*x**2*(2*x-y)**2, 4*x**2*y**2),
    "ell2": (4*x**2*y**2, 4*y**2*(x-2*y)**2),
    "ell3": (4*x**2*(2*x+3*y)**2, 4*y**2*(3*x+2*y)**2),
    "ell4": (4*x**2*y**2, 4*x**2*y**2),
}
parsed = {
    k: (sp.sympify(v["Delta1"], locals={"x": x, "y": y}), sp.sympify(v["Delta2"], locals={"x": x, "y": y}))
    for k, v in d["branch_restrictions"].items()
}
checks = {
    "restriction_table_exact": all(sp.simplify(parsed[k][i]-expected[k][i]) == 0 for k in expected for i in (0,1)),
    "generic_test_point_nonzero": all(v.subs({x: 3, y: 5}) != 0 for pair in parsed.values() for v in pair),
    "reported_positive_nonsoft_collisions_zero": d["conclusion"]["nonsoft_conductor_elliptic_collisions_in_positive_chamber"] == 0,
    "source_declares_no_new_carrier_datum": d["conclusion"]["new_carrier_datum"] is False,
}
assert all(checks.values()), checks
out = {
    "schema": "marici.voevodsky.four-energy-wall-swap-type-gate.v1",
    "passed": True,
    "energy_vertices": ["0", "2x", "2y", "2(x+y)"],
    "wall_swap_assignment_derived": False,
    "reason": "the conductor discriminants are generically nonzero on all four signed-energy branches in the positive chamber",
    "surviving_formal_identity": "(T2*s_plus-T1*s_plus)/2=s_minus inside the separate conductor monodromy module",
    "required_comparison": "based lifted cycle on the total-energy elliptic cover -> conductor wall-monodromy module",
    "checks": checks,
}
p = R / "research/voevodsky/results/four_energy_wall_swap_type_gate.json"
p.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({"passed": True, "energy_vertices_label_wall_swaps": False, "comparison_missing": True}))
