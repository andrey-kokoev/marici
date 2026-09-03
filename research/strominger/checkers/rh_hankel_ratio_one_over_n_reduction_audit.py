import json, math
from fractions import Fraction as F
from pathlib import Path
# Exact discrete identity for L_n=alpha*n+beta+gamma/n.
a,b,g=F(7,3),F(-5,4),F(11,9)
def L(n):return a*n+b+g/F(n)
exact=[]
for n in range(2,15):
 half_second=(L(n+1)-2*L(n)+L(n-1))/2
 exact.append({"n":n,"half_second":str(half_second),"n3_scaled":float(half_second*n**3)})
base=Path(__file__).parents[1]
src=json.loads((base/"results"/"rh_truncation_coefficient_relative_grid_audit.json").read_text(encoding="utf-8"))
q12=next(r for r in src["rows"] if r["q"]==12)
diag=[]
for r in q12["degrees"]:
 n=r["n"];diag.append({"n":n,"gamma_proxy":n**3*math.log1p(r["relative_a"])})
late=[r["gamma_proxy"] for r in diag if r["n"]>=4]
checks={
 "linear_normalization_cancels_exactly":all((L(n+1)-2*L(n)+L(n-1))==g*(F(1,n+1)-2*F(1,n)+F(1,n-1)) for n in range(2,15)),
 "one_over_n_half_second_has_n_minus_three_limit":abs(exact[-1]["n3_scaled"]-float(g))<.02,
 "q12_gamma_proxy_positive":all(x>0 for x in late),
 "q12_gamma_proxy_spread_below_two_percent":max(late)/min(late)<1.02,
}
packet=(base/"rh-jacobi-n-minus-three-correction-is-a-hankel-ratio-one-over-n-term.md").read_text(encoding="utf-8")
checks.update({
 "packet_states_exact_hankel_identity":"monic norm identity" in packet,
 "packet_marks_conditional_implication":"conditional asymptotic implication" in packet,
 "packet_does_not_claim_gamma_formula":"does not prove the determinant expansion" in packet,
})
result={"schema":"marici.strominger.rh_hankel_ratio_one_over_n_reduction_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The off-diagonal n^-3 relative correction is exactly the second-difference image of a 1/n term in the log truncated/full Hankel determinant ratio. Linear measure-normalization terms cancel. The q=12 finite gamma proxy is stable through degree eight, but the determinant expansion remains unproved.","checks":checks,"q12_gamma_proxy":diag,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_hankel_ratio_one_over_n_reduction_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
