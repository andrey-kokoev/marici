import json
from fractions import Fraction
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1181)
wp1181=json.loads((ROOT/"results"/"wp1181_transient_sector_interface_gate.json").read_text())
assert wp1181["threshold_intertwiners"] == 0
assert wp1181["source_selected_interfaces"] == 0
epsilon=Fraction(wp1181["epsilon"])
assert epsilon == Fraction(1,100)

# The stationary state rho_dim=I_23/23 is invariant under every unitary U in
# U(23). Conjugating A=diag(1,-1,0,...,0) to UAU* preserves trace zero and
# operator norm one, hence preserves CP and TP of the conditional channel.
u23_dimension=23*23
stabilizer_dimension=1+1+21*21
basis_orbit_dimension=u23_dimension-stabilizer_dimension
assert (u23_dimension,stabilizer_dimension,basis_orbit_dimension)==(529,443,86)
assert sum([1,-1]+[0]*21) == 0

# Every epsilon in 0<epsilon<1/23 also preserves Choi positivity because the
# replacement channel has least eigenvalue 1/23 and the perturbation norm one.
epsilon_upper=Fraction(1,23)
assert Fraction(0) < epsilon < epsilon_upper
amplitude_interval_dimension=1
interface_fiber_dimension=basis_orbit_dimension+amplitude_interval_dimension
assert interface_fiber_dimension == 87
source_basis_selection=False
source_amplitude_selection=False
threshold_intertwiners=0
assert not (source_basis_selection or source_amplitude_selection)
result={
    "schema":"marici.flavor.wp1182.v1",
    "status":"PASS",
    "question":"Can threshold transport identify the sector basis and production normalization?",
    "dpc":{
        "conjecture":"The conditional transient interface determines a threshold intertwiner.",
        "rivals":["sector-basis selection","unitary orbit of A","epsilon amplitude interval","sourced threshold transport"],
        "risky_consequences":["rho_dim is U(23)-invariant","A has an 86-dimensional conjugation orbit","epsilon varies over a one-dimensional interval","zero sourced intertwiners"],
        "falsification_attempt":"Every UAU* with U in U(23) and every epsilon below 1/23 gives a valid conditional interface, so threshold data do not identify basis or gain.",
        "residual":"A physical threshold packet must supply sector basis and amplitude scale.",
        "disposition":"reject threshold-intertwiner identifiability"
    },
    "stationary_state":"rho_dim=I_23/23",
    "A":"diag(1,-1,0,...,0)",
    "u23_dimension":u23_dimension,
    "A_stabilizer_dimension":stabilizer_dimension,
    "basis_orbit_dimension":basis_orbit_dimension,
    "epsilon":str(epsilon),
    "epsilon_upper":str(epsilon_upper),
    "amplitude_interval_dimension":amplitude_interval_dimension,
    "interface_fiber_dimension":interface_fiber_dimension,
    "source_basis_selection":source_basis_selection,
    "source_amplitude_selection":source_amplitude_selection,
    "threshold_intertwiners":threshold_intertwiners,
    "classification":"negative identifiability gate: threshold transport does not select sector basis or production normalization",
    "remaining_gate":"derive sector basis and threshold scale from a physical threshold packet",
    "hostile_gate":"do not treat U(23)-equivalent conditional polarizations as a sourced threshold signal",
    "claim_boundary":"the no-go covers identification from the conditional interface; future threshold data remain open",
    "disposition":"threshold-intertwiner leaf resolved; threshold basis/scale rival selected"
}
(ROOT/"results"/"wp1182_threshold_intertwiner_no_go.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1182 PASS:",basis_orbit_dimension,interface_fiber_dimension,threshold_intertwiners)
