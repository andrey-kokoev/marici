#!/usr/bin/env python3
"""Canonical exact basis of six-point triangulation-weight relations."""
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
triangulations=sorted((tuple(sorted(t)) for t in poly.dissections_on(channels) if len(t)==n-3),key=repr)
A=Matrix([[int(c in t) for c in channels] for t in triangulations])

def primitive(vector):
    multiplier=1
    for entry in vector:
        multiplier=ilcm(multiplier,entry.q)
    values=[int(entry*multiplier) for entry in vector]
    divisor=0
    for value in values:
        divisor=gcd(divisor,abs(value))
    values=[value//divisor for value in values]
    first=next(value for value in values if value)
    return [-value for value in values] if first<0 else values

relations=[primitive(vector) for vector in A.T.nullspace()]
B=Matrix(relations)
assert B.shape==(5,14) and B.rank()==5
assert B*A==Matrix.zeros(5,9)
assert all(sum(row)==0 for row in relations)

relation_records=[]
for index,row in enumerate(relations):
    terms=[]
    for triangulation_index,exponent in enumerate(row):
        if exponent:
            terms.append({"triangulation_index":triangulation_index,"exponent":exponent,"channels":[list(c) for c in triangulations[triangulation_index]]})
    relation_records.append({"relation":index,"terms":terms,"unit_weight_binomial":"1"})

# Choose a single-weight deformation detected by the largest number of basis relations.
column_counts=[sum(relations[r][c]!=0 for r in range(5)) for c in range(14)]
pivot=max(range(14),key=lambda c:column_counts[c])
violations=[{"relation":r,"ratio":f"2^{relations[r][pivot]}"} for r in range(5) if relations[r][pivot]]
assert violations

result={
    "schema":"marici.six-point-weight-relations.v1",
    "status":"passed",
    "strength":"exact primitive rational-kernel basis for the declared triangulation ordering; equivalent bases encode the same positive-real factorability test",
    "channels":[list(c) for c in channels],
    "triangulations":[[list(c) for c in t] for t in triangulations],
    "incidence_rank":A.rank(),
    "relation_rank":B.rank(),
    "relations":relation_records,
    "deliberate_single_weight_deformation":{"triangulation_index":pivot,"weight":2,"violated_basis_relations":violations},
    "acceptance":"all five binomial ratios must equal one before six-point coefficients can be absorbed into positive facet scales",
    "boundary":"the basis depends on ordering but its kernel subspace does not; passing factorability does not supply source provenance",
}
out=Path("research/nima/results/six_point_weight_relations.json")
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(result,sort_keys=True))
