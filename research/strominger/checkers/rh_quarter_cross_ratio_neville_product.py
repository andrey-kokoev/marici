import json
from fractions import Fraction as F
from functools import lru_cache,reduce
from pathlib import Path
base=Path(__file__).parents[1];mono=json.loads((base/"results"/"rh_quarter_cross_ratio_degree_monotonicity.json").read_text(encoding="utf-8"));ss=(F(1),F(5,4),F(3,2),F(7,4))
def q(a,i):return reduce(lambda z,s:z*(s+a+i),ss,F(1))
@lru_cache(None)
def D(n,a):
 if n<=1:return F(1)
 return (q(a,n-1)*D(n-1,a)*D(n-1,a+2)-q(a,0)*D(n-1,a+1)**2)/D(n-2,a+2)
def P(k,a):return D(k,a)/D(k-1,a)
def theta(n,a):return q(a,0)*D(n-1,a+1)**2/(q(a,n-1)*D(n-1,a)*D(n-1,a+2))
rows=[]
for n in range(2,31):
 for a in range(13):
  pivot_curvature=P(n,a+1)**2/(P(n,a)*P(n,a+2));q_ratio=q(a,n)/q(a,n-1);successive=theta(n+1,a)/theta(n,a)
  rows.append({"n":n,"shift":a,"identity":successive==pivot_curvature/q_ratio,"pivot_curvature_below_q_ratio":pivot_curvature<q_ratio,"pivot_curvature":float(pivot_curvature),"q_ratio":float(q_ratio),"successive_theta_ratio":float(successive)})
checks={"finite_monotonicity_source_passed":mono["status"]=="passed","exact_successive_ratio_identity":all(r["identity"] for r in rows),"pivot_curvature_bound_on_grid":all(r["pivot_curvature_below_q_ratio"] for r in rows),"all_neville_pivots_positive":all(P(n,a)>0 for n in range(1,31) for a in range(15)),"tested_377_cases":len(rows)==377,"deliberate_bound_one_too_strong":any(r["pivot_curvature"]>1 for r in rows)}
result={"schema":"marici.strominger.rh_quarter_cross_ratio_neville_product.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Successive cross-ratio monotonicity reduces exactly to a curvature bound for positive leading Neville pivots: theta_(n+1,a)/theta_(n,a)=[P_(n,a+1)^2/(P_(n,a)P_(n,a+2))]/[q_a(n)/q_a(n-1)]. Exact checks verify the identity and bound finitely; total positivity alone does not supply the quantitative upper bound.","equivalent_all_degree_gate":"P(n,a+1)^2/[P(n,a)P(n,a+2)] < q_a(n)/q_a(n-1)","rows":rows,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
(base/"results"/"rh_quarter_cross_ratio_neville_product.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
