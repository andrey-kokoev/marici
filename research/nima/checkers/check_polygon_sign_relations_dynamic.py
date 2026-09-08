#!/usr/bin/env python3
"""Dynamic triangulation generation and F2 sign-rank checks through n=10."""
import json
from functools import lru_cache
from math import comb
from pathlib import Path

@lru_cache(None)
def triangulations(vertices):
    if len(vertices)<=3:
        return (frozenset(),)
    out=set()
    last=len(vertices)-1
    for k in range(1,last):
        left=vertices[:k+1]
        right=vertices[k:]
        left_triangulations=triangulations(left)
        right_triangulations=triangulations(right)
        added=set()
        if k>1: added.add(tuple(sorted((vertices[0],vertices[k]))))
        if k<last-1: added.add(tuple(sorted((vertices[k],vertices[last]))))
        for a in left_triangulations:
            for b in right_triangulations:
                out.add(frozenset(set(a)|set(b)|added))
    return tuple(sorted(out,key=repr))

def rank_mod2(bit_rows,width):
    rows=list(bit_rows); rank=0
    for column in range(width):
        pivot=next((r for r in range(rank,len(rows)) if (rows[r]>>column)&1),None)
        if pivot is None: continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        for r in range(len(rows)):
            if r!=rank and ((rows[r]>>column)&1): rows[r]^=rows[rank]
        rank+=1
    return rank

def catalan(k): return comb(2*k,k)//(k+1)

def diagonals(n):
    return tuple((i,j) for i in range(n) for j in range(i+1,n) if j-i>1 and not (i==0 and j==n-1))

stages=[]
for n in range(4,11):
    channels=diagonals(n); index={c:i for i,c in enumerate(channels)}
    ts=triangulations(tuple(range(n)))
    assert len(ts)==catalan(n-2)
    assert all(len(t)==n-3 for t in ts)
    rows=[sum(1<<index[c] for c in t) for t in ts]
    rank=rank_mod2(rows,len(channels))
    expected=len(channels)-(1 if (n-3)%2==0 else 0)
    assert rank==expected
    stages.append({"n":n,"channels":len(channels),"triangulations":len(ts),"f2_rank":rank,"sign_relations":len(ts)-rank})

result={
    "schema":"marici.polygon-sign-relations-dynamic.v1",
    "status":"passed",
    "strength":"exact dynamic triangulation census and F2 ranks n=4..10; generic formula still derives from the Smith theorem",
    "stages":stages,
    "repair":"replaced exhaustive enumeration of all diagonal subsets by Catalan recursion, eliminating the n=9 timeout",
    "boundary":"finite dynamic checks validate implementation but do not replace the all-n lattice proof",
}
out=Path("research/nima/results/polygon_sign_relations_dynamic.json")
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(result,sort_keys=True))
