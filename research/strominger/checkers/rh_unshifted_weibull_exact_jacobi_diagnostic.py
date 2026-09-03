import json, math
from fractions import Fraction as F
from pathlib import Path
N=6
def mu(r): return F(4*math.factorial(4*r+3),2**(4*r+4))
def inner(p,q,shift=0):
 return sum((p[i]*q[j]*mu(i+j+shift) for i in range(len(p)) for j in range(len(q))),F(0))
ps=[]; hs=[]; rows=[]
for n in range(N+1):
 p=[F(0)]*n+[F(1)]
 for k in range(n):
  c=inner(p,ps[k])/hs[k]
  p += [F(0)]*(len(ps[k])-len(p))
  for i,v in enumerate(ps[k]): p[i]-=c*v
 h=inner(p,p); b=inner(p,p,1)/h
 a2=None if n==0 else h/hs[n-1]
 ps.append(p); hs.append(h)
 rows.append({"n":n,"a_squared":None if a2 is None else float(a2),"b":float(b),"a_over_n4":None if n==0 else math.sqrt(float(a2))/n**4,"b_over_n4":None if n==0 else float(b)/n**4})
checks={
 "all_norms_positive":all(h>0 for h in hs),
 "all_recurrence_a_squared_positive":all(rows[n]["a_squared"]>0 for n in range(1,N+1)),
 "all_recurrence_b_positive":all(r["b"]>0 for r in rows),
 "moments_are_exact_rationals":all(isinstance(mu(r),F) for r in range(2*N+2)),
}
result={"schema":"marici.strominger.rh_unshifted_weibull_exact_jacobi_diagnostic.v1","status":"passed" if all(checks.values()) else "failed","measure":"exp(-2*x^(1/4)) dx on [0,infinity)","verdict":"Exact rational Gram-Schmidt constructs the first seven Jacobi coefficients of the unshifted continuous Weibull comparator. Their natural scale is n^4, matching the moment saddle, but this finite table proves neither asymptotics nor uniform transfer to the shifted tail measure.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1]; out=base/"results"/"rh_unshifted_weibull_exact_jacobi_diagnostic.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))
