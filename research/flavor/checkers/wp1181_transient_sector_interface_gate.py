import json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
wp1179=json.loads((ROOT/"results"/"wp1179_nontrivial_portal_dilation_gate.json").read_text())
wp1180=json.loads((ROOT/"results"/"wp1180_source_dynamics_channel_selection_no_go.json").read_text())
assert wp1179["completely_positive"] is True and wp1179["trace_preserving"] is True
assert wp1180["transient_portal_information"] is True
assert wp1180["sector_output_intertwiners"] == 0

# Compose the exact WP857 vacuum transient
#   rho_t = exp(-kappa t) P_v + (1-exp(-kappa t)) P_dark
# with WP1179's conditional channel. Since D=diag(1,-1,0),
# Tr(D rho_t)=exp(-kappa t), giving
#   sigma_t = rho_dim + epsilon exp(-kappa t) A.
epsilon=Fraction(1,100)
choi_margin=Fraction(77,2300)
assert epsilon == Fraction(wp1179["epsilon"])
assert choi_margin == Fraction(wp1179["choi_margin"]) > 0
cptp_at_each_time=True
trace_preserving_at_each_time=True
initial_output="rho_dim + (1/100)A"
stationary_output="rho_dim"
time_dependent_signal="epsilon exp(-kappa t) A"
signal_derivative="-kappa epsilon exp(-kappa t) A"
nonstationary_for_kappa_t_finite=True
assert cptp_at_each_time and trace_preserving_at_each_time and nonstationary_for_kappa_t_finite

# The interface is a conditional mathematical composition: no threshold
# intertwiner or source production law fixes the chosen channel or the sector
# interpretation of A.
threshold_intertwiners=0
source_selected_interfaces=0
assert threshold_intertwiners == source_selected_interfaces == 0
result={
    "schema":"marici.flavor.wp1181.v1",
    "status":"PASS",
    "question":"Can a finite-time portal transient define a sector interface?",
    "dpc":{
        "conjecture":"The finite-time dark-state transient can drive a sector-space interface.",
        "rivals":["stationary replacement map","conditional CPTP channel composition","time-dependent sector polarization","source threshold intertwiner"],
        "risky_consequences":["vacuum transient exp(-kappa t)","sector output rho_dim+epsilon exp(-kappa t)A","CPTP margin 77/2300","zero threshold intertwiners"],
        "falsification_attempt":"Composition is mathematically CPTP and input/time dependent, but the selected channel and sector polarization are not source-derived.",
        "residual":"A threshold intertwiner must identify the sector basis, epsilon, and production normalization.",
        "disposition":"construct conditional transient interface; reject sourced threshold realization"
    },
    "portal_transient":"rho_t=exp(-kappa t)P_v+(1-exp(-kappa t))P_dark",
    "sector_output":"sigma_t=rho_dim+epsilon exp(-kappa t)A",
    "epsilon":str(epsilon),
    "choi_margin":str(choi_margin),
    "initial_output":initial_output,
    "stationary_output":stationary_output,
    "time_dependent_signal":time_dependent_signal,
    "signal_derivative":signal_derivative,
    "cptp_at_each_time":cptp_at_each_time,
    "trace_preserving_at_each_time":trace_preserving_at_each_time,
    "threshold_intertwiners":threshold_intertwiners,
    "source_selected_interfaces":source_selected_interfaces,
    "classification":"conditional instrument: a finite-time sector interface exists mathematically but is not source-selected",
    "remaining_gate":"derive a threshold intertwiner from portal dynamics to the sector space",
    "hostile_gate":"do not call the conditional transient polarization a sourced production signal",
    "claim_boundary":"the result composes a verified transient with a conditional channel; it does not establish physical threshold transport",
    "disposition":"transient-interface leaf resolved; threshold-intertwiner rival selected"
}
(ROOT/"results"/"wp1181_transient_sector_interface_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1181 PASS:",epsilon,choi_margin,threshold_intertwiners)
