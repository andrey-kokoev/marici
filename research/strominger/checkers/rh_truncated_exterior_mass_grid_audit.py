import json, math
from decimal import Decimal as D, localcontext
from pathlib import Path
N=15
with localcontext() as ctx:
 ctx.prec=420;X=D(12).ln();z=2*X.sqrt().sqrt();full=[];tailnorm=[]
 for r in range(2*N+1):
  m=4*r+3;f=D(4)*D(math.factorial(m))/(D(2)**(m+1));s=D(0);t=D(1)
  for k in range(m+1):
   if k:t*=z/D(k)
   s+=t
  full.append(f);tailnorm.append(f*s)
 compact=[full[r]-(-z).exp()*tailnorm[r] for r in range(len(full))]
 def inn(p,q,M):return sum((p[i]*q[j]*M[i+j] for i in range(len(p)) for j in range(len(q))),D(0))
 ps=[];hs=[];rows=[]
 for n in range(N):
  p=[D(0)]*n+[D(1)]
  for k in range(n):
   c=inn(p,ps[k],tailnorm)/hs[k]
   for i,v in enumerate(ps[k]):p[i]-=c*v
  hnorm=inn(p,p,tailnorm);extmass=inn(p,p,compact)*z.exp()/hnorm
  ps.append(p);hs.append(hnorm);rows.append({"n":n,"exterior_compact_mass":float(extmass),"n2_mass":float(D(n*n)*extmass) if n else 0.})
late=[r["n2_mass"] for r in rows if r["n"]>=8]
checks={
 "exterior_masses_positive":all(r["exterior_compact_mass"]>0 for r in rows),
 "exterior_masses_decrease_after_degree_one":all(rows[i+1]["exterior_compact_mass"]<rows[i]["exterior_compact_mass"] for i in range(1,len(rows)-1)),
 "late_n2_mass_finite":all(math.isfinite(v) for v in late),
 "late_n2_mass_spread_below_twenty_percent":max(late)/min(late)<1.2,
}
result={"schema":"marici.strominger.rh_truncated_exterior_mass_grid_audit.v1","status":"passed" if all(checks.values()) else "failed","parameters":{"q":12,"degrees":"0..14","precision_digits":420},"verdict":"The compact exterior mass of polynomials orthonormal on the truncated Weibull tail decreases across the finite grid. Its n^2 rescaling is bounded with modest late spread, providing direct diagnostics for the variational O(n^-2) upper bound. This remains finite computation.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];out=base/"results"/"rh_truncated_exterior_mass_grid_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps({"status":result["status"],"checks":checks,"late_rows":rows[-7:]},indent=2))
