#!/usr/bin/env python3
"""Exact cochain-kernel verification for the triangle-incidence rank theorem."""
import itertools
import json
from functools import lru_cache
from math import comb
from pathlib import Path
from sympy import Matrix

@lru_cache(None)
def triangulations(vertices):
    if len(vertices)<=3:return (frozenset(),)
    out=set();last=len(vertices)-1
    for k in range(1,last):
        added=set()
        if k>1:added.add((vertices[0],vertices[k]))
        if k<last-1:added.add((vertices[k],vertices[last]))
        for left in triangulations(vertices[:k+1]):
            for right in triangulations(vertices[k:]):out.add(frozenset(set(left)|set(right)|added))
    return tuple(sorted(out,key=repr))

def boundary_edges(n):return {tuple(sorted((i,(i+1)%n))) for i in range(n)}

stages=[]
for n in range(4,9):
    edges=list(itertools.combinations(range(n),2));edge_index={e:i for i,e in enumerate(edges)}
    triangles=list(itertools.combinations(range(n),3));triangle_index={t:i for i,t in enumerate(triangles)}
    boundary=boundary_edges(n);ts=triangulations(tuple(range(n)))
    B=[]
    for triangulation in ts:
        graph=set(triangulation)|boundary;row=[]
        for triangle in triangles:
            pairs=list(itertools.combinations(triangle,2))
            row.append(int(all(pair in graph for pair in pairs)))
        B.append(row)
    B=Matrix(B)
    delta=Matrix.zeros(len(triangles),len(edges))
    for r,(i,j,k) in enumerate(triangles):
        delta[r,edge_index[(j,k)]]=1;delta[r,edge_index[(i,k)]]=-1;delta[r,edge_index[(i,j)]]=1
    boundary_row=Matrix([[0]*len(edges)])
    for i in range(n-1):boundary_row[0,edge_index[(i,i+1)]]=1
    boundary_row[0,edge_index[(0,n-1)]]=-1
    U=Matrix.hstack(*boundary_row.nullspace())
    H=delta*U
    assert B*H==Matrix.zeros(len(ts),U.cols)
    facet_count=n*(n-3)//2
    expected_rank=1+comb(n-1,3)
    assert H.rank()==facet_count
    assert B.rank()==expected_rank
    assert len(triangles)-B.rank()==facet_count
    stages.append({"n":n,"triangulations":len(ts),"triangles":len(triangles),"triangle_incidence_rank":B.rank(),"kernel_dimension":len(triangles)-B.rank(),"coboundary_boundary_zero_rank":H.rank()})

result={
 "schema":"marici.triangle-incidence-rank-theorem.v1","status":"passed",
 "strength":"generic simplicial-cochain proof plus exact matrix checks n=4..8",
 "theorem":"triangle-incidence rank is 1+binomial(n-1,3), with kernel the coboundaries of edge cochains having zero polygon-boundary integral",
 "proof_edges":["zero evaluation on all triangulations implies every four-vertex flip cocycle equation","the full simplex has exact positive-degree cochains, so the triangle cochain is an edge coboundary","evaluation on a triangulated polygon is the boundary integral","edge coboundaries modulo vertex coboundaries and one boundary constraint have dimension n(n-3)/2"],
 "stages":stages,
 "residual":"this proves the triangle-additive image dimension, not yet that every locally factorizing triangulation function lies in that image",
 "boundary":"the cochain theorem is combinatorial and supplies no source coefficient values or provenance",
}
out=Path("research/nima/results/triangle_incidence_rank_theorem.json")
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(result,sort_keys=True))
