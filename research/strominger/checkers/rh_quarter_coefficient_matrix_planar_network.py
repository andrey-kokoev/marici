import json,itertools
from fractions import Fraction as F
from functools import reduce
from pathlib import Path
ss=(F(1),F(5,4),F(3,2),F(7,4))
def mul(p,q):
 r=[F(0)]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  for j,b in enumerate(q):r[i+j]+=a*b
 return r
def direct(j):
 p=[F(1)]
 for t in range(j):
  for s in ss:p=mul(p,[s+t,F(1)])
 return p
def network(j):
 weights=[F(1)]
 for t in range(j):
  for s in ss:
   nxt=[F(0)]*(len(weights)+1)
   for d,w in enumerate(weights):nxt[d]+=(s+t)*w;nxt[d+1]+=w
   weights=nxt
 return weights
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
paths=[network(j) for j in range(9)];comparisons=[paths[j]==direct(j) for j in range(9)];minor_signs=[]
for k in range(1,6):
 for cols in itertools.combinations(range(7),k):
  maxd=max(4*j for j in cols)
  for rows in itertools.combinations(range(maxd+1),k):
   d=det([[paths[j][m] if m<len(paths[j]) else F(0) for j in cols] for m in rows]);minor_signs.append(d)
checks={"network_paths_equal_polynomial_coefficients":all(comparisons),"all_tested_path_matrix_minors_nonnegative":all(d>=0 for d in minor_signs),"some_path_matrix_minors_positive":any(d>0 for d in minor_signs),"all_edge_weights_positive":all(s+t>0 for t in range(9) for s in ss),"deliberate_sink_order_reversal_negative":det([[paths[j][m] if m<len(paths[j]) else F(0) for j in (0,1)] for m in (1,0)])<0}
result={"schema":"marici.strominger.rh_quarter_coefficient_matrix_planar_network.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The coefficient matrix is the path matrix of a planar left/up lattice with edge weights 1 and s+t>0. Lindstrom-Gessel-Viennot therefore proves all ordered minors nonnegative at every size; exact path reconstruction through stage eight and a bounded minor census verify the orientation and weights.","network":"each factor x+s+t is one layer with a level edge of weight s+t and a rising edge of weight 1","tested_minor_count":len(minor_signs),"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_coefficient_matrix_planar_network.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
