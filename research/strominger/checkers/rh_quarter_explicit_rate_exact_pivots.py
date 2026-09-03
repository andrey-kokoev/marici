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
def logF(x):return math.log(x.numerator)-math.log(x.denominator)
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
def Acur(k):return 1-k*k*(2*k*k+2*k+1)/(2*(k+2)*(k+1)**3)
def H(k):return math.log(Acur(k))+4*math.log(k+1)-4
def fexplicit(k,N=120000):
 s=0
 for i in range(N):
  x=(i+.5)/N;u=k+(k+2)*x/(1-x);s+=H(u)
 return s/N
rows=[]
for kap in (F(1,2),F(1),F(2),F(4)):
 ns=[n for n in range(14,29) if (kap*n).denominator==1];X=[];y=[]
 for n in ns:
  t=int(kap*n);d=S(n,t)/S(n-1,t);y.append((logF(d)-4*n*math.log(n))/n);X.append([1,math.log(n)/n,1/n,1/n**2])
 G=[[sum(x[i]*x[j] for x in X) for j in range(4)] for i in range(4)];b=[sum(x[i]*v for x,v in zip(X,y)) for i in range(4)];fit=solve(G,b);exact=fexplicit(float(kap));rows.append({"kappa":str(kap),"f_fit":fit[0],"f_explicit":exact,"residual":fit[0]-exact,"log_n_over_n_coefficient":fit[1],"sample_count":len(ns)})
checks={"all_fits_finite":all(math.isfinite(r["f_fit"]) for r in rows),"explicit_residual_below_two_e_minus_four":max(abs(r["residual"]) for r in rows)<2e-4,"log_correction_near_minus_seven_halves":max(abs(r["log_n_over_n_coefficient"]+3.5) for r in rows)<.002,"log_coefficient_kappa_independent_on_grid":max(r["log_n_over_n_coefficient"] for r in rows)-min(r["log_n_over_n_coefficient"] for r in rows)<.002,"deliberate_zero_log_coefficient_fails":all(abs(r["log_n_over_n_coefficient"])>3.49 for r in rows)}
result={"schema":"marici.strominger.rh_quarter_explicit_rate_exact_pivots.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Including a log(n)/n correction removes the apparent constant bias in degree-28 pivot fits and directly tests the zero-parameter explicit rate. Residuals quantify the remaining finite-window error.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_explicit_rate_exact_pivots.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
