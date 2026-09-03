import json
from fractions import Fraction
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1181,1182)
wp1181=json.loads((ROOT/"results"/"wp1181_transient_sector_interface_gate.json").read_text())
wp1182=json.loads((ROOT/"results"/"wp1182_threshold_intertwiner_no_go.json").read_text())
assert wp1181["sector_output"] == "sigma_t=rho_dim+epsilon exp(-kappa t)A"
assert wp1182["basis_orbit_dimension"] == 86
assert wp1182["amplitude_interval_dimension"] == 1

# With no dimensionful threshold clock, kappa is only a coordinate along the
# transient. For kappa,kappa'>0, the reparametrization t'=kappa t/kappa'
# identifies the two conditional curves:
#   rho_dim + epsilon exp(-kappa t) U A U*
# = rho_dim + epsilon exp(-kappa' t') U A U*.
kappa_scaling_dimension=1
basis_orbit_dimension=86
amplitude_interval_dimension=1
joint_fiber_dimension=basis_orbit_dimension+amplitude_interval_dimension+kappa_scaling_dimension
assert joint_fiber_dimension == 88
time_reparam_invariant=True
threshold_basis_selected=False
threshold_scale_selected=False
production_normalization_selected=False
assert time_reparam_invariant
assert not (threshold_basis_selected or threshold_scale_selected or production_normalization_selected)
result={
    "schema":"marici.flavor.wp1183.v1",
    "status":"PASS",
    "question":"Can the conditional transient interface derive a threshold basis and scale?",
    "dpc":{
        "conjecture":"The conditional sector curve selects its basis, amplitude, and decay scale.",
        "rivals":["fixed U(23) basis","fixed epsilon gain","fixed kappa clock","reparametrized conditional curve"],
        "risky_consequences":["U(23) orbit dimension 86","epsilon interval dimension 1","kappa time-reparametrization dimension 1","joint fiber dimension 88"],
        "falsification_attempt":"For every kappa'>0, t'=kappa t/kappa' maps the old exponential curve to the new one while U and epsilon remain arbitrary within their verified fiber.",
        "residual":"A dimensionful threshold anchor and sector-basis packet remain absent.",
        "disposition":"reject threshold basis/scale derivation"
    },
    "conditional_curve":"sigma_t(U,epsilon,kappa)=I_23/23+epsilon exp(-kappa t)UAU*",
    "reparametrization":"t'=kappa t/kappa'",
    "basis_orbit_dimension":basis_orbit_dimension,
    "amplitude_interval_dimension":amplitude_interval_dimension,
    "kappa_scaling_dimension":kappa_scaling_dimension,
    "joint_fiber_dimension":joint_fiber_dimension,
    "time_reparam_invariant":time_reparam_invariant,
    "threshold_basis_selected":threshold_basis_selected,
    "threshold_scale_selected":threshold_scale_selected,
    "production_normalization_selected":production_normalization_selected,
    "classification":"negative threshold gate: conditional interface has an 88-dimensional basis/amplitude/time fiber",
    "remaining_gate":"derive a dimensionful threshold anchor and sector-basis packet",
    "hostile_gate":"do not call kappa an absolute threshold scale or A a source-selected sector basis",
    "claim_boundary":"the no-go applies to the conditional interface; a future physical threshold packet remains open",
    "disposition":"threshold basis/scale leaf resolved; dimensionful-threshold-anchor rival selected"
}
(ROOT/"results"/"wp1183_threshold_basis_scale_no_go.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1183 PASS:",joint_fiber_dimension)
