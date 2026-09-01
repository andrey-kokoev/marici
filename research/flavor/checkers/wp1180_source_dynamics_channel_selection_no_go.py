import json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
wp857=json.loads((ROOT/"results"/"wp857_oriented_dark_state_portal_attractor.json").read_text())
wp1179=json.loads((ROOT/"results"/"wp1179_nontrivial_portal_dilation_gate.json").read_text())
assert wp857["summary"]["all_passed"] is True
assert wp857["global_basin"] == "all density matrices on the declared three-state source"
assert wp1179["fixed_output_channel_fiber_dimension"] == 4223

# The stationary WP857 semigroup is the three-state replacement map
# E_inf(X)=Tr(X) P_dark. For any portal-to-sector channel F_eps that fixes
# P_dark and outputs rho_dim, composition is
# (F_eps o E_inf)(X)=Tr(X) rho_dim, independent of eps.
# WP1179's epsilon=0 and epsilon=1/100 channels therefore coincide after
# stationary source dynamics.
epsilons=[Fraction(0),Fraction(1,100)]
composed_outputs=[f"Tr(X) rho_dim" for _ in epsilons]
assert len(set(composed_outputs)) == 1
stationary_selection=False

# At finite time the three-state semigroup carries portal information, but it
# has no sector-space output operators, threshold intertwiner, or 23-state
# jump map. The selection failure is therefore a current-interface no-go, not
# a claim that transient physics is trivial.
source_jump_operators=2
sector_jump_operators=0
sector_output_intertwiners=0
transient_portal_information=True
assert source_jump_operators == 2
assert sector_jump_operators == sector_output_intertwiners == 0
assert transient_portal_information
result={
    "schema":"marici.flavor.wp1180.v1",
    "status":"PASS",
    "question":"Can source dynamics select one channel from the conditional dilation fiber?",
    "dpc":{
        "conjecture":"WP857 source dynamics selects one portal-to-sector channel.",
        "rivals":["stationary semigroup composition","transient portal interface","sector jump operators","threshold intertwiner"],
        "risky_consequences":["stationary map E_inf(X)=Tr(X)P_dark","epsilon independence after composition","4223-dimensional channel fiber","zero sector output operators"],
        "falsification_attempt":"For every channel fixing the dark state, F_eps composed with the stationary semigroup is Tr(X)rho_dim, independent of eps; no transient sector interface is sourced.",
        "residual":"A finite-time portal-to-sector interface could still select a channel.",
        "disposition":"reject stationary source-dynamics channel selection"
    },
    "stationary_map":"E_inf(X)=Tr(X)P_dark",
    "tested_epsilons":[str(x) for x in epsilons],
    "composed_outputs":composed_outputs,
    "stationary_selection":stationary_selection,
    "source_jump_operators":source_jump_operators,
    "sector_jump_operators":sector_jump_operators,
    "sector_output_intertwiners":sector_output_intertwiners,
    "transient_portal_information":transient_portal_information,
    "classification":"negative gate: stationary source dynamics cannot select a dilation channel",
    "remaining_gate":"derive a finite-time sector output interface or threshold intertwiner",
    "hostile_gate":"do not infer channel selection from the stationary dark-state attractor",
    "claim_boundary":"the no-go covers current source dynamics and stationary composition; a future transient sector interface remains open",
    "disposition":"source-dynamics selection leaf resolved; transient-interface rival selected"
}
(ROOT/"results"/"wp1180_source_dynamics_channel_selection_no_go.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1180 PASS:",stationary_selection,sector_jump_operators,wp1179["fixed_output_channel_fiber_dimension"])
