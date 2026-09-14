#!/usr/bin/env python3
"""Bounded gate for the reflected marked period square."""
import json
from pathlib import Path

R=Path(__file__).resolve().parents[3]
g=json.loads((R/"research/voevodsky/results/global_del_pezzo_double_cover.json").read_text())
m=json.loads((R/"research/benincasa/full-marked-total-energy-nilpotent.json").read_text())
a=m["blocks"]["algebraic_extension"]
serialized=json.dumps(m)
checks={
 "global_rb_exists":g["checks"]["b_reflection_global"],
 "marked_matrix_exists":len(a["matrix"])==4 and all(len(row)==3 for row in a["matrix"]),
 "top_column_e6_only":[row[2] for row in a["matrix"]]==["0","0","1/(8*(x+y))","0"],
 "marked_source_rb_absent":"r_b" not in serialized and "b_reflection" not in serialized,
 "reflected_extension_absent":"reflected" not in serialized,
 "intertwiner_absent":"intertw" not in serialized,
 "integral_betti_normal_form_open":"integral normal form of the rank-twelve logarithmic nearby-cycle lattice" in m["remaining"],
}
assert all(checks.values()),checks
out={
 "schema":"marici.voevodsky.reflected-marked-period-interface-gate.v1",
 "passed":True,
 "constructed":{"global_r_b":True,"original_marked_extension_matrix":True,"original_top_column":True},
 "missing":{"r_b_on_marked_source":True,"r_b_on_target_coordinates":True,"reflected_extension_matrix":True,"reflection_intertwiner":True,"reflected_integral_Betti_column":True},
 "first_required_object":"labelled marked-reflection commutative square A_minus rM = rH A_plus",
 "decision_entry":"v0 coordinate of the transported top/component-difference column",
 "forbidden_shortcut":"the displayed coefficients are b-independent, but the basis labels are not proved r_b-invariant",
 "checks":checks,
}
p=R/"research/voevodsky/results/reflected_marked_period_interface_gate.json";p.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"passed":True,"reflected_period_column_available":False,"first_missing":"marked reflection square"}))
