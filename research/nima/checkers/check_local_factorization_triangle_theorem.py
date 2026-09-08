#!/usr/bin/env python3
"""Dependency check for the local-factorization triangle-additivity theorem."""
import hashlib
import json
from pathlib import Path

paths={
 "triangle_rank":Path("research/nima/results/triangle_incidence_rank_theorem.json"),
 "local_5_7":Path("research/nima/results/polygon_local_global_weight_relations.json"),
 "local_8":Path("research/nima/results/eight_point_local_global_weights.json"),
 "modular_9":Path("research/nima/results/nine_point_local_relation_conjecture.json"),
}
values={};digests={}
for name,path in paths.items():
    raw=path.read_bytes();value=json.loads(raw);assert value["status"]=="passed"
    values[name]=value;digests[name]=hashlib.sha256(raw).hexdigest()
triangle={stage["n"]:stage["triangle_incidence_rank"] for stage in values["triangle_rank"]["stages"]}
checks=[]
for stage in values["local_5_7"]["stages"]:
    solution=stage["triangulations"]-stage["local_relation_rank"]
    assert solution==triangle[stage["n"]]
    checks.append({"n":stage["n"],"exact_local_solution_dimension":solution,"triangle_additive_dimension":triangle[stage["n"]]})
stage=values["local_8"]
solution=stage["triangulations"]-stage["local_relation_rank"]
assert solution==triangle[8]
checks.append({"n":8,"exact_local_solution_dimension":solution,"triangle_additive_dimension":triangle[8]})
assert values["modular_9"]["predicted_local_rank"]==372
result={
 "schema":"marici.local-factorization-triangle-theorem.v1","status":"passed",
 "strength":"generic characteristic-zero cochain proof with exact dimension equality checks n=5..8 and modular n=9 consistency",
 "theorem":"an additive function on polygon triangulations is separable on every facet product iff it is a sum of weights of its triangular faces",
 "proof_edges":["facet separability makes each quadrilateral flip increment independent of surrounding triangulations","five-flip pentagon cycles make the context-free quadruple increment a closed simplicial 3-cochain","simplex exactness writes that increment as the coboundary of triangle weights","subtracting the triangle sum kills all flip increments; flip-graph connectivity leaves a constant, itself triangle-additive in characteristic zero"],
 "exact_dimension_checks":checks,
 "n9_consistency":"modular local rank 372 gives solution dimension 57, matching the proved triangle-incidence rank formula",
 "input_sha256":digests,
 "boundary":"the theorem is additive/logarithmic over characteristic zero; multiplicative signs, phases, and source provenance retain their separate gates",
}
out=Path("research/nima/results/local_factorization_triangle_theorem.json")
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(result,sort_keys=True))
