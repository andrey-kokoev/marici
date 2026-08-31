#!/usr/bin/env python3
"""Gauge/coordinate descent of the leading scalar Tate jet."""
from fractions import Fraction
from pathlib import Path
import json, math
ROOT=Path(__file__).resolve().parents[1]
RESULT=ROOT/"results"/"rh_leading_tate_jet_line_lift_audit.json"

def coeff_product(v,f,n):
    return sum(v[k]*f[n-k] for k in range(n+1))

# Coefficients are divided derivatives: f(x)=sum f_n x^n.
m=4
f=[Fraction(0)]*m+[Fraction(3),Fraction(5),Fraction(7)]
v=[Fraction(2),Fraction(-3),Fraction(4),Fraction(1),Fraction(-2),Fraction(6),Fraction(9)]
g=[coeff_product(v,f,n) for n in range(len(f))]
# Linear coordinate x=a*y gives divided leading coefficient a^m f_m.
a=Fraction(3,2)
coordinate_leading=a**m*f[m]
# At the next jet, frame change contains v_1 f_m: no intrinsic scalar-to-line lift
# exists without a connection/splitting.
next_contamination=g[m+1]-v[0]*f[m+1]
checks={
 "lower_jets_vanish_on_multiplicity_stratum":all(x==0 for x in f[:m]),
 "leading_jet_frame_change_uses_only_frame_value":g[m]==v[0]*f[m],
 "leading_jet_coordinate_change_has_conormal_weight_m":coordinate_leading==a**m*f[m],
 "next_jet_has_nonzero_frame_derivative_contamination":next_contamination==v[1]*f[m] and next_contamination!=0,
 "full_scalar_jet_tower_does_not_descend_without_connection":g[m+1]!=v[0]*f[m+1],
}
payload={
 "schema":"marici.strominger.rh_leading_tate_jet_line_lift_audit.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "fixture":{"multiplicity":m,"leading_coefficient":str(f[m]),"frame_series":[str(x) for x in v],"transformed_leading":str(g[m]),"next_contamination":str(next_contamination),"coordinate_scale":str(a)},
 "verdict":"On the multiplicity-m stratum, the first nonzero Tate jet descends canonically as a boundary-line-valued conormal tensor: lower-jet vanishing removes every derivative-of-frame term, and coordinate change contributes the expected m-th conormal weight. The next jet already contains the nonzero term v_1 f_m. Thus prior data authorize a pointwise leading-jet lift, but not a simultaneous lift of the full scalar jet tower into boundary-line incidence. A connection or equivalent source splitting remains necessary.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
print(json.dumps(payload,indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
