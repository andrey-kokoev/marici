import json,math
from fractions import Fraction as F
from pathlib import Path
q0=F(1)*F(5,4)*F(3,2)*F(7,4);theta=F(13,60);target=theta/q0
checks={
 "q0_exact":q0==F(105,32),
 "target_ratio_exact":target==F(104,1575),
 "recomposition_exact":q0*target==theta,
}
base=Path(__file__).parents[1];src=json.loads((base/"results"/"rh_quarter_four_staircase_cross_ratio_grid.json").read_text(encoding="utf-8"));rows=[]
for r in src["late_rows"]:
 n=r["n"];qnm1=(n)*(n+F(1,4))*(n+F(1,2))*(n+F(3,4));R=r["theta"]*float(qnm1/q0);scaled=R/(n-1)**2
 rows.append({"n":n,"R_over_(n-1)^2":scaled,"error_from_104_1575":scaled-float(target)})
checks.update({"finite_reconstructed_ratios":all(math.isfinite(r["R_over_(n-1)^2"]) for r in rows),"errors_decrease":all(abs(rows[i+1]["error_from_104_1575"])<abs(rows[i]["error_from_104_1575"]) for i in range(len(rows)-1))})
packet=(base/"rh-cross-limit-thirteen-sixtieths-is-a-shift-ratio-limit.md").read_text(encoding="utf-8");checks["packet_requires_parameter_uniformity"]="parameter-uniform" in packet or "uniform control" in packet
result={"schema":"marici.strominger.rh_cross_limit_shift_ratio_reduction.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The candidate theta2=13/60 is exactly equivalent to R_m/m^2->104/1575 because q0=105/32 and q_(n-1)~n^4. Reconstructed exact-grid ratios move toward the target, but parameter-uniform staircase asymptotics remain unproved.","checks":checks,"constants":{"q0":str(q0),"theta2":str(theta),"shift_ratio_limit":str(target)},"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_cross_limit_shift_ratio_reduction.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
