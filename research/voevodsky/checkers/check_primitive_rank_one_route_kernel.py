#!/usr/bin/env python3
"""Integral normal form for the anchored rank-three to rank-two readout."""
import json
from math import gcd
from pathlib import Path
import sympy as sp

R = Path(__file__).resolve().parents[3]
a,b,u,v = sp.symbols("a b u v", integer=True)
Q = sp.Matrix([[1,u,v],[0,a,b]])
# Integral target-row representative changes clear anchored e6 leakage.
C = sp.Matrix([[1,-u,-v],[0,1,0],[0,0,1]])
Qred = Q*C
# Exact representative cases test zero, indexed, and primitive behavior.
cases = {
 "zero": (0,0),
 "indexed": (2,4),
 "primitive": (2,3),
}
def facts(pair):
 aa,bb=pair;g=gcd(abs(aa),abs(bb));return {"rank":1+(pair!=(0,0)),"image_index":g if g else None,"kernel_generator":None if not g else [0,bb//g,-aa//g]}
observed={k:facts(p) for k,p in cases.items()}
checks={
 "anchored_leakage_clears": Qred == sp.Matrix([[1,0,0],[0,a,b]]),
 "zero_case_rank_one": observed["zero"]["rank"]==1,
 "indexed_case_index_two": observed["indexed"]["rank"]==2 and observed["indexed"]["image_index"]==2,
 "primitive_case_surjective": observed["primitive"]["rank"]==2 and observed["primitive"]["image_index"]==1,
 "primitive_kernel": observed["primitive"]["kernel_generator"]==[0,3,-2],
 "kernel_annihilated": sp.Matrix([[1,0,0],[0,2,3]])*sp.Matrix([0,3,-2])==sp.zeros(2,1),
}
assert all(checks.values()),checks
out={
 "schema":"marici.voevodsky.primitive-rank-one-route-kernel.v1",
 "passed":True,
 "normal_form":[[1,0,0],[0,"a","b"]],
 "full_rank_condition":"(a,b)!=(0,0)",
 "primitive_image_condition":"gcd(a,b)=1",
 "route_kernel_generator":"b*beta12-a*beta13 when gcd(a,b)=1",
 "cases":observed,
 "information_flow":"anchored A1^3 -> quotient by primitive route kernel -> span(e6,v_alg)",
 "remaining":"derive a,b and the physical nullity of the kernel from the period comparison",
 "checks":checks,
}
p=R/"research/voevodsky/results/primitive_rank_one_route_kernel.json";p.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"passed":True,"essential_data":["a","b"],"acceptance":"gcd(a,b)=1"}))
