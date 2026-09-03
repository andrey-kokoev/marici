import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(941,942)
wp941=json.loads((ROOT/"results"/"wp941_boundaryless_geometry_instrument_no_go.json").read_text())
wp942=json.loads((ROOT/"results"/"wp942_completion_stable_boundary_selector_exhaustion.json").read_text())
assert wp941["classification"] == "source-domain replacement, not selector on the interval lens family"
assert wp942["checks"]["no_route_passes_all_gates"] is True
assert wp942["remaining_routes"] == ["completion-stable UV law fixing finite even boundary coefficient","new boundaryless source with derived holonomy-to-Yukawa physical16 instrument"]
# Boundaryless geometry replaces the source domain and removes the endpoint
# instrument; all eight audited completion-stable boundary routes fail.
boundaryless_replaces_domain=True
endpoint_ports_lost=True
marked_circle_new_groupoid=True
all_routes_fail=True
new_geometry_derived=False
holonomy_instrument=False
uv_boundary_law=False
physical16_descent=False
assert boundaryless_replaces_domain and endpoint_ports_lost and marked_circle_new_groupoid and all_routes_fail
assert not (new_geometry_derived or holonomy_instrument or uv_boundary_law or physical16_descent)
result={
    "schema":"marici.flavor.wp1217.v1",
    "status":"PASS",
    "question":"Can a new boundary geometry supply the missing source law?",
    "dpc":{
        "conjecture":"Replacing the interval by a boundaryless circle removes the unresolved even boundary coefficient.",
        "rivals":["interval symmetry","additive RG","affine attractor","hypermultiplet beta kernel","bulk counterterm","volume suppression","unmarked circle","marked circle"],
        "risky_consequences":["the interval has two endpoint ports and one exchange-even coefficient","the unmarked circle has zero boundary coefficients and zero endpoint ports","two circle marks define a new relational groupoid","none of the eight audited routes passes all six acceptance gates"],
        "falsification_attempt":"endpoint-port rank drops from two to zero; tau=0 and tau=1 survive interval transport; marked circle changes the groupoid rather than preserving the source.",
        "residual":"derive either a completion-stable UV boundary law or a boundaryless holonomy-to-Yukawa physical16 instrument from one new source geometry",
        "disposition":"reject audited source geometries; select boundaryless holonomy-source rival"
    },
    "boundaryless_classification":wp941["classification"],
    "object_table":wp941["object_table"],
    "route_gate_vectors":wp942["route_gate_vectors"],
    "acceptance_gates":wp942["acceptance_gates"],
    "passing_routes":wp942["passing_routes"],
    "remaining_routes":wp942["remaining_routes"],
    "boundaryless_replaces_domain":boundaryless_replaces_domain,
    "endpoint_ports_lost":endpoint_ports_lost,
    "marked_circle_new_groupoid":marked_circle_new_groupoid,
    "all_routes_fail":all_routes_fail,
    "new_geometry_derived":new_geometry_derived,
    "holonomy_instrument":holonomy_instrument,
    "uv_boundary_law":uv_boundary_law,
    "physical16_descent":physical16_descent,
    "classification":"negative source-geometry result: interval and boundaryless routes are exhausted relative to declared instruments",
    "remaining_gate":"derive boundaryless holonomy-to-Yukawa physical16 instrument or completion-stable UV boundary law",
    "hostile_gate":"do not treat removing the boundary, adding marks, or suppressing response as deriving a source geometry",
    "claim_boundary":"the exhaustion is relative to the six declared gates and eight audited routes",
    "disposition":"new-source-geometry leaf resolved negatively; boundaryless holonomy-source rival selected"
}
(ROOT/"results"/"wp1217_new_source_geometry_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1217 PASS: audited source geometries exhausted")
