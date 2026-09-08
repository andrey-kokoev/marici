#!/usr/bin/env python3
"""Exact weighted factorization on every six-point polygon facet."""
import importlib.util
import itertools
import json
from pathlib import Path

helper_path=Path(__file__).with_name("check_generic_polygon_face_product.py")
spec=importlib.util.spec_from_file_location("polygon_faces",helper_path)
poly=importlib.util.module_from_spec(spec)
spec.loader.exec_module(poly)

n=6
channels=tuple(sorted(poly.diagonals(n)))
scales={channel:prime for channel,prime in zip(channels,[2,3,5,7,11,13,17,19,23])}
triangulations=sorted((frozenset(t) for t in poly.dissections_on(channels) if len(t)==n-3),key=repr)
def weight(t):
    value=1
    for c in t: value*=scales[c]
    return value
weights={t:weight(t) for t in triangulations}

def regional_triangulations(region):
    ds=poly.region_diagonals(region)
    return sorted((frozenset(t) for t in poly.dissections_on(ds) if len(t)==len(region)-3),key=repr)

records=[]
rank_one_checks=0
for cut in channels:
    regions=poly.split_regions(n,frozenset([cut]))
    assert len(regions)==2
    left,right=[regional_triangulations(region) for region in regions]
    matrix=[]
    for lt in left:
        row=[]
        for rt in right:
            global_t=frozenset(set(lt)|set(rt)|{cut})
            assert global_t in weights
            expected=scales[cut]*weight(lt)*weight(rt)
            assert weights[global_t]==expected
            row.append(weights[global_t])
        matrix.append(row)
    checks=0
    for i,j in itertools.combinations(range(len(left)),2):
        for k,l in itertools.combinations(range(len(right)),2):
            assert matrix[i][k]*matrix[j][l]==matrix[i][l]*matrix[j][k]
            checks+=1
    rank_one_checks+=checks
    records.append({"cut":list(cut),"regional_triangulations":[len(left),len(right)],"coefficient_pairs":len(left)*len(right),"rank_one_cross_ratios":checks})

# Deform one triangulation participating in a 2x2 long-diagonal facet matrix.
long_record=next(record for record in records if record["regional_triangulations"]==[2,2])
cut=tuple(long_record["cut"])
regions=poly.split_regions(n,frozenset([cut]))
left,right=[regional_triangulations(region) for region in regions]
deformed=dict(weights)
pivot=frozenset(set(left[0])|set(right[0])|{cut})
deformed[pivot]*=2
matrix=[[deformed[frozenset(set(lt)|set(rt)|{cut})] for rt in right] for lt in left]
residual=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
assert residual!=0

result={
    "schema":"marici.six-point-weighted-facet-factorization.v1",
    "status":"passed",
    "strength":"exact all-facet six-point test for one algebraically independent factorable scale assignment",
    "facets_checked":len(records),
    "records":records,
    "rank_one_cross_ratios_checked":rank_one_checks,
    "factorization":"w_(TL union {c} union TR)=lambda_c w_TL w_TR",
    "deliberate_failure":{"cut":list(cut),"deformed_triangulation":[list(c) for c in sorted(pivot)],"multiplier":2,"rank_one_residual":residual},
    "boundary":"rank-one regional coefficients test weighted gluing; passing one assignment does not supply source coefficients or embedding provenance",
}
out=Path("research/nima/results/six_point_weighted_facet_factorization.json")
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(result,sort_keys=True))
