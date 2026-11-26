"""Enumerate all *deletable* order-20 edge-46 types from the complete stored 45-layer. Independently reconstruct all minimum-degree-two types over max 17-cores. LP on that complete low-degree stratum, not on the entire augmented layer."""
import itertools,json,gzip,collections
import igraph as ig
import numpy as np
from scipy.optimize import linprog
from ramsey_retention_slice import D,CAT,decode,check
P=D.parent;n=20;E=[(i,j) for j in range(n) for i in range(j)];
def unpack(m):
 a=[0]*20
 for k,(i,j) in enumerate(E):
  if m>>k&1:a[i]|=1<<j;a[j]|=1<<i
 return a
def key(a):
 G=ig.Graph(20,[(i,j) for i,j in E if a[i]>>j&1]);return sum(1<<(max(i,j)*(max(i,j)-1)//2+min(i,j)) for i,j in G.permute_vertices(G.canonical_permutation()).get_edgelist())
def ind(a):
 I=[0]
 for i,v in enumerate(a):I.extend([s|1<<i for s in I if not s&v])
 return I
parents={key(unpack(int(z['core'],16))) for z in json.loads((P/'ramsey_38_window_new_types.json').read_text())}
for f in ('ramsey_38_degree3_inventory_32_36.json','ramsey_38_degree4_inventory.json'):parents.update(key(a) for a in json.loads((P/f).read_text())['resistant'])
assert len(parents)==479;children=set();moves=0
for m in parents:
 a=unpack(m)
 for i,j in E:
  if a[i]>>j&1 or a[i]&a[j]:continue
  a[i]^=1<<j;a[j]^=1<<i;children.add(key(a));moves+=1;a[i]^=1<<j;a[j]^=1<<i
print('augmented',moves,len(children),flush=True);low=set()
for s in (CAT/'r36_17.g6').read_text().splitlines():
 a=decode(s);I=ind(a);five=[q for q in I if q.bit_count()==5];cost=44-sum(v.bit_count() for v in a)//2
 for t,u in itertools.combinations_with_replacement([q for q in I if 0<q.bit_count()<cost],2):
  if t.bit_count()+u.bit_count()!=cost or any(not q&(t|u) for q in five):continue
  b=a.copy()+[t|1<<19,u|1<<19,3<<17]
  for j,v in enumerate((t,u),17):
   for i in range(17):
    if v>>i&1:b[i]|=1<<j
  if min(v.bit_count() for v in b)!=2:continue
  assert check(b,2**20-1,3,7);low.add(key(b))
print('min2',len(low),'not in augmentation',len(low-children),flush=True);rec=[]
for m in sorted(low):
 I=ind(unpack(m));S=[s for s in I if not any(s!=t and s&t==s for t in I)];Q=[q for q in I if q.bit_count()>=5];A=np.array([[int(bool(s&q)) for s in S] for q in Q]);d=np.array([q.bit_count() for q in Q]);lp=linprog(np.ones(len(S)),A_ub=-A,b_ub=-d);assert lp.success;y=np.rint(-lp.ineqlin.marginals*10**7).astype('int64');assert min(y)>=0;den=int(max(A.T@y));num=int(d@y);rec.append(dict(core=hex(m),deletable=m in children,excluded=num>7*den,den=den,num=num,weights={q:int(w) for q,w in zip(Q,y) if w}));
print('excluded',sum(z['excluded'] for z in rec));(P/'ramsey_38_layer46.json').write_text(json.dumps(dict(parents=len(parents),moves=moves,deletable_count=len(children),low=rec))+'\n');
with gzip.open(P/'ramsey_38_layer46_deletable.json.gz','wt') as f:json.dump(sorted(map(hex,children)),f)
