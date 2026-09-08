#!/usr/bin/env python3
"""Exact F2 gate for absorbing triangulation signs into facet signs."""
import importlib.util
import json
from pathlib import Path

helper_path=Path(__file__).with_name("check_generic_polygon_face_product.py")
spec=importlib.util.spec_from_file_location("polygon_faces",helper_path)
poly=importlib.util.module_from_spec(spec)
spec.loader.exec_module(poly)

def rref_nullspace_mod2(matrix):
    rows=[sum((value&1)<<j for j,value in enumerate(row)) for row in matrix]
    width=len(matrix[0]) if matrix else 0
    pivot_columns=[]
    pivot_row=0
    for column in range(width):
        pivot=next((r for r in range(pivot_row,len(rows)) if (rows[r]>>column)&1),None)
        if pivot is None:
            continue
        rows[pivot_row],rows[pivot]=rows[pivot],rows[pivot_row]
        for r in range(len(rows)):
            if r!=pivot_row and ((rows[r]>>column)&1):
                rows[r]^=rows[pivot_row]
        pivot_columns.append(column)
        pivot_row+=1
    free=[c for c in range(width) if c not in pivot_columns]
    basis=[]
    for free_column in free:
        vector=1<<free_column
        for r,pivot_column in enumerate(pivot_columns):
            if (rows[r]>>free_column)&1:
                vector|=1<<pivot_column
        basis.append([(vector>>c)&1 for c in range(width)])
    return len(pivot_columns),basis

stages=[]
five_relation=None
six_relation_count=None
for n in range(4,8):
    channels=tuple(sorted(poly.diagonals(n)))
    triangulations=sorted((tuple(sorted(t)) for t in poly.dissections_on(channels) if len(t)==n-3),key=repr)
    A=[[int(c in t) for c in channels] for t in triangulations]
    rank,_=rref_nullspace_mod2(A)
    transpose=[[A[row][column] for row in range(len(A))] for column in range(len(channels))]
    _,left_basis=rref_nullspace_mod2(transpose)
    assert len(left_basis)==len(triangulations)-rank
    for relation in left_basis:
        for channel_index in range(len(channels)):
            assert sum(relation[t]*A[t][channel_index] for t in range(len(triangulations)))%2==0
    stages.append({"n":n,"channels":len(channels),"triangulations":len(triangulations),"f2_incidence_rank":rank,"independent_sign_relations":len(left_basis)})
    if n==5:
        assert len(left_basis)==1
        five_relation={"negative_weight_indices":[i for i,value in enumerate(left_basis[0]) if value],"condition":"product of all five triangulation signs is +1"}
        assert sum(left_basis[0])==5
    if n==6:
        six_relation_count=len(left_basis)

result={
    "schema":"marici.signed-weight-factorability.v1",
    "status":"passed",
    "strength":"exact F2 incidence theorem with exhaustive polygon matrices n=4..7; no claim about complex phases",
    "criterion":"triangulation signs are products of facet signs iff their bit vector lies in the F2 incidence image, equivalently every F2 left-kernel parity is even",
    "stages":stages,
    "five_point_relation":five_relation,
    "six_point_sign_relations":six_relation_count,
    "deliberate_failure":"one negative five-point triangulation weight makes the total sign product -1 and cannot be absorbed",
    "boundary":"positive-magnitude and sign gates are independent; complex phases require a coefficient-group analysis",
}
out=Path("research/nima/results/signed_weight_factorability.json")
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(result,sort_keys=True))
