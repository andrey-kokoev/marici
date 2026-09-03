import json
from fractions import Fraction as F
from functools import lru_cache,reduce
from pathlib import Path
ss=(F(1),F(5,4),F(3,2),F(7,4))
def q(a,i):return reduce(lambda z,s:z*(s+a+i),ss,F(1))
@lru_cache(None)
def D(n,a):
 if n<=1:return F(1)
 return (q(a,n-1)*D(n-1,a)*D(n-1,a+2)-q(a,0)*D(n-1,a+1)**2)/D(n-2,a+2)
def theta(n,a):return q(a,0)*D(n-1,a+1)**2/(q(a,n-1)*D(n-1,a)*D(n-1,a+2))
records=[];failures=[]
for a in range(13):
 cur=[theta(n,a) for n in range(2,33)]
 for order in range(7):
  signed=[((-1)**order)*x for x in cur];ok=all(x>0 for x in signed);rec={"shift":a,"difference_order":order,"entry_count":len(signed),"all_strictly_positive":ok,"minimum_signed_difference":float(min(signed))};records.append(rec)
  if not ok:failures.append(rec)
  cur=[cur[i+1]-cur[i] for i in range(len(cur)-1)]
checks={"complete_monotonicity_orders_zero_through_six":not failures,"tested_thirteen_shifts":len(records)==13*7,"all_minima_finite":all(__import__('math').isfinite(r["minimum_signed_difference"]) for r in records),"degree_window_supports_six_differences":all(r["entry_count"]>=25 for r in records),"deliberate_first_difference_sign_reversal_negative":theta(3,0)-theta(2,0)<0}
result={"schema":"marici.strominger.rh_quarter_cross_ratio_complete_monotonicity.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact recurrence data test discrete complete monotonicity (-1)^k Delta^k theta_(n,a)>0 for difference orders zero through six, degrees two through thirty-two, and shifts zero through twelve. Passing is finite evidence for a Hausdorff-moment representation, not its proof.","records":records,"failures":failures,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_cross_ratio_complete_monotonicity.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
