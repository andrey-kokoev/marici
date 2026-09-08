#!/usr/bin/env python3
"""Dependency and boundary audit for the source-embedding owner acceptance bundle."""
import hashlib
import json
from pathlib import Path

paths={
 "five_point_conformance":Path("research/nima/results/source_embedding_conformance.json"),
 "adjacent_normalization":Path("research/nima/results/source_embedding_adjacent_fixtures.json"),
 "gauge_orientation":Path("research/nima/results/source_embedding_orientation_character.json"),
 "weight_covariance":Path("research/nima/results/facet_rescaling_weight_covariance.json"),
 "global_weight_relations":Path("research/nima/results/six_point_weight_relations.json"),
 "scale_reconstruction":Path("research/nima/results/six_point_scale_reconstruction.json"),
 "signed_weights":Path("research/nima/results/signed_weight_factorability.json"),
 "complex_weights":Path("research/nima/results/polygon_incidence_smith_theorem.json"),
 "weighted_gluing":Path("research/nima/results/six_point_weighted_facet_factorization.json"),
 "local_global_separation":Path("research/nima/results/six_point_local_vs_global_weights.json"),
 "normalization_descent":Path("research/nima/results/polygon_normalization_descent.json"),
}
loaded={}; digests={}
for name,path in paths.items():
    raw=path.read_bytes(); value=json.loads(raw)
    assert value["status"]=="passed"
    loaded[name]=value; digests[name]=hashlib.sha256(raw).hexdigest()
assert loaded["five_point_conformance"]["residuals"]==["source_derived_provenance","zero_dimensional_normalization"]
assert loaded["global_weight_relations"]["relation_rank"]==5
assert loaded["local_global_separation"]["nonlocal_quotient_dimension"]==2
assert loaded["complex_weights"]["consequence"].endswith("roots of unity")

gates=[
 {"order":1,"gate":"source provenance and formulas","status":"blocked","acceptance":"source locator and derivation of E_n"},
 {"order":2,"gate":"five-point geometry and canonical form","status":"fixture_passed_source_unverified"},
 {"order":3,"gate":"coefficient scale/sign/phase compatibility","status":"harness_ready_source_coefficients_absent"},
 {"order":4,"gate":"six-point local and global gluing","status":"harness_ready_source_coefficients_absent"},
 {"order":5,"gate":"base normalization and orientation","status":"conditional_descent_only"},
 {"order":6,"gate":"physical sector map and analytic prescription","status":"absent"},
]
result={
 "schema":"marici.source-embedding-acceptance-bundle.v1",
 "status":"passed",
 "strength":"dependency-checked acceptance bundle; no blocked gate is promoted",
 "gates":gates,
 "first_blocker":"source-derived E_n with locator, formulas, channel scales or transported weights, and orientation",
 "reopening_test":"owner packet supplies gate 1, then existing harnesses run in order without replacing provenance by fixture agreement",
 "input_sha256":digests,
 "boundary":"bundle integrity and algebraic readiness do not authenticate sources, supply coefficients, or establish a physical comparison",
}
out=Path("research/nima/results/source_embedding_acceptance_bundle.json")
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(result,sort_keys=True))
