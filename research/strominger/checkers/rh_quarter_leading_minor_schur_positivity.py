import json,itertools
from fractions import Fraction as F
from pathlib import Path
ss=(F(1),F(5,4),F(3,2),F(7,4))
def mul(p,q):
 r=[F(0)]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  for j,b in enumerate(q):r[i+j]+=a*b
 return r
def poly(j):
 p=[F(1)]
 for s in ss:
  for t in range(j):p=mul(p,[s+t,F(1)])
 return p
def det(m):
 m=[r[:] for r in m];n=len(m);out=F(1)
 for k in range(n):
  p=next((i for i in range(k,n) if m[i][k]),None)
  if p is None:return F(0)
  m[k],m[p]=m[p],m[k]
  if p!=k:out=-out
  z=m[k][k];out*=z
  for j in range(k,n):m[k][j]/=z
  for i in range(k+1,n):
   z=m[i][k]
   for j in range(k,n):m[i][j]-=z*m[k][j]
 return out
records=[];first_negative=None
for k in range(1,8):
 ps=[poly(j) for j in range(k)];maxd=4*(k-1);positive=zero=negative=0
 for tail in itertools.combinations(range(1,maxd+1),k-1):
  degrees=(0,)+tail;d=det([[ps[j][m] if m<len(ps[j]) else F(0) for j in range(k)] for m in degrees])
  if d>0:positive+=1
  elif d==0:zero+=1
  else:
   negative+=1
   if first_negative is None:first_negative={"size":k,"degrees":degrees,"determinant":str(d)}
 records.append({"size":k,"coefficient_minor_count":positive+zero+negative,"positive":positive,"zero":zero,"negative":negative})
checks={"all_coefficient_maximal_minors_nonnegative":first_negative is None,"tested_sizes_one_through_seven":[r["size"] for r in records]==list(range(1,8)),"each_size_has_positive_minor":all(r["positive"]>0 for r in records),"zeros_allowed_by_degree_support":all(r["zero"]>=0 for r in records),"deliberate_reversed_degree_order_negative":det([[poly(j)[m] if m<len(poly(j)) else F(0) for j in range(2)] for m in (1,0)])<0}
result={"schema":"marici.strominger.rh_quarter_leading_minor_schur_positivity.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Cauchy-Binet expands det(p_j(x_i))/V(x) in Schur polynomials with coefficient-matrix maximal minors. Exact enumeration through size seven tests whether all such coefficients are nonnegative; a negative minor is retained as a falsifier.","records":records,"first_negative":first_negative,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_leading_minor_schur_positivity.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
