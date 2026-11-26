"""Pick first compatible marked pair from stored 13 and 17 graphs. Orbit classification uses automorphisms preserving each marked seed. Replay negative SAT proofs by unit propagation."""
from itertools import combinations,product
import networkx as nx,json
from pysat.solvers import Solver
from ramsey_retention_slice import D,decode,check
P=D.parent;rows=json.loads(D.read_text());g=decode(next(r['graph6'] for r in rows if (r['l'],r['k'])==(3,5)));z=rows[-1];full=decode(z['graph6']);vv=[i for i in range(24) if z['seed17']>>i&1];h=[sum(1<<j for j,v in enumerate(vv) if full[u]>>v&1) for u in vv]
def graph(a):
 G=nx.Graph();G.add_nodes_from(range(len(a)));G.add_edges_from((i,j) for i,j in combinations(G,2) if a[i]>>j&1);return G
G,H=graph(g),graph(h);iso=nx.isomorphism.GraphMatcher
def seeds(G,adj):
 autos=list(iso(G,G).isomorphisms_iter());seen=set();reps=[]
 for s in combinations(G,8):
  if s in seen or not check(adj,sum(1<<i for i in s),3,4):continue
  orbit={tuple(sorted(m[i] for i in s)) for m in autos};seen|=orbit;reps.append((list(s),[m for m in autos if {m[i] for i in s}==set(s)],len(orbit)))
 return reps
def cases():
 for (s,A,f),(t,B,j) in product(seeds(G,g),seeds(H,h)):
  seen=set()
  for m in iso(G.subgraph(s),H.subgraph(t)).isomorphisms_iter():
   key=tuple(m[i] for i in s)
   if key in seen:continue
   orbit={tuple(b[m[a[i]]] for i in s) for a,b in product(A,B)};seen|=orbit;yield s,t,key,f*j*len(orbit)
out=[]
for s,t,key,count in cases():
 L=[i for i in G if i not in s];R=[i for i in H if i not in t];rec=dict(left_seed=s,right_seed=t,match=key,multiplicity=count);out.append(rec)
 for n in [22,24]:
  fixed={}
  for order,slots,adj in [(s+L,list(range(13)),g),(list(key)+R,list(range(8))+list(range(13,22)),h)]:
   for (i,u),(j,v) in combinations(zip(slots,order),2):fixed[i,j]=adj[u]>>v&1
  var={e:i+1 for i,e in enumerate(e for e in combinations(range(n),2) if e not in fixed)};cs=[]
  for k,c in [(4,1),(5,0)]:
   for q in combinations(range(n),k):
    edges=list(combinations(q,2))
    if all(fixed.get(e,c)==c for e in edges):cs.append([(-1 if c else 1)*var[e] for e in edges if e in var])
  with Solver(name='g4',bootstrap_with=cs,with_proof=True) as sl:
   ok=sl.solve();d=dict(sat=ok);rec[n]=d
   if ok:
    pos=set(sl.get_model());adj=[0]*n
    for i,j in combinations(range(n),2):
     if fixed.get((i,j),var.get((i,j)) in pos):adj[i]|=1<<j;adj[j]|=1<<i
    assert check(adj,2**n-1,4,5);d['red_masks']=adj
   else:
    units={c[0] for c in cs if len(c)==1};d['immediate_conflicts']=[list(e) for e,v in var.items() if {v,-v}<=units];proof=sl.get_proof();db=[set(c) for c in cs];empty=False
    for line in proof:
     if line.startswith('d'):continue
     c=list(map(int,line.split()))[:-1];assign=set(-x for x in c)
     while True:
      change=False;bad=False
      for clause in db:
       if clause&assign:continue
       rest=[x for x in clause if -x not in assign]
       if not rest:bad=True;break
       if len(rest)==1:assign.add(rest[0]);change=True
      if bad:break
      assert change,'not RUP'
     db.append(set(c));empty|=not c
    assert empty or [] in cs;d['rup_lines']=len(proof)
  print(n,ok,flush=True)
(P/'ramsey_asymmetric_square_all.json').write_text(json.dumps(dict(matches=sum(x['multiplicity'] for x in out),orbits=out),indent=1)+'\n')
