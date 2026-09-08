#!/usr/bin/env python3
"""Exact comparison of local facet gluing and global scale factorability at six points."""
import importlib.util
import json
from math import gcd
from pathlib import Path
from sympy import Matrix, ilcm

helper_path=Path(__file__).with_name("check_generic_polygon_face_product.py")
spec=importlib.util.spec_from_file_location("polygon_faces",helper_path)
poly=importlib.util.module_from_spec(spec)
spec.loader.exec_module(poly)

n=6
channels=tuple(sorted(poly.diagonals(n)))
triangulations=sorted((frozenset(t) for t in poly.dissections_on(channels) if len(t)==n-3),key=repr)
index={t:i for i,t in enumerate(triangulations)}
A=Matrix([[int(c in t) for c in channels] for t in triangulations])

def regional(region):
    ds=poly.region_diagonals(region)
    return sorted((frozenset(t) for t in poly.dissections_on(ds) if len(t)==len(region)-3),key=repr)

def primitive(vector):
    multiple=1
    for value in vector: multiple=ilcm(multiple,value.q)
    values=[int(value*multiple) for value in vector]
    divisor=0
    for value in values: divisor=gcd(divisor,abs(value))
    values=[value//divisor for value in values]
    first=next(value for value in values if value)
    return [-value for value in values] if first<0 else values

local=[]
local_records=[]
for cut in channels:
    regions=poly.split_regions(n,frozenset([cut]))
    left,right=[regional(region) for region in regions]
    if len(left)==len(right)==2:
        cells=[[index[frozenset(set(lt)|set(rt)|{cut})] for rt in right] for lt in left]
        row=[0]*len(triangulations)
        row[cells[0][0]]+=1; row[cells[1][1]]+=1
        row[cells[0][1]]-=1; row[cells[1][0]]-=1
        local.append(row)
        local_records.append({"cut":list(cut),"positive_indices":[cells[0][0],cells[1][1]],"negative_indices":[cells[0][1],cells[1][0]]})
Rlocal=Matrix(local)
assert Rlocal.rank()==3 and Rlocal*A==Matrix.zeros(3,len(channels))

full=[primitive(vector) for vector in A.T.nullspace()]
Rfull=Matrix(full)
assert Rfull.rank()==5
combined=list(local)
complement=[]
rank=Rlocal.rank()
for row in full:
    trial=Matrix(combined+[row]).rank()
    if trial>rank:
        complement.append(row); combined.append(row); rank=trial
assert len(complement)==2 and rank==5

# Construct a positive weight vector w_T=2^ell_T satisfying all local equations
# while violating a complementary global relation.
witness=None
for vector in Rlocal.nullspace():
    values=primitive(vector)
    violations=[sum(row[i]*values[i] for i in range(14)) for row in complement]
    if any(violations):
        witness={"log2_exponents":values,"local_exponents":[sum(row[i]*values[i] for i in range(14)) for row in local],"complement_exponents":violations}
        break
assert witness is not None and witness["local_exponents"]==[0,0,0]

result={
    "schema":"marici.six-point-local-vs-global-weights.v1",
    "status":"passed",
    "strength":"exact relation-space comparison at six points",
    "global_relation_rank":5,
    "local_long_facet_relation_rank":3,
    "nonlocal_quotient_dimension":2,
    "local_relations":local_records,
    "complement_relations":[{"terms":[{"triangulation_index":i,"exponent":value} for i,value in enumerate(row) if value]} for row in complement],
    "local_pass_global_fail_witness":witness,
    "interpretation":"all facet rank-one tests can pass while two independent global cycle constraints fail",
    "boundary":"the distinction is combinatorial coefficient compatibility, not source provenance or geometric embedding",
}
out=Path("research/nima/results/six_point_local_vs_global_weights.json")
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(result,sort_keys=True))
