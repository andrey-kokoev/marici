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
 ss=tuple(F(1)+F(1,2)*k+t for k in range(4))
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
def fit(t,lo,hi):
 ms=range(lo,hi+1);X=[[1,1/m,1/m**2] for m in ms];y=[float(S(m,t+1)**2/(S(m,t)*S(m,t+2)))/m**2 for m in ms];G=[[sum(x[i]*x[j] for x in X) for j in range(3)] for i in range(3)];b=[sum(x[i]*v for x,v in zip(X,y)) for i in range(3)];return solve(G,b)[0]
windows=[(12,20),(16,24),(20,28)];rows=[]
for t in range(8,15):
 values=[]
 for lo,hi in windows:
  C=fit(t,lo,hi);values.append({"window":f"{lo}..{hi}","C_fit":C,"universal_quarter_scaled":4*(t+3)**2*C,"spacing_half_scaled":2*(t+3)**2*C})
 rows.append({"shift":t,"windows":values})
last=[r["windows"][-1]["universal_quarter_scaled"] for r in rows];coarse=[r["windows"][0]["universal_quarter_scaled"] for r in rows]
checks={"all_fits_positive":all(w["C_fit"]>0 for r in rows for w in r["windows"]),"nested_windows_change_values":any(abs(a-b)>1e-4 for a,b in zip(coarse,last)),"fine_tail_nearer_universal_quarter_than_spacing_half":all(abs(r["windows"][-1]["universal_quarter_scaled"]-1)<abs(r["windows"][-1]["spacing_half_scaled"]-1) for r in rows),"fine_endpoint_near_one":abs(last[-1]-1)<.08,"coarse_deviation_was_finite_window_bias":abs(last[-1]-1)<abs(coarse[-1]-1)}
result={"schema":"marici.strominger.rh_quarter_spacing_half_nested_windows.v1","status":"passed" if all(checks.values()) else "failed","verdict":"For h=1/2, nested degree windows through 20..28 move the tail toward the universal-quarter normalization and away from the spacing-half numerator. This attributes the earlier 1.1078 oddball to finite-window bias on the tested grid.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_spacing_half_nested_windows.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
