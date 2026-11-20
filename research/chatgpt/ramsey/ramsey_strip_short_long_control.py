"""Test shortest/longest active completion with the same boundary and invariant core. Do not assume a length-changing cage automorphism."""
from collections import Counter
from ramsey_strip_connected_rotation_core import winners
from ramsey_strip_matching_restart import turn
from ramsey_strip_short_output_isomorphism import graph,iso,G
single=[]
for m in winners:
 d=m^turn(m);adj={}
 for x,y in d:adj.setdefault(x,set()).add(y);adj.setdefault(y,set()).add(x)
 reached=set();stack=[0]
 while stack:
    x=stack.pop()
    if x in reached:continue
    reached.add(x);stack.extend(adj[x]-reached)
 if len(reached)==len(adj):single.append(m)
print('single-cycle completion counts by length',dict(sorted(Counter(len(m^turn(m)) for m in single).items())));long,=[m for m in single if len(m^turn(m))==26];print('longest shared residue',sorted(long&turn(long)))
B=graph(long);print('longest graph isomorphic to alternative-short class',iso(G[0],B,{}) is not None,'to accumulated-short class',iso(G[4],B,{}) is not None)
for m in single:assert len(m^turn(m))+2*len(m&turn(m))==30
