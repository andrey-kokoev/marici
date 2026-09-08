#!/usr/bin/env python3
"""Modular n=9 falsification test for the local-relation rank conjecture."""
import importlib.util
import json
from functools import lru_cache
from math import comb
from pathlib import Path

helper_path=Path(__file__).with_name("check_generic_polygon_face_product.py")
spec=importlib.util.spec_from_file_location("polygon_faces",helper_path)
poly=importlib.util.module_from_spec(spec)
spec.loader.exec_module(poly)

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

def modular_rank(rows,p):
    basis={}
    for source in rows:
        row={column:value%p for column,value in source.items() if value%p}
        while row:
            pivot=min(row); value=row[pivot]
            if pivot not in basis:
                inverse=pow(value,-1,p)
                row={c:(v*inverse)%p for c,v in row.items() if (v*inverse)%p}
                basis[pivot]=row; break
            factor=value
            known=basis[pivot]
            for c,v in known.items():
                updated=(row.get(c,0)-factor*v)%p
                if updated:row[c]=updated
                elif c in row:del row[c]
    return len(basis)

n=9
channels=tuple(sorted(poly.diagonals(n)))
ts=triangulations(tuple(range(n))); index={t:i for i,t in enumerate(ts)}
assert len(ts)==429
rows=[]; cut_types={}
for cut in channels:
    regions=poly.split_regions(n,frozenset([cut]))
    left,right=[triangulations(tuple(region)) for region in regions]
    key=f"{len(left)}x{len(right)}"; cut_types[key]=cut_types.get(key,0)+1
    for i in range(1,len(left)):
        for j in range(1,len(right)):
            ids=[index[frozenset(set(left[i])|set(right[j])|{cut})],index[frozenset(set(left[0])|set(right[0])|{cut})],index[frozenset(set(left[i])|set(right[0])|{cut})],index[frozenset(set(left[0])|set(right[j])|{cut})]]
            row={}
            for position,sign in zip(ids,[1,1,-1,-1]):row[position]=row.get(position,0)+sign
            rows.append({c:v for c,v in row.items() if v})
predicted_solution_dimension=1+comb(n-1,3)
predicted_rank=len(ts)-predicted_solution_dimension
ranks={str(p):modular_rank(rows,p) for p in [2,3,5,1000003]}
assert all(rank==predicted_rank for rank in ranks.values())
global_rank=len(ts)-len(channels)
result={
 "schema":"marici.nine-point-local-relation-conjecture.v1","status":"passed",
 "strength":"multi-prime modular rank at n=9; supports but does not prove the all-n conjecture",
 "triangulations":len(ts),"channels":len(channels),"generated_local_relations":len(rows),"cut_types":cut_types,
 "conjectured_local_solution_dimension":"1+binomial(n-1,3)","predicted_local_rank":predicted_rank,
 "modular_ranks":ranks,"predicted_nonlocal_quotient":predicted_solution_dimension-len(channels),"global_relation_rank":global_rank,
 "residual":"no rank discrepancy at primes 2,3,5,1000003; missing object is an explicit all-n basis or dimension proof",
 "boundary":"equal modular ranks are finite evidence and do not establish rational rank or the generic formula without an upper-bound construction",
}
out=Path("research/nima/results/nine_point_local_relation_conjecture.json")
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(result,sort_keys=True))
