import json,math
from fractions import Fraction as F
from pathlib import Path
gamma=F(3,8);alpha2=-gamma/2
rows=[]
for n in (20,50,100,500,1000):
 d2=math.log(n+1)+math.log(n-1)-2*math.log(n);scaled=n*n*float(gamma)*d2
 rows.append({"n":n,"n2_centered_gamma_log":scaled,"error_from_minus_gamma":scaled+float(gamma)})
checks={
 "alpha2_exactly_minus_three_sixteenths":alpha2==F(-3,16),
 "centered_gamma_log_tends_to_minus_gamma":abs(rows[-1]["error_from_minus_gamma"])<1e-6,
 "error_decays":all(abs(rows[i+1]["error_from_minus_gamma"])<abs(rows[i]["error_from_minus_gamma"]) for i in range(len(rows)-1)),
 "twice_alpha2_equals_minus_gamma":2*alpha2==-gamma,
}
base=Path(__file__).parents[1];packet=(base/"rh-quarter-alpha2-is-the-centered-image-of-three-eighths-log-n.md").read_text(encoding="utf-8")
checks.update({
 "packet_requires_centered_remainder":"centered remainder \\(O(n^{-3})\\)" in packet,
 "packet_marks_equivalence_not_derivation":"exact equivalence, not a derivation" in packet,
})
result={"schema":"marici.strominger.rh_quarter_alpha2_log_free_energy_reduction.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Centered differencing maps +(3/8)log n in log D_n to -(3/8)n^-2 in log a_n^2, exactly equivalent to alpha2=-3/16. The determinant logarithmic coefficient and centered remainder remain to be proved.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_quarter_alpha2_log_free_energy_reduction.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
