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
def integral(k,n=4000):
 h=k/n;s=H(0)/4+H(k)/(k+2)**2
 for i in range(1,n):
  x=i*h;s+=(4 if i%2 else 2)*H(x)/(x+2)**2
 return s*h/3
rows=[]
for kap in (F(1,2),F(1),F(2),F(4)):
 ns=[n for n in range(14,29) if (kap*n).denominator==1];X=[];y=[]
 for n in ns:
  t=int(kap*n);d=S(n,t)/S(n-1,t);fest=(logF(d)-4*n*math.log(n))/n;X.append([1,1/n,1/n**2]);y.append(fest)
 G=[[sum(x[i]*x[j] for x in X) for j in range(3)] for i in range(3)];b=[sum(x[i]*v for x,v in zip(X,y)) for i in range(3)];flim=solve(G,b)[0];k=float(kap);C=flim/(k+2)+integral(k)
 rows.append({"kappa":str(kap),"f_limit_fit":flim,"inferred_C":C,"sample_count":len(ns)})
Cs=[r["inferred_C"] for r in rows];spread=max(Cs)-min(Cs);mean=sum(Cs)/len(Cs)
checks={"all_f_limits_finite":all(math.isfinite(r["f_limit_fit"]) for r in rows),"inferred_constants_finite":all(math.isfinite(c) for c in Cs),"direct_fits_show_systematic_kappa_bias":all(Cs[i+1]>Cs[i] for i in range(len(Cs)-1)),"direct_fit_spread_exceeds_tight_consistency_gate":spread>.02,"deliberate_zero_normalization_fails":max(abs(c) for c in Cs)>.1}
result={"schema":"marici.strominger.rh_quarter_pivot_rate_boundary_fit.v1","status":"passed" if all(checks.values()) else "failed","verdict":f"Direct degree-28 pivot fits do not determine one boundary constant: inferred C rises systematically with kappa and has spread {spread:.3g}. This finite-window bias requires the independent leading-symbol boundary.","checks":checks,"rows":rows,"mean_C":mean,"spread_C":spread,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_pivot_rate_boundary_fit.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
