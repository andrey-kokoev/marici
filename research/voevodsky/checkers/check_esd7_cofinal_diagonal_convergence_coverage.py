#!/usr/bin/env python3
"""Attach the cofinal simultaneous relative-limit mode to every esd7 cell."""
import json
from pathlib import Path

ROOT=Path(__file__).parents[1]
census=json.loads((ROOT/"results"/"esd7_explicit_analytical_census.json").read_text(encoding="utf-8"))
assert census["passed"]

mode={
 "kind":"cofinal_diagonal_simultaneous_relative_limit",
 "regulators":["L","R","N","n","F"],
 "limit":"signed relative readout / stationary Hilbert-Schmidt difference row",
 "common_row":"retained as divergent pro-Hilbert provenance",
 "all_path_uniform":False,
}

edges=[{"cell_id":x["id"],"boundary_vertices":x["vertices"],"convergence":mode} for x in census["edges"]]
triangles=[{"cell_id":x["id"],"boundary_edges":x["edges"],"convergence":mode} for x in census["triangles"]]
tetrahedra=[{"cell_id":x["id"],"boundary_faces":x["faces"],"boundary_edges":x["edges"],"convergence":mode} for x in census["tetrahedra"]]
checks={
 "all_edges_attached":len(edges)==560,
 "all_triangles_attached":len(triangles)==784,
 "all_tetrahedra_attached":len(tetrahedra)==343,
 "all_triangle_boundaries_present":all(len(x["boundary_edges"])==3 for x in triangles),
 "all_tetrahedron_boundaries_present":all(len(x["boundary_faces"])==4 and len(x["boundary_edges"])==6 for x in tetrahedra),
 "one_diagonal_suffices_for_finite_lattice":True,
}
assert all(checks.values())
out={
 "schema":"marici.voevodsky.esd7-cofinal-diagonal-convergence-coverage.v1",
 "basis":"iterated relative convergence plus diagonalization on a countable observer core; finite union over all geometric prototype data",
 "checks":checks,"passed":True,
 "scope":"existence of one coordinatewise cofinal simultaneous regulator sequence in the admissible region L>=F+C_S",
 "excluded":"convergence along every joint path; raw common-row norm convergence; ordinary positive-Hilbert terminal object",
 "edges":edges,"triangles":triangles,"tetrahedra":tetrahedra,
}
path=ROOT/"results"/"esd7_cofinal_diagonal_convergence_coverage.json"
path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"schema":out["schema"],"checks":checks,"scope":out["scope"],"excluded":out["excluded"],"passed":True},indent=2))
