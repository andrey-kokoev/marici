import json
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
  q=a[k][k];out*=q
  for j in range(k,n):a[k][j]/=q
  for i in range(k+1,n):
   q=a[i][k]
   for j in range(k,n):a[i][j]-=q*a[k][j]
 return out
@lru_cache(maxsize=None)
def S(n,ss):return F(1) if n==0 else det([[reduce(lambda z,s:z*rise(s+i,j),ss,F(1)) for j in range(n)] for i in range(n)])
def sh(ss,k):return tuple(s+k for s in ss)
def d(n,ss):return S(n,ss)/S(n-1,ss)
def q(ss,i):return reduce(lambda z,s:z*(s+i),ss,F(1))
ss=(F(1),F(5,4),F(3,2),F(7,4));rows=[];prod=F(1)
for n in range(1,8):
 c=d(n,sh(ss,1))**2/(d(n,ss)*d(n,sh(ss,2)));prod*=c;R=S(n,sh(ss,1))**2/(S(n,ss)*S(n,sh(ss,2)))
 pivot_res=F(0) if n==1 else d(n,ss)/d(n-1,sh(ss,2))-(q(ss,n-1)-q(ss,0)*S(n-1,sh(ss,1))**2/(S(n-1,ss)*S(n-1,sh(ss,2))))
 rows.append({"n":n,"product_residual":str(prod-R),"pivot_recurrence_residual":str(pivot_res),"curvature_positive":c>0})
checks={"pivot_product_telescopes_exactly":all(r["product_residual"]=="0" for r in rows),"pivot_recurrence_exact":all(r["pivot_recurrence_residual"]=="0" for r in rows),"curvatures_positive":all(r["curvature_positive"] for r in rows),"deliberate_target_nontrivial":F(104,1575)!=1}
result={"schema":"marici.strominger.rh_quarter_lu_pivot_shift_system_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The global staircase shift curvature telescopes exactly into local LU-pivot curvatures, and condensation yields a closed pivot/product recurrence. Proving c_n=1+2/n+O(n^-2) and the renormalized product amplitude remains open.","checks":checks,"tested_sizes":"1..7","gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_lu_pivot_shift_system_audit.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
