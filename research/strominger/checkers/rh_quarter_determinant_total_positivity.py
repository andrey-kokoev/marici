import json,itertools
from fractions import Fraction as F
from functools import reduce
from pathlib import Path
ss=(F(1),F(5,4),F(3,2),F(7,4))
def rise(x,k):
 r=F(1)
 for j in range(k):r*=x+j
 return r
def entry(i,j,a):return reduce(lambda z,s:z*rise(s+a+i,j),ss,F(1))
def det(m):
 m=[r[:] for r in m];n=len(m);out=F(1)
 for k in range(n):
  piv=next((i for i in range(k,n) if m[i][k]),None)
  if piv is None:return F(0)
  m[k],m[piv]=m[piv],m[k]
  if piv!=k:out=-out
  z=m[k][k];out*=z
  for j in range(k,n):m[k][j]/=z
  for i in range(k+1,n):
   z=m[i][k]
   for j in range(k,n):m[i][j]-=z*m[k][j]
 return out
N=7;count=0;nonpositive=[];by_size={}
for a in range(5):
 A=[[entry(i,j,a) for j in range(N)] for i in range(N)]
 for k in range(1,N+1):
  for rr in itertools.combinations(range(N),k):
   for cc in itertools.combinations(range(N),k):
    d=det([[A[i][j] for j in cc] for i in rr]);count+=1;by_size[str(k)]=by_size.get(str(k),0)+1
    if d<=0 and len(nonpositive)<10:nonpositive.append({"shift":a,"rows":rr,"columns":cc,"determinant":str(d)})
checks={"all_tested_minors_strictly_positive":not nonpositive,"tested_all_sizes_one_through_seven":set(by_size)==set(str(k) for k in range(1,8)),"tested_five_shifts":count==5*sum(__import__('math').comb(N,k)**2 for k in range(1,N+1)),"full_determinants_positive":all(det([[entry(i,j,a) for j in range(N)] for i in range(N)])>0 for a in range(5)),"deliberate_row_reversal_negative":det([[entry(i,j,0) for j in range(2)] for i in (1,0)])<0}
result={"schema":"marici.strominger.rh_quarter_determinant_total_positivity.v1","status":"passed" if all(checks.values()) else "failed","verdict":"All minors of the 7x7 quarter source matrices at shifts 0..4 are tested exactly for strict total positivity. Passing is a finite structural diagnostic, not an all-size proof.","matrix_size":N,"shifts":[0,1,2,3,4],"minor_count":count,"minor_counts_by_size":by_size,"first_nonpositive":nonpositive,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_determinant_total_positivity.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
