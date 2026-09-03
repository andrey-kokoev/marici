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
 ss=tuple(F(1)+F(k,4)+t for k in range(4))
 return det([[reduce(lambda z,s:z*rise(s+i,j),ss,F(1)) for j in range(n)] for i in range(n)])
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
kappas=(F(1,2),F(1),F(3,2),F(2),F(3),F(4),F(6));rows=[]
for kap in kappas:
 ns=[n for n in range(14,29) if (kap*n).denominator==1];X=[];y=[]
 for n in ns:
  t=int(kap*n);R=float(S(n,t+1)**2/(S(n,t)*S(n,t+2)));X.append([1,1/n,1/n**2]);y.append(R)
 G=[[sum(x[i]*x[j] for x in X) for j in range(3)] for i in range(3)];b=[sum(x[i]*v for x,v in zip(X,y)) for i in range(3)];fit=solve(G,b);candidate=1+1/(4*float(kap)**2)
 rows.append({"kappa":str(kap),"limit_fit":fit[0],"naive_candidate":candidate,"naive_residual":fit[0]-candidate,"scaled_curvature":float(kap)**2*(fit[0]-1),"sample_count":len(ns)})
scaled=[r["scaled_curvature"] for r in rows]
checks={"all_limits_above_one":all(r["limit_fit"]>1 for r in rows),"all_fits_finite":all(math.isfinite(r["limit_fit"]) for r in rows),"naive_additive_crossover_refuted":sum(abs(r["naive_residual"]) for r in rows)>.5,"scaled_curvature_increases":all(scaled[i+1]>scaled[i] for i in range(len(scaled)-1)),"scaled_curvature_between_quarter_and_three_halves":all(.25<z<1.5 for z in scaled)}
result={"schema":"marici.strominger.rh_quarter_double_scaling_curvature.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The naive crossover 1+1/(4kappa^2) is refuted. Instead kappa^2(F(kappa)-1) rises across the enlarged kappa grid, lying between the quarter small-kappa coefficient and the 3/2 fixed-degree leading-symbol coefficient.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_double_scaling_curvature.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
