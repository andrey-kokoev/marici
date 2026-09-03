import json,math
from decimal import Decimal as D,localcontext
from pathlib import Path
N=17
with localcontext() as ctx:
 ctx.prec=520;X=D(12).ln();z=2*X.sqrt().sqrt();M=[]
 for r in range(2*N+2):
  m=4*r+3;v=D(4)*D(math.factorial(m))/D(2)**(m+1);s=D(0);t=D(1)
  for k in range(m+1):
   if k:t*=z/D(k)
   s+=t
  M.append(v*s)
 def inn(p,q):return sum((p[i]*q[j]*M[i+j] for i in range(len(p)) for j in range(len(q))),D(0))
 ps=[];hs=[];rows=[]
 for n in range(N+1):
  p=[D(0)]*n+[D(1)]
  for k in range(n):
   c=inn(p,ps[k])/hs[k]
   for i,v in enumerate(ps[k]):p[i]-=c*v
  h=inn(p,p);ps.append(p);hs.append(h)
  if n>=1:
   val=abs(p[0]/h.sqrt());rows.append({"n":n,"abs_P_at_zero":float(val),"nP":float(D(n)*val),"n2P":float(D(n*n)*val)})
late=[r for r in rows if r["n"]>=8];xs=[math.log(r["n"]) for r in late];ys=[math.log(r["abs_P_at_zero"]) for r in late];xm=sum(xs)/len(xs);ym=sum(ys)/len(ys);slope=sum((x-xm)*(y-ym) for x,y in zip(xs,ys))/sum((x-xm)**2 for x in xs)
checks={"values_strictly_nonzero":all(r["abs_P_at_zero"]>0 for r in rows),"slope_closer_to_minus_one_than_minus_two":abs(slope+1)<abs(slope+2),"late_nP_bounded_away_from_zero":min(r["nP"] for r in late)>1e-6,"n2P_grows_on_late_grid":late[-1]["n2P"]>late[0]["n2P"]}
result={"schema":"marici.strominger.rh_weibull_polynomial_branch_separation_grid.v1","status":"passed" if all(checks.values()) else "failed","verdict":f"A 520-digit truncated-Weibull grid through degree 17 gives log-log slope {slope:.6g} for |P_n(0)|. The finite data discriminate n^-1 from n^-2 but do not prove a nonzero asymptotic Wronskian.","checks":checks,"fit":{"degrees":"8..17","power_slope":slope},"late_rows":late,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_weibull_polynomial_branch_separation_grid.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
