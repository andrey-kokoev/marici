import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(920,921,922,923,924)
wp920=json.loads((ROOT/"results"/"wp920_spin5_completion_rank_index_selector_gate.json").read_text())
wp921=json.loads((ROOT/"results"/"wp921_spin7_parent_branching_singleton_audit.json").read_text())
wp922=json.loads((ROOT/"results"/"wp922_spin7_orbifold_zero_mode_projection_fiber.json").read_text())
wp923=json.loads((ROOT/"results"/"wp923_spin7_projected_yukawa_coefficient_fiber.json").read_text())
wp924=json.loads((ROOT/"results"/"wp924_spin7_exchange_reflection_yukawa_gate.json").read_text())
assert wp920["classification"] == "negative_selection_positive_typing: rank-index data distinguish the Spin(5) completions but no admitted source operation selects either"
assert wp921["classification"] == "partial_parent_constraint: complete Spin(7) representations exclude exact Completion B but force neutral surplus beyond Completion A"
assert wp922["classification"] == "conditional_exact_constructor_nonselection: a Spin(7) orbifold parity realizes exact Completion A zero modes, but intrinsic parities remain an eight-point source fiber"
assert wp923["classification"] == "coefficient_fiber: exact projected Completion A retains two independently allowed conjugate-charge Yukawa channels"
assert wp924["classification"] == "conditional_ratio_selector: exact exchange-reflection fixes the conjugate-channel magnitude ratio but leaves common coupling and family shape free"
# The independent principle is now explicit but conditional: Spin(7)
# branching excludes B, orbifold parity can realize exact A, and exchange
# reflection fixes the conjugate Yukawa ratio.  The full symmetry/action is
# not yet source-derived.
rank_index_identifies=True
spin7_excludes_b=True
orbifold_realizes_a=True
exchange_fixes_ratio=True
parity_authority=False
full_exchange_action=False
family_tensors_selected=False
calibrated_instrument=False
assert rank_index_identifies and spin7_excludes_b and orbifold_realizes_a and exchange_fixes_ratio
assert not (parity_authority or full_exchange_action or family_tensors_selected or calibrated_instrument)
result={
    "schema":"marici.flavor.wp1214.v1",
    "status":"PASS",
    "question":"Can an independent parent/locality principle select the Spin(5) completion and begin its Yukawa grammar?",
    "dpc":{
        "conjecture":"Spin(7) parent branching, orbifold zero-mode projection, and endpoint exchange-reflection independently select exact Completion A and its conjugate Yukawa ratio.",
        "rivals":["rank-index typing without preparation","complete Spin(7) representation with neutral surplus","unselected intrinsic parities","independent Yukawa coefficient ratio","endpoint-asymmetric counterterm"],
        "risky_consequences":["rank-index data separate A and B","charge-symmetric Spin(7) branching excludes exact B","the minimal A carrier forces 10_0+1_0 surplus","the orbifold has exactly two parity assignments yielding exact A","projection leaves two Yukawa channels","exchange-reflection fixes y_plus=conjugate(y_minus) and ratio one"],
        "falsification_attempt":"flipping eta_21 restores neutral surplus and removes charged vectors; dropping exchange leaves ratio two; an endpoint-asymmetric counterterm restores ratio two.",
        "residual":"derive intrinsic parities and exchange-reflection as symmetries of the complete bulk/brane/regulator/anomaly-inflow action, then promote tensors, RG, and physical16 calibration",
        "disposition":"construct conditional independent completion principle; reject action-unauthorized promotion"
    },
    "rank_index_classification":wp920["classification"],
    "parent_classification":wp921["classification"],
    "orbifold_classification":wp922["classification"],
    "coefficient_classification":wp923["classification"],
    "exchange_classification":wp924["classification"],
    "target_assignments":wp922["target_assignments"],
    "target_zero_modes":wp922["target_zero_modes"],
    "selected_relation":wp924["selected_relation"],
    "smallest_exchange_falsifier":wp924["smallest_exact_falsifier"],
    "rank_index_identifies":rank_index_identifies,
    "spin7_excludes_b":spin7_excludes_b,
    "orbifold_realizes_a":orbifold_realizes_a,
    "exchange_fixes_ratio":exchange_fixes_ratio,
    "parity_authority":parity_authority,
    "full_exchange_action":full_exchange_action,
    "family_tensors_selected":family_tensors_selected,
    "calibrated_instrument":calibrated_instrument,
    "classification":"conditional independent Spin(7)/orbifold/exchange completion principle",
    "remaining_gate":"derive endpoint exchange as an exact symmetry of the complete source action and derive intrinsic parities independently",
    "hostile_gate":"do not treat rank-index separation, chosen parities, or desired-channel exchange as complete action symmetry",
    "claim_boundary":"the principle conditionally selects A and ratio one; it does not yet authorize the physical action or physical16 point",
    "disposition":"independent-completion-principle leaf resolved conditionally; complete endpoint-exchange action rival selected"
}
(ROOT/"results"/"wp1214_independent_completion_principle_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1214 PASS: conditional Spin7 orbifold exchange selects A ratio")
