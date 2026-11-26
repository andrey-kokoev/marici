"""Greedy one-vertex SAT extension at (5,5), requiring each new vertex to violate both individual 24-vertex sides. Lift to the saved matrix without recoloring any edge."""
from itertools import combinations
from pysat.solvers import Solver
from ramsey_retention_slice import D,check
import json
P=D.parent;old=json.loads((P/'ramsey_nested_44_to_1010.json').read_text());h=old['red_masks'];a=[x&((1<<31)-1) for x in h[:31]];side=[list(range(24)),list(range(17))+list(range(24,31))];status=None
pair=set(json.loads((P/'ramsey_joint_gain_pair.json').read_text())['positive_edge_variables']);
for j in range(2):
 v=sum(1<<i for i in range(31) if 1+31*j+i in pair)+(1<<31 if j and 63 in pair else 0);a.append(v)
 for i in range(31+j):
  if v>>i&1:a[i]|=1<<(31+j)
while len(a)<42:
 n=len(a);clauses=[];aux=n
 for color in (1,0):
  g=a if color else [~v for v in a];sign=1 if color else -1
  def clique(t):return all(g[i]>>j&1 for i,j in combinations(t,2))
  for t in combinations(range(n),4):
   if clique(t):clauses.append([-sign*(i+1) for i in t])
  opts=[]
  for t in combinations(side[1-color],3):
   if clique(t):
    aux+=1;opts.append(aux);clauses.extend([[-aux,sign*(i+1)] for i in t])
  clauses.append(opts)
 with Solver(name='g4',bootstrap_with=clauses) as s:
  status=s.solve();
  if not status:break
  pos=set(s.get_model());v=sum(1<<i for i in range(n) if i+1 in pos);a.append(v)
  for i in range(n):
   if v>>i&1:a[i]|=1<<n
assert check(a,(1<<len(a))-1,5,5);mask=lambda seq:sum(1<<i for i in seq);m=len(a)-31;extra=list(range(61,61+m));red_ports=sum(old['l_groups'][2:],[]);b=h.copy()+[0]*m
for j,v in enumerate(extra):
 for i in list(range(31))+red_ports+extra[:j]:
  if i in red_ports or a[31+j]>>(i if i<31 else i-30)&1:b[v]|=1<<i;b[i]|=1<<v
 for k,p in enumerate(side):assert not check(b,mask(p+[v]),4+k,5-k)
M=[]
for l in range(4,11):
 row=[]
 for k in range(4,11):
  p=mask(list(range(17))+sum(old['k_groups'][:k-3],[])+sum(old['l_groups'][:l-3],[])+(extra if min(l,k)>=5 else []));assert check(b,p,l,k);row.append(p.bit_count())
 M.append(row)
print(m,status,M);(P/'ramsey_joint_gain.json').write_text(json.dumps(dict(extra=extra,orders=M,red_masks=b,final_step_sat=status))+'\n')
