"""Explain order five from the union of the two row-swap matchings on ground labels, and control that fixing 23 alone does not force it."""
from itertools import permutations,combinations
from collections import Counter
from ramsey_strip_fivefold_phase_anchor import transport_records
X=list(combinations(range(1,5),2));a=(1,0,2,3,5,4);comp=lambda p,q:tuple(p[x] for x in q);identity=tuple(range(6))
def conjugate(p):
 inv=tuple(p.index(x) for x in range(6));return comp(p,comp(a,inv))
def order(p):
 q=p;n=1
 while q!=identity:q=comp(p,q);n+=1
 return n
edges=lambda p:{tuple(sorted((i,j))) for i,j in enumerate(p) if i<j}
for n,o,p in transport_records:
 if p[3]!=3:continue
 b=conjugate(p);A,B=edges(a),edges(b);assert not A&B
 fixedA={i for i in range(6) if a[i]==i};fixedB={i for i in range(6) if b[i]==i};assert fixedA&fixedB=={3}
 adj={i:set() for i in range(6) if i!=3}
 for i,j in A|B:adj[i].add(j);adj[j].add(i)
 start=min(i for i in adj if len(adj[i])==1);path=[start]
 while len(path)<5:
  nxt,=adj[path[-1]]-set(path);path.append(nxt)
 assert order(comp(a,b))==5;print('source',n,o,'alternating path',[X[i] for i in path])
control=Counter(order(comp(a,conjugate(p))) for p in permutations(range(6)) if p[3]==3);print('all permutations fixing 23, product orders',dict(sorted(control.items())))
