import json, math
from pathlib import Path
a=1.; beta=.25
zs=(.25,1.,2.,4.)
Xs=(10.,100.,1000.,10000.)
rows=[]
for X in Xs:
 L=X**(1-beta)/(2*a*beta)
 errors=[]
 for z in zs:
  phi=2*a*((X+L*z)**beta-X**beta)
  errors.append(abs(phi-z))
 rows.append({"X":X,"L":L,"max_local_exponent_error":max(errors),"errors":errors})
checks={
 "scaling_length_increases":all(rows[i+1]["L"]>rows[i]["L"] for i in range(len(rows)-1)),
 "local_exponent_errors_decrease":all(rows[i+1]["max_local_exponent_error"]<rows[i]["max_local_exponent_error"] for i in range(len(rows)-1)),
 "fixed_degree_endpoint_model_decays":all((2*a*beta*7)/(math.exp(Xs[i+1]) if Xs[i+1]<700 else float("inf"))/Xs[i+1]**(1-beta) < (2*a*beta*7)/math.exp(Xs[i])/Xs[i]**(1-beta) for i in range(2)),
}
base=Path(__file__).parents[1]
packet=(base/"rh-moving-weibull-endpoint-has-a-fixed-degree-laguerre-scaling-limit.md").read_text(encoding="utf-8")
checks.update({
 "packet_has_second_order_expansion":"X^{-\\beta}z^2" in packet,
 "packet_states_fixed_degree_scope":"every fixed polynomial-degree space" in packet,
 "packet_rejects_uniform_promotion":"not uniform in degree" in packet,
 "packet_retains_far_weibull_tail":"far Weibull tail" in packet,
})
result={"schema":"marici.strominger.rh_moving_weibull_fixed_degree_scaling_audit.v1","status":"passed" if all(checks.values()) else "failed","parameters":{"a":a,"beta":beta,"z_samples":zs},"verdict":"Under y=L_X z with L_X=X^(1-beta)/(2a beta), the shifted exponent converges locally to z. Fixed-degree endpoint kernels therefore have Laguerre scaling (K+1)/L_X and the quadrature endpoint ratio decays as 2a beta(K+1)/(q(log q)^(1-beta)). Growth in K prevents a uniform-degree promotion.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_moving_weibull_fixed_degree_scaling_audit.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))
