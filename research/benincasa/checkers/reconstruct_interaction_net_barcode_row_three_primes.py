#!/usr/bin/env python3
"""Three-prime rational reconstruction pilot for one source-labelled barcode row."""
from __future__ import annotations
from fractions import Fraction
from math import gcd,isqrt
import json,pickle
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; R=ROOT/"research"/"benincasa"/"results"
class SparseBasis: pass
primes=[31991,32003,32009]
with (R/"interaction-net-barcode-basis-stage1-p31991.pkl").open("rb") as f: cp=pickle.load(f)
r31991=cp["adapted_source"][0]
pack={p:json.loads((R/f"interaction-net-barcode-basis-export-p{p}.json").read_text()) for p in (32003,32009)}
rows={
 31991:{"indices":sorted(r31991),"values":[r31991[i] for i in sorted(r31991)]},
 32003:pack[32003]["adapted_depth3_quotient_basis"]["first_death_rows"][0],
 32009:pack[32009]["adapted_depth3_quotient_basis"]["first_death_rows"][0],
}
assert rows[31991]["indices"]==rows[32003]["indices"]==rows[32009]["indices"]
def crt_pair(x,m,a,p):
 return x+m*(((a-x)*pow(m,-1,p))%p),m*p
def reconstruct(x,m):
 B=isqrt(m//2); r0,r1=m,x; t0,t1=0,1
 while r1>B:
  q=r0//r1; r0,r1=r1,r0-q*r1; t0,t1=t1,t0-q*t1
 if t1==0:return None
 n,d=r1,t1
 if d<0:n,d=-n,-d
 g=gcd(abs(n),d);n//=g;d//=g
 if abs(n)>B or d>B or (d*x-n)%m:return None
 return Fraction(n,d)
M=1
for p in primes:M*=p
B=isqrt(M//2); coeffs=[]
for j in range(len(rows[31991]["indices"])):
 x,m=0,1
 for p in primes:x,m=crt_pair(x,m,rows[p]["values"][j],p)
 q=reconstruct(x,m)
 valid=q is not None and all((q.numerator-q.denominator*rows[p]["values"][j])%p==0 for p in primes)
 coeffs.append({"crt":x,"rational":None if q is None else [q.numerator,q.denominator],"all_prime_check":valid})
count=sum(x["rational"] is not None for x in coeffs)
two=json.loads((R/"interaction-net-barcode-row0-rational-reconstruction-p32003-p32009.json").read_text())
two_candidates=0; two_survive=0
for j,item in enumerate(two["coefficients"]):
 if item["rational"] is not None:
  two_candidates+=1; n,d=item["rational"]
  if (n-d*rows[31991]["values"][j])%31991==0:two_survive+=1
out={"schema":"marici.barcode-row-three-prime-rational-reconstruction.v1","primes":primes,
 "modulus":M,"height_bound":B,"block":"first_death_rows","row_index":0,
 "indices":rows[31991]["indices"],"coefficients":coeffs,"reconstructed_count":count,
 "coefficient_count":len(coeffs),"complete_candidate":count==len(coeffs),
 "all_prime_checks":all(x["all_prime_check"] for x in coeffs if x["rational"] is not None),
 "two_prime_candidate_count":two_candidates,"two_prime_candidates_surviving_third_prime":two_survive,
 "status":"candidate_only_unverified_against_characteristic_zero_source"}
path=R/"interaction-net-barcode-row0-rational-reconstruction-p31991-p32003-p32009.json"
path.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"complete_candidate":out["complete_candidate"],"reconstructed_count":count,
 "coefficient_count":len(coeffs),"height_bound":B,"all_prime_checks":out["all_prime_checks"]},indent=2))
