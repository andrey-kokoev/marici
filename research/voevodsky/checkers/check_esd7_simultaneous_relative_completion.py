#!/usr/bin/env python3
"""Aggregate the explicit lattice and cofinal simultaneous-limit certificates."""
import hashlib, json
from pathlib import Path

ROOT=Path(__file__).parents[1]/"results"
files={
 "cell_census":"esd7_explicit_analytical_census.json",
 "convergence_coverage":"esd7_cofinal_diagonal_convergence_coverage.json",
 "angular_tail":"angular_phase_energy_uniform_tail.json",
 "finite_rank_reduction":"uniform_trace_exhaustion_finite_rank_reduction.json",
}
data={k:json.loads((ROOT/v).read_text(encoding="utf-8")) for k,v in files.items()}
c=data["cell_census"]; d=data["convergence_coverage"]
checks={
 "all_dependencies_pass":all(x["passed"] for x in data.values()),
 "cell_counts_match":(len(c["edges"]),len(c["triangles"]),len(c["tetrahedra"]))==(560,784,343),
 "convergence_counts_match":(len(d["edges"]),len(d["triangles"]),len(d["tetrahedra"]))==(560,784,343),
 "edge_ids_match":{x["id"] for x in c["edges"]}=={x["cell_id"] for x in d["edges"]},
 "triangle_ids_match":{x["id"] for x in c["triangles"]}=={x["cell_id"] for x in d["triangles"]},
 "tetrahedron_ids_match":{x["id"] for x in c["tetrahedra"]}=={x["cell_id"] for x in d["tetrahedra"]},
 "single_cofinal_mode":len({json.dumps(x["convergence"],sort_keys=True) for dim in ("edges","triangles","tetrahedra") for x in d[dim]})==1,
}
assert all(checks.values()),checks
out={
 "schema":"marici.voevodsky.esd7-simultaneous-relative-completion.v1",
 "checks":checks,"passed":True,
 "theorem":"Every edge, triangle, and tetrahedron of esd_7(Delta^3) has a finite signed/relative analytical form and converges along one common coordinatewise-cofinal admissible regulator sequence on the chosen countable observer core.",
 "counts":{"edges":560,"triangles":784,"tetrahedra":343},
 "limit_strength":"signed relative readouts and stationary Hilbert-Schmidt difference rows",
 "not_claimed":["all-path uniform convergence","raw common-row norm convergence","ordinary positive-Hilbert terminal completion"],
 "dependencies":{k:{"path":v,"sha256":hashlib.sha256((ROOT/v).read_bytes()).hexdigest()} for k,v in files.items()},
}
path=ROOT/"esd7_simultaneous_relative_completion.json"
path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in out.items() if k!="dependencies"},indent=2))
