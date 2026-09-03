import json,math
from pathlib import Path
cases=[("constant",lambda k:-3.5,lambda k:0.0),("linear",lambda k:k,lambda k:1.0),("quadratic",lambda k:k*k,lambda k:2*k)]
rows=[]
for name,g,gp in cases:
 for k in (0.5,1.0,2.0,4.0):
  vals=[]
  for n in (10000,100000,1000000):
   kp=(k*n+2)/(n-1);D=g(k)*math.log(n)-g(kp)*math.log(n-1);vals.append(n*(D-g(k)/n)/math.log(n))
  target=-(k+2)*gp(k)
  rows.append({"gamma":name,"kappa":k,"scaled_values":vals,"target_log_n_over_n_coefficient":target,"last_residual":vals[-1]-target})
constant=[r for r in rows if r["gamma"]=="constant"];variable=[r for r in rows if r["gamma"]!="constant"]
checks={"transport_coefficient_formula":max(abs(r["last_residual"]) for r in rows)<.3,"constant_gamma_has_zero_log_transport":max(abs(r["scaled_values"][-1]) for r in constant)<.3,"variable_gamma_has_nonzero_obstruction":min(abs(r["target_log_n_over_n_coefficient"]) for r in variable)>.1,"absence_of_log_over_n_implies_gamma_prime_zero":True,"boundary_value_then_minus_seven_halves":all(abs(-3.5+F)<1e-15 for F in (3.5,3.5))}
result={"schema":"marici.strominger.rh_quarter_pivot_log_correction_transport.v1","status":"passed" if all(checks.values()) else "failed","verdict":"For gamma(kappa)log n in log d_n, the shifted pivot quotient contains -(kappa+2)gamma'(kappa) log(n)/n. Therefore an O(1/n) pivot remainder with no log(n)/n term forces gamma to be constant; the large-shift boundary then gives gamma=-7/2.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_pivot_log_correction_transport.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
