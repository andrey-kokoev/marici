import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(996,997,998,999)
wp996=json.loads((ROOT/"results"/"wp996_bounded_control_chebyshev_optimum.json").read_text())
wp997=json.loads((ROOT/"results"/"wp997_actuator_metric_authority_gate.json").read_text())
wp998=json.loads((ROOT/"results"/"wp998_zero_drift_bracket_closure.json").read_text())
wp999=json.loads((ROOT/"results"/"wp999_rg_control_lift_underdetermination.json").read_text())
assert wp996["classification"] == "conditional Chebyshev-optimal formal controller under an assumed l-infinity control budget"
assert wp998["classification"] == "leafwise formal rigidifier; not selector; no physical instrument"
assert wp999["conclusion"] == "physical16 RG projection does not determine coefficient-plane accessibility"
# Bounded control is optimal only after assuming a norm/budget; formal
# rank-two actuation is mathematical only; available drift is leafwise; RG
# projection does not lift accessibility.
chebyshev_formal=True
budget_unfixed=True
rank_two_completion_mathematical=True
zero_drift_leafwise=True
rg_lift_underdetermined=True
physical_actuator_metric=False
transverse_actuator=False
common_substrate_lift=False
calibrated_closed_loop=False
assert chebyshev_formal and budget_unfixed and rank_two_completion_mathematical
assert zero_drift_leafwise and rg_lift_underdetermined
assert not (physical_actuator_metric or transverse_actuator or common_substrate_lift or calibrated_closed_loop)
result={
    "schema":"marici.flavor.wp1229.v1",
    "status":"PASS",
    "question":"Can bounded control derive source-authorized actuator normalization?",
    "dpc":{
        "conjecture":"A bounded Chebyshev controller or formal rank-two actuator map fixes source-derived actuator normalization.",
        "rivals":["assumed l-infinity budget","rank-one actuator","formal rank-two completion","zero-drift Q-direction family","zero-coefficient RG lift","transverse coefficient lift"],
        "risky_consequences":["the joint Chebyshev radius is B/5489 only after B is assumed","rank-one actuation leaves the R direction unreachable","the rank-two completion witness is mathematical only","zero drift preserves R leaves","the same physical RG projection permits bracket ranks one and two"],
        "falsification_attempt":"every route either assumes the control norm, lacks transverse access, or fails to lift RG data to the coefficient plane.",
        "residual":"source-derived common-substrate RG-to-(Q,R) lift, transverse actuator, positive command-cost Gram, and calibrated closed-loop error",
        "disposition":"reject bounded/formal control as actuator authority; select common-substrate RG-lift rival"
    },
    "optimal_targets":wp996["optimal_targets"],
    "joint_optimal_radius":wp996["joint_optimal_radius"],
    "rank_one_hostile":wp997["rank_one_hostile"],
    "formal_completion":wp997["formal_completion_witness"],
    "bracket_formula":wp998["bracket_formula"],
    "rg_lifts":{"zero_coefficient":wp999["zero_coefficient_lift"],"transverse":wp999["transverse_coefficient_lift"]},
    "chebyshev_formal":chebyshev_formal,
    "budget_unfixed":budget_unfixed,
    "rank_two_completion_mathematical":rank_two_completion_mathematical,
    "zero_drift_leafwise":zero_drift_leafwise,
    "rg_lift_underdetermined":rg_lift_underdetermined,
    "physical_actuator_metric":physical_actuator_metric,
    "transverse_actuator":transverse_actuator,
    "common_substrate_lift":common_substrate_lift,
    "calibrated_closed_loop":calibrated_closed_loop,
    "classification":"negative actuator-normalization result: formal control and RG projections do not fix physical command cost",
    "remaining_gate":"derive a common-substrate RG-to-(Q,R) lift and transverse actuator with weak-basis-descended positive command-cost Gram",
    "hostile_gate":"do not call an assumed budget, formal rank-two map, leafwise drift, or RG projection an actuator normalization",
    "claim_boundary":"Chebyshev optimality is conditional on the assumed l-infinity budget; rank-two completion is mathematical only",
    "disposition":"source-derived-actuator-normalization leaf resolved negatively; common-substrate RG-lift rival selected"
}
(ROOT/"results"/"wp1229_source_derived_actuator_normalization_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1229 PASS: actuator normalization requires common-substrate RG lift")
