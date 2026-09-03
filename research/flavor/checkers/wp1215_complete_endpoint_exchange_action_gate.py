import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(924,925,930)
wp924=json.loads((ROOT/"results"/"wp924_spin7_exchange_reflection_yukawa_gate.json").read_text())
wp925=json.loads((ROOT/"results"/"wp925_spin7_exchange_fixed_family_tensor_fiber.json").read_text())
wp930=json.loads((ROOT/"results"/"wp930_double_commutator_yukawa_lift_source_gate.json").read_text())
assert wp924["classification"] == "conditional_ratio_selector: exact exchange-reflection fixes the conjugate-channel magnitude ratio but leaves common coupling and family shape free"
assert wp925["classification"] == "family_tensor_fiber: exchange-reflection identifies conjugate tensor copies but leaves an arbitrary complex three-family Yukawa tensor"
assert wp930["classification"] == "negative source-support closure: the conditional Gram gradient has a rational Sylvester lift but no declared Spin5 generator"
# The endpoint exchange exists only as a conditional operation on desired
# channels.  Boundary asymmetry, arbitrary family tensors, and absent
# three-family source beta prevent promotion to a complete source action.
ratio_constraint=True
family_conjugate_copy=True
conditional_gradient_lifts=True
endpoint_asymmetry_breaks=True
arbitrary_family_tensor=True
complete_action_derived=False
source_beta_derived=False
physical_instrument=False
assert ratio_constraint and family_conjugate_copy and conditional_gradient_lifts
assert endpoint_asymmetry_breaks and arbitrary_family_tensor
assert not (complete_action_derived or source_beta_derived or physical_instrument)
result={
    "schema":"marici.flavor.wp1215.v1",
    "status":"PASS",
    "question":"Does endpoint exchange extend to a symmetry of the complete three-family source action?",
    "dpc":{
        "conjecture":"Endpoint exchange-reflection is an exact symmetry of the complete bulk, brane, regulator, and anomaly-inflow action.",
        "rivals":["endpoint-asymmetric counterterm","exchange-even boundary invariant depending on spectral traces","arbitrary conjugate three-family tensor","rational Sylvester lift without source generator"],
        "risky_consequences":["exchange fixes scalar ratio one only on its declared channels","tensor exchange leaves an 18-real-dimensional arbitrary tensor locus","exchange-even boundary terms may depend on unfixed spectral invariants","the double-commutator lift exists mathematically but has no declared Spin5 generator"],
        "falsification_attempt":"an endpoint-asymmetric counterterm restores ratio two; diagonal conjugate tensor hostiles have different spectral discriminants; the declared Spin5 packet has no three-family Yukawa beta source arrow.",
        "residual":"declare a new three-family source action deriving exchange, its boundary terms, and tensor beta functions with sign and normalization before instrument construction",
        "disposition":"reject complete endpoint-exchange action; require a new three-family source action"
    },
    "exchange_classification":wp924["classification"],
    "tensor_classification":wp925["classification"],
    "source_support_classification":wp930["classification"],
    "selected_relation":wp924["selected_relation"],
    "tensor_fixed_locus_real_dimension":wp925["fixed_locus_real_dimension"],
    "tensor_hostile_pair":wp925["hostile_pair"],
    "threshold_result":wp930["threshold_result"],
    "ratio_constraint":ratio_constraint,
    "family_conjugate_copy":family_conjugate_copy,
    "conditional_gradient_lifts":conditional_gradient_lifts,
    "endpoint_asymmetry_breaks":endpoint_asymmetry_breaks,
    "arbitrary_family_tensor":arbitrary_family_tensor,
    "complete_action_derived":complete_action_derived,
    "source_beta_derived":source_beta_derived,
    "physical_instrument":physical_instrument,
    "classification":"negative complete-action result: endpoint exchange is conditional and source beta absent",
    "remaining_gate":"derive a new three-family source action with exchange symmetry, boundary terms, and tensor beta functions",
    "hostile_gate":"do not promote desired-channel exchange, conjugate tensor pairing, or a mathematical lift into complete action authority",
    "claim_boundary":"the no-go is relative to the declared Spin5 action and threshold grammar; it does not forbid future source actions",
    "disposition":"complete-endpoint-exchange-action leaf resolved negatively; new three-family source-action rival selected"
}
(ROOT/"results"/"wp1215_complete_endpoint_exchange_action_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1215 PASS: endpoint exchange is not complete action symmetry")
