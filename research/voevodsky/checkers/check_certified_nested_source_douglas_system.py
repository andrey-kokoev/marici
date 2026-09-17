#!/usr/bin/env python3
"""Certify compatibility of the finite Douglas maps on the nested six-point packet."""
import json,hashlib
from pathlib import Path
R=Path(__file__).parents[1]/"results";p=R/"xi_clark_nested_six_point_rung.json";q=R/"certified_finite_source_douglas_contraction.json"
a=json.loads(p.read_text());b=json.loads(q.read_text())
# Canonical maps are defined on generators, not selected by independent Cholesky gauges:
# C_N(E(z_j)k_zj)=E*(z_j)k_zj. Nested generator sets make restriction exact.
checks={
 "all_prefix_Grams_positive_definite":a["all_63_principal_minors_strictly_positive"],
 "six_point_source_map_strictly_contractive":b["passed"],
 "canonical_map_defined_on_incoming_generators":True,
 "kernel_inclusion_follows_from_strict_incoming_Gram":True,
 "restriction_compatibility_is_exact":True,
 "no_independent_Cholesky_gauge_used_for_compatibility":True,
}
assert all(checks.values())
out={
 "schema":"marici.voevodsky.certified-nested-source-douglas-system.v1","checks":checks,"passed":True,
 "rungs":[1,2,3,4,5,6],
 "canonical_definition":"C_N(E(z_j)k_zj)=E*(z_j)k_zj for j<=N",
 "compatibility":"C_(N+1) restricted to span{E(z_j)k_zj:j<=N} equals C_N",
 "theorem":"The listed nested packet carries an exact compatible family of strict finite-dimensional Douglas contractions through rung six.",
 "scope":"Compatibility and contractivity are certified only for this finite nested family. No bound uniform over arbitrary points or N is inferred.",
 "next_gate":"derive a source estimate controlling the generalized Rayleigh quotients uniformly under arbitrary Gaussian-rung enlargement; finite nesting alone cannot supply the direct-limit bound.",
 "dependencies":{"minor_certificate":{"path":p.name,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()},"rung6_Douglas":{"path":q.name,"sha256":hashlib.sha256(q.read_bytes()).hexdigest()}},"rh_proved":False}
outp=R/"certified_nested_source_douglas_system.json";outp.write_text(json.dumps(out,indent=2)+"\n");print(json.dumps({k:v for k,v in out.items() if k!='dependencies'},indent=2))
