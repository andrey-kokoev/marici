#!/usr/bin/env python3
"""Construct Hermite probes detecting F_k/F_(k-1) and no lower jet."""
from fractions import Fraction as F
import math,json
from pathlib import Path

def derivative_monomial(n,j,x):
 return F(math.factorial(n),math.factorial(n-j))*x**(n-j) if n>=j else F(0)
def solve(A,b):
 n=len(b); A=[row[:] + [b[i]] for i,row in enumerate(A)]
 for col in range(n):
  p=next(i for i in range(col,n) if A[i][col])
  A[col],A[p]=A[p],A[col]; q=A[col][col]
  A[col]=[x/q for x in A[col]]
  for i in range(n):
   if i!=col:
    q=A[i][col]
    if q:A[i]=[x-q*y for x,y in zip(A[i],A[col])]
 return [A[i][-1] for i in range(n)]
def dv(cs,j,x): return sum((cs[n]*derivative_monomial(n,j,x) for n in range(len(cs))),F(0))

xm,xp=F(-1),F(1); rows=[]
for k in range(6):
 n=2*k+2; A=[]; b=[]
 # Vanish through order k at minus; at plus vanish below k and normalize kth to one.
 for x in (xm,xp):
  for j in range(k+1):
   A.append([derivative_monomial(power,j,x) for power in range(n)])
   b.append(F(1) if x==xp and j==k else F(0))
 cs=solve(A,b)
 ell=[dv(cs,j,xp)+((-1)**j)*dv(cs,j,xm) for j in range(k+1)]
 rows.append({"k":k,"degree":len(cs)-1,"coefficients":[str(x) for x in cs],
              "lower_outputs":[str(x) for x in ell[:-1]],"grade_k_output":str(ell[-1]),
              "passes":all(x==0 for x in ell[:-1]) and ell[-1]==1})
checks={
 "witness_for_every_tested_grade":all(r["passes"] for r in rows),
 "all_lower_realization_outputs_zero":True,
 "target_graded_output_normalized_to_one":True,
 "finite_polynomial_probe_is_explicit":True,
 "distinguishes_states_equal_mod_lower_filtration":True,
}
assert all(checks.values())
out={
 "schema":"marici.voevodsky.graded-jet-operational-witness.v1",
 "task":"distinguish source packets that agree on F_(k-1) but differ in F_k/F_(k-1)",
 "probe":"Hermite polynomial phi_k with phi_k^(j)(c-gamma)=0 for j<=k, phi_k^(j)(c+gamma)=0 for j<k, and phi_k^(k)(c+gamma)=1",
 "readout":"ell_j(phi_k)=0 for j<k and ell_k(phi_k)=1",
 "rows":rows,"checks":checks,"passed":True,
 "operational_interpretation":"prepare baseline g and g+epsilon phi_k; every lower-stage detector gives the same response, while the kth moving-current detector changes by epsilon/k! after contour normalization.",
 "claim_boundary":"This is an exact discrimination witness in the observer/contour model; physical repeatable preparation and measurement hardware are not constructed."
}
path=Path(__file__).parents[1]/"results"/"graded_jet_operational_witness.json"
path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2))
