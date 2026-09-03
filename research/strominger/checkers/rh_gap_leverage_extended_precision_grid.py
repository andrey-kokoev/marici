import json, math
from decimal import Decimal as D, localcontext
from pathlib import Path
N=18
def norms(truncated,prec):
 with localcontext() as ctx:
  ctx.prec=prec;X=D(12).ln();z=2*X.sqrt().sqrt();M=[]
  for r in range(2*N+1):
   m=4*r+3;v=D(4)*D(math.factorial(m))/(D(2)**(m+1))
   if truncated:
    s=D(0);t=D(1)
    for k in range(m+1):
     if k:t*=z/D(k)
     s+=t
    v*=s
   M.append(v)
  def inn(p,q):return sum((p[i]*q[j]*M[i+j] for i in range(len(p)) for j in range(len(q))),D(0))
  ps=[];hs=[]
  for n in range(N):
   p=[D(0)]*n+[D(1)]
   for k in range(n):
    c=inn(p,ps[k])/hs[k]
    for i,v in enumerate(ps[k]):p[i]-=c*v
   h=inn(p,p);ps.append(p);hs.append(h)
  return hs,z
def grid(prec):
 hx,z=norms(True,prec);hu,_=norms(False,prec);logg=D(0);logs=[D(0)]
 for x,u in zip(hx,hu):logg+=(x/u).ln()-z;logs.append(logg)
 rows=[]
 for n in range(1,N):
  ell=D(1)-(logs[n+1]-logs[n]).exp();rows.append((n,ell,D(n*n)*ell))
 return rows
lo=grid(320);hi=grid(520);rows=[{"n":n,"leverage":float(e),"n2_leverage":float(s),"precision_delta":abs(float(e-lo[i][1]))} for i,(n,e,s) in enumerate(hi)]
late=[r["n2_leverage"] for r in rows if r["n"]>=10]
checks={
 "precision_320_vs_520_stable":max(r["precision_delta"] for r in rows)<1e-250,
 "leverage_positive":all(r["leverage"]>0 for r in rows),
 "n2_leverage_increases_on_grid":all(rows[i+1]["n2_leverage"]>rows[i]["n2_leverage"] for i in range(len(rows)-1)),
 "late_n2_leverage_spread_below_five_percent":max(late)/min(late)<1.05,
}
result={"schema":"marici.strominger.rh_gap_leverage_extended_precision_grid.v1","status":"passed" if all(checks.values()) else "failed","parameters":{"q":12,"degrees":"1..17","precision_crosscheck":[320,520]},"verdict":"The 520-digit extension through degree seventeen keeps leverage positive and n^2 leverage slowly increasing with under five-percent late spread. This strengthens the n^-2 diagnostic and estimates its limiting coefficient, but remains finite computation rather than a decay theorem.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];out=base/"results"/"rh_gap_leverage_extended_precision_grid.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps({"status":result["status"],"checks":checks,"late_rows":rows[-6:]},indent=2))
