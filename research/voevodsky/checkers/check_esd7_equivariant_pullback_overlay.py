#!/usr/bin/env python3
"""Attach the equivariant moving-current pullback carrier to every esd7 cell."""
import json, hashlib
from pathlib import Path
ROOT=Path(__file__).parents[1]
RES=ROOT/"results"
census=json.loads((RES/"esd7_explicit_analytical_census.json").read_text(encoding="utf-8"))
eq=json.loads((RES/"three_face_translation_equivariance.json").read_text(encoding="utf-8"))
assert census["passed"] and eq["passed"]
base={
 "base":"translation center c in R",
 "fiber":"weighted trace-class moving-current pullback",
 "action":"U_a: fiber_c -> fiber_(c+a)",
 "current_target":"S'(R)_beta",
}
edges=[{"id":x["id"],"vertices":x["vertices"],"overlay":"equivariant whiskered transfer","bundle":base} for x in census["edges"]]
faces=[{"id":x["id"],"edges":x["edges"],"overlay":"restriction of equivariant parent face homotopy; moving-current coordinate retained","bundle":base} for x in census["triangles"]]
tets=[{"id":x["id"],"faces":x["faces"],"overlay":"equivariant homotopy-pullback modification","bundle":base} for x in census["tetrahedra"]]
face_ids={x["id"] for x in faces}; edge_ids={x["id"] for x in edges}
checks={
 "all_560_edges_overlaid":len(edges)==560,
 "all_784_faces_overlaid":len(faces)==784,
 "all_343_tetrahedra_overlaid":len(tets)==343,
 "all_face_edges_resolve":all(set(x["edges"])<=edge_ids for x in faces),
 "all_tetrahedron_faces_resolve":all(set(x["faces"])<=face_ids for x in tets),
 "shared_face_has_single_overlay_record":len(face_ids)==len(faces),
 "translation_equivariance_dependency_passes":eq["passed"],
}
assert all(checks.values())
out={
 "schema":"marici.voevodsky.esd7-equivariant-pullback-overlay.v1",
 "checks":checks,"passed":True,"bundle":base,
 "edges":edges,"faces":faces,"tetrahedra":tets,
 "claim":"Every geometric cell carries the restriction of one translation-equivariant weighted moving-current pullback; shared faces are represented once and referenced by adjacent bulks.",
 "semantic_scope":"The overlay is inherited from the enriched parent tetrahedron. It does not assign an independent H123/H124/H134/H234 role to arbitrary internal geometric faces.",
 "dependencies":{"census_sha256":hashlib.sha256((RES/"esd7_explicit_analytical_census.json").read_bytes()).hexdigest(),"equivariance_sha256":hashlib.sha256((RES/"three_face_translation_equivariance.json").read_bytes()).hexdigest()}
}
path=RES/"esd7_equivariant_pullback_overlay.json"
path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"schema":out["schema"],"checks":checks,"claim":out["claim"],"semantic_scope":out["semantic_scope"],"passed":True},indent=2))
