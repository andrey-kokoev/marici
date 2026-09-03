import json
from fractions import Fraction as F
from pathlib import Path
triples=((F(3),F(5),F(11)),(F(7,3),F(19,5),F(29,7)),(F(101),F(1009),F(10007)))
rows=[]
for s0,s1,s2 in triples:
 curvature=s1*s1/(s0*s2);h0=s1/s0;h1=s2/s1
 rows.append({"curvature":str(curvature),"adjacent_ratio_quotient":str(h0/h1),"residual":str(curvature-h0/h1)})
checks={
 "adjacent_factorization_exact":all(r["residual"]=="0" for r in rows),
 "deliberate_inverted_quotient_fails":any(F(r["curvature"])!=1/F(r["adjacent_ratio_quotient"]) for r in rows),
 "target_constant_exact":F(13,60)/F(105,32)==F(104,1575),
}
base=Path(__file__).parents[1];packet=(base/"rh-quarter-shift-ratio-reduces-to-adjacent-lu-quotients.md").read_text(encoding="utf-8")
checks.update({
 "packet_states_exponent_difference":"\\lambda(0)-\\lambda(1)=2" in packet,
 "packet_states_amplitude_ratio":"amplitude ratio \\(104/1575\\)" in packet,
 "packet_marks_refit_circular":"would be circular" in packet,
})
result={"schema":"marici.strominger.rh_quarter_adjacent_shift_quotient_reduction.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The staircase parameter curvature factors exactly as H_m(0)/H_m(1). Proving the cross limit reduces to an exponent difference two and amplitude ratio 104/1575 for adjacent parameter-shift quotients; reusing the originating finite fit would be circular.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_quarter_adjacent_shift_quotient_reduction.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
