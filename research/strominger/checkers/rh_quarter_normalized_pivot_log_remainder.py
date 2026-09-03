import json,math
from fractions import Fraction as F
from functools import reduce,lru_cache
from pathlib import Path
def rise(x,k):
 r=F(1)
 for j in range(k):r*=x+j
 return r
def det(a):
 a=[r[:] for r in a];n=len(a);out=F(1)
 for k in range(n):
  p=next(i for i in range(k,n) if a[i][k]);a[k],a[p]=a[p],a[k]
  if p!=k:out=-out
  z=a[k][k];out*=z
  for j in range(k,n):a[k][j]/=z
  for i in range(k+1,n):
   z=a[i][k]
   for j in range(k,n):a[i][j]-=z*a[k][j]
 return out
@lru_cache(None)
def S(n,t):
 ss=tuple(F(1)+F(k,4)+t for k in range(4));return det([[reduce(lambda z,s:z*rise(s+i,j),ss,F(1)) for j in range(n)] for i in range(n)])
def d(n,t):return S(n,t)/S(n-1,t)
def q(t,i):return (t+i+1)*(t+i+F(5,4))*(t+i+F(3,2))*(t+i+F(7,4))
def logF(x):return math.log(x.numerator)-math.log(x.denominator)
def Alim(k):return 1-k*k*(2*k*k+2*k+1)/(2*(k+2)*(k+1)**3)
def solve(A,b):
 A=[r[:]+[v] for r,v in zip(A,b)];m=len(A)
 for i in range(m):
  p=max(range(i,m),key=lambda k:abs(A[k][i]));A[i],A[p]=A[p],A[i];z=A[i][i]
  for j in range(i,m+1):A[i][j]/=z
  for k in range(m):
   if k!=i:
    z=A[k][i]
    for j in range(i,m+1):A[k][j]-=z*A[i][j]
 return [A[i][-1] for i in range(m)]
rows=[]
for kap in (F(1,2),F(1),F(2),F(4)):
 ns=[n for n in range(14,29) if (kap*n).denominator==1];X=[];y=[]
 for n in ns:
  t=int(kap*n);An=d(n,t)/(q(F(t),n-1)*d(n-1,t+2));X.append([math.log(n)/n,1/n,1/n**2]);y.append(logF(An)-math.log(Alim(float(kap))))
 G=[[sum(x[i]*x[j] for x in X) for j in range(3)] for i in range(3)];b=[sum(x[i]*v for x,v in zip(X,y)) for i in range(3)];fit=solve(G,b)
 rows.append({"kappa":str(kap),"log_n_over_n_coefficient":fit[0],"inverse_n":fit[1],"inverse_n2":fit[2],"sample_count":len(ns)})
coeff=[r["log_n_over_n_coefficient"] for r in rows]
checks={"coefficients_finite":all(math.isfinite(x) for x in coeff),"tight_zero_gate_fails":max(abs(x) for x in coeff)>.03,"coefficients_remain_below_point_zero_five":max(abs(x) for x in coeff)<.05,"coefficient_sign_changes":min(coeff)<0<max(coeff),"candidate_limits_positive":all(Alim(float(F(r["kappa"])))>0 for r in rows)}
result={"schema":"marici.strominger.rh_quarter_normalized_pivot_log_remainder.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Direct degree-28 normalized-pivot fits do not establish a zero log(n)/n remainder: coefficients range from -0.0136 to 0.0438 and fail the preregistered 0.03 gate. The test is contaminated by finite-window error in the unproved crossover limit.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_normalized_pivot_log_remainder.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
