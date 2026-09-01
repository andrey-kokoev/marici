import json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
wp1173=json.loads((ROOT/"results"/"wp1173_phase_gauge_production_law.json").read_text())
assert wp1173["sourced_channel_maps"] == 0
q=[Fraction(x,23) for x in (6,8,1,4,2,2)]
assert sum(q) == 1

# Let y be any normalized physical16 output and A a 16x6 column-stochastic
# channel with Aq=y. A has 6*(16-1)=90 parameters. Column normalization gives
# 6 constraints; Aq=y gives 16 equations, one redundant because sum q=sum y=1.
# The generic fiber therefore has dimension 90-6-15=69.
parameter_count=6*(16-1)
column_constraints=6
independent_output_constraints=16-1
fiber_dimension=parameter_count-column_constraints-independent_output_constraints
assert (parameter_count,column_constraints,independent_output_constraints,fiber_dimension)==(90,6,15,69)

# Explicit nonidentifiability witness for the normalized target y=(1/16)^16.
# A0 has every column equal to y. D has zero column sums and Dq=0, so A0 and
# A0+D are distinct stochastic channels with the same input q and output y.
y=[Fraction(1,16) for _ in range(16)]
A0=[[Fraction(1,16) for _ in range(6)] for _ in range(16)]
epsilon=Fraction(1,100)
D=[[Fraction(0) for _ in range(6)] for _ in range(16)]
D[0][0]=epsilon/q[0]
D[0][1]=-epsilon/q[1]
D[1][0]=-epsilon/q[0]
D[1][1]=epsilon/q[1]
A1=[[A0[r][j]+D[r][j] for j in range(6)] for r in range(16)]
assert A0 != A1
for A in (A0,A1):
    assert all(sum(A[r][j] for r in range(16)) == 1 for j in range(6))
    assert all(A[r][j] > 0 for r in range(16) for j in range(6))
    assert [sum(A[r][j]*q[j] for j in range(6)) for r in range(16)] == y
assert all(sum(D[r][j] for r in range(16)) == 0 for j in range(6))
assert all(sum(D[r][j]*q[j] for j in range(6)) == 0 for r in range(16))

sourced_channel_maps=0
unique_channel_from_modulus=False
assert sourced_channel_maps == 0 and unique_channel_from_modulus is False
result={
    "schema":"marici.flavor.wp1174.v1",
    "status":"PASS",
    "question":"Can a sourced six-branch-to-physical16 channel map be derived from the certified modulus?",
    "dpc":{
        "conjecture":"The modulus and q determine the physical16 production channel.",
        "rivals":["unique stochastic channel","rank-one output channel","source-derived kernel","common coupling scale"],
        "risky_consequences":["90 channel parameters","21 exact-target constraints","69-dimensional generic fiber","two explicit channels with identical q and y"],
        "falsification_attempt":"A0 and A0+D are distinct positive stochastic channels with the same input q and same normalized 16-output y.",
        "residual":"Only source dynamics can select the physical channel and gain.",
        "disposition":"reject channel identifiability from modulus and output alone"
    },
    "channel_shape":[16,6],
    "parameter_count":parameter_count,
    "exact_target_constraints":column_constraints+independent_output_constraints,
    "generic_fiber_dimension":fiber_dimension,
    "explicit_nonidentifiability":{
        "input_q":[str(x) for x in q],
        "output_y":"uniform_1_over_16",
        "epsilon":str(epsilon),
        "channels_distinct":True,
        "both_positive_stochastic":True,
        "same_input_output":True,
    },
    "sourced_channel_maps":sourced_channel_maps,
    "classification":"negative identifiability gate: a six-branch-to-physical16 channel is not determined by the certified modulus",
    "remaining_gate":"derive the production kernel from localized source dynamics",
    "hostile_gate":"do not fit a stochastic channel to physical16 and call it source-derived",
    "claim_boundary":"the result proves nonidentifiability of the channel from q and output data, not nonexistence of a physical kernel",
    "disposition":"channel-map leaf resolved; source-kernel rival selected"
}
(ROOT/"results"/"wp1174_physical16_channel_map_no_go.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1174 PASS:",fiber_dimension,sourced_channel_maps)
