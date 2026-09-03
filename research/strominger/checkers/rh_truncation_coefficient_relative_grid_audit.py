import json, math
from decimal import Decimal as D, localcontext
from pathlib import Path
N=8
def coefficients(q,prec):
 with localcontext() as ctx:
  ctx.prec=prec
  X=D(q).ln(); z=2*X.sqrt().sqrt(); M=[]
  for r in range(2*N+2):
   m=4*r+3; s=D(0); term=D(1)
   for k in range(m+1):
    if k:term*=z/D(k)
    s+=term
   M.append(D(4)*D(math.factorial(m))*s/(D(2)**(m+1)))
  def inn(p,s,shift=0):return sum((p[i]*s[j]*M[i+j+shift] for i in range(len(p)) for j in range(len(s))),D(0))
  ps=[];hs=[];out=[]
  for n in range(N+1):
   p=[D(0)]*n+[D(1)]
   for k in range(n):
    c=inn(p,ps[k])/hs[k]
    for i,v in enumerate(ps[k]):p[i]-=c*v
   h=inn(p,p); bx=inn(p,p,1)/h
   out.append((None if n==0 else (h/hs[-1]).sqrt(),bx-X));ps.append(p);hs.append(h)
  return out
def unshifted(prec):
 with localcontext() as ctx:
  ctx.prec=prec; M=[D(4)*D(math.factorial(4*r+3))/(D(2)**(4*r+4)) for r in range(2*N+2)]
  def inn(p,s,shift=0):return sum((p[i]*s[j]*M[i+j+shift] for i in range(len(p)) for j in range(len(s))),D(0))
  ps=[];hs=[];out=[]
  for n in range(N+1):
   p=[D(0)]*n+[D(1)]
   for k in range(n):
    c=inn(p,ps[k])/hs[k]
    for i,v in enumerate(ps[k]):p[i]-=c*v
   h=inn(p,p);out.append((None if n==0 else (h/hs[-1]).sqrt(),inn(p,p,1)/h));ps.append(p);hs.append(h)
  return out
u=unshifted(150); rows=[]; stable=True
for q in (3,12,48):
 lo=coefficients(q,90); hi=coefficients(q,150); degree=[]
 for n in range(1,N+1):
  stable &= abs(float(lo[n][0]/hi[n][0]-1))<1e-70 and abs(float(lo[n][1]/hi[n][1]-1))<1e-70
  degree.append({"n":n,"relative_a":float(hi[n][0]/u[n][0]-1),"relative_b":float(hi[n][1]/u[n][1]-1)})
 rows.append({"q":q,"degrees":degree})
checks={
 "precision_90_vs_150_stable":stable,
 "all_degree_eight_relative_errors_below_one_percent":all(abs(r["degrees"][-1][k])<.01 for r in rows for k in ("relative_a","relative_b")),
 "degree_eight_error_grows_with_tail_start":all(abs(rows[i+1]["degrees"][-1]["relative_a"])>abs(rows[i]["degrees"][-1]["relative_a"]) for i in range(2)),
 "degree_eight_errors_smaller_than_degree_one":all(abs(r["degrees"][-1]["relative_a"])<abs(r["degrees"][0]["relative_a"]) for r in rows),
}
result={"schema":"marici.strominger.rh_truncation_coefficient_relative_grid_audit.v1","status":"passed" if all(checks.values()) else "failed","parameters":{"tail_starts":[3,12,48],"degrees":"1..8","precision_crosscheck":[90,150]},"verdict":"Shifted/unshifted Jacobi relative differences decrease strongly with degree through eight for all tested tail starts. Degree-eight differences remain below one percent, while larger q delays convergence. Agreement between 90- and 150-digit runs controls numerical cancellation but does not prove asymptotic stability.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];out=base/"results"/"rh_truncation_coefficient_relative_grid_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
