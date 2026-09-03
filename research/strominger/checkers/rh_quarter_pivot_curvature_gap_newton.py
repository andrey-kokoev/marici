import json
from fractions import Fraction as F
from functools import reduce,lru_cache
from pathlib import Path
ss=(F(1),F(5,4),F(3,2),F(7,4))
def rise(x,k):
 r=F(1)
 for j in range(k):r*=x+j
 return r
def q(a,i):return reduce(lambda z,s:z*(s+a+i),ss,F(1))
def det(m):
 m=[r[:] for r in m];n=len(m);out=F(1)
 for k in range(n):
  p=next((i for i in range(k,n) if m[i][k]),None)
  if p is None:return F(0)
  m[k],m[p]=m[p],m[k]
  if p!=k:out=-out
  z=m[k][k];out*=z
  for j in range(k,n):m[k][j]/=z
  for i in range(k+1,n):
   z=m[i][k]
   for j in range(k,n):m[i][j]-=z*m[k][j]
 return out
@lru_cache(None)
def D(n,a):return F(1) if n==0 else det([[reduce(lambda z,s:z*rise(s+a+i,j),ss,F(1)) for j in range(n)] for i in range(n)])
def gap(n,a):return q(a,n)*D(n,a)*D(n,a+2)*D(n-1,a+1)**2-q(a,n-1)*D(n,a+1)**2*D(n-1,a)*D(n-1,a+2)
records=[];failures=[]
for n in range(2,8):
 bound=4+6*(n-1)**2;cur=[gap(n,a) for a in range(bound+2)];coeff=[]
 while cur:
  coeff.append(cur[0]);cur=[cur[i+1]-cur[i] for i in range(len(cur)-1)]
 actual=max((i for i,x in enumerate(coeff) if x),default=-1);within=coeff[:actual+1];ok=within and within[0]>0 and all(x>=0 for x in within) and all(x==0 for x in coeff[actual+1:])
 rec={"degree":n,"loose_degree_bound":bound,"actual_gap_degree":actual,"constant_positive":bool(within and within[0]>0),"all_newton_coefficients_nonnegative":bool(within and all(x>=0 for x in within)),"tail_zero":all(x==0 for x in coeff[actual+1:]),"positive_coefficient_count":sum(x>0 for x in within)};records.append(rec)
 if not ok:failures.append(rec)
checks={"all_gap_polynomials_newton_positive":not failures,"tested_degrees_two_through_seven":[r["degree"] for r in records]==list(range(2,8)),"all_gap_constants_positive":all(r["constant_positive"] for r in records),"all_degree_tails_zero":all(r["tail_zero"] for r in records),"deliberate_negated_gap_rejected":gap(2,0)>0 and -gap(2,0)<0}
result={"schema":"marici.strominger.rh_quarter_pivot_curvature_gap_newton.v1","status":"passed" if all(checks.values()) else "failed","verdict":"After clearing positive denominators, the pivot-curvature monotonicity gate becomes a polynomial gap in the shift. Exact Newton coefficients test positivity for every integer shift at degrees two through seven; failure is retained without changing the gate.","gap":"q_a(n)D_n(a)D_n(a+2)D_(n-1)(a+1)^2-q_a(n-1)D_n(a+1)^2D_(n-1)(a)D_(n-1)(a+2)","records":records,"failures":failures,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_pivot_curvature_gap_newton.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
