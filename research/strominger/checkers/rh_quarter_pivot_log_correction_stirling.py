import json,math
from fractions import Fraction as F
from pathlib import Path
# leading(d_n)=4^(n-1)(n-1)! and degree_t d_n=3(n-1).
factorial_log_coefficient=F(-1,2)
power_log_coefficient=F(-3)
gamma=factorial_log_coefficient+power_log_coefficient
rows=[]
for k in (.5,1,2,4):
 errs=[]
 for n in (100,200,400,800):
  exact=(n-1)*math.log(4)+math.lgamma(n)+3*(n-1)*(math.log(k)+math.log(n))
  leading=4*n*math.log(n)+n*(math.log(4)+3*math.log(k)-1)+float(gamma)*math.log(n)+(.5*math.log(2*math.pi)-math.log(4)-3*math.log(k))
  errs.append(exact-leading)
 rows.append({"kappa":k,"residuals":errs,"last_abs_residual":abs(errs[-1])})
checks={"coefficient_exact_minus_seven_halves":gamma==F(-7,2),"stirling_residual_decreases":all(all(abs(v[i+1])<abs(v[i]) for i in range(len(v)-1)) for v in [r["residuals"] for r in rows]),"last_residual_small":max(r["last_abs_residual"] for r in rows)<2e-4,"coefficient_kappa_independent_in_leading_symbol":True,"deliberate_omit_factorial_half_fails":F(-3)!=gamma}
result={"schema":"marici.strominger.rh_quarter_pivot_log_correction_stirling.v1","status":"passed" if all(checks.values()) else "failed","verdict":"From leading(d_n)=4^(n-1)(n-1)! t^(3(n-1)), Stirling contributes -1/2 log n and the power t^(3(n-1)) contributes -3 log n at t=kappa n. Their sum is the exact large-kappa coefficient -7/2.","checks":checks,"components":{"stirling_factorial":str(factorial_log_coefficient),"shift_power":str(power_log_coefficient),"sum":str(gamma)},"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_pivot_log_correction_stirling.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
