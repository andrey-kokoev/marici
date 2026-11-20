"""Enumerate three row-invariant flag orbits across the entire cage, with no accumulated-residue restriction. Only afterward classify two-completion results by poles and required opposite-row flags."""
from itertools import combinations
from collections import Counter
from ramsey_strip_minimal_shared_constraints import allms,N,turn,ms
orbits={frozenset({(i,j)})|turn({(i,j)}) for i in N for j in N[i]};valid=[o for o in orbits if len({v for e in o for v in e})==2*len(o)];support={o:{k for k,m in enumerate(allms) if o<=m} for o in valid};pairs={};counts=Counter()
for os in combinations(valid,3):
    hit=set.intersection(*(support[o] for o in os))
    if len(hit)!=2:continue
    a,b=sorted(hit)
    if turn(allms[a])!=allms[b]:continue
    counts['two swapped completions']+=1;pairs.setdefault((a,b),0);pairs[a,b]+=1
selected={}
for (a,b),n in pairs.items():
    A,B=allms[a],allms[b]
    if any({(0,16),(7,29)}<=m for m in (A,B)):
        selected[a,b]=n
print('invariant flag orbits',len(orbits),'compatible orbits',len(valid),'triple certificates',counts,'different swapped pairs',len(pairs),'pairs with literal directed boundary',len(selected))
print('literal pairs: symmetric difference edges, certificates',Counter((len(allms[a]^allms[b]),n) for (a,b),n in selected.items()))
print('target selected',any({allms[a],allms[b]}==set(ms) for a,b in selected))
