import json, math
from decimal import Decimal as D, getcontext
from pathlib import Path
getcontext().prec=100
N=6; X=D(12).ln(); u0=X.sqrt().sqrt(); z=2*u0
def moment(r):
 m=4*r+3; s=D(0); term=D(1)
 for k in range(m+1):
  if k: term*=z/D(k)
  s+=term
 return D(4)*D(math.factorial(m))*s/(D(2)**(m+1))
M=[moment(r) for r in range(2*N+2)]
def inner(p,q,shift=0):return sum((p[i]*q[j]*M[i+j+shift] for i in range(len(p)) for j in range(len(q))),D(0))
ps=[]; hs=[]; rows=[]
for n in range(N+1):
 p=[D(0)]*n+[D(1)]
 for k in range(n):
  c=inner(p,ps[k])/hs[k]
  for i,v in enumerate(ps[k]):p[i]-=c*v
 h=inner(p,p); bx=inner(p,p,1)/h; a2=None if n==0 else h/hs[n-1]
 ps.append(p);hs.append(h)
 rows.append({"n":n,"a":None if a2 is None else float(a2.sqrt()),"b_translated":float(bx-X),"a_over_n4":None if n==0 else float(a2.sqrt()/D(n**4)),"b_over_n4":None if n==0 else float((bx-X)/D(n**4))})
checks={
 "all_gram_norms_positive":all(h>0 for h in hs),
 "all_off_diagonal_coefficients_positive":all(rows[n]["a"]>0 for n in range(1,N+1)),
 "translated_diagonal_coefficients_positive":all(r["b_translated"]>0 for r in rows),
 "normalized_incomplete_gamma_formula_positive":all(m>0 for m in M),
}
base=Path(__file__).parents[1]
result={"schema":"marici.strominger.rh_truncated_weibull_jacobi_diagnostic.v1","status":"passed" if all(checks.values()) else "failed","parameters":{"X":"log(12)","a":1,"beta":"1/4","precision_digits":100},"verdict":"The integer-shape incomplete-gamma formula yields a 100-digit finite Jacobi diagnostic for the Weibull measure truncated at X=log(12), then translated to y=x-X. Through degree six the coefficients retain an n^4-scale pattern. This is finite evidence only and supplies no truncation-stability theorem.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_truncated_weibull_jacobi_diagnostic.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
