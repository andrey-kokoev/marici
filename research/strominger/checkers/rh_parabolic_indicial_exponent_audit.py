import json
from fractions import Fraction as F
from pathlib import Path
def residual(n,p,C=F(2)):
 r=F(n**4,(n+1)**4);eps=C/F(n*n);u=lambda k:F(1,k**(-p)) if p<0 else F(k**p)
 return u(n+1)-(1+r-eps)*u(n)+r*u(n-1)
rows=[]
for n in (10,20,40,80,160):rows.append({"n":n,"p_minus_1_residual":float(residual(n,-1)),"p_minus_2_residual":float(residual(n,-2))})
checks={
 "p_minus_1_residual_decreases":all(abs(rows[i+1]["p_minus_1_residual"])<abs(rows[i]["p_minus_1_residual"]) for i in range(len(rows)-1)),
 "p_minus_2_residual_decreases":all(abs(rows[i+1]["p_minus_2_residual"])<abs(rows[i]["p_minus_2_residual"]) for i in range(len(rows)-1)),
 "indicial_roots_exact_for_s4_c2":((-1)**2+3*(-1)+2==0 and (-2)**2+3*(-2)+2==0),
}
base=Path(__file__).parents[1]
prior=json.loads((base/"results"/"rh_truncated_hard_edge_parabolic_recurrence_audit.json").read_text(encoding="utf-8"));scaled=[r["n2_abs_defect"] for r in prior["rows"]]
checks["finite_scaled_defect_moves_toward_two"]=all(scaled[i+1]>scaled[i] for i in range(len(scaled)-1)) and scaled[-1]<2
packet=(base/"rh-parabolic-hard-edge-exponent-is-set-by-the-second-order-defect.md").read_text(encoding="utf-8")
checks.update({
 "packet_states_indicial_equation":"p^2+(s-1)p+C=0" in packet,
 "packet_identifies_required_c2_limit":"\\longrightarrow2" in packet,
 "packet_does_not_claim_branch_selection":"Neither \\(C=2\\) nor selection" in packet,
})
result={"schema":"marici.strominger.rh_parabolic_indicial_exponent_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"For a_n~A n^4 and hard-edge defect epsilon_n~C/n^2, the parabolic recurrence has indicial equation p^2+3p+C=0. The candidate C=2 gives p=-1,-2, with the slower branch producing n^-2 compact mass. The coefficient limit and branch selection remain unproved.","checks":checks,"model_residuals":rows,"finite_scaled_defects":scaled,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_parabolic_indicial_exponent_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
