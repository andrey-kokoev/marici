#!/usr/bin/env python3
"""Exact local-versus-global coefficient relation rank at eight points."""
import importlib.util
import json
from functools import lru_cache
from pathlib import Path
from sympy import Matrix

helper_path=Path(__file__).with_name("check_generic_polygon_face_product.py")
spec=importlib.util.spec_from_file_location("polygon_faces",helper_path)
poly=importlib.util.module_from_spec(spec)
spec.loader.exec_module(poly)

@lru_cache(None)
def triangulations(vertices):
    if len(vertices)<=3: return (frozenset(),)
    out=set(); last=len(vertices)-1
    for k in range(1,last):
        added=set()
        if k>1: added.add(tuple(sorted((vertices[0],vertices[k]))))
        if k<last-1: added.add(tuple(sorted((vertices[k],vertices[last]))))
        for left in triangulations(vertices[:k+1]):
            for right in triangulations(vertices[k:]):
                out.add(frozenset(set(left)|set(right)|added))
    return tuple(sorted(out,key=repr))

n=8
channels=tuple(sorted(poly.diagonals(n)))
ts=triangulations(tuple(range(n)))
assert len(ts)==132 and all(len(t)==5 for t in ts)
index={t:i for i,t in enumerate(ts)}
A=Matrix([[int(c in t) for c in channels] for t in ts])
assert A.rank()==20
local=[]; cut_records=[]
for cut in channels:
    regions=poly.split_regions(n,frozenset([cut]))
    left,right=[triangulations(tuple(region)) for region in regions]
    before=len(local)
    for i in range(1,len(left)):
        for j in range(1,len(right)):
            ids=[index[frozenset(set(left[i])|set(right[j])|{cut})],index[frozenset(set(left[0])|set(right[0])|{cut})],index[frozenset(set(left[i])|set(right[0])|{cut})],index[frozenset(set(left[0])|set(right[j])|{cut})]]
            row=[0]*len(ts)
            row[ids[0]]+=1; row[ids[1]]+=1; row[ids[2]]-=1; row[ids[3]]-=1
            local.append(row)
    cut_records.append({"cut":list(cut),"regional_triangulations":[len(left),len(right)],"generated_relations":len(local)-before})
R=Matrix(local)
assert R*A==Matrix.zeros(R.rows,len(channels))
local_rank=R.rank(); global_rank=len(ts)-len(channels)
assert global_rank==112 and local_rank<=global_rank
result={
 "schema":"marici.eight-point-local-global-weights.v1","status":"passed",
 "strength":"exact rational rank comparison at n=8 only",
 "channels":len(channels),"triangulations":len(ts),"generated_local_relations":len(local),
 "local_relation_rank":local_rank,"global_relation_rank":global_rank,
 "nonlocal_quotient_dimension":global_rank-local_rank,"cuts":cut_records,
 "boundary":"one additional finite stage does not establish an all-n local-quotient formula or source provenance",
}
out=Path("research/nima/results/eight_point_local_global_weights.json")
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(result,sort_keys=True))
