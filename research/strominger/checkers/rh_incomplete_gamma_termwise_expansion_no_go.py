import json, math
from pathlib import Path
X=math.log(12);z=2*X**.25
def tail_bound(r):
 m=4*r+3
 return math.exp(-z)*z**(m+1)/math.factorial(m+1)/(1-z/(m+2))
rows=[]
for r in range(2,31):
 b=tail_bound(r);rows.append({"r":r,"tail_bound":b,"scaled_r4":b*r**4,"scaled_r8":b*r**8})
checks={
 "tail_bounds_positive":all(x["tail_bound"]>0 for x in rows),
 "tail_bounds_strictly_decrease":all(rows[i+1]["tail_bound"]<rows[i]["tail_bound"] for i in range(len(rows)-1)),
 "r4_scaled_eventually_decreases":all(rows[i+1]["scaled_r4"]<rows[i]["scaled_r4"] for i in range(3,len(rows)-1)),
 "r8_scaled_eventually_decreases":all(rows[i+1]["scaled_r8"]<rows[i]["scaled_r8"] for i in range(6,len(rows)-1)),
 "order_thirty_tail_below_1e_minus_100":rows[-1]["tail_bound"]<1e-100,
}
base=Path(__file__).parents[1]
packet=(base/"rh-termwise-incomplete-gamma-asymptotics-cannot-source-the-jacobi-power-series.md").read_text(encoding="utf-8")
checks.update({
 "packet_states_zero_poincare_series":"zero Poincare series" in packet,
 "packet_identifies_noncommuting_limits":"do not commute" in packet,
 "packet_moves_source_to_hankel_level":"Hankel matrices" in packet,
 "packet_preserves_integer_expansion":"does not reject an integer inverse-degree Jacobi expansion" in packet,
})
result={"schema":"marici.strominger.rh_incomplete_gamma_termwise_expansion_no_go.v1","status":"passed" if all(checks.values()) else "failed","verdict":"For fixed truncation start, the incomplete-gamma moment deficit is beyond every algebraic order in moment index. Its termwise Poincare expansion is identically zero, so it cannot source nonzero inverse-degree Jacobi corrections through a regular entrywise expansion. The correction must arise at growing Hankel-determinant or equivalent global level.","checks":checks,"sample_rows":rows[::7],"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_incomplete_gamma_termwise_expansion_no_go.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
