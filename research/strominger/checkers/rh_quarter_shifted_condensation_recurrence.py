import json
from fractions import Fraction as F
from functools import lru_cache,reduce
from pathlib import Path
ss=(F(1),F(5,4),F(3,2),F(7,4))
def rise(x,k):
 r=F(1)
 for j in range(k):r*=x+j
 return r
def det(a):
 a=[r[:] for r in a];out=F(1);n=len(a)
 for k in range(n):
  p=next(i for i in range(k,n) if a[i][k]);a[k],a[p]=a[p],a[k]
  if p!=k:out=-out
  z=a[k][k];out*=z
  for j in range(k,n):a[k][j]/=z
  for i in range(k+1,n):
   z=a[i][k]
   for j in range(k,n):a[i][j]-=z*a[k][j]
 return out
def q(a,i):return reduce(lambda z,s:z*(s+a+i),ss,F(1))
@lru_cache(None)
def D(n,a):return F(1) if n==0 else det([[reduce(lambda z,s:z*rise(s+a+i,j),ss,F(1)) for j in range(n)] for i in range(n)])
@lru_cache(None)
def R(n,a):
 if n<=1:return F(1)
 return (q(a,n-1)*R(n-1,a)*R(n-1,a+2)-q(a,0)*R(n-1,a+1)**2)/R(n-2,a+2)
comparisons=[{"n":n,"shift":a,"equal":R(n,a)==D(n,a)} for n in range(0,9) for a in range(0,7)]
theta=[]
for n in range(2,9):
 td=q(0,0)*D(n-1,1)**2/(q(0,n-1)*D(n-1,0)*D(n-1,2));tr=q(0,0)*R(n-1,1)**2/(q(0,n-1)*R(n-1,0)*R(n-1,2));theta.append({"n":n,"equal":td==tr,"value":str(tr)})
checks={"recurrence_matches_all_tested_determinants":all(x["equal"] for x in comparisons),"theta_matches":all(x["equal"] for x in theta),"boundary_is_unit":R(0,0)==R(1,0)==1,"recurrence_values_positive":all(R(n,a)>0 for n in range(9) for a in range(7)),"deliberate_wrong_shift_rejected":R(5,1)!=D(5,2)}
result={"schema":"marici.strominger.rh_quarter_shifted_condensation_recurrence.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Dodgson condensation gives a closed shifted half-lattice recurrence with unit n=0,1 boundary. Exact checks through n=8 and shifts 0..6 reproduce determinants and cross ratios; asymptotic control of this recurrence remains unproved.","recurrence":"R(n,a)=[q_a(n-1)R(n-1,a)R(n-1,a+2)-q_a(0)R(n-1,a+1)^2]/R(n-2,a+2)","checks":checks,"comparison_count":len(comparisons),"theta":theta,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_shifted_condensation_recurrence.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
