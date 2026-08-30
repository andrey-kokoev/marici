#!/usr/bin/env python3
"""Exact square roots controlling physical sheet switches on three shared walls."""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research"/"benincasa"/"results"/"rank26-shared-wall-sheet-switch-polynomials.json"
a,b,x,y,z=sp.symbols("a b x y z")
E=x+y+z;c=-E
K=(x**2*a**4-a**2*b**2*(x**2+y**2-z**2)+y**2*b**4
   +a**2*x**2*(x**2-y**2-z**2)+c**2*a**2*(y**2-x**2-z**2)
   +b**2*y**2*(y**2-x**2-z**2)+c**2*b**2*(x**2-y**2-z**2)
   +z**2*c**4+c**2*z**2*(z**2-x**2-y**2)+z**2*x**2*y**2)
walls={"g1":(b,y+z,a),"g2":(a,x+z,b),"g3":(b,-a-z,a)}
rows=[];checks={}
for label,(variable,value,tangent) in walls.items():
    restricted=sp.factor(K.subs(variable,value))
    coeff, factors=sp.factor_list(restricted)
    assert coeff==1 and len(factors)==1 and factors[0][1]==2
    root=sp.factor(factors[0][0])
    discriminant=sp.factor(sp.discriminant(root,tangent))
    checks[f"{label}_restriction_is_square"]=sp.expand(restricted-root**2)==0
    checks[f"{label}_root_is_quadratic"]=sp.Poly(root,tangent).degree()==2
    rows.append({"wall":label,"substitution":f"{variable}={value}","tangent":str(tangent),
                 "square_root_R":str(root),"root_discriminant":str(discriminant)})

sample={x:2,y:3,z:4}
for row in rows:
    tangent=a if row["tangent"]=="a" else b
    root=sp.sympify(row["square_root_R"])
    row["sample_2_3_4"]={"R":str(sp.factor(root.subs(sample))),
                         "switch_points":[str(v) for v in sp.solve(root.subs(sample),tangent)]}

checks["three_source_face_roots_derived"]=len(rows)==3
packet={"schema":"marici.rank26-shared-wall-sheet-switch-polynomials.v1",
        "surface":"W^2=K","positive_sheet_rule":"W=abs(R_i) on wall i",
        "walls":rows,"checks":{k:bool(v) for k,v in checks.items()},
        "passed":all(bool(v) for v in checks.values()),
        "scope":"The roots locate every possible sheet switch on each shared wall. They do not select an analytically continued wall segment or define independent occurrence-wall periods."}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8")
print(json.dumps(packet,indent=2))
if not packet["passed"]:raise SystemExit(1)
