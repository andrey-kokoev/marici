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
def d(n,t):return S(n,t)/S(n-1,t)
def rho(n):return (d(n,1)**2/(d(n,0)*d(n,2)))/F(n+2,n)
def solve(A,b):
 A=[r[:]+[v] for r,v in zip(A,b)];m=len(A)
 for i in range(m):
  p=next(k for k in range(i,m) if A[k][i]);A[i],A[p]=A[p],A[i];z=A[i][i];A[i]=[v/z for v in A[i]]
  for k in range(m):
   if k!=i:
    z=A[k][i];A[k]=[u-z*v for u,v in zip(A[k],A[i])]
 return [r[-1] for r in A]
vals={n:rho(n) for n in range(1,26)};tests=[]
for residue in range(4):
 ns=[n for n in vals if n%4==residue]
 for deg in (1,2):
  need=2*deg+1;train=ns[:need];hold=ns[need:]
  A=[];b=[]
  for n in train:
   y=vals[n];A.append([F(n)**k for k in range(deg+1)]+[-y*F(n)**k for k in range(deg)]);b.append(y*F(n)**deg)
  sol=solve(A,b);p=sol[:deg+1];q=sol[deg+1:]+[F(1)]
  pred=lambda n:sum(p[k]*n**k for k in range(deg+1))/sum(q[k]*n**k for k in range(deg+1))
  tests.append({"residue_mod_4":residue,"degree":deg,"training":train,"holdout":hold,"holdout_exact":bool(hold) and all(pred(n)==vals[n] for n in hold)})
checks={"exact_factors_through_25":len(vals)==25,"all_factors_positive":all(v>0 for v in vals.values()),"every_test_has_holdout":all(t["holdout"] for t in tests),"no_residuewise_degree_one_or_two_formula":not any(t["holdout_exact"] for t in tests),"deliberate_residue_partition_nonempty":all(any(n%4==r for n in vals) for r in range(4))}
result={"schema":"marici.strominger.rh_quarter_renormalized_pivot_block_interpolation.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact rho_j through j=25 reject residue-mod-4 rational formulas of equal numerator/denominator degree 1 or 2 on holdout. Quarter-lattice block periodicity does not rescue low-degree termwise telescoping.","checks":checks,"tests":tests,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_renormalized_pivot_block_interpolation.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
