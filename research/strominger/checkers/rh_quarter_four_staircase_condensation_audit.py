import json
from fractions import Fraction as F
from functools import reduce
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
def S(n,ss):return F(1) if n==0 else det([[reduce(lambda z,s:z*rise(s+i,j),ss,F(1)) for j in range(n)] for i in range(n)])
def sh(ss,c):return tuple(s+c for s in ss)
def q(ss,i):return reduce(lambda z,s:z*(s+i),ss,F(1))
vectors=((F(1),F(5,4),F(3,2),F(7,4)),(F(2),F(9,4),F(5,2),F(11,4)))
rows=[]
for ss in vectors:
 for n in range(2,8):
  lhs=S(n,ss)*S(n-2,sh(ss,2));rhs=q(ss,n-1)*S(n-1,ss)*S(n-1,sh(ss,2))-q(ss,0)*S(n-1,sh(ss,1))**2
  rows.append({"parameters":[str(x) for x in ss],"n":n,"residual":str(lhs-rhs)})
ss=vectors[0];n=6;wrong=q(ss,n)*S(n-1,ss)*S(n-1,sh(ss,2))-q(ss,0)*S(n-1,sh(ss,1))**2
checks={"all_condensation_residuals_zero":all(r["residual"]=="0" for r in rows),"source_vector_tested":any(r["parameters"][0]=="1" for r in rows),"shifted_vector_tested":any(r["parameters"][0]=="2" for r in rows),"deliberate_wrong_q_index_nonzero":S(n,ss)*S(n-2,sh(ss,2))!=wrong}
result={"schema":"marici.strominger.rh_quarter_four_staircase_condensation_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The quarter four-staircase determinant satisfies an exact vector-shifted Desnanot-Jacobi recurrence. Twelve rational cases pass and a wrong q-index control fails. The cross-minor asymptotic remains necessary for the 13/48 coefficient.","checks":checks,"tested_rows":len(rows),"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_four_staircase_condensation_audit.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
