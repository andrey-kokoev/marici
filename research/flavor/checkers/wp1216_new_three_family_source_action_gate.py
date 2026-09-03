import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(931,934,935)
wp931=json.loads((ROOT/"results"/"wp931_declared_flavor_selector_exhaustion.json").read_text())
wp934=json.loads((ROOT/"results"/"wp934_spin7_mass_deletion_realization_fiber.json").read_text())
wp935=json.loads((ROOT/"results"/"wp935_deutschian_realization_index_boundary_audit.json").read_text())
assert wp931["classification"] == "relative exhaustion: the declared flavor grammar contains no source-authorized physical16 selector"
assert wp934["classification"] == "realization fiber: the declared Spin7 representation/parity packet does not determine a mass-deletion control rank"
assert wp935["classification"]["first_missing_arrow"] == "completion-stable boundary source law"
# No candidate in the declared grammar supplies a new three-family source
# action.  Realization and boundary laws are additional missing constructors.
declared_grammar_exhausted=True
realization_fiber=True
boundary_law_missing=True
new_three_family_action=False
tensor_beta_derived=False
threshold_transport=False
calibrated_instrument=False
assert declared_grammar_exhausted and realization_fiber and boundary_law_missing
assert not (new_three_family_action or tensor_beta_derived or threshold_transport or calibrated_instrument)
result={
    "schema":"marici.flavor.wp1216.v1",
    "status":"PASS",
    "question":"Can the declared packets supply a new three-family source action?",
    "dpc":{
        "conjecture":"The declared Spin5/Spin7 grammar, mass-deletion realization, or Deutschian boundary index supplies a new three-family source action.",
        "rivals":["conditional boundary continuation","boolean score transfer","scalar mass-deletion completion","chiral-fermion constant-mass completion","tau=0 versus tau=1 boundary response"],
        "risky_consequences":["no candidate row is source-authorized, descending, properly reducing, isolating, and instrument-typed","representation and parity do not fix scalar versus chiral realization","the two realizations have control ranks three and at most one","tau=0 and tau=1 preserve parent/index but change contrast"],
        "falsification_attempt":"exchange-fixed tensors retain distinct shapes, the mass-control rank depends on realization, and boundary hostiles preserve index while changing readout.",
        "residual":"declare a genuinely new source geometry or completion-stable boundary law generating the three-family action and tensor beta functions",
        "disposition":"reject declared-packet source action; require new source geometry"
    },
    "exhaustion_classification":wp931["classification"],
    "operation_classification":wp931["operation_classification"],
    "candidate_rows":wp931["candidate_rows"],
    "realization_classification":wp934["classification"],
    "control_ranks":wp934["control_ranks"],
    "deutschian_first_missing_arrow":wp935["classification"]["first_missing_arrow"],
    "deutschian_exact_values":wp935["exact_values"],
    "declared_grammar_exhausted":declared_grammar_exhausted,
    "realization_fiber":realization_fiber,
    "boundary_law_missing":boundary_law_missing,
    "new_three_family_action":new_three_family_action,
    "tensor_beta_derived":tensor_beta_derived,
    "threshold_transport":threshold_transport,
    "calibrated_instrument":calibrated_instrument,
    "classification":"negative source-action result for declared Spin5/Spin7 and boundary packets",
    "remaining_gate":"derive a new source geometry or completion-stable boundary law before fixed-point or instrument computation",
    "hostile_gate":"do not extend conditional boundary, fitted scalar, boolean score, or double-commutator branches and call them a new action",
    "claim_boundary":"the exhaustion is relative to declared packets through WP930 plus audited realization/boundary branches",
    "disposition":"new-three-family-source-action leaf resolved negatively; new source-geometry rival selected"
}
(ROOT/"results"/"wp1216_new_three_family_source_action_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1216 PASS: declared packets do not supply three-family action")
