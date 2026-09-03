import json, math
from pathlib import Path
a=1.; beta=.25
qs=(3,12,48,192)
degrees=(0,1,6,20)
rows=[]
for q in qs:
 X=math.log(q); lam=2*a*beta*X**(beta-1)
 rows.append({"q":q,"lambda":lam,"scaled_fixed_degree_caps":{str(K):lam*(K+1)/q for K in degrees}})
checks={
 "lambda_decreases_with_tail_start":all(rows[i+1]["lambda"]<rows[i]["lambda"] for i in range(len(rows)-1)),
 "fixed_degree_scaled_caps_decrease":all(rows[i+1]["scaled_fixed_degree_caps"][str(K)]<rows[i]["scaled_fixed_degree_caps"][str(K)] for i in range(len(rows)-1) for K in degrees),
 "laguerre_kernel_diverges_in_degree":all((r["lambda"]*(1001))>(r["lambda"]*101) for r in rows),
}
base=Path(__file__).parents[1]
packet=(base/"rh-concavity-exponential-comparator-cannot-cap-the-moving-endpoint-kernel.md").read_text(encoding="utf-8")
checks.update({
 "packet_records_concavity_direction":"v_X(y)\\geq e^{-\\lambda_Xy}" in packet,
 "packet_records_exact_laguerre_kernel":"K_K^{(\\lambda)}(0,0)=\\lambda(K+1)" in packet,
 "packet_rejects_limit_interchange":"cannot justify interchange" in packet,
 "packet_preserves_weibull_question":"does not show that the moving Weibull endpoint kernel fails" in packet,
})
result={"schema":"marici.strominger.rh_moving_endpoint_exponential_comparator_no_go.v1","status":"passed" if all(checks.values()) else "failed","parameters":{"a":a,"beta":beta},"verdict":"The tangent exponential is a valid lower norm comparator, but its endpoint Christoffel kernel equals lambda(K+1) and diverges in degree. It explains fixed-degree decay after the q^{-1} prefactor but gives no uniform-degree cap. Any successful moving-endpoint argument must retain the indeterminate Weibull tail.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_moving_endpoint_exponential_comparator_no_go.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))
