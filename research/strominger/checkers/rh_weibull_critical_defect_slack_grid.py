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
 def inn(p,q,h=0):return sum((p[i]*q[j]*M[i+j+h] for i in range(len(p)) for j in range(len(q))),D(0))
 ps=[];hs=[];aa=[];bb=[]
 for n in range(N+1):
  p=[D(0)]*n+[D(1)]
  for k in range(n):
   c=inn(p,ps[k])/hs[k]
   for i,v in enumerate(ps[k]):p[i]-=c*v
  h=inn(p,p);aa.append(None if n==0 else (h/hs[-1]).sqrt());bb.append(inn(p,p,1)/h-X);ps.append(p);hs.append(h)
 rows=[]
 for n in range(2,N):
  r=aa[n]/aa[n+1];eps=(aa[n]+aa[n+1]-bb[n])/aa[n+1];critical=D(1)/D(n+1)-r/D(n-1);slack=critical-eps
  rows.append({"n":n,"epsilon":float(eps),"critical":float(critical),"slack":float(slack),"n4_slack":float(D(n**4)*slack),"n5_slack":float(D(n**5)*slack)})
late=[r for r in rows if r["n"]>=8]
checks={"all_slacks_negative":all(r["slack"]<0 for r in rows),"late_n4_slack_bounded_away_from_zero":all(r["n4_slack"]<-.3 for r in late),"finite_values":all(math.isfinite(r["n5_slack"]) for r in rows),"degree16_reached":rows[-1]["n"]==16}
result={"schema":"marici.strominger.rh_weibull_critical_defect_slack_grid.v1","status":"passed" if all(checks.values()) else "failed","verdict":"A 520-digit degree-16 truncated-Weibull grid falsifies the unshifted 1/n Riccati barrier: epsilon*_n-epsilon_n is negative throughout and n^4 times the slack approaches roughly -0.5. A shifted comparison profile is required.","checks":checks,"late_rows":late,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_weibull_critical_defect_slack_grid.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
