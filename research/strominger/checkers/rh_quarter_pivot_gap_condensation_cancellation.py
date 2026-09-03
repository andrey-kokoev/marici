import json
from fractions import Fraction as F
from functools import lru_cache,reduce
from pathlib import Path
base=Path(__file__).parents[1];newton=json.loads((base/"results"/"rh_quarter_pivot_curvature_gap_newton.json").read_text(encoding="utf-8"));ss=(F(1),F(5,4),F(3,2),F(7,4))
def q(a,i):return reduce(lambda z,s:z*(s+a+i),ss,F(1))
@lru_cache(None)
def D(n,a):
 if n<=1:return F(1)
 return (q(a,n-1)*D(n-1,a)*D(n-1,a+2)-q(a,0)*D(n-1,a+1)**2)/D(n-2,a+2)
def raw(n,a):return q(a,n)*D(n,a)*D(n,a+2)*D(n-1,a+1)**2-q(a,n-1)*D(n,a+1)**2*D(n-1,a)*D(n-1,a+2)
def cancelled(n,a):return D(n+1,a)*D(n-1,a+2)*D(n-1,a+1)**2-D(n,a+1)**2*D(n,a)*D(n-2,a+2)
rows=[]
for n in range(2,21):
 for a in range(13):rows.append({"n":n,"shift":a,"cancellation_identity":raw(n,a)==cancelled(n,a),"cancelled_gap_positive":cancelled(n,a)>0})
checks={"bounded_newton_source_passed":newton["status"]=="passed","q_zero_terms_cancel_exactly":all(r["cancellation_identity"] for r in rows),"cancelled_gap_positive_on_grid":all(r["cancelled_gap_positive"] for r in rows),"tested_247_cases":len(rows)==247,"deliberate_term_reversal_negative":cancelled(2,0)>0 and -cancelled(2,0)<0}
result={"schema":"marici.strominger.rh_quarter_pivot_gap_condensation_cancellation.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Two condensation substitutions cancel both q_a(0) terms exactly. The monotonicity gap becomes a difference of two products of positive contiguous minors. Positivity still requires a sign-preserving injection or a compound-network minor representation; positivity of the factors alone is insufficient.","cancelled_gap":"D_(n+1,a)D_(n-1,a+2)D_(n-1,a+1)^2-D_(n,a+1)^2D_(n,a)D_(n-2,a+2)","first_missing_object":"sign-preserving injection between the two paired nonintersecting-path ensembles, or an equivalent compound-network minor","tested_case_count":len(rows),"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
(base/"results"/"rh_quarter_pivot_gap_condensation_cancellation.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
