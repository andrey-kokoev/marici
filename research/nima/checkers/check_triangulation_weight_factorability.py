#!/usr/bin/env python3
"""Exact incidence-rank gate for absorbing triangulation weights into facet scales."""
import importlib.util
import json
from math import gcd
from pathlib import Path
from sympy import Matrix, ilcm

helper_path = Path(__file__).with_name("check_generic_polygon_face_product.py")
spec = importlib.util.spec_from_file_location("polygon_faces", helper_path)
poly = importlib.util.module_from_spec(spec)
spec.loader.exec_module(poly)

stages=[]
six_relation=None
for n in range(4,8):
    channels=tuple(sorted(poly.diagonals(n)))
    triangulations=sorted((tuple(sorted(t)) for t in poly.dissections_on(channels) if len(t)==n-3),key=repr)
    A=Matrix([[1 if channel in triangulation else 0 for channel in channels] for triangulation in triangulations])
    rank=A.rank()
    relations=A.T.nullspace()
    assert rank==len(channels)
    assert len(relations)==len(triangulations)-rank
    stage={"n":n,"channels":len(channels),"triangulations":len(triangulations),"incidence_rank":rank,"independent_weight_relations":len(relations)}
    stages.append(stage)
    if n==6:
        vector=relations[0]
        denominator_lcm=1
        for entry in vector:
            denominator_lcm=ilcm(denominator_lcm,entry.q)
        integers=[int(entry*denominator_lcm) for entry in vector]
        common=0
        for entry in integers:
            common=gcd(common,abs(entry))
        integers=[entry//common for entry in integers]
        assert any(integers) and Matrix([integers])*A==Matrix.zeros(1,len(channels))
        pivot=next(i for i,value in enumerate(integers) if value)
        six_relation={
            "nonzero_terms":[{"triangulation_index":i,"exponent":value,"channels":[list(c) for c in triangulations[i]]} for i,value in enumerate(integers) if value],
            "deliberate_weight_deformation":{"triangulation_index":pivot,"weight":2,"binomial_ratio":f"2^{integers[pivot]}","violates_factorability":True},
        }

assert [(s["n"],s["independent_weight_relations"]) for s in stages]==[(4,0),(5,0),(6,5),(7,28)]
result={
    "schema":"marici.triangulation-weight-factorability.v1",
    "status":"passed",
    "strength":"exact incidence ranks for n=4..7; generic factorability criterion is a torus-image theorem, not inferred from finite ranks",
    "criterion":"positive weights w_T factor as product_{c in T} lambda_c iff log(w) lies in the incidence-column image, equivalently every integer left-kernel binomial equals one",
    "stages":stages,
    "six_point_relation":six_relation,
    "boundary":"n=4,5 have no weight invariants, while n>=6 tested stages do; facet rescaling cannot absorb a violating coefficient system",
}
out=Path("research/nima/results/triangulation_weight_factorability.json")
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(result,sort_keys=True))
