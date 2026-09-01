import json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
wp1075=json.loads((ROOT/"results"/"wp1075_soft_channel_reweighting_rank_gate.json").read_text())
wp1076=json.loads((ROOT/"results"/"wp1076_symmetric_production_law_cofiber.json").read_text())
q=[Fraction(x,23) for x in (6,8,1,4,2,2)]
r=[Fraction(1,4) for _ in range(6)]
gain=Fraction(3,2)
B=[[Fraction(1,6) for _ in range(6)] for _ in range(6)]
K=[[gain*x for x in row] for row in B]
assert all(x == Fraction(1,4) for row in K for x in row)
assert [sum(K[i][j]*q[j] for j in range(6)) for i in range(6)] == r
assert all(sum(K[i][j] for i in range(6)) == gain for j in range(6))

# K is exactly rank one: all rows are identical and nonzero. Rank zero cannot
# produce the nonzero target r, so rank one is minimal.
kernel_rank=1
minimal_rank=1
assert kernel_rank == minimal_rank
assert wp1075["minimal_rank_one_solution"]["rank"] == 1
assert wp1075["minimal_rank_one_solution"]["common_gain"] == "3/2"
assert wp1076["missing_certificates"] == {
    "all_six_branch_permutation_symmetry":False,
    "common_production_kernel":False,
    "source_derived_gain_3_over_2":False,
}
source_certificates=0
assert source_certificates == 0
result={
    "schema":"marici.flavor.wp1175.v1",
    "status":"PASS",
    "question":"Does a source production kernel select the channel and common gain?",
    "dpc":{
        "conjecture":"The localized source derives the production kernel and gain.",
        "rivals":["minimum-rank branch-democracy kernel","higher-rank channel","admitted symmetry selection","UV boundary ensemble"],
        "risky_consequences":["K=(1/4)J_6","rank one","common gain 3/2","zero admitted source certificates"],
        "falsification_attempt":"K maps q to the six event weights exactly and is minimum rank, but WP1076's admitted symmetries do not select it or derive the gain.",
        "residual":"UV boundary-state matching and microstate uniformity remain the only possible source authority.",
        "disposition":"construct the minimum-rank conditional kernel; reject current source authority"
    },
    "kernel":"K=(1/4)J_6",
    "kernel_rank":kernel_rank,
    "minimal_rank":minimal_rank,
    "common_gain":str(gain),
    "input_q":[str(x) for x in q],
    "output_event_weights":[str(x) for x in r],
    "source_certificates":source_certificates,
    "classification":"conditional kernel gate: minimum-rank production algebra exists but is not source-selected",
    "remaining_gate":"match the UV boundary state to the dimension-trace ensemble and derive microstate uniformity",
    "hostile_gate":"do not call K=(1/4)J_6 a sourced production kernel",
    "claim_boundary":"the result gives minimum-rank algebra only; source dynamics and normalization remain absent",
    "disposition":"source-kernel leaf resolved; UV ensemble matching rival selected"
}
(ROOT/"results"/"wp1175_source_production_kernel_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1175 PASS:",kernel_rank,gain,source_certificates)
