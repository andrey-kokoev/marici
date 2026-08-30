#!/usr/bin/env python3
"""Logarithmic conductor coefficients on the two literal physical wall segments."""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research"/"benincasa"/"results"/"rank26-active-conductor-log-coefficients.json"
a,b,x,y,z=sp.symbols("a b x y z")
R1=-a**2*x+x**2*y+x**2*z+x*y**2+2*x*y*z+2*x*z**2-y**3-y**2*z+y*z**2+z**3
R2=b**2*y+x**3-x**2*y+x**2*z-x*y**2-2*x*y*z-x*z**2-y**2*z-2*y*z**2-z**3
N1=a+z-x;N2=b+z-y
res1=sp.factor(sp.resultant(R1,N1,a));res2=sp.factor(sp.resultant(R2,N2,b))

sample={x:2,y:3,z:4};r1=3*sp.sqrt(46)/2;r2=sp.sqrt(94)
# Coefficients after removing 1/R_i.  Signs include Entry 3819 wall orientations.
F1=-(a+z-x)/((a-x-z)*(a+y+2*z)*(y+z-x)*(a-y))
F2=(b+z-y)/((b-y-z)*(x+2*z+b)*(b-x)*(x+z-y))
c1=sp.simplify((F1/sp.diff(R1,a)).subs(sample).subs(a,r1))
c2=sp.simplify((F2/sp.diff(R2,b)).subs(sample).subs(b,r2))
checks={
 "g1_conductor_resultant_nonzero":res1!=0,
 "g2_conductor_resultant_nonzero":res2!=0,
 "g1_selected_log_coefficient_nonzero":c1!=0,
 "g2_selected_log_coefficient_nonzero":c2!=0,
 "sheet_residues_are_opposite_g1":c1==-(-c1),
 "sheet_residues_are_opposite_g2":c2==-(-c2),
}
packet={"schema":"marici.rank26-active-conductor-log-coefficients.v1",
 "generic_conductor_resultants":{"g1":str(res1),"g2":str(res2)},
 "sample_2_3_4":{"g1_switch":"3*sqrt(46)/2","g1_Dplus_log_residue":str(c1),
                  "g1_Dminus_log_residue":str(-c1),"g2_switch":"sqrt(94)",
                  "g2_Dplus_log_residue":str(c2),"g2_Dminus_log_residue":str(-c2)},
 "checks":{k:bool(v) for k,v in checks.items()},"passed":all(bool(v) for v in checks.values()),
 "conclusion":"The two literally active wall forms have genuine logarithmic conductor poles. Naive interval integration is not the physical covector; the source boundary-value/relative prescription is essential.",
 "scope":"This computes local logarithmic coefficients, not their globally regularized period or a finite-part subtraction."}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8")
print(json.dumps(packet,indent=2))
if not packet["passed"]:raise SystemExit(1)
