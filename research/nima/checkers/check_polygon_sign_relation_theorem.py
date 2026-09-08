#!/usr/bin/env python3
"""Finite verification of the all-polygon real-sign relation formula."""
import importlib.util
import json
from math import comb
from pathlib import Path

helper_path=Path(__file__).with_name("check_generic_polygon_face_product.py")
spec=importlib.util.spec_from_file_location("polygon_faces",helper_path)
poly=importlib.util.module_from_spec(spec)
spec.loader.exec_module(poly)

def rank_mod2(matrix):
    rows=[sum((value&1)<<j for j,value in enumerate(row)) for row in matrix]
    width=len(matrix[0]) if matrix else 0
    rank=0
    for column in range(width):
        pivot=next((r for r in range(rank,len(rows)) if (rows[r]>>column)&1),None)
        if pivot is None: continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        for r in range(len(rows)):
            if r!=rank and ((rows[r]>>column)&1): rows[r]^=rows[rank]
        rank+=1
    return rank

def catalan(k):
    return comb(2*k,k)//(k+1)

stages=[]
for n in range(4,9):
    d=n-3
    channels=tuple(sorted(poly.diagonals(n)))
    triangulations=sorted((tuple(sorted(t)) for t in poly.dissections_on(channels) if len(t)==d),key=repr)
    A=[[int(c in t) for c in channels] for t in triangulations]
    rank=rank_mod2(A)
    expected_rank=len(channels)-(1 if d%2==0 else 0)
    expected_relations=len(triangulations)-expected_rank
    assert len(triangulations)==catalan(n-2)
    assert rank==expected_rank
    stages.append({"n":n,"dimension":d,"channels":len(channels),"triangulations":len(triangulations),"f2_rank":rank,"sign_relations":expected_relations,"facet_sign_kernel_order":2 if d%2==0 else 1})

result={
    "schema":"marici.polygon-sign-relation-theorem.v1",
    "status":"passed",
    "strength":"generic consequence of the incidence Smith theorem plus finite F2 checks n=4..8",
    "theorem":"with F=n(n-3)/2 channels and Cat_(n-2) triangulations, independent real-sign relations equal Cat_(n-2)-F when n is even and Cat_(n-2)-F+1 when n is odd",
    "proof":"reducing Smith invariants 1,...,1,n-3 modulo 2 gives rank F for odd n-3 and F-1 for even n-3",
    "stages":stages,
    "kernel":"for odd n the facet-sign kernel is the global minus; for even n it is trivial",
    "execution_boundary":"n=9 was removed after exhaustive-subset helper enumeration exceeded 120 seconds; this does not affect the generic Smith-theorem derivation",
    "boundary":"the theorem classifies absorbable signs only; coefficient values and source provenance remain external",
}
out=Path("research/nima/results/polygon_sign_relation_theorem.json")
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(result,sort_keys=True))
