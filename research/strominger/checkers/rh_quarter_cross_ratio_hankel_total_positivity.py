import json,itertools,math
from fractions import Fraction as F
from functools import lru_cache,reduce
from pathlib import Path
ss=(F(1),F(5,4),F(3,2),F(7,4))
def q(a,i):return reduce(lambda z,s:z*(s+a+i),ss,F(1))
@lru_cache(None)
def D(n,a):
 if n<=1:return F(1)
 return (q(a,n-1)*D(n-1,a)*D(n-1,a+2)-q(a,0)*D(n-1,a+1)**2)/D(n-2,a+2)
def m(k,a):
 n=k+2;return q(a,0)*D(n-1,a+1)**2/(q(a,n-1)*D(n-1,a)*D(n-1,a+2))
def det(A):
 A=[r[:] for r in A];n=len(A);out=F(1)
 for k in range(n):
  p=next((i for i in range(k,n) if A[i][k]),None)
  if p is None:return F(0)
  A[k],A[p]=A[p],A[k]
  if p!=k:out=-out
  z=A[k][k];out*=z
  for j in range(k,n):A[k][j]/=z
  for i in range(k+1,n):
   z=A[i][k]
   for j in range(k,n):A[i][j]-=z*A[k][j]
 return out
N=7;count=0;first_nonpositive=None;by_size={}
for a in range(5):
 H=[[m(i+j,a) for j in range(N)] for i in range(N)]
 for k in range(1,N+1):
  for rr in itertools.combinations(range(N),k):
   for cc in itertools.combinations(range(N),k):
    z=det([[H[i][j] for j in cc] for i in rr]);count+=1;by_size[str(k)]=by_size.get(str(k),0)+1
    if z<=0 and first_nonpositive is None:first_nonpositive={"shift":a,"rows":rr,"columns":cc,"determinant":str(z)}
checks={"all_bounded_hankel_minors_strictly_positive":first_nonpositive is None,"tested_all_minor_sizes":set(by_size)==set(str(k) for k in range(1,8)),"minor_count_correct":count==5*sum(math.comb(N,k)**2 for k in range(1,N+1)),"deliberate_row_reversal_negative":det([[m(i+j,0) for j in range(2)] for i in (1,0)])<0}
result={"schema":"marici.strominger.rh_quarter_cross_ratio_hankel_total_positivity.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Every minor of the 7x7 cross-ratio Hankel matrices at shifts zero through four is tested exactly. Passing is finite Hankel total positivity, the target sign pattern for a positive moment network, but does not construct an all-order network.","matrix_size":N,"minor_count":count,"minor_counts_by_size":by_size,"first_nonpositive":first_nonpositive,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_cross_ratio_hankel_total_positivity.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
