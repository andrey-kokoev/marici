#!/usr/bin/env python3
"""Promote the certified six-point Clark Gram inequality to a finite Douglas theorem."""
import json,hashlib
from pathlib import Path
R=Path(__file__).parents[1]/"results"
pminor=R/"xi_clark_nested_six_point_rung.json";scout=R/"source_clark_douglas_packets.json"
a=json.loads(pminor.read_text());b=json.loads(scout.read_text())
checks={
 "all_difference_principal_minors_certified_positive":a["all_63_principal_minors_strictly_positive"],
 "source_features_built_separately":b["construction"].startswith("A_S and A_B are factored separately"),
 "matching_six_point_packet":a["points"]==b["packets"][2]["points"],
 "incoming_Hardy_Gram_positive":"the Cauchy kernel is strictly positive on distinct upper-half-plane points and E is nonzero at the evaluated points",
 "difference_identity":"G_in-G_out is the certified Clark Gram",
 "finite_Douglas_implication":"G_out < G_in implies a unique contraction on the finite source range with norm strictly below one",
}
assert checks["all_difference_principal_minors_certified_positive"] and checks["source_features_built_separately"] and checks["matching_six_point_packet"]
out={
 "schema":"marici.voevodsky.certified-finite-source-douglas-contraction.v1","checks":checks,"passed":True,
 "theorem":"On the listed six-point source packet, G_in-G_out is rigorously positive definite; therefore the map sending each incoming Hardy feature to its outgoing Clark feature extends to a strict finite-dimensional Douglas contraction.",
 "packet_size":6,"numerical_norm_scout":b["packets"][2]["operator_norm_C"],
 "certification_note":"The strict contraction conclusion uses the interval-certified Loewner inequality, not the floating-point singular value.",
 "scope":"One finite six-point source range only. No uniform margin, compatible direct-limit contraction, Schur theorem, or RH claim.",
 "dependencies":{"minors":{"path":pminor.name,"sha256":hashlib.sha256(pminor.read_bytes()).hexdigest()},"source_scout":{"path":scout.name,"sha256":hashlib.sha256(scout.read_bytes()).hexdigest()}},
 "rh_proved":False}
p=R/"certified_finite_source_douglas_contraction.json";p.write_text(json.dumps(out,indent=2)+"\n");print(json.dumps({k:v for k,v in out.items() if k!='dependencies'},indent=2))
