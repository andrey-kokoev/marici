#!/usr/bin/env python3
"""Exact Smith invariants for complex triangulation-weight factorability."""
import importlib.util
import json
from pathlib import Path
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

helper_path=Path(__file__).with_name("check_generic_polygon_face_product.py")
spec=importlib.util.spec_from_file_location("polygon_faces",helper_path)
poly=importlib.util.module_from_spec(spec)
spec.loader.exec_module(poly)

stages=[]
for n in range(4,8):
    channels=tuple(sorted(poly.diagonals(n)))
    triangulations=sorted((tuple(sorted(t)) for t in poly.dissections_on(channels) if len(t)==n-3),key=repr)
    A=Matrix([[int(c in t) for c in channels] for t in triangulations])
    D=smith_normal_form(A,domain=ZZ)
    invariants=[abs(int(D[i,i])) for i in range(len(channels))]
    assert all(value>0 for value in invariants)
    kernel_order=1
    for value in invariants:
        kernel_order*=value
    global_minus=(n-3)%2==0
    if global_minus:
        assert kernel_order%2==0
    stages.append({
        "n":n,
        "dimension":n-3,
        "channels":len(channels),
        "triangulations":len(triangulations),
        "smith_invariants":invariants,
        "complex_scale_kernel_order":kernel_order,
        "global_minus_in_kernel":global_minus,
        "independent_complex_weight_relations":len(triangulations)-len(channels),
    })

result={
    "schema":"marici.complex-weight-factorability.v1",
    "status":"passed",
    "strength":"exact Smith normal forms for n=4..7 plus the character-lattice criterion; no unbounded Smith-pattern theorem",
    "criterion":"nonzero complex weights are in the monomial facet-scale image iff every integer left-kernel character evaluates to one",
    "stages":stages,
    "branch_ambiguity":"the finite kernel order is the product of nonzero Smith invariants; a global facet minus lies in the kernel whenever triangulations have even size",
    "relation_counts":"complex character relations match rational magnitude relation counts; real signs can have additional F2 constraints from 2-torsion",
    "boundary":"complex reconstruction needs root-branch data; finite n=4..7 evidence does not prove a Smith pattern for all n",
}
out=Path("research/nima/results/complex_weight_factorability.json")
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(result,sort_keys=True))
