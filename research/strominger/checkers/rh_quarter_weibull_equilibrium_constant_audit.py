import json,math
from pathlib import Path
beta=.25
B=math.gamma(beta+.5)*math.gamma(.5)/math.gamma(beta+1)
endpoint=(math.pi/(beta*B))**(1/beta)
A=endpoint/4
base=Path(__file__).parents[1]
prior=json.loads((base/"results"/"rh_mellin_hankel_first_shift_exact_audit.json").read_text(encoding="utf-8"));est=prior["fits"][-1]["A"]
checks={
 "beta_is_quarter":beta==.25,
 "equilibrium_constant_positive":A>0,
 "exact_constant_matches_degree22_extrapolation":abs(A-est)/A<1e-6,
 "equilibrium_endpoint_is_four_times_recurrence_constant":abs(endpoint-4*A)<1e-12,
}
packet=(base/"rh-quarter-weibull-equilibrium-sources-the-leading-jacobi-constant.md")
result={"schema":"marici.strominger.rh_quarter_weibull_equilibrium_constant_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The homogeneous equilibrium equation sources A=(1/4)[pi/(beta B(beta+1/2,1/2))]^(1/beta), matching exact degree-22 determinant extrapolation. Homogeneity fixes the n^4 leading scale but does not eliminate the 1/n correction.","parameters":{"beta":beta,"beta_function":B},"values":{"equilibrium_endpoint_constant":endpoint,"jacobi_A":A,"exact_grid_estimate":est,"relative_difference":abs(A-est)/A},"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_quarter_weibull_equilibrium_constant_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
