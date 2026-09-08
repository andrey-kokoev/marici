#!/usr/bin/env python3
"""Finite rank tests for triangle-additive locally factorizing functions."""
import itertools
import json
from functools import lru_cache
from math import comb
from pathlib import Path

@lru_cache(None)
def triangulations(vertices):
    if len(vertices)<=3:return (frozenset(),)
    out=set(); last=len(vertices)-1
    for k in range(1,last):
        added=set()
        if k>1:added.add(tuple(sorted((vertices[0],vertices[k]))))
        if k<last-1:added.add(tuple(sorted((vertices[k],vertices[last]))))
        for left in triangulations(vertices[:k+1]):
            for right in triangulations(vertices[k:]):
                out.add(frozenset(set(left)|set(right)|added))
    return tuple(sorted(out,key=repr))

def boundary_edges(n):return {tuple(sorted((i,(i+1)%n))) for i in range(n)}
def modular_rank(rows,width,p):
    basis={}
    for columns in rows:
        row={c:1 for c in columns}
        while row:
            pivot=min(row);value=row[pivot]
            if pivot not in basis:
                inverse=pow(value,-1,p);basis[pivot]={c:(v*inverse)%p for c,v in row.items() if (v*inverse)%p};break
            factor=value
            for c,v in basis[pivot].items():
                updated=(row.get(c,0)-factor*v)%p
                if updated:row[c]=updated
                elif c in row:del row[c]
    return len(basis)

stages=[]
for n in range(5,10):
    ts=triangulations(tuple(range(n)))
    triangles=list(itertools.combinations(range(n),3)); triangle_index={triangle:i for i,triangle in enumerate(triangles)}
    boundary=boundary_edges(n)
    rows=[]
    for triangulation in ts:
        edges=set(triangulation)|boundary
        present=[]
        for triangle in triangles:
            pairs=[tuple(sorted(pair)) for pair in itertools.combinations(triangle,2)]
            if all(pair in edges for pair in pairs):present.append(triangle_index[triangle])
        assert len(present)==n-2
        rows.append(present)
    expected=1+comb(n-1,3)
    ranks={str(p):modular_rank(rows,len(triangles),p) for p in [2,3,5,1000003]}
    assert all(rank==expected for rank in ranks.values())
    stages.append({"n":n,"triangulations":len(ts),"possible_triangles":len(triangles),"triangles_per_triangulation":n-2,"predicted_rank":expected,"modular_ranks":ranks,"triangle_weight_kernel_dimension":len(triangles)-expected})

result={
 "schema":"marici.triangle-additive-local-solutions.v1","status":"passed",
 "strength":"generic inclusion in the local-solution space plus multi-prime finite ranks n=5..9; generic spanning remains unproved",
 "construction":"assign a scalar to every boundary-vertex triple and sum weights of the n-2 triangles in each triangulation",
 "locality_proof":"on a cut, triangles partition between the two regional triangulations, so every mixed 2x2 difference vanishes",
 "conjectured_rank":"1+binomial(n-1,3)","stages":stages,
 "residual":"finite ranks match the full conjectured local-solution dimension, but no all-n rank proof or spanning theorem is supplied",
 "boundary":"triangle additivity provides an explicit candidate model; modular finite agreement does not promote it to generic equality",
}
out=Path("research/nima/results/triangle_additive_local_solutions.json")
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(result,sort_keys=True))
