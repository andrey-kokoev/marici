#!/usr/bin/env python3
"""Test extension of six physical positive-root weights to A3 mutation transport."""
from itertools import combinations
from pathlib import Path
import json
import sympy as sp
ROOT=Path(__file__).resolve().parents[3]
N=6
boundary={tuple(sorted((i,(i+1)%N))) for i in range(N)}
diags=[(i,j) for i in range(N) for j in range(i+1,N) if (i,j) not in boundary]
def cross(a,b):
 x,y=a;u,v=b;return x<u<y<v or u<x<v<y
clusters=sorted(tuple(sorted(c)) for c in combinations(diags,3) if all(not cross(a,b) for a,b in combinations(c,2)))
edges=sorted((i,j) for i,a in enumerate(clusters) for j,b in enumerate(clusters) if i<j and len(set(a)^set(b))==2)
# One-based positive-root map [i,j] -> (i,j+2), translated to zero-based polygon vertices.
pos={(i-1,j+1) for i in range(1,4) for j in range(i,4)}
neg=set(diags)-pos
x={d:sp.Symbol('x_'+str(d[0]+1)+str(d[1]+1), nonzero=True) for d in diags}
W=[sp.prod(x[d] for d in c) for c in clusters]
ratios={e:sp.cancel(W[e[1]]/W[e[0]]) for e in edges}
known=[e for e,r in ratios.items() if not any(r.has(x[d]) for d in neg)]
unknown=[e for e in edges if e not in known]
# Faces are fixed-diagonal cycles; product of oriented edge ratios telescopes.
face_products=[]
for d in diags:
 vs=sorted(i for i,c in enumerate(clusters) if d in c)
 adj={i:sorted((b if a==i else a) for a,b in edges if i in (a,b) and (b if a==i else a) in vs) for i in vs}
 start=min(vs);prev=None;cur=start;cyc=[start];nxt=min(adj[start])
 while nxt!=start:
  cyc.append(nxt);prev,cur=cur,nxt;nxt=next(z for z in adj[cur] if z!=prev)
 p=sp.Integer(1)
 for a,b in zip(cyc,cyc[1:]+cyc[:1]):p*=W[b]/W[a]
 face_products.append(sp.cancel(p))
checks={'six_positive_roots':len(pos)==6,'three_missing_negative_simple_roots':len(neg)==3,'twenty_one_edges':len(edges)==21,'all_face_holonomies_one':all(p==1 for p in face_products),'physical_weights_do_not_determine_all_edges':len(unknown)>0,'completion_requires_exactly_missing_coordinates':set().union(*(set(diags) for _ in [0]))-pos==neg}
out={'schema':'marici.nima.a3-physical-weight-transport.v1','positive_root_diagonals':[list(d) for d in sorted(pos)],'missing_negative_simple_diagonals':[list(d) for d in sorted(neg)],'mutation_edges_total':len(edges),'edges_determined_by_positive_root_weights':len(known),'edges_requiring_missing_coordinates':len(unknown),'face_holonomies':[str(p) for p in face_products],'checks':checks,'passed':all(checks.values()),'theorem':'Any nonzero assignment to all nine almost-positive-root coordinates defines cluster-vertex product weights and exact mutation ratios with unit square/pentagon holonomy. The six physical positive-root weights alone leave mutation edges involving three negative-simple coordinates undetermined.','claim_boundary':'This proves a coefficient-completion criterion, not that cluster-product vertex weights equal canonical-form weights.'}
p=ROOT/'research/nima/results/a3-physical-weight-transport.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
