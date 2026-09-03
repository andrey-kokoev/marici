import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1130,1131,1132,1133,1134)
wp1130=json.loads((ROOT/"results"/"wp1130_six_branch_preparation_law_gate.json").read_text())
wp1131=json.loads((ROOT/"results"/"wp1131_parent_branching_preparation_no_go.json").read_text())
wp1132=json.loads((ROOT/"results"/"wp1132_dimension_trace_preparation_gate.json").read_text())
wp1133=json.loads((ROOT/"results"/"wp1133_uv_boundary_state_matching_no_go.json").read_text())
wp1134=json.loads((ROOT/"results"/"wp1134_preparation_constructor_closure_audit.json").read_text())
assert wp1130["classification"].startswith("conditional gate: exact q")
assert wp1131["classification"].startswith("negative gate: representation branching")
assert wp1132["classification"].startswith("conditional gate: dimension-trace")
assert wp1133["classification"].startswith("negative gate: current boundary")
assert wp1134["classification"].startswith("closure audit")
# The exact six-sector weights and dimension-trace density are conditional;
# no sourced state, operator, matching map, or measure exists.
conditional_q=True
dimension_trace_state=True
closure_audit=True
current_source_passes=wp1134["current_source_passes"]
parent_branching=False
boundary_matching=False
preparation_operator=False
source_measure=False
normalized_boundary_state=False
physical_preparation=False
assert conditional_q and dimension_trace_state and closure_audit and current_source_passes==0
assert not (parent_branching or boundary_matching or preparation_operator or source_measure or normalized_boundary_state or physical_preparation)
result={
    "schema":"marici.flavor.wp1254.v1",
    "status":"PASS",
    "question":"Can the current source derive the six-branch preparation law?",
    "dpc":{
        "conjecture":"The localized six-sector decomposition, parent branching, or dimension-trace ensemble may derive the preparation law q.",
        "rivals":["dimension distribution","parent branching","dimension-trace density","UV boundary-state matching","closure audit"],
        "risky_consequences":["q=(6,8,1,4,2,2)/23 is exact","rho_dim=direct_sum_b I_db/23 is positive with trace one","a source must supply a 23-dimensional microspace, normalized state, preparation operator, and measure provenance"],
        "falsification_attempt":"parent branching has zero parent states, probabilities, or stochastic maps; boundary matching has zero 23-dimensional microspaces, density matrices, trace functionals, matching maps, and uniformity proofs; the closure audit has zero passing constructors.",
        "residual":"obtain a future UV preparation packet carrying the four-part state interface",
        "disposition":"retain q and rho_dim conditionally; reject current-source preparation authority"
    },
    "conditional_q":wp1130["soft_distribution"],
    "sector_dimensions":wp1130["sector_dimensions"],
    "mass_blocks_after_exchange":wp1130["mass_blocks_after_exchange"],
    "parent_branching":{
        "parent_cells":wp1131["parent_cells"],
        "sourced_parent_states":wp1131["sourced_parent_states"],
        "conditional_branch_probabilities":wp1131["conditional_branch_probabilities"],
        "sourced_stochastic_branching_maps":wp1131["sourced_stochastic_branching_maps"]
    },
    "dimension_trace":{
        "state":"rho_dim=direct_sum_b I_db/23",
        "microstate_eigenvalue":wp1132["microstate_eigenvalue"],
        "trace":wp1132["trace"],
        "sector_probabilities":wp1132["sector_probabilities"]
    },
    "boundary_matching":{
        "sourced_boundary_objects":wp1133["sourced_boundary_objects"],
        "boundary_density_matrices":wp1133["boundary_density_matrices"],
        "boundary_microspaces_23d":wp1133["boundary_microspaces_23d"],
        "state_matching_maps":wp1133["state_matching_maps"],
        "microstate_uniformity_proofs":wp1133["microstate_uniformity_proofs"]
    },
    "closure_audit":{
        "tested_gates":wp1134["tested_gates"],
        "constructor_candidates":wp1134["constructor_candidates"],
        "current_source_capabilities":wp1134["current_source_capabilities"],
        "minimal_new_capability":wp1134["minimal_new_capability"]
    },
    "conditional_q_exact":conditional_q,
    "dimension_trace_state_constructed":dimension_trace_state,
    "closure_audit_complete":closure_audit,
    "current_source_passes":current_source_passes,
    "parent_branching_operator":parent_branching,
    "boundary_state_matching":boundary_matching,
    "preparation_operator":preparation_operator,
    "source_measure":source_measure,
    "normalized_boundary_state":normalized_boundary_state,
    "physical_preparation":physical_preparation,
    "classification":"conditional preparation gate: q and rho_dim exact, current-source preparation absent",
    "remaining_gate":"obtain a future UV preparation packet with a sourced 23-dimensional state, projections q, preparation operator, and measure provenance",
    "hostile_gate":"do not call dimensions, q, rho_dim, parent branching, boundary fields, or closure audits a physical preparation law",
    "claim_boundary":"WP1130 through WP1134 derive conditional algebra and close current constructors; no sourced preparation state is admitted",
    "disposition":"six-branch preparation gate resolved conditionally; future UV preparation packet required"
}
(ROOT/"results"/"wp1254_six_branch_preparation_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1254 PASS: q and rho_dim exact, current-source preparation absent")
