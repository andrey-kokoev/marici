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
 ss=tuple(x+t for x in (F(1),F(5,4),F(3,2),F(7,4)))
 return F(1) if n==0 else det([[reduce(lambda z,s:z*rise(s+i,j),ss,F(1)) for j in range(n)] for i in range(n)])
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
for t in range(13):
 ms=range(14,25);X=[[1,1/m,1/m**2] for m in ms];y=[]
 for m in ms:y.append(float(S(m,t+1)**2/(S(m,t)*S(m,t+2)))/m**2)
 G=[[sum(x[i]*x[j] for x in X) for j in range(3)] for i in range(3)];b=[sum(x[i]*v for x,v in zip(X,y)) for i in range(3)];fit=solve(G,b);rat=F(fit[0]).limit_denominator(5000)
 rows.append({"shift":t,"C_fit":fit[0],"inverse_C_fit":1/fit[0],"rational_candidate":str(rat),"candidate_error":fit[0]-float(rat),"relative_first_correction":fit[1]/fit[0]})
checks={"all_fits_positive":all(r["C_fit"]>0 for r in rows),"all_fits_finite":all(math.isfinite(r["C_fit"]) for r in rows),"source_candidate_recovered":abs(rows[0]["C_fit"]-104/1575)<2e-4,"shift_dependence_nonconstant":len({round(r["C_fit"],8) for r in rows})==len(rows)}
result={"schema":"marici.strominger.rh_quarter_common_shift_amplitude_grid.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Parameter-uniform exact determinants yield distinct fitted curvature amplitudes C(t) for shifts 0..12. This supplies finite data for a Barnes shift equation but does not identify its divisor.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_common_shift_amplitude_grid.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
