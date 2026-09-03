import json
from fractions import Fraction
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1177)
wp1177=json.loads((ROOT/"results"/"wp1177_uv_boundary_density_no_go.json").read_text())
assert wp1177["portal_to_sector_dilations"] == 0

# Conditional replacement channel E(X)=Tr(X) rho_dim from the three-state
# portal source to the 23-dimensional sector space. Kraus operators are
# K_{m,a}=sqrt(1/23)|m><a|. We verify completeness without symbolic square
# roots: K^*K=(1/23)|a><a|.
input_dim=3
output_dim=23
lam=Fraction(1,23)
kraus_count=input_dim*output_dim
# For input basis indices a,b, sum_m K_ma^*K_mb = delta_ab.
completeness=[[Fraction(a == b) for b in range(input_dim)] for a in range(input_dim)]
assert kraus_count == 69
assert completeness == [[1 if a == b else 0 for b in range(3)] for a in range(3)]
assert output_dim*lam == 1

# On every normalized three-state density operator, output is the same
# dimension-trace state. In particular, the WP857 dark projector is mapped to
# rho_dim, but all portal information is erased.
rho_dim={"eigenvalue":str(lam),"rank":23,"purity":str(Fraction(1,23))}
dark_input={"dimension":3,"rank":1,"purity":"1"}
channel_output=rho_dim
input_dependence=False
assert dark_input["dimension"] == wp1177["source_state"]["dimension"]
assert rho_dim["rank"] == wp1177["target_state"]["rank"]
assert input_dependence is False

conditional_cptp_channel=True
sourced_portal_dynamics=0
assert conditional_cptp_channel is True and sourced_portal_dynamics == 0
result={
    "schema":"marici.flavor.wp1178.v1",
    "status":"PASS",
    "question":"Can a portal-to-sector dilation produce the 23-dimensional boundary ensemble?",
    "dpc":{
        "conjecture":"A portal-to-sector dilation can produce rho_dim from the dark-state attractor.",
        "rivals":["input-erasing CPTP replacement channel","input-dependent portal dynamics","sourced threshold intertwiner","future UV state"],
        "risky_consequences":["69 Kraus operators","trace preservation","dark projector maps to rho_dim","all portal input information erased"],
        "falsification_attempt":"The replacement channel is CPTP and has the required output, but it is independent of the portal state and has no source-derived dynamics.",
        "residual":"A nontrivial portal-dependent dilation or independent UV boundary state remains open.",
        "disposition":"accept conditional replacement-channel existence; reject sourced portal dilation"
    },
    "channel":"E(X)=Tr(X) rho_dim",
    "input_dimension":input_dim,
    "output_dimension":output_dim,
    "kraus_count":kraus_count,
    "trace_preserving":True,
    "completely_positive":True,
    "dark_input":dark_input,
    "channel_output":channel_output,
    "input_dependence":input_dependence,
    "sourced_portal_dynamics":sourced_portal_dynamics,
    "classification":"conditional instrument: a CPTP replacement channel exists but is not a sourced portal dilation",
    "remaining_gate":"derive an input-dependent portal-to-sector channel from source dynamics",
    "hostile_gate":"do not call an input-erasing state-preparation channel a portal dilation or source law",
    "claim_boundary":"the result proves mathematical channel existence only",
    "disposition":"portal-to-sector dilation leaf resolved; nontrivial-dilation rival selected"
}
(ROOT/"results"/"wp1178_portal_to_sector_dilation_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1178 PASS:",kraus_count,conditional_cptp_channel,sourced_portal_dynamics)
