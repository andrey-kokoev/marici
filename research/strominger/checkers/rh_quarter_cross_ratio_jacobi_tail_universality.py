import json,math
from fractions import Fraction as F
from functools import lru_cache,reduce
from pathlib import Path
ss=(F(1),F(5,4),F(3,2),F(7,4))
def q(a,i):return reduce(lambda z,s:z*(s+a+i),ss,F(1))
@lru_cache(None)
def D(n,a):
 if n<=1:return F(1)
 return (q(a,n-1)*D(n-1,a)*D(n-1,a+2)-q(a,0)*D(n-1,a+1)**2)/D(n-2,a+2)
def moment(k,a):
 n=k+2;return q(a,0)*D(n-1,a+1)**2/(q(a,n-1)*D(n-1,a)*D(n-1,a+2))
def add(p,qv,c=F(1)):
 r=p+[F(0)]*max(0,len(qv)-len(p))
 for i,x in enumerate(qv):r[i]+=c*x
 while len(r)>1 and r[-1]==0:r.pop()
 return r
def inner(p,qv,m):return sum(x*y*m[i+j] for i,x in enumerate(p) for j,y in enumerate(qv))
def xp(p):return [F(0)]+p
records=[];exact=[]
for a in range(5):
 m=[moment(k,a) for k in range(24)];P=[];h=[]
 for n in range(12):
  p=[F(0)]*n+[F(1)]
  for j,z in enumerate(P):p=add(p,z,-inner(p,z,m)/h[j])
  P.append(p);h.append(inner(p,p,m))
 for n in range(11):
  alpha=inner(xp(P[n]),P[n],m)/h[n];beta=None if n==0 else h[n]/h[n-1];res=add(add(xp(P[n]),P[n+1],F(-1)),P[n],-alpha)
  if n:res=add(res,P[n-1],-beta)
  exact.append(all(x==0 for x in res));records.append({"shift":a,"order":n,"alpha":float(alpha),"beta":None if beta is None else float(beta),"alpha_deviation":float(abs(alpha-F(1,2))),"beta_deviation":None if beta is None else float(abs(beta-F(1,16)))})
order4=[r for r in records if r["order"]==4];latest=[r for r in records if r["order"]==10]
checks={"all_recurrences_exact":all(exact),"latest_alpha_deviation_below_point_zero_zero_two":max(r["alpha_deviation"] for r in latest)<.002,"latest_beta_deviation_below_point_zero_zero_two":max(r["beta_deviation"] for r in latest)<.002,"alpha_improves_from_order_four":max(r["alpha_deviation"] for r in latest)<max(r["alpha_deviation"] for r in order4),"beta_improves_from_order_four":max(r["beta_deviation"] for r in latest)<max(r["beta_deviation"] for r in order4),"all_tail_values_finite":all(math.isfinite(r["alpha"]) and (r["beta"] is None or math.isfinite(r["beta"])) for r in records)}
result={"schema":"marici.strominger.rh_quarter_cross_ratio_jacobi_tail_universality.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact Jacobi recurrences through order ten test convergence toward alpha=1/2 and beta=1/16 uniformly across shifts zero through four. Passing supports regular [0,1] spectral support but does not determine endpoint density exponent.","records":records,"latest_max_deviation":{"alpha":max(r["alpha_deviation"] for r in latest),"beta":max(r["beta_deviation"] for r in latest)},"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_cross_ratio_jacobi_tail_universality.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
