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
def marginals(j):return (j[0]+j[1],j[0]+j[2])
records=[]
for a in range(13):
 for n in range(2,20):
  p,qv=theta(n,a),theta(n+1,a)
  nested=(qv,p-qv,F(0),F(1)-p)
  independent=(p*qv,p*(1-qv),(1-p)*qv,(1-p)*(1-qv))
  records.append({"shift":a,"degree":n,"ordered_marginals":0<qv<p<1,"nested_nonnegative":all(x>=0 for x in nested),"independent_strictly_positive":all(x>0 for x in independent),"same_exact_marginals":marginals(nested)==(p,qv)==marginals(independent),"couplings_distinct":nested!=independent})
checks={"all_adjacent_probabilities_strictly_ordered":all(r["ordered_marginals"] for r in records),"all_nested_couplings_nonnegative":all(r["nested_nonnegative"] for r in records),"all_independent_couplings_positive":all(r["independent_strictly_positive"] for r in records),"all_rival_couplings_share_exact_marginals":all(r["same_exact_marginals"] for r in records),"all_rival_couplings_distinct":all(r["couplings_distinct"] for r in records),"tested_234_pairs":len(records)==234}
result={"schema":"marici.strominger.rh_quarter_condensation_coupling_nonidentifiability.v1","status":"passed" if all(checks.values()) else "failed","verdict":"For every tested adjacent-degree pair, nested and independent exact couplings are distinct but have the same condensation-event marginals. Partition totals therefore do not determine a canonical configuration-level lift; an explicit deletion/interlacing map or source configuration relation is additional necessary data.","record_count":len(records),"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_condensation_coupling_nonidentifiability.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
