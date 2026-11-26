"""Core-first capacity audit, k=6. Sources: all stored max (3,5) cores, their one-deletions, and size-12 cores observed at roots in the seven max (3,6) graphs. Not an enumeration of all order-12 cores."""
import json,itertools,collections,networkx as nx
from pysat.solvers import Solver
from scipy.optimize import linprog
from ramsey_retention_slice import D,CAT,decode,check
cases=[]
def add(a,idx,source):
 idx=list(idx);g=[sum(1<<j for j,v in enumerate(idx) if a[u]>>v&1) for u in idx];n=len(g);assert check(g,2**n-1,3,5);G=nx.Graph();G.add_nodes_from(range(n));G.add_edges_from((i,j) for i,j in itertools.combinations(G,2) if g[i]>>j&1)
 for H,_,sources in cases:
  if nx.is_isomorphic(G,H):sources[source]+=1;return
 cases.append((G,g,collections.Counter([source])))
for line in (CAT/'r35_13.g6').read_text().splitlines():
 a=decode(line);add(a,range(13),'maximum');
 for i in range(13):add(a,[j for j in range(13) if i!=j],'deletion')
for line in (CAT/'r36_17.g6').read_text().splitlines():
 a=decode(line)
 for i,v in enumerate(a):
  if v.bit_count()==4:add(a,[j for j in range(17) if i!=j and not(v>>j&1)],'observed')
out=[]
for G,g,src in cases:
 n=len(g);d=16-n;E=list(G.edges());supports=[t for t in range(1<<n) if not any(t>>i&t>>j&1 for i,j in E)];ms=[t for t in supports if not any(t!=u and t&u==t for u in supports)];marg=[];cs=[];var=lambda j,i:1+j*n+i
 for j in range(d):cs.extend([[-var(j,i),-var(j,h)] for i,h in E]);
 for q in range(1,5):
  cl=[t for t in supports if t.bit_count()==q];rq=max(0,d+q-5);H=max(sum(bool(t&u) for t in cl) for u in ms);marg.append(dict(q=q,N=len(cl),H=H,r=rq,margin=d*H-rq*len(cl)))
  for js in itertools.combinations(range(d),6-q):
   for t in cl:cs.append([var(j,i) for j in js for i in range(n) if t>>i&1])
 with Solver(name='g4',bootstrap_with=cs) as s:
  ok=s.solve();w=None
  if ok:
   pos=set(s.get_model());w=[sum(1<<i for i in range(n) if var(j,i) in pos) for j in range(d)];b=g.copy()+[0]*(d+1)
   for j,t in enumerate(w):
    b[n+j]=t|(1<<16);b[16]|=1<<(n+j)
    for i in range(n):
     if t>>i&1:b[i]|=1<<(n+j)
   assert check(b,2**17-1,3,6)
 dem=[t for t in supports if d+t.bit_count()>5];lp=linprog([1]*len(ms),A_ub=[[-int(bool(t&u)) for u in ms] for t in dem],b_ub=[5-d-t.bit_count() for t in dem],method='highs');assert lp.success
 out.append(dict(core=g,sources=src,degree=d,sat=ok,witness=w,coverage=marg,fractional_mass=lp.fun));print(src,n,ok,[m['margin'] for m in marg if m['r']],lp.fun)
(D.parent/'ramsey_core_capacity_36.json').write_text(json.dumps(out,indent=1)+'\n')
