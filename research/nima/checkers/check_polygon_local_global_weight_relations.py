#!/usr/bin/env python3
"""Exact ranks of local facet-gluing relations versus global scale relations."""
import importlib.util
import json
from pathlib import Path
from sympy import Matrix

helper_path=Path(__file__).with_name("check_generic_polygon_face_product.py")
spec=importlib.util.spec_from_file_location("polygon_faces",helper_path)
poly=importlib.util.module_from_spec(spec)
spec.loader.exec_module(poly)

def regional(region):
    ds=poly.region_diagonals(region)
    return sorted((frozenset(t) for t in poly.dissections_on(ds) if len(t)==len(region)-3),key=repr)

stages=[]
for n in range(5,8):
    channels=tuple(sorted(poly.diagonals(n)))
    triangulations=sorted((frozenset(t) for t in poly.dissections_on(channels) if len(t)==n-3),key=repr)
    index={t:i for i,t in enumerate(triangulations)}
    A=Matrix([[int(c in t) for c in channels] for t in triangulations])
    assert A.rank()==len(channels)
    local_rows=[]
    cut_records=[]
    for cut in channels:
        regions=poly.split_regions(n,frozenset([cut]))
        left,right=[regional(region) for region in regions]
        before=len(local_rows)
        for i in range(1,len(left)):
            for j in range(1,len(right)):
                cells=[
                    index[frozenset(set(left[i])|set(right[j])|{cut})],
                    index[frozenset(set(left[0])|set(right[0])|{cut})],
                    index[frozenset(set(left[i])|set(right[0])|{cut})],
                    index[frozenset(set(left[0])|set(right[j])|{cut})],
                ]
                row=[0]*len(triangulations)
                row[cells[0]]+=1; row[cells[1]]+=1; row[cells[2]]-=1; row[cells[3]]-=1
                local_rows.append(row)
        cut_records.append({"cut":list(cut),"regional_triangulations":[len(left),len(right)],"generated_relations":len(local_rows)-before})
    R=Matrix(local_rows) if local_rows else Matrix.zeros(0,len(triangulations))
    assert R*A==Matrix.zeros(R.rows,len(channels))
    local_rank=R.rank()
    global_rank=len(triangulations)-len(channels)
    stages.append({
        "n":n,"channels":len(channels),"triangulations":len(triangulations),
        "generated_local_relations":len(local_rows),"local_relation_rank":local_rank,
        "global_relation_rank":global_rank,"nonlocal_quotient_dimension":global_rank-local_rank,
        "cuts":cut_records,
    })
assert stages[1]["local_relation_rank"]==3 and stages[1]["nonlocal_quotient_dimension"]==2

result={
    "schema":"marici.polygon-local-global-weight-relations.v1",
    "status":"passed",
    "strength":"exact rational relation-space ranks for n=5..7; no all-n formula inferred",
    "stages":stages,
    "criterion":"local rows are all anchored 2x2 logarithmic minors on each facet product; global rows are the full incidence left kernel",
    "boundary":"local residue gluing can miss global coefficient compatibility; finite ranks do not establish a generic quotient dimension",
}
out=Path("research/nima/results/polygon_local_global_weight_relations.json")
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(result,sort_keys=True))
