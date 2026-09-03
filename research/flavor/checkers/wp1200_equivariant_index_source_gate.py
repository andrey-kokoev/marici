import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(847,848)
wp847=json.loads((ROOT/"results"/"wp847_incidence_kernel_not_equivariant_charge_index.json").read_text())
wp848=json.loads((ROOT/"results"/"wp848_charged_spurion_equivariant_incidence_lift.json").read_text())
assert wp847["summary"]["all_passed"] is True
assert wp848["summary"]["all_passed"] is True
assert wp847["equivariance_obstruction"] == "BQq=(-2,-6), so no A satisfies AB=BQ"
assert wp847["actual_index"] == "ordinary Euler index dim ker B-dim coker B=1"
assert wp848["lifted_differential"] == "[[2s1,-s2,0],[3s1,0,-s3]], with weights(sj)=-j"
assert wp848["kernel"] == "(s2 s3, 2 s1 s3, 3 s1 s2)"
assert wp848["virtual_character"] == "z+z^2+z^3-2"
assert wp848["smallest_exact_falsifier"] == "VEVs (1,2,1) give kernel ray (1,1,3), not (1,2,3)"
assert wp848["classification"] == "equivariance typing repair, not a source selector; vacuum alignment and character transport remain open"
# The old incidence has no equivariant index. The charged-spurion lift repairs
# typing but neither selects VEV alignment nor transports WP846's character.
incidence_equivariant_index=False
spurion_equivariant_lift=True
primitive_character_transport=False
vacuum_alignment_selected=False
calibrated_holonomy_ports=False
assert spurion_equivariant_lift
assert not (incidence_equivariant_index or primitive_character_transport or vacuum_alignment_selected or calibrated_holonomy_ports)
result={
    "schema":"marici.flavor.wp1200.v1",
    "status":"PASS",
    "question":"Can incidence source the equivariant character index?",
    "dpc":{
        "conjecture":"WP820 incidence derives the equivariant index needed for character sewing.",
        "rivals":["incidence kernel as charge index","charged-spurion lift","equal-VEV spurion potential","protected pre-vacuum index transport"],
        "risky_consequences":["BQq=(-2,-6), so no intertwiner exists","ordinary Euler index is 1","the spurion lift has kernel (s2s3,2s1s3,3s1s2)","its virtual character is z+z^2+z^3-2 and VEVs (1,2,1) give ray (1,1,3)"],
        "falsification_attempt":"The old incidence fails equivariance exactly; the typed lift relocates selection to VEV alignment and changes the index character.",
        "residual":"An independently sourced spurion potential and protected equivariant-index transport remain required.",
        "disposition":"reject incidence-sourced index; construct typed spurion lift"
    },
    "incidence":wp847["incidence"],
    "kernel_coefficient":wp847["kernel_coefficient"],
    "equivariance_obstruction":wp847["equivariance_obstruction"],
    "ordinary_index":wp847["actual_index"],
    "spurion_lift":wp848["lifted_differential"],
    "spurion_kernel":wp848["kernel"],
    "virtual_character":wp848["virtual_character"],
    "vev_falsifier":wp848["smallest_exact_falsifier"],
    "incidence_equivariant_index":incidence_equivariant_index,
    "spurion_equivariant_lift":spurion_equivariant_lift,
    "primitive_character_transport":primitive_character_transport,
    "vacuum_alignment_selected":vacuum_alignment_selected,
    "calibrated_holonomy_ports":calibrated_holonomy_ports,
    "classification":"negative source-index gate with typed repair: incidence is not equivariant; spurion lift leaves alignment and character transport open",
    "remaining_gate":"derive the spurion alignment potential and protected pre-vacuum index transport",
    "hostile_gate":"do not treat kernel coefficients as representation weights",
    "claim_boundary":"the spurion lift repairs typing only; it does not select the primitive ray or WP846's positive character",
    "disposition":"equivariant-index-source leaf resolved; spurion-alignment-source rival selected"
}
(ROOT/"results"/"wp1200_equivariant_index_source_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1200 PASS: BQq=(-2,-6); spurion lift leaves alignment open")
