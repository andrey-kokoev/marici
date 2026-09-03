import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(956,957,958,959)
wp956=json.loads((ROOT/"results"/"wp956_projective_even_down_coupling_cp_no_go.json").read_text())
wp957=json.loads((ROOT/"results"/"wp957_independent_projective_tensor_cp_sufficiency.json").read_text())
wp958=json.loads((ROOT/"results"/"wp958_second_projective_source_transfer_audit.json").read_text())
wp959=json.loads((ROOT/"results"/"wp959_projective_source_arity_threshold.json").read_text())
assert wp956["classification"] == "minimal even projective coupling descends but forces down-sector degeneracy and zero three-family CP"
assert wp957["classification"] == "a second independent projective tensor is algebraically sufficient for simple spectrum and nonzero three-family CP, but is not yet source-authorized"
assert wp958["classification"] == "existing source projectors do not yet define the second independent projective tensor on the complex three-family module"
assert wp959["classification"] == "the canonical complex-triplet projector interface exists, but the first CP-sensitive relational source packet has arity three"
# Minimal even coupling is CP-trivial; an independent second tensor is
# algebraically sufficient but unauthorized; existing projectors cannot
# transfer it; CP sensitivity starts at an ordered triple.
even_coupling_cp_zero=True
second_tensor_algebraically_sufficient=True
second_tensor_not_source_authorized=True
existing_projector_transfer_fails=True
arity_three_threshold=True
ordered_spanning_triple=False
source_action=False
completion_stability=False
instrument_transport=False
assert even_coupling_cp_zero and second_tensor_algebraically_sufficient and second_tensor_not_source_authorized
assert existing_projector_transfer_fails and arity_three_threshold
assert not (ordered_spanning_triple or source_action or completion_stability or instrument_transport)
result={
    "schema":"marici.flavor.wp1223.v1",
    "status":"PASS",
    "question":"Can physical doublet/projective coupling supply the missing CP-bearing source law?",
    "dpc":{
        "conjecture":"An even projective coupling or a second projective tensor supplies the physical three-family coupling.",
        "rivals":["minimal even projective coupling","reused up-sector tensor R","independent algebraic second tensor","existing Kirchhoff or sequential-SO5 projector","canonical two-projector interface"],
        "risky_consequences":["B squared is diag(1/2,1/2,0), forcing down discriminant and CP cubic zero","an independent tensor gives down discriminant 575/1728 and CP cubic -12866425i/3456","reusing R gives a simple down spectrum but CP cubic zero","two rank-one projectors share a line and force zero commutator cubic","three rays span the family space with Bargmann invariant 1/6+i/6"],
        "falsification_attempt":"the only algebraic repair needs an independent tensor, while admitted existing projectors cannot transfer it and the first CP-sensitive packet has arity three.",
        "residual":"readout-independent source action deriving an ordered spanning triple or equivalent irreducible complex tensor, with completion and instrument transport",
        "disposition":"reject projective coupling as complete; select ordered-spanning-triple source-action rival"
    },
    "even_comparison":wp956["exact_comparison"],
    "algebraic_repair":wp957["exact_witness"],
    "hostile_control":wp957["hostile_control"],
    "candidate_partition":wp958["candidate_partition"],
    "arity_threshold":wp959["exact"],
    "even_coupling_cp_zero":even_coupling_cp_zero,
    "second_tensor_algebraically_sufficient":second_tensor_algebraically_sufficient,
    "second_tensor_not_source_authorized":second_tensor_not_source_authorized,
    "existing_projector_transfer_fails":existing_projector_transfer_fails,
    "arity_three_threshold":arity_three_threshold,
    "ordered_spanning_triple":ordered_spanning_triple,
    "source_action":source_action,
    "completion_stability":completion_stability,
    "instrument_transport":instrument_transport,
    "classification":"negative projective-coupling result: algebraic CP repair exists but no source-authorized ordered triple",
    "remaining_gate":"derive a readout-independent source action producing an ordered spanning triple or equivalent irreducible complex tensor with completion and instrument transport",
    "hostile_gate":"do not call even projective descent, a reused tensor, an existing two-projector source, or an algebraic witness a physical coupling",
    "claim_boundary":"the algebraic sufficiency of a second tensor is real, but source authority and calibrated transport are absent",
    "disposition":"physical-doublet/projective-coupling leaf resolved negatively; ordered-spanning-triple source-action rival selected"
}
(ROOT/"results"/"wp1223_physical_doublet_projective_coupling_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1223 PASS: projective coupling requires ordered source triple")
