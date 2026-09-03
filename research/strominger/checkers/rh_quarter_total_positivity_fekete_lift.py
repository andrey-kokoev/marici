import json,itertools
from fractions import Fraction as F
from functools import reduce
from pathlib import Path
base=Path(__file__).parents[1];network=json.loads((base/"results"/"rh_quarter_coefficient_matrix_planar_network.json").read_text(encoding="utf-8"));ss=(F(1),F(5,4),F(3,2),F(7,4))
def rise(x,k):
 r=F(1)
 for j in range(k):r*=x+j
 return r
def entry(i,j,a):return reduce(lambda z,s:z*rise(s+a+i,j),ss,F(1))
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
N=8;initial=[];arbitrary=[]
for a in range(4):
 A=[[entry(i,j,a) for j in range(N)] for i in range(N)]
 for k in range(1,N+1):
  for r in range(N-k+1):initial.append(det([[A[r+i][j] for j in range(k)] for i in range(k)]))
  for c in range(N-k+1):initial.append(det([[A[i][c+j] for j in range(k)] for i in range(k)]))
 for k in range(1,5):
  for rr in itertools.combinations(range(N),k):
   for cc in itertools.combinations(range(N),k):arbitrary.append(det([[A[i][j] for j in cc] for i in rr]))
checks={"planar_network_source_passed":network["status"]=="passed","all_initial_minors_positive":all(x>0 for x in initial),"initial_minor_count_correct":len(initial)==4*N*(N+1),"bounded_arbitrary_minors_positive":all(x>0 for x in arbitrary),"deliberate_row_reversal_negative":det([[entry(i,j,0) for j in range(2)] for i in (1,0)])<0}
result={"schema":"marici.strominger.rh_quarter_total_positivity_fekete_lift.v1","status":"passed" if all(checks.values()) else "failed","verdict":"All-size solid-minor positivity includes both families of positive initial minors. The initial-minor/Neville criterion therefore promotes every finite quarter source matrix to strict total positivity. Exact size-8 checks verify both initial families and bounded arbitrary minors.","criterion":"positive minors with consecutive rows and first columns, together with first rows and consecutive columns, imply strict total positivity via complete Neville elimination","initial_minor_count":len(initial),"bounded_arbitrary_minor_count":len(arbitrary),"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
(base/"results"/"rh_quarter_total_positivity_fekete_lift.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
