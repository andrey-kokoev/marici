import json
from fractions import Fraction as F
from pathlib import Path
def derived(alpha2,d2):
 return {"r3":-20+2*alpha2,"e4":d2+12-2*alpha2}
a=F(-3,16);d=F(1,2);got=derived(a,d);target={"r3":F(-163,8),"e4":F(103,8)}
checks={
 "r3_exact":got["r3"]==target["r3"],
 "e4_exact":got["e4"]==target["e4"],
 "sum_exact":got["r3"]+got["e4"]==F(-15,2),
 "altered_alpha2_fails_r3":derived(a+F(1,100),d)["r3"]!=target["r3"],
 "altered_d2_fails_e4":derived(a,d+F(1,100))["e4"]!=target["e4"],
}
base=Path(__file__).parents[1];packet=(base/"rh-rational-fourth-order-coefficients-reduce-to-two-normalized-inputs.md").read_text(encoding="utf-8")
checks.update({
 "packet_marks_equivalence_not_proof":"algebra proves equivalence" in packet,
 "packet_separates_two_inputs":"weibull-offdiagonal-alpha2" in packet and "weibull-defect-numerator-d2" in packet,
})
result={"schema":"marici.strominger.rh_rational_fourth_coefficient_reduction.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact algebra reduces r3=-163/8 and e4=103/8 to alpha2=-3/16 in a_n/(A n^4) and d2=1/2 in the normalized defect numerator. Deliberate perturbations change the claimed coefficients.","checks":checks,"inputs":{"alpha2":str(a),"d2":str(d)},"outputs":{k:str(v) for k,v in got.items()},"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_rational_fourth_coefficient_reduction.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
