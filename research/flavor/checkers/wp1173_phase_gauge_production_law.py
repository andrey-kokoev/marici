import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
wp1171=json.loads((ROOT/"results"/"wp1171_exact_unistochastic_certificate.json").read_text())
wp1172=json.loads((ROOT/"results"/"wp1172_production_realization_no_go.json").read_text())
assert wp1171["exact_real_orthogonal_solution_certified"] is True
assert wp1172["physical_production_maps"] == 0

# The phase-gauge quotient is now explicit: diagonal unitary phases act by
# (L S R)_ij = exp(i(alpha_i+beta_j)) S_ij. The 12 phases have one redundant
# global phase, leaving an 11-dimensional fiber. The canonical gauge-invariant
# datum is P_ij=|S_ij|^2.
phase_fiber_dimension=6+6-1
assert phase_fiber_dimension == wp1172["phase_orbit_dimension"] == 11
canonical_quotient={
    "action":"(L S R)_ij = exp(i(alpha_i+beta_j)) S_ij",
    "fiber_dimension":phase_fiber_dimension,
    "invariant":"P_ij = |S_ij|^2",
}

# A phase-gauge law by itself does not choose a six-branch-to-physical16
# production channel. A general column-stochastic 16x6 channel has 90 free
# parameters: fifteen independent entries in each of six columns.
physical16_dimension=16
branch_dimension=6
stochastic_channel_parameters=branch_dimension*(physical16_dimension-1)
assert stochastic_channel_parameters == 90
assert "channel_map" not in wp1171 and "channel_map" not in wp1172
sourced_channel_maps=0
phase_gauge_law_constructed=True
physical_production_maps=0
assert sourced_channel_maps == physical_production_maps == 0
result={
    "schema":"marici.flavor.wp1173.v1",
    "status":"PASS",
    "question":"Can a phase-gauge production law be derived from the certified modulus?",
    "dpc":{
        "conjecture":"A sourced phase-gauge production law follows from the exact modulus.",
        "rivals":["diagonal phase quotient","physical16 channel map","common coupling scale","production authority"],
        "risky_consequences":["11-dimensional phase fiber","canonical invariant P=|S|^2","90 stochastic-channel parameters","no sourced channel map"],
        "falsification_attempt":"The quotient law is constructed, but it collapses to the modulus and leaves the 16x6 channel unconstrained.",
        "residual":"A source-derived channel map and common coupling scale remain open.",
        "disposition":"accept the gauge quotient; reject it as sourced physical production"
    },
    "canonical_quotient":canonical_quotient,
    "physical16_dimension":physical16_dimension,
    "branch_dimension":branch_dimension,
    "stochastic_channel_parameters":stochastic_channel_parameters,
    "sourced_channel_maps":sourced_channel_maps,
    "phase_gauge_law_constructed":phase_gauge_law_constructed,
    "physical_production_maps":physical_production_maps,
    "classification":"conditional instrument: phase-gauge quotient exists but production channel authority is absent",
    "remaining_gate":"derive or exclude a sourced six-branch-to-physical16 channel map",
    "hostile_gate":"do not call the phase quotient a production channel or coupling law",
    "claim_boundary":"the quotient is a mathematical reduction of the certified modulus, not a sourced physical map",
    "disposition":"phase-gauge leaf resolved; channel-map rival selected"
}
(ROOT/"results"/"wp1173_phase_gauge_production_law.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1173 PASS:",phase_fiber_dimension,stochastic_channel_parameters,sourced_channel_maps)
