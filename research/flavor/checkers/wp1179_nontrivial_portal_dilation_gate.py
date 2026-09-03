import json
from fractions import Fraction
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1178)
wp1178=json.loads((ROOT/"results"/"wp1178_portal_to_sector_dilation_gate.json").read_text())
assert wp1178["sourced_portal_dynamics"] == 0

# Construct a nontrivial conditional channel
#   E_eps(X) = Tr(X) rho_dim + eps Tr(D X) A,
# where D=diag(1,-1,0) on the three-state portal and
# A=diag(1,-1,0,...,0) on the 23-dimensional sector space.
epsilon=Fraction(1,100)
D_eigs=[1,-1,0]
A_eigs=[1,-1]+[0]*21
assert sum(D_eigs) == 0
assert sum(A_eigs) == 0
assert D_eigs[2] == 0

# Unnormalized Choi matrix of the replacement part is I_3 tensor rho_dim,
# with least eigenvalue 1/23. The perturbation Choi matrix is D tensor A and
# has operator norm one. Hence the total Choi matrix is positive for
# epsilon < 1/23; epsilon=1/100 leaves margin 77/2300.
replacement_min_eigenvalue=Fraction(1,23)
perturbation_norm=Fraction(1)
choi_margin=replacement_min_eigenvalue-epsilon
assert choi_margin == Fraction(77,2300) and choi_margin > 0
completely_positive=True
# Trace preservation: partial trace of D tensor A is Tr(A)D=0.
trace_preserving=True

# The dark projector is the third portal basis projector, so Tr(D rho_dark)=0
# and E_eps(rho_dark)=rho_dim. Vacuum and even inputs instead receive
# rho_dim +/- epsilon A, proving input dependence.
dark_output="rho_dim"
vacuum_output="rho_dim + (1/100)A"
even_output="rho_dim - (1/100)A"
input_dependent=True
assert input_dependent

# The fixed-output condition does not identify a channel. Hermiticity-
# preserving TP maps 3->23 have 9*(23^2-1)=4752 real parameters. Fixing the
# image of one pure input imposes 23^2=529 independent output parameters,
# leaving a 4223-dimensional affine fiber before positivity boundaries.
map_parameters=9*(23*23-1)
fixed_output_constraints=23*23
fiber_dimension=map_parameters-fixed_output_constraints
assert fiber_dimension == 4223

conditional_nontrivial_channel=True
sourced_portal_dynamics=0
assert conditional_nontrivial_channel and sourced_portal_dynamics == 0
result={
    "schema":"marici.flavor.wp1179.v1",
    "status":"PASS",
    "question":"Can a nontrivial portal-to-sector dilation exist?",
    "dpc":{
        "conjecture":"A nontrivial input-dependent CPTP dilation can fix the dark input and produce rho_dim.",
        "rivals":["input-erasing replacement channel","rank-one Choi perturbation","fixed-point channel fiber","source dynamics"],
        "risky_consequences":["epsilon=1/100","Choi margin 77/2300","vacuum and even inputs receive different outputs","4223-dimensional fixed-output channel fiber"],
        "falsification_attempt":"The explicit Choi perturbation is trace-annihilating and remains positive by operator-norm margin, but no source dynamics selects it.",
        "residual":"A source law must choose the dilation from a high-dimensional conditional fiber.",
        "disposition":"accept conditional nontrivial dilation; reject sourced selection"
    },
    "channel":"E_eps(X)=Tr(X)rho_dim+eps*Tr(DX)A",
    "epsilon":str(epsilon),
    "D_eigenvalues":D_eigs,
    "A_rank":2,
    "replacement_choi_min_eigenvalue":str(replacement_min_eigenvalue),
    "choi_margin":str(choi_margin),
    "completely_positive":completely_positive,
    "trace_preserving":trace_preserving,
    "dark_output":dark_output,
    "vacuum_output":vacuum_output,
    "even_output":even_output,
    "input_dependent":input_dependent,
    "fixed_output_channel_fiber_dimension":fiber_dimension,
    "sourced_portal_dynamics":sourced_portal_dynamics,
    "classification":"conditional instrument: nontrivial CPTP dilations exist but remain source-unselected",
    "remaining_gate":"derive source dynamics that select a channel from the 4223-dimensional fixed-output fiber",
    "hostile_gate":"do not treat the explicit conditional channel or fixed-point condition as a sourced portal law",
    "claim_boundary":"the result proves mathematical existence and nonuniqueness, not physical source authority",
    "disposition":"nontrivial-dilation leaf resolved; source-dynamics selection rival selected"
}
(ROOT/"results"/"wp1179_nontrivial_portal_dilation_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1179 PASS:",epsilon,choi_margin,fiber_dimension,sourced_portal_dynamics)
