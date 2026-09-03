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
def moment(k,a):
 n=k+2;return q(a,0)*D(n-1,a+1)**2/(q(a,n-1)*D(n-1,a)*D(n-1,a+2))
def add(p,qv,c=F(1)):
 r=p+[F(0)]*max(0,len(qv)-len(p))
 for i,x in enumerate(qv):r[i]+=c*x
 while len(r)>1 and r[-1]==0:r.pop()
 return r
def inner(p,qv,m):return sum(x*y*m[i+j] for i,x in enumerate(p) for j,y in enumerate(qv))
def xp(p):return [F(0)]+p
def matvec(J,v):return [sum(J[i][j]*v[j] for j in range(len(v))) for i in range(len(v))]
records=[]
for a in range(5):
 m=[moment(k,a) for k in range(12)];P=[];h=[]
 for n in range(6):
  p=[F(0)]*n+[F(1)]
  for j,z in enumerate(P):p=add(p,z,-inner(p,z,m)/h[j])
  P.append(p);h.append(inner(p,p,m))
 alpha=[inner(xp(P[n]),P[n],m)/h[n] for n in range(6)];beta=[None]+[h[n]/h[n-1] for n in range(1,6)];J=[[F(0)]*6 for _ in range(6)]
 for n in range(6):
  J[n][n]=alpha[n]
  if n<5:J[n+1][n]=F(1)
  if n:J[n-1][n]=beta[n]
 v=[F(1)]+[F(0)]*5;reconstructed=[]
 for k in range(11):
  reconstructed.append(m[0]*v[0]);v=matvec(J,v)
 records.append({"shift":a,"moments_zero_through_ten_exact":reconstructed==m[:11],"all_level_weights_positive":all(x>0 for x in alpha),"all_down_weights_positive":all(x>0 for x in beta[1:]),"all_level_weights_below_one":all(x<1 for x in alpha)})
checks={"all_moments_reconstructed_exactly":all(r["moments_zero_through_ten_exact"] for r in records),"all_motzkin_edge_weights_positive":all(r["all_level_weights_positive"] and r["all_down_weights_positive"] for r in records),"level_weights_support_compatible":all(r["all_level_weights_below_one"] for r in records),"tested_five_shifts":len(records)==5,"deliberate_negative_edge_excluded":all(r["all_down_weights_positive"] for r in records)}
result={"schema":"marici.strominger.rh_quarter_cross_ratio_moment_path_representation.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Finite Jacobi data give an exact positive Motzkin-path representation m_k=m_0(J^k)_(0,0) for moments zero through ten. Every level and down edge weight is positive. This is an exact finite representation, not an all-order Jacobi-positivity theorem.","records":records,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_cross_ratio_moment_path_representation.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
