import json,math
from pathlib import Path
base=Path(__file__).parents[1];src=json.loads((base/"results"/"rh_quarter_four_staircase_cross_ratio_grid.json").read_text(encoding="utf-8"));T=13/60
rows=[r for r in src["rows"] if r["n"]>=10]
# Fixed-limit least squares: n^2 theta/T-1 = u/n+v/n^2.
X=[[1/r["n"],1/r["n"]**2] for r in rows];y=[r["n2_theta"]/T-1 for r in rows]
g00=sum(x[0]**2 for x in X);g01=sum(x[0]*x[1] for x in X);g11=sum(x[1]**2 for x in X);b0=sum(x[0]*z for x,z in zip(X,y));b1=sum(x[1]*z for x,z in zip(X,y));det=g00*g11-g01*g01;u=(b0*g11-b1*g01)/det;v=(g00*b1-g01*b0)/det
a=u+3.5;beta=3-a
checks={"source_grid_passed":src["status"]=="passed","fit_finite":all(math.isfinite(z) for z in (u,v,a,beta)),"u_near_six_fifths":abs(u-1.2)<.02,"a_near_forty_seven_tenths":abs(a-4.7)<.02,"beta_near_minus_seventeen_tenths":abs(beta+1.7)<.02}
result={"schema":"marici.strominger.rh_quarter_global_shift_first_correction.v1","status":"passed" if all(checks.values()) else "failed","verdict":f"With theta2 fixed at 13/60, degrees 10..24 give cross-ratio relative correction u={u:.8g}. Index conversion and q_(n-1)=n^4(1+3/(2n)+...) imply a=u+7/2={a:.8g} and beta=3-a={beta:.8g}, supporting candidates 6/5, 47/10, and -17/10 respectively. These are finite recognitions.","checks":checks,"fit":{"u":u,"v":v,"global_shift_a":a,"pivot_beta":beta},"candidates":{"u":"6/5","a":"47/10","beta":"-17/10"},"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_quarter_global_shift_first_correction.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
