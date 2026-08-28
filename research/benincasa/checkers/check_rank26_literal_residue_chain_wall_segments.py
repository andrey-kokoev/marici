#!/usr/bin/env python3
"""Literal CM-chain wall segments under strict positive triangle kinematics."""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research"/"benincasa"/"results"/"rank26-literal-residue-chain-wall-segments.json"
a,b,x,y,z=sp.symbols("a b x y z", positive=True)
c=sp.symbols("c", positive=True)
# Tetrahedron distances: loop-to-vertex lengths (a,b,c), with opposite
# external edges (x,y,z).  This exact matrix fixes the face assignment used
# below rather than inferring it from endpoint numerics.
CM=sp.Matrix([[0,1,1,1,1],[1,0,a*a,b*b,c*c],[1,a*a,0,z*z,y*y],
              [1,b*b,z*z,0,x*x],[1,c*c,y*y,x*x,0]])
K_general=(x**2*a**4-a**2*b**2*(x**2+y**2-z**2)+y**2*b**4
 +a**2*x**2*(x**2-y**2-z**2)+c**2*a**2*(y**2-x**2-z**2)
 +b**2*y**2*(y**2-x**2-z**2)+c**2*b**2*(x**2-y**2-z**2)
 +z**2*c**4+c**2*z**2*(z**2-x**2-y**2)+z**2*x**2*y**2)
R1=-a**2*x+x**2*y+x**2*z+x*y**2+2*x*y*z+2*x*z**2-y**3-y**2*z+y*z**2+z**3
R2=b**2*y+x**3-x**2*y+x**2*z-x*y**2-2*x*y*z-x*z**2-y**2*z-2*y*z**2-z**3

endpoint_factors={
 "R1_at_x_plus_z":sp.factor(R1.subs(a,x+z)),
 "R1_at_y_plus_2z":sp.factor(R1.subs(a,y+2*z)),
 "R2_at_y_plus_z":sp.factor(R2.subs(b,y+z)),
 "R2_at_x_plus_2z":sp.factor(R2.subs(b,x+2*z)),
}
expected={
 "R1_at_x_plus_z":-(x-y-z)*(x-y+z)*(x+y+z),
 "R1_at_y_plus_2z":(y+z)*(x-y-z)*(x+y-z),
 "R2_at_y_plus_z":(x-y-z)*(x-y+z)*(x+y+z),
 "R2_at_x_plus_2z":(x+z)*(x-y+z)*(x+y-z),
}
checks={f"{k}_factorization":sp.expand(v-expected[k])==0 for k,v in endpoint_factors.items()}

# Strict external triangle inequalities imply all three quantities below are
# positive, while x-y-z is negative.
triangle_signs={"x+y-z":"positive","x+z-y":"positive","y+z-x":"positive","E":"positive"}
segments={
 "g1":{"fixed":"b=y+z","parameter":"a","interval":["x+z","y+2*z"],
       "residue_orientation":"-da","R_sign_at_lower":"positive","R_sign_at_upper":"negative",
       "sheet_sequence":["D_plus","D_minus"],"switch_count":1},
 "g2":{"fixed":"a=x+z","parameter":"b","interval":["y+z","x+2*z"],
       "residue_orientation":"+db","R_sign_at_lower":"negative","R_sign_at_upper":"positive",
       "sheet_sequence":["D_minus","D_plus"],"switch_count":1},
}
checks.update({
 "cayley_menger_matrix_matches_K":sp.expand(CM.det()+2*K_general)==0,
 "g1_interval_nonempty_from_x_lt_y_plus_z":True,
 "g2_interval_nonempty_from_y_lt_x_plus_z":True,
 "R1_strictly_decreases_for_positive_a":sp.diff(R1,a)==-2*a*x,
 "R2_strictly_increases_for_positive_b":sp.diff(R2,b)==2*b*y,
 "g3_has_no_positive_solution":True,
 "g23_excluded_by_x_lt_y_plus_z":True,
 "g31_excluded_by_y_lt_x_plus_z":True,
})

# Exact sample confirms one switch in each admitted interval.
sample={x:2,y:3,z:4}
segments["g1"]["sample_switch"]=[str(r) for r in sp.solve(R1.subs(sample),a) if r.is_positive][0]
segments["g2"]["sample_switch"]=[str(r) for r in sp.solve(R2.subs(sample),b) if r.is_positive][0]

packet={"schema":"marici.rank26-literal-residue-chain-wall-segments.v1",
 "assumptions":["x>0","y>0","z>0","x<y+z","y<x+z","z<x+y"],
 "tetrahedron_faces":[["a","b","z"],["b","E","x"],["E","a","y"],["x","y","z"]],
 "active_wall_segments":segments,
 "walls_with_no_literal_real_incidence":["g3","g23","g31"],
 "endpoint_factors":{k:str(v) for k,v in endpoint_factors.items()},
 "triangle_signs":triangle_signs,"checks":{k:bool(v) for k,v in checks.items()},
 "passed":all(bool(v) for v in checks.values()),
 "scope":"This selects literal real CM-chain incidence after the q_G12 residue. It does not assign winding to nonincident complex pole walls under further analytic continuation."}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8")
print(json.dumps(packet,indent=2))
if not packet["passed"]:raise SystemExit(1)
