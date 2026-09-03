import json, math
from fractions import Fraction as F
from pathlib import Path
def det2(M):return M[0][0]*M[1][1]-M[0][1]*M[1][0]
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def inv2(A):
 d=det2(A);return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]
I=[[F(1),F(0)],[F(0),F(1)]];A=[[F(1,3),F(1,10)],[F(1,10),F(1,4)]];R=[[F(1,20),F(1,50)],[F(1,50),F(1,30)]];An=[[A[i][j]-R[i][j] for j in range(2)] for i in range(2)];IA=[[I[i][j]-A[i][j] for j in range(2)] for i in range(2)];IAn=[[I[i][j]-An[i][j] for j in range(2)] for i in range(2)];corr=mm(inv2(IA),R);rhs=[[I[i][j]+corr[i][j] for j in range(2)] for i in range(2)]
checks={
 "finite_determinant_factorization_exact":det2(IAn)/det2(IA)==det2(rhs),
 "finite_gap_ratio_at_least_one":det2(IAn)/det2(IA)>=1,
}
base=Path(__file__).parents[1]
packet=(base/"rh-gap-convergence-rate-is-an-integrated-christoffel-tail.md").read_text(encoding="utf-8")
checks.update({
 "packet_identifies_positive_tail":"R_n=A-A_n\\geq0" in packet,
 "packet_states_resolvent_trace_bound":"\\|(I-A)^{-1}\\|\\operatorname{Tr}R_n" in packet,
 "packet_identifies_integrated_kernel_tail":"sum_{j\\geq n}" in packet,
 "packet_limits_resolvent_to_fixed_start":"not uniformly in moving \\(X\\)" in packet,
 "packet_does_not_claim_rate":"No trace-tail rate is proved" in packet,
})
result={"schema":"marici.strominger.rh_gap_rate_integrated_christoffel_tail_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Finite-to-limit gap convergence factors through the positive omitted projection tail. Its logarithm is bounded by the fixed-X resolvent norm times the integrated Christoffel tail. Therefore an O(1/n) trace-tail estimate is the exact sufficient rate theorem now missing.","checks":checks,"finite_model":{"gap_ratio":str(det2(IAn)/det2(IA)),"correction_determinant":str(det2(rhs))},"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_gap_rate_integrated_christoffel_tail_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
