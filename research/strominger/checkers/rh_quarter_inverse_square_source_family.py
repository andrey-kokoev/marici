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
def S(n,a,h,t):
 ss=tuple(a+h*k+t for k in range(4))
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
def fitC(a,h,t):
 ms=range(12,21);X=[[1,1/m,1/m**2] for m in ms];y=[float(S(m,a,h,t+1)**2/(S(m,a,h,t)*S(m,a,h,t+2)))/m**2 for m in ms];G=[[sum(x[i]*x[j] for x in X) for j in range(3)] for i in range(3)];b=[sum(x[i]*v for x,v in zip(X,y)) for i in range(3)];return solve(G,b)[0]
families=[(F(1),F(1,4)),(F(2),F(1,4)),(F(1),F(1,2)),(F(1,2),F(1,4))];rows=[]
for a,h in families:
 scaled=[]
 for t in range(6,11):
  C=fitC(a,h,t);z=4*C*(float(a+4*h)+t)**2;scaled.append(z)
 rows.append({"a":str(a),"h":str(h),"completed_endpoint":str(a+4*h),"four_endpoint_squared_C":scaled,"last":scaled[-1]})
checks={"all_scaled_positive":all(z>0 for r in rows for z in r["four_endpoint_squared_C"]),"base_shift_is_translation_exact_on_overlap":rows[1]["four_endpoint_squared_C"][:4]==rows[0]["four_endpoint_squared_C"][1:],"original_endpoint_two":rows[0]["completed_endpoint"]=="2","original_tail_near_one":abs(rows[0]["last"]-1)<.08,"spacing_numerator_h_refuted":abs(rows[2]["last"]/(4*float(F(1,2)))-1)>.4,"universal_quarter_numerator_not_verified":abs(rows[2]["last"]-1)>.1}
result={"schema":"marici.strominger.rh_quarter_inverse_square_source_family.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Changing the base a translates the common-shift grid exactly, but the proposed numerator h is refuted by the h=1/2 family. A universal 1/4 numerator remains plausible for h=1/4 and unresolved for h=1/2, whose finite normalized tail ends at 1.1078.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_inverse_square_source_family.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
