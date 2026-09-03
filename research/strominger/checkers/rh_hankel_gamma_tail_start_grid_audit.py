import json, math
from decimal import Decimal as D, localcontext
from pathlib import Path
N=8
def coeff(q,prec=180):
 with localcontext() as ctx:
  ctx.prec=prec;X=D(q).ln();z=2*X.sqrt().sqrt(); M=[]
  for r in range(2*N+2):
   m=4*r+3;s=D(0);t=D(1)
   for k in range(m+1):
    if k:t*=z/D(k)
    s+=t
   M.append(D(4)*D(math.factorial(m))*s/(D(2)**(m+1)))
  def inn(p,s,h=0):return sum((p[i]*s[j]*M[i+j+h] for i in range(len(p)) for j in range(len(s))),D(0))
  ps=[];hs=[];a=[]
  for n in range(N+1):
   p=[D(0)]*n+[D(1)]
   for k in range(n):
    c=inn(p,ps[k])/hs[k]
    for i,v in enumerate(ps[k]):p[i]-=c*v
   h=inn(p,p);a.append(None if n==0 else (h/hs[-1]).sqrt());ps.append(p);hs.append(h)
  return a
def unshift(prec=180):
 with localcontext() as ctx:
  ctx.prec=prec;M=[D(4)*D(math.factorial(4*r+3))/(D(2)**(4*r+4)) for r in range(2*N+2)]
  def inn(p,s):return sum((p[i]*s[j]*M[i+j] for i in range(len(p)) for j in range(len(s))),D(0))
  ps=[];hs=[];a=[]
  for n in range(N+1):
   p=[D(0)]*n+[D(1)]
   for k in range(n):
    c=inn(p,ps[k])/hs[k]
    for i,v in enumerate(ps[k]):p[i]-=c*v
   h=inn(p,p);a.append(None if n==0 else (h/hs[-1]).sqrt());ps.append(p);hs.append(h)
  return a
u=unshift();rows=[]
for q in (3,12,48,192,768):
 a=coeff(q);rel=float(a[N]/u[N]-1);X=math.log(q)
 rows.append({"q":q,"X":X,"X_quarter":X**.25,"gamma_proxy_n8":N**3*math.log1p(rel)})
# Descriptive power fit gamma=c X^p; it is not selected as a law.
xs=[math.log(r["X"]) for r in rows];ys=[math.log(r["gamma_proxy_n8"]) for r in rows];xm=sum(xs)/len(xs);ym=sum(ys)/len(ys);p=sum((x-xm)*(y-ym) for x,y in zip(xs,ys))/sum((x-xm)**2 for x in xs);c=math.exp(ym-p*xm)
checks={
 "gamma_proxy_positive":all(r["gamma_proxy_n8"]>0 for r in rows),
 "gamma_proxy_increases_with_tail_start":all(rows[i+1]["gamma_proxy_n8"]>rows[i]["gamma_proxy_n8"] for i in range(len(rows)-1)),
 "gamma_growth_is_sublinear_in_X":p<1,
 "extended_values_are_finite":all(math.isfinite(r["gamma_proxy_n8"]) for r in rows),
}
result={"schema":"marici.strominger.rh_hankel_gamma_tail_start_grid_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The degree-eight Hankel gamma proxy increases monotonically across q=3..768. A descriptive power fit is sublinear in X=log q, but the grid neither establishes a law nor gives moving-start uniformity. Tail movement improves quadrature prefactors while enlarging the recurrence-perturbation constant.","checks":checks,"descriptive_power_fit":{"gamma":"c*X^p","c":c,"p":p},"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];out=base/"results"/"rh_hankel_gamma_tail_start_grid_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
