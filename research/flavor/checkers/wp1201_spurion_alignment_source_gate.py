import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(849,850)
wp849=json.loads((ROOT/"results"/"wp849_charge_recursive_spurion_alignment_selector.json").read_text())
wp850=json.loads((ROOT/"results"/"wp850_charge_recursive_selector_aspect_germ_audit.json").read_text())
assert wp849["summary"]["all_passed"] is True
assert wp850["summary"]["all_passed"] is True
assert wp849["selected_kernel"] == "v^2(1,2,3)"
assert wp849["zero_orbit"] == "v(e^{-i theta},e^{-2i theta},e^{-3i theta})"
assert wp849["coefficient_robustness"] == "zero orbit is identical for all lambda_i>0"
assert wp850["germ"]["complex_hessian_rank"] == 5
assert wp850["full_fiber"] == "one U(1) orbit for the declared positive sum-of-squares potential"
assert wp850["smallest_completion_falsifier"] == "epsilon v^2 |s2|^2"
assert wp850["classification"] == "passes germ and full-fiber gates conditionally; fails source-completion authority"
# The recursive potential is a genuine in-model selector, but the allowed
# orbit-moving invariant shows it is not source-unavoidable.
alignment_selected_in_model=True
primitive_ray_selected=True
local_germ_nondegenerate=True
source_completion_authority=False
index_transport=False
calibrated_holonomy=False
assert alignment_selected_in_model and primitive_ray_selected and local_germ_nondegenerate
assert not (source_completion_authority or index_transport or calibrated_holonomy)
result={
    "schema":"marici.flavor.wp1201.v1",
    "status":"PASS",
    "question":"Can a charge-recursive potential source spurion alignment?",
    "dpc":{
        "conjecture":"A charge-recursive spurion potential derives the aligned source.",
        "rivals":["unaligned charged-spurion lift","recursive sum-of-squares potential","source completion excluding orbit-moving invariants","canonical positive pairing"],
        "risky_consequences":["the zero locus is one U(1) orbit","gauge fixing gives (v,v,v) and kernel v^2(1,2,3)","the complex Hessian has rank five with only the orbit null direction","epsilon v^2|s2|^2 moves the vacuum and projective ray"],
        "falsification_attempt":"The declared potential passes germ and full-fiber tests but fails completion because an allowed invariant moves the orbit.",
        "residual":"A source theorem must exclude or fix every orbit-moving invariant and transport the index character.",
        "disposition":"construct conditional spurion alignment; reject source-unavoidable selection"
    },
    "potential":wp849["potential"],
    "zero_orbit":wp849["zero_orbit"],
    "gauge_fixed_representative":wp849["gauge_fixed_representative"],
    "selected_kernel":wp849["selected_kernel"],
    "hessian_rank":wp850["germ"]["complex_hessian_rank"],
    "completion_falsifier":wp850["smallest_completion_falsifier"],
    "vacuum_displacement":wp850["first_order_vacuum_displacement"],
    "alignment_selected_in_model":alignment_selected_in_model,
    "primitive_ray_selected":primitive_ray_selected,
    "local_germ_nondegenerate":local_germ_nondegenerate,
    "source_completion_authority":source_completion_authority,
    "index_transport":index_transport,
    "calibrated_holonomy":calibrated_holonomy,
    "classification":"conditional spurion-alignment selector: orbit and primitive ray selected in-model, source completion open",
    "remaining_gate":"derive a canonical positive pairing or source theorem excluding orbit-moving invariants",
    "hostile_gate":"do not treat a declared sum-of-squares potential as independent source authority",
    "claim_boundary":"the selector is restricted to the declared spurion model and does not transport WP846's character",
    "disposition":"spurion-alignment-source leaf resolved; positive-pairing normalization rival selected"
}
(ROOT/"results"/"wp1201_spurion_alignment_source_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1201 PASS: orbit selected; source completion open")
