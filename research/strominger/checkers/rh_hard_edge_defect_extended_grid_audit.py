import json, math
from decimal import Decimal as D, localcontext
from pathlib import Path
N=17
def coeffs(prec):
 with localcontext() as ctx:
  ctx.prec=prec;X=D(12).ln();z=2*X.sqrt().sqrt();M=[]
  for r in range(2*N+2):
   m=4*r+3;v=D(4)*D(math.factorial(m))/(D(2)**(m+1));s=D(0);t=D(1)
   for k in range(m+1):
    if k:t*=z/D(k)
    s+=t
   M.append(v*s)
  def inn(p,q,h=0):return sum((p[i]*q[j]*M[i+j+h] for i in range(len(p)) for j in range(len(q))),D(0))
  ps=[];hs=[];a=[];b=[]
  for n in range(N+1):
   p=[D(0)]*n+[D(1)]
   for k in range(n):
    c=inn(p,ps[k])/hs[k]
    for i,v in enumerate(ps[k]):p[i]-=c*v
   h=inn(p,p);a.append(None if n==0 else (h/hs[-1]).sqrt());b.append(inn(p,p,1)/h-X);ps.append(p);hs.append(h)
  return a,b
alo,blo=coeffs(320);a,b=coeffs(520);rows=[]
for n in range(1,N):
 eps=(a[n]+a[n+1]-b[n])/a[n+1];elo=(alo[n]+alo[n+1]-blo[n])/alo[n+1]
 rows.append({"n":n,"edge_defect":float(eps),"n2_defect":float(D(n*n)*eps),"precision_delta":abs(float(eps-elo))})
late=[r["n2_defect"] for r in rows if r["n"]>=10]
checks={
 "precision_crosscheck_stable":max(r["precision_delta"] for r in rows)<1e-250,
 "defects_positive":all(r["edge_defect"]>0 for r in rows),
 "scaled_defect_increases":all(rows[i+1]["n2_defect"]>rows[i]["n2_defect"] for i in range(len(rows)-1)),
 "late_scaled_defects_remain_below_two":all(v<2 for v in late),
}
result={"schema":"marici.strominger.rh_hard_edge_defect_extended_grid_audit.v1","status":"passed" if all(checks.values()) else "failed","parameters":{"q":12,"degrees":"1..16","precision_crosscheck":[320,520]},"verdict":"The precision-controlled hard-edge defect remains positive and n^2 epsilon_n increases through degree sixteen while staying below two. This extends compatibility with the candidate limit two but does not establish convergence or exclude a different limit.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];out=base/"results"/"rh_hard_edge_defect_extended_grid_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps({"status":result["status"],"checks":checks,"late_rows":rows[-7:]},indent=2))
