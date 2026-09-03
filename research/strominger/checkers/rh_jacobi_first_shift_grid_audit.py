import json,math
from decimal import Decimal as D,localcontext
from pathlib import Path
N=17
with localcontext() as ctx:
 ctx.prec=500;X=D(12).ln();z=2*X.sqrt().sqrt();M=[]
 for r in range(2*N+2):
  m=4*r+3;v=D(4)*D(math.factorial(m))/D(2)**(m+1);s=D(0);t=D(1)
  for k in range(m+1):
   if k:t*=z/D(k)
   s+=t
  M.append(v*s)
 def inn(p,q):return sum((p[i]*q[j]*M[i+j] for i in range(len(p)) for j in range(len(q))),D(0))
 ps=[];hs=[];aa=[]
 for n in range(N+1):
  p=[D(0)]*n+[D(1)]
  for k in range(n):
   c=inn(p,ps[k])/hs[k]
   for i,v in enumerate(ps[k]):p[i]-=c*v
  h=inn(p,p);aa.append(None if n==0 else (h/hs[-1]).sqrt());ps.append(p);hs.append(h)
rows=[{"n":n,"scaled_a":float(aa[n]/D(n**4))} for n in range(6,N)]
def solve(A,b):
 A=[r[:]+[v] for r,v in zip(A,b)];m=len(A)
 for i in range(m):
  k=max(range(i,m),key=lambda r:abs(A[r][i]));A[i],A[k]=A[k],A[i];p=A[i][i]
  for j in range(i,m+1):A[i][j]/=p
  for r in range(m):
   if r!=i:
    f=A[r][i]
    for j in range(i,m+1):A[r][j]-=f*A[i][j]
 return [A[i][-1] for i in range(m)]
def fit(order):
 tr=[r for r in rows if r["n"]<=13];Xv=[[r["n"]**(-p) for p in range(order+1)] for r in tr];y=[r["scaled_a"] for r in tr];m=order+1;G=[[sum(x[i]*x[j] for x in Xv) for j in range(m)] for i in range(m)];b=[sum(x[i]*v for x,v in zip(Xv,y)) for i in range(m)];c=solve(G,b);a1=c[1]/c[0]
 te=[r for r in rows if r["n"]>=14];rm=math.sqrt(sum((r["scaled_a"]-sum(c[p]*r["n"]**(-p) for p in range(m)))**2 for r in te)/len(te));return {"order":order,"A":c[0],"a1":a1,"coefficients":c,"holdout_rmse":rm}
fits=[fit(k) for k in (1,2,3)];best=min(fits,key=lambda x:x["holdout_rmse"])
checks={"scaled_a_positive":all(r["scaled_a"]>0 for r in rows),"higher_order_improves_holdout":fits[2]["holdout_rmse"]<fits[1]["holdout_rmse"]<fits[0]["holdout_rmse"],"best_a1_is_numerically_zero":abs(best["a1"])<1e-4,"finite_outputs":all(math.isfinite(v) for f in fits for v in (f["A"],f["a1"],f["holdout_rmse"]))}
result={"schema":"marici.strominger.rh_jacobi_first_shift_grid_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":f"Finite inverse-degree fits to a_n/n^4 select order {best['order']} with a1={best['a1']:.6g}. This tests whether canonical a1 plausibly vanishes but does not establish its asymptotic value.","checks":checks,"rows":rows,"fits":fits,"winner":best,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_jacobi_first_shift_grid_audit.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps({"status":result["status"],"checks":checks,"fits":fits},indent=2))
