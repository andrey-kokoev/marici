#!/usr/bin/env python3
"""Attempt bounded rational reconstruction of one stable barcode row from two primes."""
from __future__ import annotations
from fractions import Fraction
from math import gcd,isqrt
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; R=ROOT/"research"/"benincasa"/"results"
pack=[json.loads((R/f"interaction-net-barcode-basis-export-p{p}.json").read_text()) for p in (32003,32009)]
p1,p2=[x["prime"] for x in pack]; M=p1*p2; B=isqrt(M//2)
rows=[x["adapted_depth3_quotient_basis"]["first_death_rows"][0] for x in pack]
assert rows[0]["indices"]==rows[1]["indices"]
def crt(a,b):
 return (a+p1*(((b-a)*pow(p1,-1,p2))%p2))%M
def reconstruct(x):
 r0,r1=M,x; t0,t1=0,1
 while r1>B:
  q=r0//r1; r0,r1=r1,r0-q*r1; t0,t1=t1,t0-q*t1
 if t1==0:return None
 n,d=r1,t1
 if d<0:n,d=-n,-d
 g=gcd(abs(n),d); n//=g; d//=g
 if abs(n)>B or d>B or (d*x-n)%M:return None
 return Fraction(n,d)
vals=[]
for a,b in zip(rows[0]["values"],rows[1]["values"]):
 x=crt(a,b); q=reconstruct(x)
 vals.append({"crt":x,"rational":None if q is None else [q.numerator,q.denominator]})
ok=sum(v["rational"] is not None for v in vals)
out={"schema":"marici.barcode-row-two-prime-rational-reconstruction.v1",
 "primes":[p1,p2],"modulus":M,"height_bound":B,
 "block":"first_death_rows","row_index":0,"indices":rows[0]["indices"],
 "coefficients":vals,"reconstructed_count":ok,"coefficient_count":len(vals),
 "complete_candidate":ok==len(vals),
 "status":"candidate_only_unverified_against_characteristic_zero_source"}
path=R/"interaction-net-barcode-row0-rational-reconstruction-p32003-p32009.json"
path.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
