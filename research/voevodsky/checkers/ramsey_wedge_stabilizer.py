"""Graph automorphisms: mark wedge roles pointwise, or mark only the resulting clique setwise. Test for a fixed-point-free involution on its eight vertices."""
from collections import Counter
import json,itertools,igraph as ig
from ramsey_retention_slice import D,decode
P=D.parent;g=decode(next(r['graph6'] for r in json.loads(D.read_text()) if (r['l'],r['k'])==(3,9)));n=len(g);V=set(range(n));adj={i:[j for j in V if g[i]>>j&1] for i in V}
def aut(parts):
 G=ig.Graph(n,[(i,j) for i in V for j in adj[i] if i<j]);color=[next((k for k,p in enumerate(parts) if i in p),0) for i in range(n)];return G.automorphism_group(color=color),G.count_automorphisms(color=color)
def orbit(t,gens):
 seen={t};stack=[t]
 while stack:
  cur=stack.pop()
  for m in gens:
   v=tuple(m[i] for i in cur)
   if v not in seen:seen.add(v);stack.append(v)
 return seen
A,order=aut([]);W={}
for x,a,b in itertools.permutations(range(n),3):
 if g[x]>>a&1 and not g[x]>>b&1:
  C=[y for y in V-{x,a,b} if g[b]>>y&1 and not g[a]>>y&1];
  if len(C)==7:W[x,a,b]=C
seen=set();rows=[];hist=Counter();revhist=Counter()
for t,C in W.items():
 if t in seen:continue
 orb=orbit(t,A);seen|=orb;x,a,b=t;S,sz=aut([{x},{a},{b},V-set(t)]);assert sz*len(orb)==order;partition={tuple(sorted(v[0] for v in orbit((y,),S))) for y in C};pat=tuple(sorted(map(len,partition)));hist[pat]+=len(orb);Q=set(C)|{a};B,bs=aut([Q,V-Q]);seq=tuple(sorted(Q));actions=orbit(seq,B);rev=sum(all(f!=v and p[seq.index(f)]==v for f,v in zip(p,seq)) for p in actions);revhist[bool(rev)]+=len(orb);rows.append(dict(wedge=t,orbit=len(orb),stabilizer=sz,completion_orbits=sorted(partition),clique_stabilizer=bs,clique_reversals=rev))
assert seen==set(W);print(order,len(rows),hist,revhist,Counter((r['orbit'],r['stabilizer'],r['clique_stabilizer'],r['clique_reversals']) for r in rows));(P/'ramsey_wedge_stabilizer.json').write_text(json.dumps(dict(group_order=order,rows=rows),indent=1)+'\n')
