"""Locate the three candidates relative to the seed's fixed bridge and marked entry block, without scoring by accumulated residues."""
from ramsey_strip_unbiased_three_constraints import selected,allms
from ramsey_strip_matching_restart import r,P,T
mark=(2,4) # ground labels 14,24 in lexicographic tetrahedral-edge indexing
assert mark in T[16-15]
for a,b in selected:
    A,B=allms[a],allms[b];diff=A^B;adj={}
    for i,j in diff:adj.setdefault(i,set()).add(j);adj.setdefault(j,set()).add(i)
    p=[0,16]
    while p[-1]!=29:
        nxt,=adj[p[-1]]-{p[-2]};p.append(nxt)
    assert all(v==r[v] for v in (0,15,9,29));print('half route',p,'fixed interior',[v for v in p[1:-1] if r[v]==v],'shared on fixed bridge',sorted((A&B)&{(0,15),(9,15),(9,29)}),'mark is next pair',P[p[2]]==mark)
