import json, math
from decimal import Decimal as D, localcontext
from pathlib import Path
def laguerre_coeff(j):return [D((-1)**k)*D(math.comb(j,k))/D(math.factorial(k)) for k in range(j+1)]
def upper_integer(m,x):
 s=D(0);term=D(1)
 for k in range(m+1):
  if k:term*=x/D(k)
  s+=term
 return D(math.factorial(m))*(-x).exp()*s
def trace(n,prec=120):
 with localcontext() as ctx:
  ctx.prec=prec;a=D(n);b=D(n**3);mom=[upper_integer(m,a)-upper_integer(m,b) for m in range(2*n-1)];total=D(0)
  for j in range(n):
   c=laguerre_coeff(j);total+=sum((c[k]*c[l]*mom[k+l] for k in range(len(c)) for l in range(len(c))),D(0))
  return float(total)
rows=[]
for n in (3,4,6,8,10,12):
 t=trace(n);rows.append({"n":n,"z_minus":n,"z_plus":n**3,"laguerre_expected_transition_occupancy":t,"occupancy_fraction":t/n})
checks={
 "occupancies_positive":all(r["laguerre_expected_transition_occupancy"]>0 for r in rows),
 "occupancy_fraction_not_vanishing_on_grid":all(r["occupancy_fraction"]>.2 for r in rows),
 "occupancy_grows_with_degree":all(rows[i+1]["laguerre_expected_transition_occupancy"]>rows[i]["laguerre_expected_transition_occupancy"] for i in range(len(rows)-1)),
}
base=Path(__file__).parents[1]
result={"schema":"marici.strominger.rh_laguerre_transition_occupancy_no_go.v1","status":"passed" if all(checks.values()) else "failed","scaling":"n=X^(beta/8), so z_-=n and z_+=n^3","verdict":"In the local Laguerre model under an admissible degree-overlap scaling, the transition buffer contains an order-one fraction of the n-particle ensemble on the tested grid. Transition occupancy is therefore not negligible and cannot be used to reduce interface pair counts without a new global mechanism.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_laguerre_transition_occupancy_no_go.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
